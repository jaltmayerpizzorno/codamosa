# Automatically generated by Pynguin.
import ansible.inventory.group as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = '\tf[9c~#'
    group_0 = module_0.Group(str_0)

def test_case_2():
    group_0 = module_0.Group()

def test_case_3():
    group_0 = module_0.Group()
    var_0 = group_0.__getstate__()

def test_case_4():
    group_0 = module_0.Group()
    var_0 = group_0.get_hosts()

def test_case_5():
    group_0 = module_0.Group()
    var_0 = group_0.clear_hosts_cache()

def test_case_6():
    group_0 = module_0.Group()
    var_0 = group_0.get_name()

def test_case_7():
    str_0 = '\x0b?HIW1FP'
    group_0 = module_0.Group()
    var_0 = group_0.set_variable(str_0, str_0)

def test_case_8():
    group_0 = module_0.Group()
    var_0 = group_0.get_vars()

def test_case_9():
    float_0 = 0.001
    set_0 = set()
    group_0 = module_0.Group(set_0)
    var_0 = group_0.set_priority(float_0)

def test_case_10():
    str_0 = 'group1'
    group_0 = module_0.Group(str_0)
    group_1 = module_0.Group(str_0)
    var_0 = group_0.add_child_group(group_1)
    var_1 = group_0.get_hosts()

def test_case_11():
    str_0 = 'group1'
    group_0 = module_0.Group(str_0)
    group_1 = module_0.Group(str_0)
    var_0 = group_0.add_child_group(group_1)
    var_1 = group_1.get_hosts()

def test_case_12():
    str_0 = '\x0bE#%}Y~e$\\z\tDl%)'
    group_0 = module_0.Group(str_0)
    group_1 = module_0.Group(str_0)
    var_0 = group_0.add_child_group(group_1)

def test_case_13():
    str_0 = 'group@example.com'
    str_1 = '_'
    var_0 = module_0.to_safe_group_name(str_0, str_1)
    bool_0 = True
    var_1 = module_0.to_safe_group_name(str_0, str_1, bool_0)

def test_case_14():
    group_0 = module_0.Group()
    var_0 = group_0.get_hosts()
    var_1 = group_0.get_ancestors()
    group_1 = module_0.Group()
    var_2 = group_1.__str__()
    str_0 = 'cU(k\x0cbF('
    var_3 = group_1.__getstate__()
    group_2 = module_0.Group(str_0)
    var_4 = group_0.get_hosts()
    var_5 = group_2.add_child_group(group_0)
    var_6 = group_1.add_child_group(group_2)

def test_case_15():
    str_0 = 'test'
    group_0 = module_0.Group(str_0)
    str_1 = 'test2'
    group_1 = module_0.Group(str_1)
    var_0 = group_0.add_child_group(group_1)
    str_2 = 'test3'
    group_2 = module_0.Group(str_2)
    var_1 = group_1.add_child_group(group_2)
    str_3 = 'test4'
    group_3 = module_0.Group(str_3)
    var_2 = group_2.add_child_group(group_3)
    group_4 = module_0.Group()

def test_case_16():
    group_0 = module_0.Group()
    var_0 = group_0.get_hosts()
    var_1 = group_0.get_vars()
    var_2 = group_0.remove_host(group_0)
    var_3 = group_0.get_name()
    var_4 = group_0.__str__()
    str_0 = '4)K'
    dict_0 = {}
    var_5 = group_0.deserialize(dict_0)
    var_6 = group_0.__getstate__()
    group_1 = module_0.Group(str_0)
    var_7 = group_1.__repr__()
    var_8 = group_0.get_hosts()
    var_9 = group_1.get_name()
    var_10 = group_1.add_child_group(group_0)
    var_11 = group_0.clear_hosts_cache()
    var_12 = group_1.get_ancestors()
    var_13 = group_0.__repr__()
    var_14 = group_0.clear_hosts_cache()
    str_1 = 'lUKt'
    var_15 = group_1.add_child_group(group_0)
    float_0 = None
    var_16 = group_1.set_variable(str_1, float_0)

def test_case_17():
    group_0 = module_0.Group()
    str_0 = 'ansible_group_priority'
    str_1 = '42'
    var_0 = group_0.set_variable(str_0, str_1)
    str_2 = 'foo'
    str_3 = 'bar'
    str_4 = {str_3: str_0}
    var_1 = group_0.set_variable(str_2, str_4)
    str_5 = 'new'
    str_6 = 'value'
    str_7 = {str_5: str_6}
    var_2 = group_0.set_variable(str_2, str_7)

def test_case_18():
    str_0 = 'test_group'
    group_0 = module_0.Group(str_0)
    str_1 = 'test_key'
    str_2 = 'test_value'
    var_0 = group_0.set_variable(str_1, str_2)
    str_3 = 'sub_key1'
    str_4 = 'sub_key2'
    str_5 = 'sub_value1'
    str_6 = 'sub_value2'
    str_7 = {str_3: str_5, str_4: str_6}
    var_1 = group_0.set_variable(str_1, str_7)
    str_8 = 'test_value2'
    var_2 = group_0.set_variable(str_1, str_8)

def test_case_19():
    str_0 = 'name'
    str_1 = 'vars'
    str_2 = 'parent_groups'
    str_3 = 'group1'
    str_4 = 'g1'
    str_5 = '1'
    str_6 = {str_4: str_5}
    str_7 = 'group2'
    str_8 = 'g2'
    str_9 = '2'
    str_10 = {str_8: str_9}
    str_11 = {str_0: str_7, str_1: str_10}
    str_12 = 'group3'
    str_13 = 'g3'
    str_14 = '3'
    str_15 = {str_13: str_14}
    str_16 = {str_0: str_12, str_1: str_15}
    str_17 = [str_11, str_16]
    str_18 = {str_0: str_3, str_1: str_6, str_2: str_17}
    group_0 = module_0.Group()
    var_0 = group_0.deserialize(str_18)
    var_1 = group_0.parent_groups
    var_2 = len(str_18)
    var_3 = str_18[str_2]
    var_4 = len(var_3)
    int_0 = 0
    var_5 = group_0.parent_groups[int_0]

def test_case_20():
    str_0 = 'valid'
    var_0 = module_0.to_safe_group_name(str_0)
    str_1 = ''
    var_1 = module_0.to_safe_group_name(str_1)
    var_2 = None
    var_3 = module_0.to_safe_group_name(var_2)
    str_2 = 'a,b'
    var_4 = module_0.to_safe_group_name(str_2)
    str_3 = '-'
    var_5 = module_0.to_safe_group_name(str_2, str_3)
    str_4 = '_'
    bool_0 = True
    var_6 = module_0.to_safe_group_name(str_2, str_4, bool_0)
    var_7 = module_0.to_safe_group_name(str_2, str_4, bool_0, bool_0)