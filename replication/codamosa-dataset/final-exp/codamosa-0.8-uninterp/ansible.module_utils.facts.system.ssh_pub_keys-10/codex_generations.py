

# Generated at 2022-06-13 03:33:25.982714
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():

    collector = SshPubKeyFactCollector()

    class MockModule:
        def __init__(self):
            self.params = {}
            self.params['gather_subset'] = ['!all', 'ssh_pub_keys']
    mod = MockModule()
    facts = collector.collect(module=mod)
    assert len(facts) == 1

# Generated at 2022-06-13 03:33:34.602711
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    # Prepare mock data
    # Content of expected keys is copied from a Centos 7
    # system, which is expected to be the least common
    # denominator for acceptable key contents.
    algos = ('dsa', 'rsa', 'ecdsa', 'ed25519')
    keydirs = ['/etc/ssh', '/etc/openssh', '/etc']
    expect_key = {}
    for keydir in keydirs:
        for algo in algos:
            factname = 'ssh_host_key_%s_public' % algo
            expect_key[factname] = None
            factname_keytype = 'ssh_host_key_%s_public_keytype' % algo
            expect_key[factname_keytype] = None
    # These are the expected keys generated by centos/7

# Generated at 2022-06-13 03:33:44.741392
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    import os
    import tempfile
    import shutil
    import sys
    import textwrap

    # create a temporary directory
    tmpdir = tempfile.mkdtemp()
    os.chdir(tmpdir)

    # create the file structure for checking
    os.makedirs('/etc/ssh')
    os.makedirs('/etc/openssh')
    os.makedirs('/etc')
    os.makedirs('/etc/notssh')

# Generated at 2022-06-13 03:33:54.742400
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    # Mock AnsibleModule
    class mock_AnsibleModule:
        def __init__(self, *args, **kwargs):
            self.params = kwargs['params']

        def get_bin_path(self, *args, **kwargs):
            return args[0]

    params = {'paths': ['/etc/ssh', '/etc/openssh', '/etc']}
    obj = SshPubKeyFactCollector()
    test_module = mock_AnsibleModule(params=params)
    ssh_pub_key_facts = obj.collect(module=test_module)


# Generated at 2022-06-13 03:34:02.445775
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():

    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes, to_text

    from ansible.module_utils.facts.collector import BaseFactCollector

    from ansible.module_utils.facts.collectors.ssh_pub_keys import SshPubKeyFactCollector

    m_ansible_module = basic.AnsibleModule(
        argument_spec={})

    m_basic = basic

    m_base_fact_collector = BaseFactCollector

    m_ssh_pub_key_fact_collector = SshPubKeyFactCollector

    class MockModuleUtilsTextToBytes:

        @staticmethod
        def to_bytes(text):
            return text


# Generated at 2022-06-13 03:34:03.150236
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    pass

# Generated at 2022-06-13 03:34:04.507704
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():

    SshPubKeyFactCollector.collect()

# Generated at 2022-06-13 03:34:14.407341
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    ''' Unit test for method collect of class SshPubKeyFactCollector '''

# Generated at 2022-06-13 03:34:25.366585
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    import os
    import tempfile
    import os.path
    import shutil

    key_dir = tempfile.mkdtemp()
    key_file = os.path.join(key_dir, 'ssh_host_rsa_key.pub')

# Generated at 2022-06-13 03:34:30.788331
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    import tempfile
    import shutil
    import os
    from ansible.module_utils.facts.collector import CollectorCache

    module = None

    key_types = ['ssh-dss', 'ssh-rsa', 'ecdsa-sha2-nistp256', 'ssh-ed25519']

    import random
    random.seed()

    test_keys = []
    for key_type in key_types:
        test_keys.append(b' '.join([key_type.encode('ascii'),
                                    str(random.randint(0, 1000000)).encode('ascii'),
                                    str(random.randint(0, 1000000)).encode('ascii')]))


# Generated at 2022-06-13 03:34:42.489516
# Unit test for method collect of class SshPubKeyFactCollector

# Generated at 2022-06-13 03:34:48.632288
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():

    # Test with a directory which contains one of each openssh host key
    # Test with a directory which contains one of each openssh host key
    module_mock = MagicMock()
    module_mock.params = {"gather_subset": ["!all", "ssh"]}
    ssh_pub_key_facts_collector = SshPubKeyFactCollector()
    result = ssh_pub_key_facts_collector.collect(module_mock)


