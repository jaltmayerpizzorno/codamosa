# Automatically generated by Pynguin.
import ansible.inventory.group as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = "e[s'"
    group_0 = module_0.Group(str_0)

def test_case_2():
    group_0 = module_0.Group()

def test_case_3():
    group_0 = module_0.Group()
    var_0 = group_0.__repr__()

def test_case_4():
    group_0 = module_0.Group()
    var_0 = group_0.__str__()
    dict_0 = {var_0: group_0, group_0: var_0, var_0: var_0, group_0: group_0}
    var_1 = group_0.__setstate__(dict_0)

def test_case_5():
    group_0 = module_0.Group()
    var_0 = group_0.__getstate__()

def test_case_6():
    group_0 = module_0.Group()
    var_0 = group_0.get_hosts()

def test_case_7():
    group_0 = module_0.Group()
    var_0 = group_0.clear_hosts_cache()
    var_1 = group_0.__getstate__()

def test_case_8():
    group_0 = module_0.Group()
    var_0 = group_0.get_name()

def test_case_9():
    group_0 = module_0.Group()
    group_1 = module_0.Group()
    var_0 = group_1.add_child_group(group_0)

def test_case_10():
    group_0 = module_0.Group()
    var_0 = group_0.remove_host(group_0)

def test_case_11():
    str_0 = None
    bool_0 = False
    group_0 = module_0.Group()
    var_0 = group_0.set_variable(str_0, bool_0)
    var_1 = group_0.remove_host(group_0)

def test_case_12():
    group_0 = module_0.Group()
    var_0 = group_0.get_vars()

def test_case_13():
    group_0 = module_0.Group()
    var_0 = group_0.serialize()
    set_0 = None
    var_1 = group_0.set_priority(set_0)
    var_2 = group_0.get_ancestors()
    var_3 = group_0.__getstate__()

def test_case_14():
    group_0 = module_0.Group()
    group_1 = module_0.Group()
    var_0 = group_0.add_child_group(group_1)
    var_1 = group_1.serialize()

def test_case_15():
    group_0 = module_0.Group()
    var_0 = group_0.set_priority(group_0)
    var_1 = group_0.get_name()
    group_1 = module_0.Group()
    var_2 = group_0.add_child_group(group_1)
    var_3 = group_0.serialize()
    var_4 = group_0.serialize()
    var_5 = group_0.serialize()
    var_6 = group_1.clear_hosts_cache()

def test_case_16():
    str_0 = 'G2'
    group_0 = module_0.Group(str_0)
    str_1 = 'G4'
    group_1 = module_0.Group(str_1)
    group_2 = module_0.Group(str_0)
    str_2 = '3ZKG7'
    group_3 = module_0.Group(str_2)
    str_3 = 'G9'
    group_4 = module_0.Group(str_3)
    var_0 = group_0.add_child_group(group_2)
    var_1 = group_2.get_vars()
    var_2 = group_1.add_child_group(group_2)

def test_case_17():
    str_0 = 'test_group'
    group_0 = module_0.Group(str_0)
    str_1 = 'test_key'
    str_2 = 'test_value'
    var_0 = group_0.set_variable(str_1, str_2)
    str_3 = 'test_key_child'
    str_4 = 'test_value_child'
    str_5 = {str_3: str_4}
    var_1 = group_0.set_variable(str_1, str_5)

def test_case_18():
    bool_0 = True
    group_0 = module_0.Group()
    str_0 = '@a,'
    var_0 = module_0.to_safe_group_name(str_0, bool_0)
    str_1 = 'a/b'
    var_1 = module_0.to_safe_group_name(str_1, bool_0)
    str_2 = 'a,b'
    var_2 = module_0.to_safe_group_name(str_2, bool_0)
    str_3 = 'x'
    var_3 = module_0.to_safe_group_name(str_2, str_3, bool_0)
    var_4 = module_0.to_safe_group_name(str_2, bool_0)

def test_case_19():
    str_0 = 'mygroup'
    group_0 = module_0.Group(str_0)
    str_1 = 'foo'
    str_2 = 'bar'
    var_0 = group_0.set_variable(str_1, str_2)
    str_3 = 'newbar'
    var_1 = group_0.set_variable(str_1, str_3)
    str_4 = 'key'
    str_5 = 'key1'
    str_6 = 'value'
    str_7 = 'value1'
    str_8 = {str_4: str_6, str_5: str_7}
    var_2 = group_0.set_variable(str_1, str_8)
    str_9 = 'key2'
    str_10 = 'value2'
    str_11 = {str_4: str_6, str_5: str_7, str_9: str_10}
    var_3 = group_0.set_variable(str_1, str_11)

def test_case_20():
    str_0 = 'mygroup'
    group_0 = module_0.Group(str_0)
    str_1 = 'ansible_group_priority'
    str_2 = '10'
    var_0 = group_0.set_variable(str_1, str_2)
    var_1 = group_0.get_hosts()

def test_case_21():
    str_0 = 'test_group'
    group_0 = module_0.Group(str_0)
    str_1 = 'foo'
    str_2 = 'bar'
    str_3 = 'baz'
    str_4 = [str_2, str_3]
    var_0 = group_0.set_variable(str_1, str_4)
    str_5 = {str_2: str_3}
    var_1 = group_0.set_variable(str_1, str_5)
    var_2 = group_0.set_variable(str_1, str_2)
    str_6 = 'ansible_group_priority'
    str_7 = '1'
    var_3 = group_0.set_variable(str_6, str_7)
    str_8 = '2'
    var_4 = group_0.set_variable(str_6, str_8)
    int_0 = 2
    var_5 = group_0.set_variable(str_6, int_0)