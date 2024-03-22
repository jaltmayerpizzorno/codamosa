

# Generated at 2022-06-13 02:51:21.400191
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dfc = DnsFactCollector()
    assert dfc.name == 'dns'
    assert dfc._fact_ids == set()


# Generated at 2022-06-13 02:51:23.536685
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    dns_fact_collector = DnsFactCollector()
    facts_dict = {}
    dns_facts = dns_fact_collector.collect(collected_facts=facts_dict)


# Generated at 2022-06-13 02:51:25.284284
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns_fact_collector = DnsFactCollector()
    assert dns_fact_collector
    assert dns_fact_collector.name == 'dns'

# Generated at 2022-06-13 02:51:27.393743
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    test_obj = DnsFactCollector()
    res = test_obj.collect()
    assert type(res) == type({})

# Generated at 2022-06-13 02:51:33.980776
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    dns_collector = DnsFactCollector()
    # Set content of file '/etc/resolv.conf'
    content = '''
; generated by /usr/sbin/dhclient-script
search no.example.com example.com
nameserver 10.174.51.250
nameserver 10.174.51.251
options timeout:2 attempts:4 single-request-reopen
    '''
    # Call method collect
    print(dns_collector.collect())

# Generated at 2022-06-13 02:51:41.737225
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    # Returns the contents of a file, given a root directory
    def mocked_get_file_content(root, filename):
        # The file is not present on the host
        if filename != '/etc/resolv.conf':
            return ''
        # The file exists on the host

# Generated at 2022-06-13 02:51:43.946554
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    test_object = DnsFactCollector()
    assert test_object
    assert test_object.collect()



# Generated at 2022-06-13 02:51:45.386306
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    dns_facts = DnsFactCollector().collect()

    assert 'dns' in dns_facts

# Generated at 2022-06-13 02:51:51.916260
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    fake_module = None
    fake_facts = None
    ffc = DnsFactCollector()
    result = ffc.collect(fake_module, fake_facts)

    assert type(result) is dict
    assert 'dns' in result
    assert 'nameservers' in result['dns']
    assert type(result['dns']['nameservers']) is list
    assert 'domain' in result['dns']
    assert 'search' in result['dns']
    assert type(result['dns']['search']) is list
    assert 'sortlist' in result['dns']
    assert type(result['dns']['sortlist']) is list
    assert 'options' in result['dns']
    assert type(result['dns']['options']) is dict

# Generated at 2022-06-13 02:51:54.417285
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    facts = DnsFactCollector()
    # Check the constructor of class DnsFactCollector
    assert facts.name == 'dns'
    assert facts._fact_ids == set()


test_DnsFactCollector()

# Generated at 2022-06-13 02:52:12.668453
# Unit test for method collect of class DnsFactCollector

# Generated at 2022-06-13 02:52:16.335105
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():

    from ansible.module_utils.facts.utils import FactsCollector

    # Test for constructor
    collect_obj = DnsFactCollector()
    assert collect_obj

    # Test for method - collect
    collect_obj = FactsCollector()
    res = collect_obj.collect(module=None, collected_facts=None)
    assert res.get('dns')

# Generated at 2022-06-13 02:52:18.292495
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns_facts = DnsFactCollector()
    assert dns_facts.name == "dns"

# Generated at 2022-06-13 02:52:21.226642
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    assert DnsFactCollector.name == 'dns'
    assert type(DnsFactCollector._fact_ids) is set

# Generated at 2022-06-13 02:52:32.991381
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    dfc = DnsFactCollector()

    facts = dfc.collect()
    assert len(facts['dns']['options']) == 7
    assert facts['dns']['options']['ndots'] == 3
    assert facts['dns']['options']['rotate'] is True
    assert facts['dns']['options']['timeout'] == '2'
    assert facts['dns']['options']['attempts'] == '1'
    assert facts['dns']['options']['edns0'] is True
    assert facts['dns']['options']['inet6'] is True
    assert facts['dns']['options']['single-request-reopen'] is True
    assert facts['dns']['domain'] == 'home'

# Generated at 2022-06-13 02:52:35.305727
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns_fact_collector = DnsFactCollector()
    assert dns_fact_collector
    assert dns_fact_collector.name == 'dns'

# Generated at 2022-06-13 02:52:39.671697
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    #Expected
    expected = dict(dns=dict())
    collectedFacts = dict()
    dnsFactCollector = DnsFactCollector()
    assert dnsFactCollector is not None
    dnsFactCollector.collect(None, collectedFacts)
    assert expected == collectedFacts

