from . import A, AAAA, CNAME
from domain import Domain


def matching_ipv4_or_ipv6(domain: Domain, ipv4, ipv6) -> bool:
    return True if A.match(domain, ipv4) else bool(AAAA.match(domain, ipv6))


def matching_ipv4_or_cname(domain: Domain, ipv4, strings) -> bool:
    return True if A.match(domain, ipv4) else bool(CNAME.match(domain, strings))
