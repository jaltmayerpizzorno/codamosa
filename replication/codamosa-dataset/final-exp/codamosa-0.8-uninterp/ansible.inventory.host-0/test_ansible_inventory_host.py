# Automatically generated by Pynguin.
import ansible.inventory.host as module_0
import ansible.inventory.group as module_1

def test_case_0():
    host_0 = module_0.Host()

def test_case_1():
    bool_0 = False
    host_0 = module_0.Host(bool_0)
    list_0 = [host_0, host_0, host_0]
    bool_1 = True
    host_1 = module_0.Host(list_0, bool_1)
    var_0 = host_1.__getstate__()

def test_case_2():
    bytes_0 = b'\xad\xbc~\xf9#\xb2\xcb\xa7\xa2r\x93[\xc9'
    dict_0 = {bytes_0: bytes_0}
    float_0 = 1386.0
    host_0 = module_0.Host(float_0)
    var_0 = host_0.__setstate__(dict_0)

def test_case_3():
    int_0 = 1202
    host_0 = module_0.Host(int_0)
    bytes_0 = b'Oc\xec\xb5n\x8a}k\x90\xd7s\x94\xc9\x06A\xf3.\xfe\xfe'
    dict_0 = {bytes_0: host_0, host_0: int_0}
    var_0 = host_0.set_variable(bytes_0, dict_0)
    var_1 = host_0.__repr__()
    str_0 = '-t\n8m/2'
    str_1 = 'y&~WDuf@dx`\tv3z(]Z|P'
    var_2 = host_0.set_variable(host_0, str_1)
    host_1 = module_0.Host(str_0)
    var_3 = host_1.serialize()

def test_case_4():
    int_0 = 568
    bytes_0 = b''
    host_0 = module_0.Host(bytes_0)
    var_0 = host_0.__str__()
    host_1 = module_0.Host(host_0, int_0)
    host_2 = module_0.Host(host_1)
    host_3 = module_0.Host(host_2)

def test_case_5():
    host_0 = module_0.Host()
    var_0 = host_0.serialize()

def test_case_6():
    host_0 = module_0.Host()
    list_0 = [host_0, host_0, host_0, host_0]
    host_1 = module_0.Host(list_0)
    var_0 = host_1.populate_ancestors()

def test_case_7():
    str_0 = 'mam|@3G'
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    int_0 = False
    host_0 = module_0.Host(list_0, int_0)
    var_0 = host_0.populate_ancestors(str_0)

def test_case_8():
    str_0 = 'test'
    host_0 = module_0.Host(str_0)
    group_0 = module_1.Group()
    var_0 = host_0.add_group(group_0)

def test_case_9():
    bool_0 = False
    host_0 = module_0.Host()
    var_0 = host_0.remove_group(bool_0)

def test_case_10():
    str_0 = 't_\\9+SC\x0c'
    host_0 = module_0.Host(str_0)
    var_0 = host_0.get_vars()
    host_1 = module_0.Host()
    var_1 = host_1.remove_group(str_0)

def test_case_11():
    int_0 = -1243
    host_0 = module_0.Host(int_0)
    var_0 = host_0.__hash__()
    bytes_0 = b'\x1a\x19\xbf\xa3\xf9\xc9s\xdf\x00A\xc1L\x96'
    var_1 = host_0.__ne__(host_0)
    float_0 = -1916.38
    var_2 = host_0.remove_group(float_0)
    host_1 = module_0.Host(bytes_0)
    var_3 = host_1.__getstate__()

def test_case_12():
    group_0 = module_1.Group()
    group_1 = module_1.Group()
    host_0 = module_0.Host()
    var_0 = host_0.add_group(group_0)
    host_1 = module_0.Host()
    str_0 = 'key'
    str_1 = 'value'
    var_1 = host_1.set_variable(str_0, str_1)
    var_2 = host_0.__getstate__()
    var_3 = host_0.__getstate__()
    var_4 = host_0.serialize()
    var_5 = host_0.deserialize(var_4)

def test_case_13():
    str_0 = 'testE'
    host_0 = module_0.Host(str_0)
    var_0 = host_0.__repr__()
    var_1 = host_0.get_vars()
    group_0 = module_1.Group(str_0)
    var_2 = host_0.add_group(group_0)
    var_3 = host_0.add_group(group_0)
    var_4 = host_0.remove_group(group_0)
    var_5 = host_0.get_magic_vars()

def test_case_14():
    str_0 = 'localhost'
    host_0 = module_0.Host(str_0)
    str_1 = 'key1'
    str_2 = 'value1'
    var_0 = host_0.set_variable(str_1, str_0)
    var_1 = {}
    var_2 = host_0.set_variable(str_1, var_1)
    var_3 = host_0.set_variable(str_1, str_2)

def test_case_15():
    str_0 = 'test'
    host_0 = module_0.Host(str_0)
    group_0 = module_1.Group(str_0)
    var_0 = host_0.add_group(group_0)
    var_1 = host_0.remove_group(group_0)

def test_case_16():
    str_0 = 'localhost'
    host_0 = module_0.Host(str_0)
    var_0 = host_0.get_vars()
    str_1 = 'foo'
    str_2 = 'bar'
    var_1 = host_0.set_variable(str_1, str_2)
    var_2 = host_0.get_vars()
    str_3 = 'bar1'
    var_3 = host_0.set_variable(str_1, str_3)
    var_4 = host_0.get_vars()
    str_4 = 'a'
    str_5 = 'b'
    str_6 = {str_4: str_5}
    var_5 = host_0.set_variable(str_1, str_6)
    var_6 = host_0.get_vars()
    str_7 = 'b1'
    str_8 = {str_4: str_7}
    var_7 = host_0.set_variable(str_1, str_8)
    var_8 = host_0.get_vars()
    str_9 = 'c'
    str_10 = 'dvk1'
    str_11 = {str_4: str_7, str_9: str_10}
    var_9 = host_0.set_variable(str_1, str_11)

def test_case_17():
    str_0 = 'test'
    host_0 = module_0.Host(str_0)
    str_1 = 'all'
    group_0 = module_1.Group(str_1)
    var_0 = host_0.get_vars()
    group_1 = module_1.Group(str_0)
    var_1 = host_0.remove_group(group_1)
    var_2 = host_0.add_group(group_0)
    var_3 = host_0.add_group(group_1)
    var_4 = host_0.remove_group(group_1)
    var_5 = host_0.get_vars()

def test_case_18():
    str_0 = 'grand_parent'
    group_0 = module_1.Group(str_0)
    str_1 = 'parent'
    group_1 = module_1.Group(str_1)
    var_0 = group_0.add_child_group(group_1)
    str_2 = 'group'
    group_2 = module_1.Group(str_2)
    var_1 = group_1.add_child_group(group_2)
    str_3 = 'host'
    host_0 = module_0.Host(str_3)
    var_2 = host_0.add_group(group_1)
    var_3 = host_0.remove_group(group_1)