# Generated at 2022-06-13 03:34:58.258737
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    pubkey_fact_name = 'ssh_host_key_rsa_public'
    pubkey_file = '/etc/ssh/ssh_host_rsa_key.pub'
    pubkey_type = 'ssh-rsa'
    pubkey = 'AAAAB3NzaC1yc2EAAAABIwAAAQEAklOUpkDHrfHY17SbrmTIpNLTGK9Tjom/BWDSU'
    collected_facts = {'ansible_local': {'ssh_pub_keys': {}}}
    module = {"get_file_content.side_effect": [pubkey]}
    # check if in collected facts
    SshPubKeyFactCollector(module=module).collect()

# Generated at 2022-06-13 03:35:01.797383
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    """ Unit test for method collect of class SshPubKeyFactCollector """
    ssh_pub_key_fact_collector = SshPubKeyFactCollector()
    collected_facts = {}
    collected_facts = ssh_pub_key_fact_collector.collect(collected_facts=collected_facts)
    assert collected_facts['ssh_host_key_dsa_public']

# Generated at 2022-06-13 03:35:07.005207
# Unit test for method collect of class SshPubKeyFactCollector

# Generated at 2022-06-13 03:35:13.276522
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    ssh_pub_key_facts = SshPubKeyFactCollector.collect()
    assert 'ssh_host_key_dsa_public' in ssh_pub_key_facts
    assert 'ssh_host_key_rsa_public' in ssh_pub_key_facts
    assert 'ssh_host_key_ecdsa_public' in ssh_pub_key_facts
    assert 'ssh_host_key_ed25519_public' in ssh_pub_key_facts

# Generated at 2022-06-13 03:35:24.397826
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    obj = SshPubKeyFactCollector()
    ansible_module = DummyAnsibleModule('ssh_host_rsa_key.pub')
    obj.collect(ansible_module, None)
    assert len(ansible_module.params['ssh_host_pub_keys']) == 5

# Generated at 2022-06-13 03:35:27.946253
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    collector = SshPubKeyFactCollector()
    # a successful execution is tested with integration tests
    # this test just confirms that the ssh_pub_keys facts are collected
    ssh_pub_key_facts = collector.collect(None, {})
    assert ssh_pub_key_facts['ssh_host_key_dsa_public'] == 'AAAAB3NzaC1kc3MAAACBAO5j5Sd1+W' + \
        'f2Sl+YasVHjtZu8tCn0n+uF7ZpIWAsP8KvD0GV0zmJTp' + \
        'wgKs2sG7/ZJc2/Xo/b6RTCJYfN1yC0xmmUwN6oJH6r3q'

# Generated at 2022-06-13 03:35:39.351077
# Unit test for method collect of class SshPubKeyFactCollector

# Generated at 2022-06-13 03:35:50.708984
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    # When:
    ssh_pub_key_facts = SshPubKeyFactCollector().collect()

    # Then:

# Generated at 2022-06-13 03:36:02.656038
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    # Set up mocked module and return values
    #
    # Use a mock to override the get_file_content function
    # in the module_utils.facts.utils module.
    # Note: Since this is a class we need to use a nested function to get
    #       a reference to the nonlocal variables mocked_get_file_content
    #       and return_values. I don't know a better way to do this in
    #       Python 2.
    #
    # return_values is a list of sets of values that will be returned from
    # the mock.  The mocked function will pop the first set from the list
    # and return those values.  This lets us set up sequences of return
    # values.
    #
    return_values = []

# Generated at 2022-06-13 03:36:14.449105
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    collector = SshPubKeyFactCollector()
    collected_facts = collector.collect(module=None, collected_facts={})

    assert 'ssh_host_key_rsa_public' in collected_facts
    assert 'ssh_host_key_rsa_public_keytype' in collected_facts
    assert 'ssh_host_key_ecdsa_public' in collected_facts
    assert 'ssh_host_key_ecdsa_public_keytype' in collected_facts
    assert 'ssh_host_key_ed25519_public' in collected_facts
    assert 'ssh_host_key_ed25519_public_keytype' in collected_facts
    assert 'ssh_host_key_dsa_public' not in collected_facts
    assert 'ssh_host_key_dsa_public_keytype' not in collected_

