#!/usr/bin/python
# get ip address from domain name

import dns.resolver

domain = "www.cisco.com"


A = dns.resolver.query(domain, 'A')

for i in A.response.answer:
    for j in i.items:
        if j.rdtype == 1:
            print j.address
        else:
            pass