#!/usr/bin/env python3
from random import seed, getrandbits
from ipaddress import IPv6Network, IPv6Address

subnet = 'fd00::/64'

seed()
network = IPv6Network(subnet)
address = IPv6Address(network.network_address + getrandbits(network.max_prefixlen - network.prefixlen))

print(address)