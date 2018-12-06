Language requirement Python 3.6 or above

DNS seeding for infnote

Infnote-seeder
==============

Infnote-seeder is a crawler for the Infnote network, which exposes a list
of reliable nodes via a built-in DNS server.

Features:
* regularly revisits known nodes to check their availability
* bans nodes after enough failures, or bad behaviour


REQUIREMENTS
------------

$ pip3 install dnslib gevent socketserver pylru asyncio

$ pip3 install json logging socket configparser websockets


USAGE
-----

Assuming you want to run a dns seed on seed.infnote.com, you will
need an authorative NS record in infnote.com's domain record, pointing
to for example ns.infnote.com:

$nslookup -type=ns seed.infnote.com freedns1.registrar-servers.com

Server:		freedns1.registrar-servers.com

Address:	45.58.122.82#53

Authoritative answers can be found from:

seed.infnote.com	nameserver = ns.infnote.com.

ns.infnote.com	internet address = 47.74.45.239

and you have a full node IP address 47.74.45.239

$ sudo nohup python3 infnote_dns.py &

$ sudo nohup python3 run_crawler_regularly.py 47.74.45.239 seed.infnote.com 60 &

parameters:

47.74.45.239 is a fule node IP

seed.infnote.com is the seed url

60 means that the interval of crawler is 60 seconds


RUNNING AS NON-ROOT
-------------------

Typically, you'll need root privileges to listen to port 53 (name service).

One solution is using an iptables rule (Linux only) to redirect it to
a non-privileged port:

$ iptables -t nat -A PREROUTING -p udp --dport 53 -j REDIRECT --to-port 5353

If properly configured, this will allow you to run dnsseed in userspace, using
the -p 5353 option.
