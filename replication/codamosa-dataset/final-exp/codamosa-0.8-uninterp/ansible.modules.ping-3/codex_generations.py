

# Generated at 2022-06-13 05:49:06.835698
# Unit test for function main
def test_main():
    import os
    import tempfile
    tmp_path = tempfile.mkdtemp()


# Generated at 2022-06-13 05:49:11.841855
# Unit test for function main
def test_main():
    module_args = dict(
        data='pong'
    )
    result = dict(
        ping='pong'
    )
    with patch.object(AnsibleModule, 'exit_json') as exit_json_mock:
        module = AnsibleModule(args=module_args)
        main()
        exit_json_mock.assert_called_once_with(**result)

        module_args = dict(
            data='crash'
        )
        result = dict(
            ping='pong'
        )
        with patch.object(AnsibleModule, 'exit_json') as exit_json_mock:
            module = AnsibleModule(args=module_args)
            with self.assertRaises(Exception):
                main()

# Generated at 2022-06-13 05:49:17.359998
# Unit test for function main
def test_main():
    args = dict(
        data=dict(type='str', default='pong'),
    )

    values = dict(
        ping=dict(type='str', default='pong'),
    )

    result = dict(
        ping=args['data'],
    )

    my_result = main(args)

    assert my_result['ping'] == result['ping']

# Generated at 2022-06-13 05:49:29.225559
# Unit test for function main

# Generated at 2022-06-13 05:49:30.099423
# Unit test for function main
def test_main():
    # no tests to perform yet
    pass

# Generated at 2022-06-13 05:49:34.107704
# Unit test for function main
def test_main():
    with patch.object(AnsibleModule, 'exit_json') as exit_json:
        module = AnsibleModule(
            argument_spec=dict(
                data=dict(type='str', default='pong'),
            ),
            supports_check_mode=True
        )
        main()
        exit_json.assert_called_once_with(
            changed=False,
            ping=module.params['data'],
        )

# Generated at 2022-06-13 05:49:41.458675
# Unit test for function main
def test_main():
    try:
        import ansible.module_utils.basic
    except ImportError as ex:
        print('Skipped as ansible.module_utils.basic is not installed')
        return

    import inspect
    import types

    # Free function.
    func = main
    req_args = ['check_mode', 'data']
    opt_args = []

    # Arguments generated by module
    # Called with `ansible-playbook --connection=local play.yml`
    params_ansible = dict(  # ansible-playbook
        args=dict(
            data='pong',
        ),
        connection='local',
        diff=False,
        check=False,
        diff_mode=False,
    )

    # Local AnsibleModule for calling main

# Generated at 2022-06-13 05:49:46.775481
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    if module.params['data'] == 'crash':
        raise Exception("boom")

    result = dict(
        ping=module.params['data'],
    )

    module.exit_json(**result)


if __name__ == '__main__':
    test_main()

# Generated at 2022-06-13 05:49:54.078115
# Unit test for function main
def test_main():
    test_input = {}
    test_result = {}
    # create patch for module ansible.module_utils.basic
    patch_result = {}
    patch_m1_result = {}
    # set param for patch
    patch_result['_ansible_check_mode'] = False
    patch_result['_ansible_no_log'] = False
    patch_result['_ansible_debug'] = False
    patch_result['_ansible_diff'] = False
    patch_result['_ansible_is_subset'] = True
    patch_result['argument_spec'] = {'data': {'type': 'str', 'default': 'pong'}}
    patch_result['check_mode'] = True
    patch_result['supports_check_mode'] = True

# Generated at 2022-06-13 05:49:57.835614
# Unit test for function main
def test_main():
    input_result = dict(
        data=dict(type='str', default='pong'),
    )
    input_result_check = dict(
        supports_check_mode = True,
    )
    input_exit_result = dict(
        ping='pong',
    )
    assert input_result_check == main(input_result)
    assert input_exit_result == main(input_result)

# Generated at 2022-06-13 05:50:10.570325
# Unit test for function main
def test_main():
    # import module snippets
    from ansible.module_utils.basic import AnsibleModule, env_fallback, return_values

    # Logic to run when testing
    data = dict(
        data='crash',
    )

    # Result of the function
    result = dict(
        ansible_facts=dict(
            ping='crash',
        )
    )

    # Setup AnsibleModule mock
    fake_module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    # Fake load_params
    fake_module.load_params(mock.Mock(**data))

    # Fake main()
    main()

    # Assertions

# Generated at 2022-06-13 05:50:15.463228
# Unit test for function main
def test_main():
    global module
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    module.exit_json = lambda **args: args
    result = module.exit_json(ping="pong")
    assert result == {'msg': 'pong', 'changed': False}

# Generated at 2022-06-13 05:50:18.826224
# Unit test for function main
def test_main():
    import pytest

    with pytest.raises(Exception) as execinfo:
        main()
        assert 'boom' in str(execinfo.value)

