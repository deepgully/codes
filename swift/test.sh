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