# Generated at 2022-06-13 03:36:25.254181
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    import mock
    from ansible.module_utils.facts import FactsCollector
    from ansible.module_utils.facts.collector import BaseFactCollector, \
        SshPubKeyFactCollector
    from ansible.module_utils.facts.utils import get_file_content

    SshPubKeyFactCollector.collect = mock.MagicMock(return_value={})
    BaseFactCollector.collect = mock.MagicMock(return_value={})

    # Call collect and check that it calls the correct methods
    FactsCollector.collect([SshPubKeyFactCollector])
    assert SshPubKeyFactCollector.collect.called

    # Call collect and check that it calls the correct methods
    FactsCollector.collect([SshPubKeyFactCollector])
    assert BaseFactCollector.collect.called
    assert get_file

# Generated at 2022-06-13 03:36:29.296544
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    from ansible.module_utils.facts.collectors.ssh_pub_keys import SshPubKeyFactCollector
    ssh_pub_key_fact_collector = SshPubKeyFactCollector()
    assert ssh_pub_key_fact_collector.collect()

# Generated at 2022-06-13 03:36:38.164472
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    """
    Test the method collect defined in class SshPubKeyFactCollector
    """
    ssh_pub_key_facts = SshPubKeyFactCollector().collect(collected_facts=None)
    assert 'ssh_host_key_dsa_public' in ssh_pub_key_facts
    assert 'ssh_host_key_dsa_public_keytype' in ssh_pub_key_facts
    assert 'ssh_host_key_rsa_public' in ssh_pub_key_facts
    assert 'ssh_host_key_rsa_public_keytype' in ssh_pub_key_facts
    assert 'ssh_host_key_ecdsa_public' in ssh_pub_key_facts
    assert 'ssh_host_key_ecdsa_public_keytype' in ssh_pub_key_facts
   

# Generated at 2022-06-13 03:36:46.979757
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    # Can't use mock.patch here due to late binding
    import os
    import os.path

# Generated at 2022-06-13 03:36:56.986513
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    ssh_pub_key_facts = SshPubKeyFactCollector().collect()
    # example key from Fedora 25 /etc/ssh/ssh_host_ecdsa_key.pub
    assert ssh_pub_key_facts['ssh_host_key_ecdsa_public'] == \
         'AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBPmTzT7Xq8WqZCDBv/1iEDnbkFhMW8W/l1Rqs20i/CucY9X8qCZKjvZwPD+hD0eNs8fTyBbzuR7L+OeYfXvl8s='

# Generated at 2022-06-13 03:37:03.653263
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():

    module = None
    collected_facts = None

    def mock_get_file_content(filename):
        return "No content"

    test_func = SshPubKeyFactCollector().collect

    # test keys not found in any directory
    ssh_pub_key_facts = test_func(module, collected_facts)
    assert ssh_pub_key_facts == {}

    # test keys found in the first directory

# Generated at 2022-06-13 03:37:15.148684
# Unit test for method collect of class SshPubKeyFactCollector

# Generated at 2022-06-13 03:37:23.419827
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    import os

    import pytest

    from ansible.module_utils.facts.collector import BaseFactCollector

    def sample_collect(self, module=None, collected_facts=None):
        return {'ssh_host_key_ed25519_public': 'ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIOk0J0TkmCxT2TKQrFqOwqvv6UHr6UzX9jL39SlpO1'}

    # replace the collect method of SshPubKeyFactCollector
    # by the sample collect method
    SshPubKeyFactCollector.collect = sample_collect


# Generated at 2022-06-13 03:37:42.485952
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    # create a MockModule object to be able to call params and fail_json
    mm = MockModule()

    # create a MockCollector object to be able to call collect
    mc = MockCollector()

    # call collect
    ssh_pub_key_facts = SshPubKeyFactCollector().collect(module=mm,
                                                         collected_facts=mc)

    # check the result

# Generated at 2022-06-13 03:37:51.189029
# Unit test for method collect of class SshPubKeyFactCollector

# Generated at 2022-06-13 03:38:01.611812
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    import os
    import tempfile

    os.environ['ANSIBLE_LOCAL'] = '1'

    algos = ('dsa', 'rsa', 'ecdsa', 'ed25519')


# Generated at 2022-06-13 03:38:08.481729
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    from ansible.module_utils.facts.system.ssh_pub_keys import SshPubKeyFactCollector
    from ansible.module_utils.facts.system.ssh_pub_keys import get_file_content
    from ansible.module_utils._text import to_bytes

    try:
        from tests.unit.module_utils import temp_module_util_loader
    except ImportError:
        from ansible.module_utils import temp_module_util_loader

    # set up a fake file which mimics some of the data in /etc/ssh/ssh_host_*_key.pub
    KEYDIR = '/etc/test_ssh_pub_keys'