# Generated at 2022-06-13 02:52:42.914790
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    dns_obj = DnsFactCollector()
    assert dns_obj.collect() == {'dns': {'nameservers': ['10.0.20.5', '10.0.20.6', '10.0.20.7'], 'search': ['ansible.com'], 'options': {'rotate': True, 'timeout:1': True}}}

# Generated at 2022-06-13 02:52:52.124404
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    from ansible.module_utils.facts import facts
    from collections import namedtuple

    DnsStruct = namedtuple('DnsStruct', ['domain', 'nameservers', 'options', 'search', 'sortlist'])
    DnsStruct.__new__.__defaults__ = (None,) * len(DnsStruct._fields)
    dns_struct = DnsStruct('t.c', ['1.2.3.4'], {'timeout': '10'}, ['s.c'], ['a.b/32'])

    fc = facts.collectors['dns']

    results = fc.collect()['dns']
    assert results['domain'] == dns_struct.domain
    assert results['nameservers'] == dns_struct.nameservers
    assert results['options'] == dns_struct.options

# Generated at 2022-06-13 02:52:56.558667
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns_fact_collector = DnsFactCollector()
    assert dns_fact_collector.name == 'dns'
    assert dns_fact_collector.collect() == {}
    assert dns_fact_collector.collect(collected_facts=None) == {}

# Generated at 2022-06-13 02:53:13.499995
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns_fact_collector = DnsFactCollector()
    assert dns_fact_collector.name == 'dns'
    assert dns_fact_collector._fact_ids == set()

# Generated at 2022-06-13 02:53:21.824329
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    from ansible.module_utils import basic
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts.collector import DnsFactCollector
    import os
    import test

    # Create a temporary file
    fd, tmpspec = test.test_support.tempfile.mkstemp()
    with os.fdopen(fd, 'w') as f:
        # Write the content of a valid /etc/resolv.conf
        f.write('; This file is managed by man:systemd-resolved(8). Do not edit.\n')
        f.write('#\n')
        f.write('# Third party programs must not access this file directly, but\n')

# Generated at 2022-06-13 02:53:29.219000
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    dns_fact_collector = DnsFactCollector()

    dns_facts = dns_fact_collector.collect()

    dns_fact_collector.cleanup()

    assert dns_facts == {'dns': {'nameservers': ['192.168.1.1'], 'domain': 'example.com', 'search': ['example.com'], 'sortlist': ['10.1.2.3/24 10.1.2.4/24'], 'options': {'timeout': '2', 'attempts': '3'}}}

# Generated at 2022-06-13 02:53:40.391250
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFileFactCollector
    from ansible.module_utils.facts.utils import get_file_content
    import collections
    import os

    # Create a BaseFileFactCollector object
    FAKE_CACHE = dict()

    class FakeBaseFileFactCollector(BaseFileFactCollector):
        name = 'fake_basefilefactcollector'
        _fact_ids = set()
        _file_paths = dict()

        def _get_file_content(self, file_path):
            try:
                return FAKE_CACHE[file_path]
            except:
                return ""

    # Create a DnsFactCollector object
    dns_fc = DnsFactCollector()

    # Create a 'resolve.conf' file with an empty content


# Generated at 2022-06-13 02:53:45.830776
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    # Create a new module
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode=True
    )
    # Create mock class for BaseFactCollector
    collector = DnsFactCollector()
    dns_facts = collector.collect(module=module)
    assert len(dns_facts.keys()) == 1

# Generated at 2022-06-13 02:53:48.124963
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dFacts = DnsFactCollector()
    assert dFacts.name == 'dns', 'name of DnsFactCollector should be dns'

# Generated at 2022-06-13 02:53:59.543670
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    testobj = DnsFactCollector()
    assert type(testobj).__name__ == 'DnsFactCollector'
    assert testobj.name == 'dns'
    assert testobj.collect()['dns']['nameservers'][0] == '8.8.8.8'
    assert testobj.collect()['dns']['domain'] == 'example.com'
    assert testobj.collect()['dns']['search'][0] == 'example.com'
    assert testobj.collect()['dns']['sortlist'][0] == '169.254.0.0'
    assert testobj.collect()['dns']['sortlist'][1] == '255.255.0.0'

# Generated at 2022-06-13 02:54:05.276389
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():

    # Test for the method with no dns related arguments
    def dummy_method():
        pass

    # Test for the method with dns related arguments
    def dummy_method_with_data(resolv_conf_data):
        return get_file_content('/etc/resolv.conf', resolv_conf_data)

    import sys
    sys.modules['os'] = MagicMock()
    sys.modules['os'].path = MagicMock()
    sys.modules['os'].path.exists = MagicMock(return_value=True)
    sys.modules['__main__'] = MagicMock()
    sys.modules['__main__'].get_file_content = dummy_method

    dns_collector = DnsFactCollector()
    sys.modules['__main__'].get_file_

