#!/bin/bash

# disk
echo Setup Harddisk...

sudo fdisk -l |grep Disk

sudo fdisk /dev/sdb

# Command (m for help): n
# Command (m for help): w

sudo fdisk /dev/sdb -l

sudo apt-get install xfsprogs

sudo mkfs.xfs -f /dev/sdb1

sudo sed -i '$a /dev/sdb1 /mnt/sdb1 xfs noatime,nodiratime,nobarrier,logbufs=8 0 0' /etc/fstab


# folders
echo Setup Swift folders...

sudo mkdir /mnt/sdb1
sudo mount /mnt/sdb1/
sudo chown gully:gully /mnt/sdb1
mkdir /mnt/sdb1/1 /mnt/sdb1/2 /mnt/sdb1/3 /mnt/sdb1/4
mkdir /srv
sudo chown gully:gully /srv

for x in {1..4}; do ln -s /mnt/sdb1/$x /srv/$x; done
sudo mkdir -p /etc/swift/object-server /etc/swift/container-server /etc/swift/account-server /srv/1/node/sdb1 /srv/2/node/sdb2 /srv/3/node/sdb3 /srv/4/node/sdb4 /var/run/swift
sudo chown -R gully:gully /etc/swift /srv/[1-4]/ /var/run/swift  


sudo sed -i '/exit 0/i\mkdir -p /var/cache/swift /var/cache/swift2 /var/cache/swift3 /var/cache/swift4' /etc/rc.local
sudo sed -i '/exit 0/i\chown gully:gully /var/cache/swift*' /etc/rc.local
sudo sed -i '/exit 0/i\mkdir -p /var/run/swift' /etc/rc.local
sudo sed -i '/exit 0/i\chown gully:gully /var/run/swift' /etc/rc.local

# rsync
echo Setup rsync...
sudo cp rsyncd.conf /etc/rsyncd.conf
sudo sed -i 's/RSYNC_ENABLE=false/RSYNC_ENABLE=true/g' /etc/default/rsync
sudo service rsync restart
sudo rsync rsync://pub@localhost/

#memcache
echo Setup memcache
sudo apt-get install memcached
sudo sed -i 's/127.0.0.1/0.0.0.0/g' /etc/memcached.conf
sudo service memcached restart


# Setup Swift
echo Setup Swift
sudo apt-get install swift swift-account swift-container swift-proxy swift-object

cp proxy-server.conf /etc/swift/proxy-server.conf
cp swift.conf /etc/swift/swift.conf
sudo sed -i '$a [container-sync]' /etc/swfit/container-server.conf

echo create account-server conf...
ports=(6012 6022 6032 6042)
for x in {1..4}
do 
    cp account-server.conf /etc/swift/account-server/$x.conf
    replace="s/devices = \/srv\/1\/node/devices = \/srv\/$x\/node/g"
    sudo sed -i "$replace" /etc/swift/account-server/$x.conf
    replace="s/log_facility = LOG_LOCAL2/log_facility = LOG_LOCAL$(($x+1))/g"
    sudo sed -i "$replace" /etc/swift/account-server/$x.conf
    replace="s/bind_port = 6012/bind_port = ${ports[x-1]}/g"
    sudo sed -i "$replace" /etc/swift/account-server/$x.conf
done

echo create container-server conf...
ports=(6011 6021 6031 6041)
for x in {1..4}
do 
    cp container-server.conf /etc/swift/container-server/$x.conf
    replace="s/devices = \/srv\/1\/node/devices = \/srv\/$x\/node/g"
    sudo sed -i "$replace" /etc/swift/container-server/$x.conf
    replace="s/log_facility = LOG_LOCAL2/log_facility = LOG_LOCAL$(($x+1))/g"
    sudo sed -i "$replace" /etc/swift/container-server/$x.conf
    replace="s/bind_port = 6011/bind_port = ${ports[x-1]}/g"
    sudo sed -i "$replace" /etc/swift/container-server/$x.conf
done

echo create object-server conf...
ports=(6010 6020 6030 6040)
for x in {1..4}
do 
    cp object-server.conf /etc/swift/object-server/$x.conf
    replace="s/devices = \/srv\/1\/node/devices = \/srv\/$x\/node/g"
    sudo sed -i "$replace" /etc/swift/object-server/$x.conf
    replace="s/log_facility = LOG_LOCAL2/log_facility = LOG_LOCAL$(($x+1))/g"
    sudo sed -i "$replace" /etc/swift/object-server/$x.conf
    replace="s/bind_port = 6010/bind_port = ${ports[x-1]}/g"
    sudo sed -i "$replace" /etc/swift/object-server/$x.conf
done

./remakerings
./startmain
./startrest