# Generated at 2022-06-13 05:50:21.746706
# Unit test for function main
def test_main():
    # Parameters
    data = "crash"
    module_params = {"data":data}
    ping = main(module_params)
    assert ping == { "ping" : "crash" }

# Generated at 2022-06-13 05:50:22.272931
# Unit test for function main
def test_main():
    assert main()

# Generated at 2022-06-13 05:50:26.453796
# Unit test for function main
def test_main():
    with patch('ansible_collections.ansible.builtin.plugins.modules.ping.AnsibleModule') as MockModule:
        instance = MockModule.return_value
        instance.params = {"data": "pong"}
        main()
        assert MockModule.call_args == call(argument_spec={"data": {"type": "str", "default": "pong"}}, supports_check_mode=True)


# Generated at 2022-06-13 05:50:37.301458
# Unit test for function main
def test_main():
    with open('test/ansible/builtin/ping_data.json') as f:
        data = json.load(f)

    input = data[1]
    expected = data[0]

    if os.path.exists('test/ansible/builtin/ping_input.json'):
        with open('test/ansible/builtin/ping_input.json') as f:
            input = json.load(f)

    if os.path.exists('test/ansible/builtin/ping_expected.json'):
        with open('test/ansible/builtin/ping_expected.json') as f:
            expected = json.load(f)

    module = AnsibleModule(argument_spec={'data': {"required":True,"type":"str"}})

# Generated at 2022-06-13 05:50:42.651547
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    assert main() == dict(
        ansible_module_results=dict(
            ping=module.params['data'],
        ),
    )

# Generated at 2022-06-13 05:50:48.221558
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    assert module.params['data'] == 'pong'
    assert module.params.get('data') == 'pong'
    assert module.params.get('foo') == None

# Generated at 2022-06-13 05:50:50.676624
# Unit test for function main
def test_main():
    result = dict(
        ping=module.params['data'],
    )
    assert result == {'ping': 'pong'}

# Generated at 2022-06-13 05:51:06.211069
# Unit test for function main
def test_main():
    import tempfile
    import json
    import sys

    # Make sure we are in the same directory as ansible so we can find the ping module
    tempdir = tempfile.gettempdir()

    sys.path.append(tempdir)
    reload(ping)
    # Make a fake module
    module = dict()
    module['params'] = dict()

    # Make a fake module.exit and assert it is called with the right result
    module['exit_json'] = fake_exit_json
    def fake_exit_json(result):
        assert result == dict(changed=False, ping=dict(ping='pong'))

    # Run the ping module and assert that exit_json is called with the right params.
    ping.main()


# Unit test function for function main

# Generated at 2022-06-13 05:51:12.652388
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    result = dict(
        ping=module.params['data'],
    )
    if module.params['data'] == 'crash':
        raise Exception("boom")
    module.exit_json(**result)

# Generated at 2022-06-13 05:51:15.947845
# Unit test for function main
def test_main():
   assert main() is None

# Generated at 2022-06-13 05:51:18.429916
# Unit test for function main
def test_main():
    m = AnsibleModule(argument_spec=dict(data=dict(type='str', default='pong')))
    results = main.__wrapped__(m)
    assert results['ping'] == 'pong'

# Generated at 2022-06-13 05:51:28.621889
# Unit test for function main

# Generated at 2022-06-13 05:51:36.581890
# Unit test for function main
def test_main():
    m = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
    )

    assert m.params['data'] == 'pong'
    assert m.params['data'] != 'crash'
    assert m.check_mode != True

    result = dict(
        ping=m.params['data'],
    )

# ansible-test compatibility
from ansible_test.unit.compat.mock import patch

with patch('ansible.module_utils.basic.AnsibleModule') as mock:
    mock.return_value = test_main()

# Generated at 2022-06-13 05:51:37.910698
# Unit test for function main
def test_main():
    # Placeholder for real unit tests
    assert True

# Generated at 2022-06-13 05:51:49.166007
# Unit test for function main
def test_main():
    with patch('ansible.module_utils.basic.AnsibleModule') as A:
        with patch('ansible.module_utils.basic.return_values') as R:
            with patch('ansible.module_utils.basic.exit_json') as E:
                R.return_value = dict(
                    ping='pong',
                )
                E.return_value = dict(
                    changed=False,
                    ping='pong',
                )
                A.return_value = dict(
                    params=dict(
                        data='pong',
                    ),
                )
                main()
                assert A.call_count == 1

