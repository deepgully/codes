#!/usr/bin/env python
from pprint import pprint
from swiftclient import client

print("hello swift!")

authurl = 'http://192.168.1.13:5000/v2.0'
user = 'admin'
key = 'admin'

auth = client.Connection(authurl, user, key, tenant_name='admin', auth_version="2") 

pprint(auth.get_auth())

print("get account")
pprint(auth.get_account())

print("create container")
pprint(auth.put_container("foo"))

print("get container")
pprint(auth.get_container('foo'))

print("put_object")
pprint(auth.put_object('foo', "test.py", open("test.py", "r")))

#print auth.get_container("foo")

#print auth.get_object("foo", "test.py")

