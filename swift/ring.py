# -*- coding: utf-8 -*-
#!/usr/bin/env python
from pprint import pprint
from swift.common.ring import Ring


servers = ("account", "container", "object")
for server in servers:
    ring = Ring('/etc/swift/%s.ring.gz' % server)
    print(server)
    pprint(ring._devs)
    ip_ports = set()
    for dev in ring.devs:
        if dev:
            ip_ports.add((dev['region'], dev['zone'],
                          dev['ip'], dev['port']))
                          
    pprint(ip_ports)
 
# the ring is now object Ring   
print(ring.partition_count, ring.replica_count)


# Partition Assignment List, 
# This is a list of array(¡®H¡¯) of devices ids. The outermost list contains an array(¡®H¡¯) for each replica. 
# Each array(¡®H¡¯) has a length equal to the partition count for the ring. 
# Each integer in the array(¡®H¡¯) is an index into the above list of devices. 
# The partition list is known internally to the Ring class as _replica2part2dev_id.

for replica in xrange(ring.replica_count):
    print("Replica %d:" % replica)
    #print(len(ring._replica2part2dev_id[replica]), ring._replica2part2dev_id[replica])
    

for partition in xrange(ring.partition_count):  
    devices = [ring.devs[part2dev_id[partition]] for part2dev_id in ring._replica2part2dev_id]
    #pprint(devices)
    
    
# Partition Shift Value
# The partition shift value is known internally to the Ring class as _part_shift. 
# This value used to shift an MD5 hash to calculate the partition on which the data for that hash should reside
# Only the top four bytes of the hash is used in this process
from hashlib import md5
from struct import unpack_from

paths = ["AUTH_d4d0fdacde194128bfc90f2f8c2dae8a"]
paths.append("foo")
paths.append("test.py")
HASH_PATH_PREFIX = HASH_PATH_SUFFIX = "deepgully"
digest = md5(HASH_PATH_PREFIX + '/' + '/'.join(paths) + HASH_PATH_SUFFIX).digest()
partition = unpack_from('>I', digest)[0] >> ring._part_shift
print(partition)


# Building the Ring
# 1. The initial building of the ring first calculates the number of partitions that should ideally be assigned 
# to each device based the device¡¯s weight
# 2. Then, the ring builder assigns each replica of each partition to the device that desires the most partitions
# at that point while keeping it as far away as possible from other replicas
    