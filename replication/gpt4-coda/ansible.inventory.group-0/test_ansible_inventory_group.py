# Automatically generated by Pynguin.
import ansible.inventory.group as module_0

def test_case_0():
    group_0 = module_0.Group()

def test_case_1():
    str_0 = '\x0child'
    group_0 = module_0.Group(str_0)

def test_case_2():
    str_0 = 'parent'
    group_0 = module_0.Group(str_0)
    group_1 = module_0.Group(str_0)
    var_0 = group_0.add_child_group(group_1)
    var_1 = group_0.__repr__()

def test_case_3():
    group_0 = module_0.Group()
    var_0 = group_0.serialize()

def test_case_4():
    str_0 = 'failed to look up user %s. Create user up to this point in real play'
    int_0 = 27
    group_0 = module_0.Group()
    var_0 = group_0.set_priority(int_0)
    group_1 = module_0.Group(str_0)
    var_1 = group_0.get_descendants()
    group_2 = module_0.Group()
    var_2 = group_2.get_vars()
    dict_0 = {group_2: var_2, group_2: var_2, group_2: var_2}
    var_3 = group_2.deserialize(dict_0)
    var_4 = group_2.get_vars()
    dict_1 = None
    bool_0 = False
    tuple_0 = (dict_1, bool_0)
    int_1 = -4753
    var_5 = group_2.set_variable(tuple_0, int_1)
    var_6 = group_2.deserialize(dict_0)

def test_case_5():
    group_0 = module_0.Group()
    var_0 = group_0.get_hosts()

def test_case_6():
    group_0 = module_0.Group()
    group_1 = module_0.Group()
    var_0 = group_1.add_child_group(group_0)

def test_case_7():
    group_0 = module_0.Group()
    var_0 = group_0.get_name()

def test_case_8():
    group_0 = module_0.Group()
    var_0 = group_0.get_vars()

def test_case_9():
    str_0 = 'tQm'
    group_0 = module_0.Group(str_0)
    group_1 = module_0.Group()
    var_0 = group_1.clear_hosts_cache()

def test_case_10():
    group_0 = module_0.Group()
    var_0 = group_0.__str__()
    group_1 = module_0.Group()
    var_1 = group_1.get_vars()
    var_2 = group_1.get_hosts()
    var_3 = group_1.__str__()
    group_2 = module_0.Group()
    var_4 = group_0.add_child_group(group_1)
    var_5 = group_1.get_ancestors()
    var_6 = group_2.__getstate__()
    group_3 = module_0.Group()
    var_7 = group_0.get_hosts()

def test_case_11():
    str_0 = 'name'
    str_1 = 'vars'
    str_2 = 'depth'
    str_3 = 'hosts'
    str_4 = 'parent_groups'
    str_5 = 'testgroup'
    int_0 = 2
    str_6 = 'host1'
    str_7 = 'host2'
    str_8 = [str_6, str_7]
    str_9 = 'parentgroup'
    var_0 = {}
    int_1 = 1
    var_1 = []
    var_2 = []
    var_3 = {str_0: str_9, str_1: var_0, str_2: int_1, str_3: var_1, str_4: var_2}
    var_4 = [var_3]
    var_5 = {str_0: str_5, str_1: str_4, str_2: int_0, str_3: str_8, str_4: var_4}
    group_0 = module_0.Group()
    var_6 = group_0.deserialize(var_5)
    var_7 = group_0.parent_groups
    var_8 = len(var_7)

def test_case_12():
    str_0 = 'testgroup'
    group_0 = module_0.Group(str_0)
    str_1 = 'test_key'
    str_2 = 'test_value'
    var_0 = group_0.set_variable(str_1, str_2)
    str_3 = 'test_dict'
    str_4 = 'nested_key'
    str_5 = 'nested_value'
    str_6 = {str_4: str_5}
    var_1 = group_0.set_variable(str_3, str_6)
    str_7 = 'another_key'
    str_8 = 'another_value'
    str_9 = {str_7: str_8}
    var_2 = group_0.set_variable(str_3, str_9)

def test_case_13():
    str_0 = 'testgroup'
    group_0 = module_0.Group(str_0)
    str_1 = 'ansible_ssh_settings'
    str_2 = 'user'
    str_3 = 'port'
    var_0 = group_0.set_variable(str_1, str_2)
    str_4 = 'timeout'
    int_0 = 2222
    int_1 = 30
    int_2 = {str_3: int_0, str_4: int_1}
    var_1 = group_0.set_variable(str_1, int_2)

def test_case_14():
    str_0 = 'parent'
    group_0 = module_0.Group(str_0)
    str_1 = 'child'
    group_1 = module_0.Group(str_1)
    var_0 = group_0.add_child_group(group_1)
    var_1 = group_0.add_child_group(group_1)

def test_case_15():
    str_0 = 'testgroup'
    group_0 = module_0.Group(str_0)
    str_1 = 'ansible_group_priority'
    str_2 = '42'
    var_0 = group_0.set_variable(str_1, str_2)
    str_3 = 'some_var'
    str_4 = 'some_value'
    var_1 = group_0.set_variable(str_3, str_4)
    str_5 = 'dict_var'
    str_6 = 'key'
    str_7 = 'value'
    str_8 = {str_6: str_7}
    var_2 = group_0.set_variable(str_5, str_8)

def test_case_16():
    str_0 = 'testgroup'
    group_0 = module_0.Group(str_0)
    str_1 = 'ansible_connection'
    str_2 = '03v$CUg'
    var_0 = group_0.set_variable(str_1, str_2)
    str_3 = 'ansible_ssh_settings'
    str_4 = 'usr'
    str_5 = 'port'
    int_0 = 22
    var_1 = {str_4: str_3, str_5: int_0}
    var_2 = group_0.set_variable(str_3, var_1)
    int_1 = 2193
    var_3 = group_0.set_variable(str_3, int_1)