# Generated at 2022-06-13 02:54:07.155769
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    test = DnsFactCollector()
    assert test.name == 'dns'
    assert test._fact_ids == set()


# Generated at 2022-06-13 02:54:08.756141
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    obj = DnsFactCollector()
    assert obj.name == "dns"

# Generated at 2022-06-13 02:54:38.129986
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    facts = DnsFactCollector().collect()
    assert "dns" in facts
    assert "nameservers" in facts["dns"]

# Generated at 2022-06-13 02:54:39.790803
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    my_obj = DnsFactCollector()
    assert my_obj.name == 'dns'
    assert my_obj._fact_ids == set()


# Generated at 2022-06-13 02:54:41.362618
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    pass

# Generated at 2022-06-13 02:54:45.386801
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    """Test constructor of class DnsFactCollector"""
    dns_fact_collector = DnsFactCollector()
    assert dns_fact_collector.name == 'dns'
    assert dns_fact_collector._fact_ids == set()

# Generated at 2022-06-13 02:54:54.365993
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    test_collector = DnsFactCollector()

    test_file_contents = \
'''#
# /etc/resolv.conf
#
nameserver 10.0.0.1
search example.com sub.example.com
sortlist 10.1.0.0/255.255.0.0 10.2.0.0/255.255.0.0
domain example.com
options ndots:2 timeout:1 attempts:1
# End of file
'''

    test_file_path = '/tmp/test_file'
    with open(test_file_path, 'w') as f:
        f.write(test_file_contents)


# Generated at 2022-06-13 02:55:01.841370
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    dns_fact_collector = DnsFactCollector()
    dns_facts = dns_fact_collector.collect()
    dns_fact_collector.assertIn("dns", dns_facts)
    dns = dns_facts["dns"]
    dns_fact_collector.assertIn("options", dns)
    dns_fact_collector.assertIn("domain", dns)
    dns_fact_collector.assertIn("search", dns)
    dns_fact_collector.assertIn("sortlist", dns)
    dns_fact_collector.assertIn("nameservers", dns)
    dns_fact_collector.assertGreater(len(dns["nameservers"]), 0)

# Generated at 2022-06-13 02:55:07.216646
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    resolv_conf_content = '''
# Generated by NetworkManager
domain example.com
example.com
# nameserver 10.0.2.3
nameserver 8.8.8.8
'nameserver 8.8.4.4
'''

    expected_dict = {
        'dns': {
            'options': {},
            'domain': ['example.com', 'example.com'],
            'nameservers': ['8.8.8.8', '8.8.4.4']
        }
    }

    test_obj = DnsFactCollector()
    test_obj.collect(collected_facts={}, module=DummyModule(resolv_conf_content))

    assert test_obj.collect_func_results == expected_dict



# Generated at 2022-06-13 02:55:08.833040
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dfc = DnsFactCollector()

    assert dfc.name == 'dns'

# Generated at 2022-06-13 02:55:14.491553
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    dns_facts = DnsFactCollector().collect()
    assert isinstance(dns_facts, dict)
    assert isinstance(dns_facts['dns'], dict)
    assert isinstance(dns_facts['dns']['nameservers'], list)
    assert isinstance(dns_facts['dns']['search'], list)
    assert isinstance(dns_facts['dns']['sortlist'], list)
    assert isinstance(dns_facts['dns']['options'], dict)

# Generated at 2022-06-13 02:55:15.020076
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    pass

# Generated at 2022-06-13 02:56:27.884878
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dfc = DnsFactCollector()
    # Test The name of this fact collector
    assert dfc.name == 'dns'
    # Test the name of each fact id which can be collected by this fact collector
    assert dfc._fact_ids == set()

# Generated at 2022-06-13 02:56:34.522825
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.collector import collector_registry

    # Test creation of DnsFactCollector object
    my_obj = DnsFactCollector()

    # Test name property
    assert my_obj.name == 'dns'

    # Test collect()
    #
    # This test assumes that get_file_content() is mocked with a function
    # that returns the expected content string. We need to mock
    # get_file_content() because the underlying function get_file_content()
    # uses file system access to get the contents, which is not desirable
    # for testing this module.

# Generated at 2022-06-13 02:56:35.112087
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    pass

# Generated at 2022-06-13 02:56:38.379748
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns_fact_collector = DnsFactCollector()
    assert dns_fact_collector.name in dns_fact_collector._fact_ids

