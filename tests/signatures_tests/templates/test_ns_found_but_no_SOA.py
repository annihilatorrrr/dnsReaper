from domain import Domain
import signatures
from signatures.templates.ns_found_but_no_SOA import (
    ns_found_but_no_SOA,
)

import pytest

test = ns_found_but_no_SOA("ns1", "mock")


def test_potential_success_with_matching_nameserver():
    domain = Domain("mock.local", fetch_standard_records=False)
    domain.NS = ["ns1"]
    assert test.potential(domain) == True


def test_potential_failure():
    domain = Domain("mock.local", fetch_standard_records=False)
    assert test.potential(domain) == False


signatures = [getattr(signatures, signature) for signature in signatures.__all__]


@pytest.mark.parametrize(
    "signature",
    [s for s in signatures if isinstance(s.test, ns_found_but_no_SOA)],
)
def test_check_success_ACTIVE(signature):
    try:
        ns = signature.test.sample_ns
    except:
        ns = signature.test.ns
    ns = ns if type(ns) == list else [ns]
    domain = Domain("mock.local", fetch_standard_records=False)
    for nameserver in ns:
        domain.NS = [nameserver]
        assert signature.test.check(domain) == True
