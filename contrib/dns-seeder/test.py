import socket

seeders = [
    'diytseed.mempool.pw',
    'diytseed1.diytubecrypto.com',
    'diytseed2.diytubecrypto.com',
    'diytseed3.diytubecrypto.com',
    'diytseed4.diytubecrypto.com',
    'diytseed5.diytubecrypto.com',
    'diytseed1.diytubecrypto.site',
    'diytseed2.diytubecrypto.site',
    'diytseed3.diytubecrypto.site',
    'diytseed4.diytubecrypto.site',
    'diytseed5.diytubecrypto.site'
]

for seeder in seeders:
    try:
        ais = socket.getaddrinfo(seeder, 0)
    except socket.gaierror:
        ais = []
    
    # Prevent duplicates, need to update to check
    # for ports, can have multiple nodes on 1 ip.
    addrs = []
    for a in ais:
        addr = a[4][0]
        if addrs.count(addr) == 0:
            addrs.append(addr)
    
    print(seeder + ' = ' + str(len(addrs)))