# Generated at 2022-06-13 02:56:39.061420
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    DnsFactCollector()

# Generated at 2022-06-13 02:56:48.051299
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    expected_dns_facts = """
nameservers:
- 172.16.0.23
- 192.168.1.1
domain: example.org
search:
- vpn.example.org
- example.org
sortlist:
- 10.0.0.0/8
- 172.16.0.0/12
- 192.168.1.0/24
options:
  timeout: 10
  attempts: 3
"""
    dns_facts = DnsFactCollector()
    dns_facts._module = 'unit_test'
    dns_facts._get_file_content = lambda path, default: expected_dns_facts
    facts = dns_facts.collect()
    print(facts)

# Generated at 2022-06-13 02:56:49.387225
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    dnsFactCollector = DnsFactCollector()
    dnsFactCollector.collect()

# Generated at 2022-06-13 02:56:53.293572
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns_fact_collector = DnsFactCollector()
    assert dns_fact_collector is not None
    assert dns_fact_collector.name == 'dns'
    assert dns_fact_collector.collect() == {}

# Generated at 2022-06-13 02:56:55.421322
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dfc = DnsFactCollector()
    assert dfc.name == 'dns'
    assert dfc._fact_ids == set()


# Generated at 2022-06-13 02:56:56.767285
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    my_obj = DnsFactCollector()
    assert my_obj


# Generated at 2022-06-13 03:00:00.552908
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns_fact_collector = DnsFactCollector()
    assert dns_fact_collector.name == "dns"
    assert dns_fact_collector.collect() == {"dns": {"options": {"timeout": 1, "attempts": 2}, "nameservers": ["8.8.8.8", "8.8.4.4"], "domain": "domain.tld"}}

# Generated at 2022-06-13 03:00:02.620611
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns_fact_collector = DnsFactCollector()
    assert dns_fact_collector.name == 'dns'
    assert dns_fact_collector._fact_ids == set()

# Generated at 2022-06-13 03:00:09.484142
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    dfc = DnsFactCollector()

    # test case 1: no content in resolv.conf
    actual_facts = dfc.collect()

    assert actual_facts == {}, \
        "Test case 1: no content = expected = {} actual = " + str(actual_facts)

    # test case 2: comment lines in resolv.conf
    actual_facts = dfc.collect(collected_facts={"ansible_facts": {}})

    assert actual_facts == {}, \
        "Test case 2: comment lines = expected = {} actual = " + str(actual_facts)

    # test case 3: empty line in resolv.conf
    actual_facts = dfc.collect(collected_facts={"ansible_facts": {}})


# Generated at 2022-06-13 03:00:11.370337
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns = DnsFactCollector()
    assert dns.name == 'dns'
    assert 'dns' in dns.collect()

# Generated at 2022-06-13 03:00:14.682805
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    # test for constructor
    dns_fact_collector = DnsFactCollector()

    assert dns_fact_collector.name == 'dns'
    assert dns_fact_collector._fact_ids == set()

# Generated at 2022-06-13 03:00:18.726745
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    facts = DnsFactCollector().collect()
    assert ('dns' in facts), 'dns fact not found'
    assert ('nameservers' in facts['dns']), 'dns.nameservers fact not found'
    assert ('search' in facts['dns']), 'dns.search fact not found'
    assert ('domain' in facts['dns']), 'dns.domain fact not found'

# Generated at 2022-06-13 03:00:19.662980
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    DnsFactCollector()

# Generated at 2022-06-13 03:00:20.526228
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    assert DnsFactCollector.name == 'dns'

# Generated at 2022-06-13 03:00:29.579705
# Unit test for method collect of class DnsFactCollector
def test_DnsFactCollector_collect():
    # Test setup
    import os
    import tempfile
    module = None
    collected_facts = {}
    collector = DnsFactCollector()
    temp_file_path = os.path.join(tempfile.gettempdir(), 'resolv.conf')
    expected_value = {
        'nameservers': ['8.8.8.8'],
        'options': {'timeout': '1'}
    }

    # Preconditions:
    #   1. A resolv.conf file is created.
    #   2. The resolv.conf file contains the following:
    #      # Generated by resolvconf
    #      nameserver 8.8.8.8
    #      options timeout:1
    # Postconditions:
    #   1. The dns fact is the same as the expected

# Generated at 2022-06-13 03:00:31.385793
# Unit test for constructor of class DnsFactCollector
def test_DnsFactCollector():
    dns_facts = DnsFactCollector()
    assert dns_facts.name == 'dns'