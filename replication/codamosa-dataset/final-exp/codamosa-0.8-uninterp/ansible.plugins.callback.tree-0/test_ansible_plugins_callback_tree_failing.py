# Automatically generated by Pynguin.
import ansible.plugins.callback.tree as module_0
import ansible.plugins.callback as module_1

def test_case_0():
    try:
        callback_module_0 = module_0.CallbackModule()
        callback_module_1 = module_0.CallbackModule()
        str_0 = '\n        Returns a list of host names matching the given pattern according to the\n        rules explained above in _match_one_pattern.\n        '
        callback_module_2 = module_0.CallbackModule()
        var_0 = callback_module_2.set_options(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.write_tree_file(callback_module_0, callback_module_0)
    except BaseException:
        pass

def test_case_2():
    try:
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_runner_on_ok(callback_module_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '\n- debug: msg="User in integration is {{ lookup(\'ini\', \'user\', section=\'integration\', file=\'users.ini\') }}"\n\n- debug: msg="User in production  is {{ lookup(\'ini\', \'user\', section=\'production\',  file=\'users.ini\') }}"\n\n- debug: msg="user.name is {{ lookup(\'ini\', \'user.name\', type=\'properties\', file=\'user.properties\') }}"\n\n- debug:\n    msg: "{{ item }}"\n  loop: "{{ q(\'ini\', \'.*\', section=\'section1\', file=\'test.ini\', re=True) }}"\n\n- name: Read ini file with allow_no_value\n  debug:\n    msg: "{{ lookup(\'ini\', \'user\', file=\'mysql.ini\', section=\'mysqld\', allow_no_value=True) }}"\n'
        set_0 = set()
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_runner_on_failed(str_0, set_0)
    except BaseException:
        pass

def test_case_4():
    try:
        callback_module_0 = module_0.CallbackModule()
        callback_module_1 = module_0.CallbackModule()
        int_0 = 3903
        var_0 = callback_module_1.v2_runner_on_unreachable(int_0)
    except BaseException:
        pass

def test_case_5():
    try:
        callback_module_0 = module_0.CallbackModule()
        str_0 = 'tree'
        var_0 = setattr(callback_module_0, str_0, callback_module_0)
        list_0 = None
        callback_base_0 = module_1.CallbackBase()
        dict_0 = {str_0: str_0, str_0: callback_module_0, str_0: list_0, callback_base_0: list_0}
        var_1 = callback_module_0.write_tree_file(list_0, dict_0)
    except BaseException:
        pass