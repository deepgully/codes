#!/bin/bash


# Create tenant, user and role
NAME=admin
PASS=admin

tenant_id=$(keystone tenant-list | grep $NAME | grep '\S\{32\}' | awk '{print $2}')
echo TenantID: $tenant_id

user_id=$(keystone user-list | grep $NAME | grep '\S\{32\}' | awk '{print $2}')
echo UserID: $user_id

role_id=$(keystone role-list | grep $NAME | grep '\S\{32\}' | awk '{print $2}')
echo RoleID: $role_id

swift_id=$(keystone service-list | grep Swift | grep '\S\{32\}' | awk '{print $2}')
if [ "$swift_id" == "" ]; then
    echo Create Swift object-store Service...
    keystone service-create --name=Swift --type=object-store --description="Swift Object Store Service"
    swift_id=$(keystone service-list | grep Swift | grep '\S\{32\}' | awk '{print $2}')
fi
echo SwiftID: $swift_id


keystone endpoint-create --region RegionOne --service_id $swift_id --publicurl http://192.168.1.13:8080/v1/AUTH_$tenant_id --adminurl http://localhost:8080 --internalurl http://localhost:8080/v1/AUTH_$tenant_id

swift -V 2 -A http://localhost:5000/v2.0 -U admin:admin -K admin stat 