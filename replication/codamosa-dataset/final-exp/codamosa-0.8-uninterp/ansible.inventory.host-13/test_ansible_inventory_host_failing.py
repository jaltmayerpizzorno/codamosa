# Automatically generated by Pynguin.
import ansible.inventory.host as module_0
import ansible.inventory.group as module_1

def test_case_0():
    try:
        float_0 = -353.978
        host_0 = module_0.Host()
        var_0 = host_0.get_groups()
        var_1 = host_0.remove_group(float_0)
        bytes_0 = b''
        var_2 = host_0.__ne__(bytes_0)
        host_1 = module_0.Host()
        str_0 = '+$(_ba5&$A{8dn>4A_G}'
        var_3 = host_1.__setstate__(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        host_0 = module_0.Host()
        var_0 = host_0.__str__()
        host_1 = module_0.Host()
        var_1 = host_1.get_vars()
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'|\xe7\xaa\xa0h\xfc6D'
        bytes_1 = b'\xb4\x17"\x07\x00\xc4\xbd\x1e\x13%\xe2\x90\xf8\x84\x13\x8az\x1d'
        host_0 = module_0.Host(bytes_0, bytes_1)
    except BaseException:
        pass

def test_case_3():
    try:
        host_0 = module_0.Host()
        var_0 = host_0.populate_ancestors()
        var_1 = host_0.get_groups()
        bytes_0 = b''
        var_2 = host_0.__ne__(bytes_0)
        host_1 = module_0.Host()
        var_3 = host_1.__getstate__()
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'The path to a {0} skeleton that the new {0} should be based upon.'
        int_0 = 730
        host_0 = module_0.Host(int_0)
        var_0 = host_0.add_group(str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        set_0 = set()
        host_0 = module_0.Host(set_0)
        var_0 = host_0.get_vars()
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '\x0bAOC_3>e[x7\x0cTdm*;)'
        host_0 = module_0.Host()
        var_0 = host_0.populate_ancestors(str_0)
        str_1 = ">Qsa49Q'<^Hhlt>?("
        host_1 = module_0.Host(str_1)
        var_1 = host_1.get_magic_vars()
        host_2 = module_0.Host(str_0)
        var_2 = host_2.__hash__()
        var_3 = host_2.get_magic_vars()
        str_2 = 'found exact match for {0} in {1}'
        dict_0 = {str_2: str_2, str_2: str_2}
        var_4 = host_0.remove_group(str_1)
        var_5 = host_0.__repr__()
        var_6 = host_1.get_name()
        bool_0 = False
        var_7 = host_2.set_variable(bool_0, dict_0)
        var_8 = host_1.get_vars()
        host_3 = module_0.Host()
        var_9 = host_2.get_groups()
        var_10 = host_0.__getstate__()
    except BaseException:
        pass

def test_case_7():
    try:
        host_0 = module_0.Host()
        str_0 = 'name'
        str_1 = 'address'
        str_2 = 'port'
        str_3 = 'vars'
        str_4 = 'groups'
        str_5 = 'implicit'
        str_6 = 'x1'
        str_7 = '22'
        str_8 = 'ansible_ssh_pass'
        str_9 = 'x1pass'
        str_10 = {str_8: str_9}
        str_11 = 'some_group'
        str_12 = [str_11, str_0]
        str_13 = '0'
        str_14 = {str_0: str_6, str_1: str_6, str_2: str_7, str_3: str_10, str_4: str_12, str_5: str_13}
        var_0 = host_0.deserialize(str_14)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'test'
        host_0 = module_0.Host(str_0)
        str_1 = 'group_1'
        group_0 = module_1.Group(str_1)
        var_0 = host_0.add_group(group_0)
        str_2 = 'group_2'
        group_1 = module_1.Group(str_2)
        var_1 = host_0.add_group(group_1)
        var_2 = host_0.add_group(group_1)
        var_3 = host_0.get_magic_vars()
        var_4 = var_3[str_0]
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'host1'
        host_0 = module_0.Host(str_0)
        str_1 = 'group1'
        group_0 = module_1.Group(str_1)
        str_2 = 'group2'
        group_1 = module_1.Group(str_2)
        str_3 = '('
        group_2 = module_1.Group(str_3)
        bool_0 = False
        dict_0 = {}
        var_0 = host_0.set_variable(bool_0, dict_0)
        str_4 = 'group4'
        group_3 = module_1.Group(str_4)
        var_1 = group_3.get_ancestors()
        str_5 = 'B.nf.fy0'
        group_4 = module_1.Group(str_5)
        var_2 = group_1.add_child_group(group_2)
        var_3 = group_1.add_child_group(group_3)
        var_4 = group_2.add_child_group(group_4)
        var_5 = group_0.add_child_group(group_1)
        var_6 = host_0.add_group(group_1)
        list_0 = None
        var_7 = group_3.set_variable(list_0, list_0)
        bool_1 = False
        var_8 = host_0.set_variable(bool_1, dict_0)
        list_1 = [var_1]
        var_9 = host_0.add_group(list_1)
    except BaseException:
        pass