# Generated at 2022-06-13 05:51:56.606838
# Unit test for function main
def test_main():
    # AnsibleModule mocks module from ansible.module_utils.basic
    class AnsibleModuleMock(object):

        # Mock init method. 
        # Returns a mock module with params and exit_json method
        @staticmethod
        def init(spec, **kwargs):
            self = AnsibleModule(spec, **kwargs)
            return self

        # Define return values of all execute_methods and methods.
        # return_values is a dictionary with keys as the method name
        # and values as lists of return values.
        # E.g. return_values = {'execute_foo': ['foo','foo','foo'], 'foo': ['foo','foo']}

        return_values = {}

        # Mock a call to the init method.
        # init_results is a list of return values for the init method.
        # E

# Generated at 2022-06-13 05:52:07.966384
# Unit test for function main
def test_main():
    output = dict(
        ping='pong')
    from ansible_collections.ansible.builtin.plugins.module_utils import basic
    import ansible_collections.ansible.builtin.plugins.modules.ping
    module = ansible_collections.ansible.builtin.plugins.modules.ping.AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    ansible_collections.ansible.builtin.plugins.modules.ping.main()
    assert basic.AnsibleModule.exit_json.called
    assert basic.AnsibleModule.exit_json.call_args[0][0] == output

# Generated at 2022-06-13 05:52:30.121766
# Unit test for function main
def test_main():
    result = dict(
        ping=module.params['data'],
    )
    module.exit_json(**result)


Methods

get_bin_path

# Generated at 2022-06-13 05:52:32.152681
# Unit test for function main
def test_main():
    my_host = { "data": 'pong' }
    assert main() == my_host

# Generated at 2022-06-13 05:52:37.719468
# Unit test for function main
def test_main():
    test_module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    m_exit_json = test_module.exit_json
    m_params = test_module.params
    m_params['data'] = 'crash'
    if m_params['data'] == 'crash':
        raise Exception("boom")
    result = dict(
        ping=m_params['data'],
    )
    m_exit_json(**result)

# Generated at 2022-06-13 05:52:38.211072
# Unit test for function main
def test_main():
    assert main() is None

# Generated at 2022-06-13 05:52:45.149445
# Unit test for function main

# Generated at 2022-06-13 05:52:53.400136
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    try:
        if module.params['data'] == 'crash':
            raise Exception("boom")
    except Exception as e:
        with pytest.raises(Exception) as e_info:
            result = dict(
                ping=module.params['data'],
            )
    else:
        result = dict(
            ping=module.params['data'],
        )
    assert result == {u'ping': 'pong'}


# Generated at 2022-06-13 05:53:03.300288
# Unit test for function main
def test_main():
    # test positive outcome
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    result = dict(
        ping=module.params['data'],
    )
    assert result['ping'] == 'pong'

    # test negative outcome using a test case
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    result = dict(
        ping=module.params['data'],
    )
    assert result['ping'] != 'this is an invalid outcome'

# Generated at 2022-06-13 05:53:09.503087
# Unit test for function main
def test_main():
    # Just a basic smoke test
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    module.params['data'] = 'crash'
    try:
        main()
    except Exception as e:
        assert 'boom' in e.message

# Generated at 2022-06-13 05:53:09.852319
# Unit test for function main
def test_main():
    print(main())

# Generated at 2022-06-13 05:53:14.165050
# Unit test for function main
def test_main():
    with patch('ansible.module_utils.basic.AnsibleModule') as mock_module:
        mock_module.return_value = mock.Mock(
            argument_spec=dict(
                data=dict(type='str', default='pong'),
            ),
            supports_check_mode=True
        )
        main()
        mock_module_instance = mock_module()
        mock_module_instance.exit_json.assert_called_once_with(
            ping='pong'
        )

# Generated at 2022-06-13 05:53:50.367877
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    if module.params['data'] == 'crash':
        raise Exception("boom")

    result = dict(
        ping=module.params['data'],
    )

    assert result == {'ping': 'pong'}


# Generated at 2022-06-13 05:53:56.719829
# Unit test for function main
def test_main():
    with mock.patch.object(sys, 'argv', ['ansible-test', 'ping', '{"data": "pong"}']):
        with mock.patch.object(sys, 'stdout') as mock_stdout:
            with mock.patch.object(sys, 'stderr') as mock_stderr:
                with pytest.raises(SystemExit) as excinfo:
                    main()
                assert excinfo.value.code == 0

        assert mock_stderr.getvalue() == ''
        assert mock_stdout.getvalue() == '{"changed": false, "ping": "pong"}\n'

# Generated at 2022-06-13 05:54:02.335137
# Unit test for function main
def test_main():
    args = dict(
        data='pong',
    )
    with mock.patch.object(AnsibleModule, 'exit_json') as exit_json, \
        mock.patch.object(AnsibleModule, 'params') as params:
        params.__getitem__.side_effect = args.__getitem__
        main()
        exit_json.assert_called_with(ping='pong')


