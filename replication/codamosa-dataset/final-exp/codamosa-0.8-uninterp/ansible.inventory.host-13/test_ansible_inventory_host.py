# Automatically generated by Pynguin.
import ansible.inventory.host as module_0
import ansible.inventory.group as module_1

def test_case_0():
    pass

def test_case_1():
    dict_0 = {}
    host_0 = module_0.Host(dict_0)
    var_0 = host_0.__getstate__()

def test_case_2():
    complex_0 = None
    bool_0 = False
    host_0 = module_0.Host()
    set_0 = {bool_0, host_0, bool_0, complex_0}
    var_0 = host_0.remove_group(set_0)

def test_case_3():
    float_0 = -353.978
    host_0 = module_0.Host()
    var_0 = host_0.get_groups()
    var_1 = host_0.remove_group(float_0)
    bytes_0 = b''
    var_2 = host_0.__ne__(bytes_0)
    host_1 = module_0.Host()
    var_3 = host_1.__getstate__()

def test_case_4():
    host_0 = module_0.Host()
    var_0 = host_0.__hash__()

def test_case_5():
    host_0 = module_0.Host()
    var_0 = host_0.__repr__()

def test_case_6():
    dict_0 = {}
    host_0 = module_0.Host()
    host_1 = module_0.Host(host_0)
    var_0 = host_1.deserialize(dict_0)

def test_case_7():
    str_0 = '\x0bAOC_3>e[x7\x0cTdm*;)'
    host_0 = module_0.Host()
    var_0 = host_0.populate_ancestors(str_0)
    str_1 = ">Qsa49Q'<^Hhlt>?("
    host_1 = module_0.Host(str_1)
    var_1 = host_1.get_magic_vars()
    host_2 = module_0.Host(str_0)
    var_2 = host_2.__hash__()
    int_0 = 2559
    var_3 = host_0.__ne__(int_0)
    var_4 = host_0.remove_group(str_1)
    var_5 = host_1.get_name()
    host_3 = module_0.Host(str_0)
    host_4 = module_0.Host()
    var_6 = host_4.get_groups()
    var_7 = host_4.__getstate__()

def test_case_8():
    bool_0 = False
    host_0 = module_0.Host(bool_0)
    set_0 = None
    var_0 = host_0.remove_group(set_0)

def test_case_9():
    complex_0 = None
    host_0 = module_0.Host(complex_0, complex_0)
    bool_0 = False
    host_1 = module_0.Host()
    var_0 = host_1.set_variable(host_0, bool_0)

def test_case_10():
    host_0 = module_0.Host()
    host_1 = module_0.Host()
    var_0 = host_1.get_groups()
    var_1 = host_1.remove_group(host_0)

def test_case_11():
    str_0 = 'RkZ:+H#8xqGrgi\x0b?7'
    host_0 = module_0.Host(str_0)
    var_0 = host_0.get_vars()
    bool_0 = False
    host_1 = module_0.Host(bool_0)
    set_0 = None
    var_1 = host_1.remove_group(set_0)

def test_case_12():
    str_0 = 'test_host'
    host_0 = module_0.Host(str_0)
    str_1 = 'key'
    str_2 = 'value'
    var_0 = host_0.set_variable(str_1, str_2)
    var_1 = host_0.get_vars()
    str_3 = 'name'
    str_4 = {str_3: str_2}
    var_2 = host_0.set_variable(str_1, str_4)
    var_3 = host_0.get_vars()
    var_4 = host_0.set_variable(str_1, str_2)
    str_5 = {str_3: str_2}
    var_5 = host_0.set_variable(str_1, str_5)
    var_6 = host_0.get_vars()

def test_case_13():
    host_0 = module_0.Host()
    var_0 = host_0.populate_ancestors()
    list_0 = []
    float_0 = -91.43551
    var_1 = host_0.__hash__()
    host_1 = module_0.Host(float_0)
    var_2 = host_1.__str__()
    host_2 = module_0.Host(list_0)
    var_3 = host_2.__getstate__()
    var_4 = host_2.__str__()
    bytes_0 = b'\x04\xf4\xbeD:6\x9f\xea\xa8\xb1\xc6'
    host_3 = module_0.Host(bytes_0)
    var_5 = host_2.__ne__(host_1)
    var_6 = host_0.get_groups()

def test_case_14():
    str_0 = 'a~'
    host_0 = module_0.Host(str_0)
    list_0 = [host_0, str_0, host_0, str_0]
    var_0 = host_0.populate_ancestors(list_0)
    str_1 = None
    host_1 = module_0.Host(str_1, str_1)
    str_2 = 'lE'
    group_0 = module_1.Group(str_2)
    str_3 = 'group2'
    group_1 = module_1.Group(str_3)
    str_4 = 'vs1Q'
    group_2 = module_1.Group(str_4)
    var_1 = group_1.add_child_group(group_2)
    var_2 = group_0.add_child_group(group_1)
    list_1 = None
    var_3 = group_2.set_variable(list_1, list_1)
    var_4 = host_1.add_group(group_2)
    var_5 = host_1.remove_group(group_2)
    tuple_0 = None
    var_6 = group_2.set_priority(tuple_0)