# Generated at 2022-06-13 03:38:15.436142
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    import mock
    import os
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.utils import get_file_content

    # remove any previous ssh key files from this directory
    keys_to_remove = ['ssh_host_dsa_key.pub',
                      'ssh_host_rsa_key.pub',
                      'ssh_host_ecdsa_key.pub',
                      'ssh_host_ed25519_key.pub']
    for key in keys_to_remove:
        key_path = os.path.join(os.getcwd(), key)
        if os.path.exists(key_path):
            os.remove(key_path)

    # create ssh key files

# Generated at 2022-06-13 03:38:26.415085
# Unit test for method collect of class SshPubKeyFactCollector

# Generated at 2022-06-13 03:38:35.707915
# Unit test for method collect of class SshPubKeyFactCollector

# Generated at 2022-06-13 03:38:40.058451
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    module = object()
    collected_facts = {}
    fact_collector = SshPubKeyFactCollector()
    # XXX: not a real test, just call method without setup or assertions
    fact_collector.collect(module=module, collected_facts=collected_facts)

# Generated at 2022-06-13 03:38:49.255187
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    '''Unit test for method collect of class SshPubKeyFactCollector'''
    ###########################################################################
    # When all keys are available, the keys are returned in facts
    ###########################################################################
    # Test setup
    ssh_pub_key_facts = {}
    fact_collector = SshPubKeyFactCollector(
        module=None, collected_facts=ssh_pub_key_facts)

    # Test run
    result = fact_collector.collect()

# Generated at 2022-06-13 03:38:59.310835
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    c = SshPubKeyFactCollector()

    # Test without ssh keys
    ret = c.collect()
    assert(ret.keys() == set())

    # Test with ssh key
    import tempfile
    tmpfile = tempfile.NamedTemporaryFile()
    tmpfile.write("ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIBXmAkEhDdG/PYDLBjhC/PzRFWV7/uJGCa8V7c3GqQNb7CJ bobbarker\n")
    tmpfile.flush()
    ret = c.collect(ssh_pub_key_facts={'/etc/ssh/ssh_host_ed25519_key.pub': tmpfile.name})

# Generated at 2022-06-13 03:39:24.784286
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    collector = SshPubKeyFactCollector()
    result = collector._collect_base_platform_facts()


# Generated at 2022-06-13 03:39:35.359222
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    tst_dict = {}
    m_facts = SshPubKeyFactCollector(None, None)
    ret = m_facts.collect(tst_dict)

    assert isinstance(ret, dict)
    assert len(ret) < 5 or 'ssh_host_key_rsa_public' in ret
    assert len(ret) < 5 or 'ssh_host_key_rsa_public_keytype' in ret
    assert len(ret) < 5 or 'ssh_host_key_dsa_public' in ret
    assert len(ret) < 5 or 'ssh_host_key_dsa_public_keytype' in ret
    assert len(ret) < 5 or 'ssh_host_key_ecdsa_public' in ret

# Generated at 2022-06-13 03:39:43.588534
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    # test with mock _file module
    # normal case, returned dict with all keys
    # existing file with content
    from ansible.module_utils.facts.collector import get_collector_instance
    from ansible.module_utils.facts.utils import mock_file_module
    from ansible.module_utils.facts.collector import AnsibleFileModule
    class fakeAnsibleModule(AnsibleFileModule):
        def __init__(self, *args, **kwargs):
            self._file = mock_file_module()

# Generated at 2022-06-13 03:39:54.348658
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    # Test in absence of the SSH keys
    module = mock.MagicMock()
    facts_collector = ssh_pub_key_collector.SshPubKeyFactCollector(module)
    ssh_pub_key_facts = facts_collector._collect()
    assert ssh_pub_key_facts == {}

    # Test in presence of the SSH keys
    module = mock.MagicMock()
    facts_collector = ssh_pub_key_collector.SshPubKeyFactCollector(module)
    ssh_pub_key_facts['ssh_host_key_ecdsa_public'] = "AAAA"
    ssh_pub_key_facts['ssh_host_key_ecdsa_public_keytype'] = "AAAA"

