# Automatically generated by Pynguin.
import ansible.inventory.group as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = '}~I~u X'
    group_0 = module_0.Group(str_0)

def test_case_2():
    group_0 = module_0.Group()

def test_case_3():
    group_0 = module_0.Group()
    var_0 = group_0.get_hosts()
    var_1 = group_0.__getstate__()
    group_1 = module_0.Group()
    var_2 = group_0.get_descendants()
    var_3 = group_1.remove_host(group_1)
    var_4 = group_1.__repr__()
    var_5 = group_0.__repr__()

def test_case_4():
    group_0 = module_0.Group()
    var_0 = group_0.__str__()
    var_1 = group_0.__getstate__()
    var_2 = group_0.get_ancestors()

def test_case_5():
    group_0 = module_0.Group()
    var_0 = group_0.get_vars()
    var_1 = group_0.__getstate__()

def test_case_6():
    str_0 = '}~I~u X'
    dict_0 = {str_0: str_0}
    group_0 = module_0.Group(str_0)
    var_0 = group_0.__setstate__(dict_0)

def test_case_7():
    group_0 = module_0.Group()
    var_0 = group_0.get_hosts()

def test_case_8():
    group_0 = module_0.Group()
    var_0 = group_0.clear_hosts_cache()

def test_case_9():
    group_0 = module_0.Group()
    var_0 = group_0.remove_host(group_0)

def test_case_10():
    int_0 = -2291
    group_0 = None
    group_1 = module_0.Group()
    var_0 = group_1.set_variable(int_0, group_0)

def test_case_11():
    tuple_0 = None
    str_0 = '\nI\x0b}-HlAc/d@k'
    group_0 = module_0.Group(str_0)
    var_0 = group_0.set_priority(tuple_0)

def test_case_12():
    str_0 = 'l'
    group_0 = module_0.Group(str_0)
    var_0 = group_0.get_vars()
    var_1 = group_0.get_vars()

def test_case_13():
    group_0 = module_0.Group()
    group_1 = module_0.Group()
    var_0 = group_0.add_child_group(group_1)

def test_case_14():
    group_0 = module_0.Group()
    list_0 = None
    var_0 = group_0.set_priority(list_0)
    group_1 = module_0.Group()
    var_1 = group_0.add_child_group(group_1)
    var_2 = group_1.get_name()
    group_2 = module_0.Group()
    var_3 = group_0.get_hosts()

def test_case_15():
    group_0 = module_0.Group()
    group_1 = module_0.Group()
    var_0 = group_0.add_child_group(group_1)
    group_2 = module_0.Group()
    var_1 = group_1.add_child_group(group_2)

def test_case_16():
    str_0 = 'test'
    group_0 = module_0.Group(str_0)
    int_0 = 1
    var_0 = group_0.set_variable(str_0, int_0)
    str_1 = 'test2'
    int_1 = 2
    var_1 = group_0.set_variable(str_1, int_1)
    int_2 = 3
    var_2 = group_0.set_variable(str_0, int_2)

def test_case_17():
    str_0 = 'parent_groups'
    str_1 = 'depth'
    str_2 = 'name'
    str_3 = 'vars'
    var_0 = {}
    var_1 = []
    int_0 = 0
    str_4 = '1.2.3.4'
    str_5 = [str_4]
    str_6 = 'all'
    var_2 = {str_3: var_0, str_0: var_1, str_1: int_0, str_1: str_5, str_2: str_6}
    var_3 = [var_2]
    int_1 = 1
    str_7 = [str_4]
    str_8 = 'test'
    str_9 = 'test_var'
    str_10 = 'test_value'
    str_11 = {str_9: str_10}
    var_4 = {str_0: var_3, str_1: int_1, str_3: str_7, str_2: str_8, str_3: str_11}
    group_0 = module_0.Group()
    var_5 = group_0.deserialize(var_4)

def test_case_18():
    str_0 = 'Test_123'
    var_0 = module_0.to_safe_group_name(str_0)
    var_1 = None
    var_2 = module_0.to_safe_group_name(var_1)
    str_1 = '123_Test'
    var_3 = module_0.to_safe_group_name(str_1)
    str_2 = '[localhost]'
    var_4 = module_0.to_safe_group_name(str_2)
    str_3 = '_'
    bool_0 = True
    var_5 = module_0.to_safe_group_name(str_2, str_3, bool_0)
    bool_1 = False
    var_6 = module_0.to_safe_group_name(str_2, str_3, bool_1)
    str_4 = '$'
    var_7 = module_0.to_safe_group_name(str_2, str_4)

def test_case_19():
    str_0 = 'test_group'
    group_0 = module_0.Group(str_0)
    str_1 = 'ansible_group_priority'
    int_0 = 0
    var_0 = group_0.set_variable(str_1, int_0)
    str_2 = 'test_var1'
    str_3 = 'test1'
    var_1 = group_0.set_variable(str_2, str_3)

def test_case_20():
    str_0 = 'group_1'
    group_0 = module_0.Group(str_0)
    group_1 = module_0.Group(str_0)
    str_1 = 'group_3'
    group_2 = module_0.Group(str_1)
    str_2 = 'group_4'
    group_3 = module_0.Group(str_2)
    var_0 = group_0.add_child_group(group_1)
    var_1 = group_0.add_child_group(group_2)
    var_2 = group_1.add_child_group(group_3)
    var_3 = group_0.get_hosts()
    var_4 = set(var_3)

def test_case_21():
    group_0 = module_0.Group()
    str_0 = 'foo'
    int_0 = 5
    int_1 = {str_0: int_0}
    var_0 = group_0.set_variable(str_0, int_1)
    str_1 = 'baz'
    int_2 = 0
    int_3 = {str_0: int_0, str_1: int_2}
    var_1 = group_0.set_variable(str_0, int_3)
    str_2 = 'ansible_group_priority'
    var_2 = group_0.set_variable(str_2, int_2)
    var_3 = group_0.set_variable(str_2, int_0)

def test_case_22():
    str_0 = 'test'
    group_0 = module_0.Group(str_0)
    str_1 = 'foo'
    str_2 = 'bar'
    var_0 = group_0.set_variable(str_1, str_2)
    var_1 = group_0.get_vars()
    str_3 = 'fizz'
    str_4 = 'a'
    str_5 = 'b'
    int_0 = 1
    int_1 = 2
    int_2 = {str_4: int_0, str_5: int_1}
    var_2 = group_0.set_variable(str_3, int_2)
    var_3 = group_0.get_vars()
    str_6 = 'c'
    str_7 = 'd'
    int_3 = 3
    int_4 = 4
    int_5 = {str_6: int_3, str_7: int_4}
    var_4 = group_0.set_variable(str_3, int_5)
    var_5 = group_0.get_vars()
    var_6 = group_0.set_variable(str_3, str_1)