def test_case_15():
    str_0 = None
    host_0 = module_0.Host(str_0, str_0)
    str_1 = 'F'
    group_0 = module_1.Group(str_1)
    group_1 = module_1.Group(str_0)
    var_0 = group_0.add_child_group(group_1)
    var_1 = host_0.add_group(group_1)
    var_2 = host_0.remove_group(group_1)

def test_case_16():
    str_0 = 'Host1'
    host_0 = module_0.Host(str_0)
    str_1 = 'G1'
    group_0 = module_1.Group(str_1)
    var_0 = host_0.add_group(group_0)
    var_1 = host_0.remove_group(group_0)

def test_case_17():
    str_0 = None
    host_0 = module_0.Host(str_0, str_0)
    str_1 = 'lE'
    group_0 = module_1.Group(str_1)
    group_1 = module_1.Group(str_1)
    str_2 = 'vs1Q'
    group_2 = module_1.Group(str_2)
    var_0 = group_1.add_child_group(group_2)
    var_1 = group_0.add_child_group(group_1)
    var_2 = host_0.add_group(group_2)
    var_3 = host_0.remove_group(group_2)

def test_case_18():
    str_0 = 'host1'
    host_0 = module_0.Host(str_0)
    str_1 = 'group1'
    group_0 = module_1.Group(str_1)
    str_2 = 'group2'
    group_1 = module_1.Group(str_2)
    str_3 = 'group3'
    group_2 = module_1.Group(str_3)
    group_3 = module_1.Group(str_2)
    str_4 = 'group5'
    group_4 = module_1.Group(str_4)
    var_0 = group_1.add_child_group(group_2)
    var_1 = group_1.add_child_group(group_3)
    var_2 = group_2.add_child_group(group_4)
    var_3 = group_0.add_child_group(group_1)
    var_4 = host_0.add_group(group_1)
    var_5 = host_0.add_group(group_4)
    var_6 = host_0.add_group(group_3)
    var_7 = host_0.remove_group(group_3)

def test_case_19():
    str_0 = 'example.com'
    host_0 = module_0.Host(str_0)
    str_1 = 'all'
    group_0 = module_1.Group(str_1)
    var_0 = host_0.add_group(group_0)
    str_2 = 'group1'
    group_1 = module_1.Group(str_2)
    var_1 = host_0.add_group(group_1)
    str_3 = 'group2'
    group_2 = module_1.Group(str_3)
    var_2 = host_0.add_group(group_2)
    var_3 = host_0.get_magic_vars()

def test_case_20():
    str_0 = 'host1'
    host_0 = module_0.Host(str_0)
    str_1 = 'group1'
    group_0 = module_1.Group(str_1)
    str_2 = 'group2'
    var_0 = host_0.__hash__()
    group_1 = module_1.Group(str_2)
    str_3 = 'g\touf3'
    group_2 = module_1.Group(str_3)
    bool_0 = False
    dict_0 = {}
    var_1 = host_0.set_variable(bool_0, dict_0)
    str_4 = 'grouK4'
    group_3 = module_1.Group(str_4)
    str_5 = 'group5'
    group_4 = module_1.Group(str_5)
    var_2 = group_1.add_child_group(group_3)
    var_3 = group_2.add_child_group(group_4)
    var_4 = group_0.add_child_group(group_1)
    var_5 = host_0.add_group(group_1)
    host_1 = module_0.Host(dict_0)
    complex_0 = None
    var_6 = host_0.remove_group(complex_0)
    var_7 = host_0.populate_ancestors()

def test_case_21():
    host_0 = module_0.Host()
    str_0 = 'name'
    str_1 = 'vars'
    str_2 = 'address'
    str_3 = 'uuid'
    str_4 = 'groups'
    str_5 = 'test_host'
    str_6 = 'testk'
    str_7 = 'testmk'
    str_8 = 'testv'
    str_9 = 'testmvk'
    str_10 = 'testmvv'
    str_11 = {str_9: str_10}
    str_12 = {str_6: str_8, str_7: str_11}
    str_13 = '127.0.0.1'
    str_14 = 'test_host_uuid'
    str_15 = 'test_group'
    str_16 = {str_9: str_10}
    str_17 = {str_6: str_8, str_7: str_16}
    var_0 = []
    var_1 = {str_0: str_15, str_1: str_17, str_4: var_0}
    var_2 = [var_1]
    var_3 = {str_0: str_5, str_1: str_12, str_2: str_13, str_3: str_14, str_4: var_2}
    var_4 = host_0.deserialize(var_3)