# Generated at 2022-06-13 03:39:59.768445
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    # Create a fake module and facts
    # An empty dict will work as the module and facts
    fake_module = dict()
    fake_facts = dict()
    # Create a new fact collector
    fact_collector = SshPubKeyFactCollector()
    # Run it
    fact_collector.collect(fake_module, fake_facts)
    # Test if the fact ssh_pub_key exists
    assert(fake_facts['ssh_host_pub_keys'] is not None)

# Generated at 2022-06-13 03:40:05.351459
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    ssh_pub_key_facts = SshPubKeyFactCollector().collect()
    assert "ssh_host_key_ed25519_public" in ssh_pub_key_facts
    assert "ssh_host_key_ed25519_public_keytype" in ssh_pub_key_facts


# Generated at 2022-06-13 03:40:08.895167
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    ssh_pub_key_facts = SshPubKeyFactCollector()
    assert ssh_pub_key_facts.collect() is not None
    # not much of a test, but look at the code coverage

# Generated at 2022-06-13 03:40:18.721912
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    """
    The SSH host key public keys could be stored in three different locations:
    /etc/openssh (CentOS, Fedora)
    /etc/ssh (Debian, Ubuntu)
    /etc (MacOS)
    If the keys are not found, it is normal and the ssh_host_key_* facts
    should be empty.
    """
    from ansible_collections.ansible.netcommon.tests.unit.compat import unittest
    from ansible_collections.ansible.netcommon.tests.unit.compat.mock import patch
    from ansible.module_utils.facts import FactCollector

    class TestSshPubKeyFactCollector(SshPubKeyFactCollector):
        # Define a mocked content for DMZ_SSH_HOST_KEY_RSA_PUBLIC
        DMZ_SS

# Generated at 2022-06-13 03:40:26.428293
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    sshPubKeyFactCollector = SshPubKeyFactCollector()
    module = None
    collected_facts = None
    ssh_pub_key_facts = None
    key_facts = None

    # Verify list of fact identifiers
    fact_ids = sshPubKeyFactCollector.collect_fact_ids()
    assert 'ssh_host_pub_keys' in fact_ids
    assert 'ssh_host_key_dsa_public' in fact_ids
    assert 'ssh_host_key_rsa_public' in fact_ids
    assert 'ssh_host_key_ecdsa_public' in fact_ids
    assert 'ssh_host_key_ed25519_public' in fact_ids
    assert len(fact_ids) == 5

    # Test keys not found
    ssh_pub_key_facts = sshPubKeyFact

# Generated at 2022-06-13 03:40:35.769109
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    class TestModule(object):
        def __init__(self, params=None, facts=None):
            self.params = params
            self.facts = facts

    class TestAnsibleModule(object):
        def __init__(self, module_name='Ignored',
                     module_args=None,
                     module_class=TestModule):
            self.module_name = module_name
            self.module_args = module_args
            self.module = module_class(params=module_args)

        def get_bin_path(self, executable_name, required=True, opt_dirs=[]):
            if executable_name == 'ssh-keygen':
                executable_name = 'fake_ssh-keygen'
            return executable_name

    class FakeResult(object):
        def __init__(self):
            self

# Generated at 2022-06-13 03:41:16.739220
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    # create a mock version of AnsibleModule
    class MockAnsibleModule():
        def __init__(self):
            self.params = dict()

    # create a mock version of arguments to SshPubKeyFactCollector
    class MockSshPubKeyFactCollectorArgs(object):
        def __init__(self):
            self.module = MockAnsibleModule()
            self.module.params = dict(
                keysdirs=["/tmp/keydir"]
            )
            # these facts are global across modules, but we need to declare
            # them in the scope of the SshPubKeyFactCollector module
            self.collected_facts = dict(
                ansible_local=dict(ssh_pub_key_facts=dict())
            )

    # create a mock version of get_file_content

# Generated at 2022-06-13 03:41:27.889907
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.utils import get_file_content
    import os

    Facter = Collector()
    SshPubKeyFactCollector = SshPubKeyFactCollector()
    get_file_content_orig = get_file_content

    if (hasattr(Facter, 'collected_facts')):
        Facter.collected_facts = {}

    def get_file_content_mock(filename):
        content = '{0} ssh-rsa {1} {2}\n'.format('testhost', 'testhosttesthosttesthosttesthosttesthosttesthosttesthosttesthosttesthosttesthosttesthosttesthost', 'testhosttesthosttesthosttesthosttesthosttesthosttesthosttesthosttesthosttesthosttesthosttesthost')
       