# Generated at 2022-06-13 05:54:09.344348
# Unit test for function main
def test_main():
    # This is a test using the unittest module.

    # Import modules and objects
    import sys
    import unittest
    # This is the module to be tested
    sys.path.append('../')
    from ping import main

    # Define test information
    class TestMain(unittest.TestCase):

        # Define unit tests as functions
        def test_ansible_module_main(self):
            ''' This is a unit test for the ansible module
            '''
            # Define module arguments
            module_args = dict(
                data='pong',
            )

            # Create a mock module object
            mock_args = dict(
                params=module_args
            )
            mock_module = type('', (), mock_args)()

            # Define correct exit arguments

# Generated at 2022-06-13 05:54:14.343373
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    if module.params['data'] == 'crash':
        raise Exception("boom")

    result = dict(
        ping=module.params['data'],
    )

    module.exit_json(**result)


# Generated at 2022-06-13 05:54:20.894959
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    assert(module.params['data'] == 'pong')
    assert(module.params['data'] != 'crash')


# Generated at 2022-06-13 05:54:25.035244
# Unit test for function main
def test_main():
	data = dict(
        data=dict(type='str', default='pong'),
    )
	result = dict(
        ping=data['data'],
    )
	return result

# Generated at 2022-06-13 05:54:29.318591
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    main()
    assert module.params.get('data') == 'pong', 'Data default value is not correct'


# Generated at 2022-06-13 05:54:29.853029
# Unit test for function main
def test_main():
  pass

# Generated at 2022-06-13 05:54:35.488991
# Unit test for function main
def test_main():
    # import module snippet
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    test_param = 'pong'
    result = dict(
        ping=test_param,
    )

    module.exit_json(**result)
    # assert result['ping'] == test_param
# test_main()

# Generated at 2022-06-13 05:55:50.513013
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
  

# Generated at 2022-06-13 05:55:57.990870
# Unit test for function main
def test_main():
    sentinel = object()
    data = sentinel
    def mock_exit_json(rc=None, **kwargs):
        assert rc == 0
        assert kwargs['ping'] == 'pong'
    mock_module = Mock()
    mock_module.params = {'data': 'pong'}
    mock_module.exit_json.side_effect = mock_exit_json

    with patch.object(ansible.module_utils.basic, 'AnsibleModule', return_value=mock_module):
        main()

# Generated at 2022-06-13 05:56:03.840795
# Unit test for function main
def test_main():
    data = {
        'data' : 'pong'
    }
    ansible_module = MockedModule(**data)
    main()
    assert ansible_module.exit_json_called
    assert not ansible_module.fail_json_called
    assert ansible_module.exit_json_kwargs == dict(
        ping='pong'
    )


# Generated at 2022-06-13 05:56:10.742427
# Unit test for function main
def test_main():

# Module Ping is not supported in Windows
    from ansible.module_utils.common.removed import removed_module

    with pytest.raises(removed_module):
        main()

# Requiring in this test file so that we can use MOCK_PLUGIN_PATH
from ansible.module_utils.six import PY2
from ansible.module_utils import basic

# Plugin name to be used in dynamic plugins call
MODULE_NAME = 'ansible.builtin.ping'


# Generated at 2022-06-13 05:56:11.438556
# Unit test for function main
def test_main():
  main()

# Generated at 2022-06-13 05:56:22.622803
# Unit test for function main
def test_main():
    test_args = {}
    test_args['data'] = 'crash'
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    result = module.params['data']
    # Check if the result is as expected
    assert result == test_args['data']
    test_args['data'] = 'pong'
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    result = module.params['data']
    # Check if the result is as expected
    assert result == test_args['data']
    test_args['data'] = ''
    module

# Generated at 2022-06-13 05:56:31.151800
# Unit test for function main
def test_main():
    from ansible.modules.core import ping
    import ansible.module_utils.basic
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes

    module = AnsibleModule(argument_spec={'data': {'type': 'str', 'default': 'pong'}})
    m_run_command = module.run_command = MagicMock()
    m_run_command.return_value = (0, b'pong', b'')
    m_fail_json = module.fail_json = MagicMock()
    m_exit_json = module.exit_json = MagicMock()

    ping.main()
    m_exit_json.assert_called_with(changed=False, ping="pong")
    m_fail_json.assert_not

# Generated at 2022-06-13 05:56:35.074789
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    if module.params['data'] == 'crash':
        raise Exception("boom")

    result = dict(
        ping=module.params['data'],
    )

    module.exit_json(**result)

# Generated at 2022-06-13 05:56:36.977913
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    assert main() is NotImplementedError

# Generated at 2022-06-13 05:56:40.683225
# Unit test for function main
def test_main():

    # Set up arguments
    module = AnsibleModule(argument_spec={'data': dict(type='str', default='pong')})

    result = dict(
        ping=module.params['data'],
    )
    module.exit_json(**result)

