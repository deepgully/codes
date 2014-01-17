#!/bin/bash

echo Setup apt-get
sudo cp /etc/apt/sources.list /etc/apt/sources.list.old
sudo cp apt-sources.list /etc/apt/sources.list
sudo apt-get update

echo Install keystone and mysql...

sudo apt-get install keystone
sudo apt-get install python-mysqldb mysql-server
sudo apt-get install curl
sudo sed -i 's/127.0.0.1/0.0.0.0/g' /etc/mysql/my.cnf
sudo service mysql restart


# Create keystone database in mySQL
echo Create keystone database...

mysql -uroot -p
# mysql> CREATE DATABASE keystone;
# mysql> GRANT ALL ON keystone.* TO 'keystone'@'%' IDENTIFIED BY 'zzz';
# mysql> GRANT ALL ON keystone.* TO 'keystone'@'localhost' IDENTIFIED BY 'zzz';
# mysql> EXIT; 

# sudo vi /etc/keystone/keystone.conf
# Change connection
# connection = mysql://keystone:zzz@localhost/keystone
sudo sed -i 's/sqlite:\/\/\/\/var\/lib\/keystone\/keystone.db/mysql:\/\/keystone:zzz@localhost\/keystone/g' /etc/keystone/keystone.conf
sudo sed -i 's/# admin_token =/admin_token =/g' /etc/keystone/keystone.conf
sudo sed -i 's/# bind_host =/bind_host =/g' /etc/keystone/keystone.conf
sudo sed -i 's/# public_port =/public_port =/g' /etc/keystone/keystone.conf
sudo sed -i 's/# admin_port =/admin_port =/g' /etc/keystone/keystone.conf

sudo service keystone restart
sudo keystone-manage db_sync


echo Set env...
sed -i '/export SERVICE_TOKEN=/d' ~/.bashrc
sed -i '/export SERVICE_ENDPOINT=/d' ~/.bashrc
echo export SERVICE_TOKEN=ADMIN >> ~/.bashrc
echo export SERVICE_ENDPOINT=http://localhost:35357/v2.0 >> ~/.bashrc
. ~/.bashrc


echo Create tenant...
# Create tenant, user and role
NAME=admin
PASS=admin

keystone tenant-create --name $NAME --description "Admin Tenant" --enabled true
tenant_id=$(keystone tenant-list | grep $NAME | grep '\S\{32\}' | awk '{print $2}')
echo TenantID: $tenant_id

keystone user-create --tenant_id $tenant_id --name $NAME --pass $PASS --enabled true
user_id=$(keystone user-list | grep $NAME | grep '\S\{32\}' | awk '{print $2}')
echo UserID: $user_id

keystone role-create --name $NAME
role_id=$(keystone role-list | grep $NAME | grep '\S\{32\}' | awk '{print $2}')
echo RoleID: $role_id

echo like tenant, user and role...
keystone user-role-add --user $user_id --tenant_id $tenant_id --role $role_id

curl -d '{"auth": {"tenantName": "admin", "passwordCredentials":{"username": "admin", "password": "admin"}}}' -H "Content-type: application/json" http://localhost:35357/v2.0/tokens | python -mjson.tool