# Generated at 2022-06-13 03:41:35.175383
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    from ansible.module_utils.facts.collector import FactsCollector
    from ansible.module_utils.facts import FactCache

    ssh_pub_key_facts = SshPubKeyFactCollector()
    facts = ssh_pub_key_facts.collect()
    assert 'ssh_host_key_dsa_public' in facts
    assert 'ssh_host_key_rsa_public' in facts
    assert 'ssh_host_key_ecdsa_public' in facts
    assert 'ssh_host_key_ed25519_public' in facts
    assert 'ssh_host_key_ed25519_public_keytype' in facts

# Generated at 2022-06-13 03:41:43.827062
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    collector = SshPubKeyFactCollector()
    facts = collector.collect()
    for key in ('ssh_host_key_dsa_public', 'ssh_host_key_rsa_public',
                'ssh_host_key_ecdsa_public', 'ssh_host_key_ed25519_public'):
        assert key in facts
    assert 'ssh_host_pub_keys' in facts
    assert 'ssh_host_pub_keys' in facts['ssh_host_key_dsa_public']
    assert 'ssh_host_pub_keys' in facts['ssh_host_key_rsa_public']
    assert 'ssh_host_pub_keys' in facts['ssh_host_key_ecdsa_public']

# Generated at 2022-06-13 03:41:46.911370
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    pub_keys = SshPubKeyFactCollector().collect()
    assert 'ssh_host_key_rsa_public' in pub_keys
    assert 'ssh_host_key_rsa_public_keytype' in pub_keys

# Generated at 2022-06-13 03:41:55.789509
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    # Arrange
    module = None
    collected_facts = {}
    algos = ('dsa', 'rsa', 'ecdsa', 'ed25519')
    ssh_pub_key_facts = {}
    for algo in algos:
        factname = 'ssh_host_key_%s_public' % algo
        factname_keytype = factname + '_keytype'
        factvalue = 'test_value'
        factvalue_keytype = 'test_keytype'
        ssh_pub_key_facts[factname] = factvalue
        ssh_pub_key_facts[factname_keytype] = factvalue_keytype

    expected_facts = dict(ssh_host_pub_keys=ssh_pub_key_facts)
    # Act
    actual_facts = SshPubKeyFactCollect

# Generated at 2022-06-13 03:42:01.789041
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    # Test for content of key file
    mock_get_file_content = lambda x: 'ssh-rsa AAAA'
    SshPubKeyFactCollector._get_file_content = mock_get_file_content

    # Test for empty key file
    ssh_pub_key_facts1 = SshPubKeyFactCollector().collect()
    for key in SshPubKeyFactCollector._fact_ids:
        assert(ssh_pub_key_facts1.get(key) is None)

    # Setup of key files
    mock_get_file_content = lambda x: 'ssh-rsa AAAA'
    SshPubKeyFactCollector._get_file_content = mock_get_file_content

    # Test for successful key file in first directory

# Generated at 2022-06-13 03:42:11.188441
# Unit test for method collect of class SshPubKeyFactCollector

# Generated at 2022-06-13 03:42:20.710082
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    import ansible.module_utils.facts.collector
    from ansible.module_utils.facts.utils import get_file_content
    import shutil
    import tempfile
    import os
    tmpdir = tempfile.mkdtemp()
    assert not os.path.exists(tmpdir + '/etc/ssh')
    assert not os.path.exists(tmpdir + '/etc/openssh')
    assert not os.path.exists(tmpdir + '/etc')
    shutil.copytree(os.path.dirname(ansible.module_utils.facts.collector.__file__) + '/__test__/ssh_pub_keys_test',
                    tmpdir)
    old_get_file_content = get_file_content

# Generated at 2022-06-13 03:42:26.708659
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    from ansible_collections.community.general.plugins.module_utils.facts import collector

    collector.collectors = [SshPubKeyFactCollector]
    collected_facts = collector.collect(None)
    assert type(collected_facts['ssh_host_pub_keys']) is list
    assert type(collected_facts['ssh_host_key_dsa_public']) is str
    assert type(collected_facts['ssh_host_key_ecdsa_public']) is str
    assert type(collected_facts['ssh_host_key_rsa_public']) is str
    assert type(collected_facts['ssh_host_key_ed25519_public']) is str