# Automatically generated by Pynguin.
import ansible.inventory.host as module_0
import ansible.inventory.group as module_1

def test_case_0():
    try:
        str_0 = "mWYFJ%'\ty4|e"
        host_0 = module_0.Host(str_0)
        dict_0 = {str_0: host_0, host_0: host_0, host_0: host_0}
        var_0 = host_0.__str__()
        host_1 = module_0.Host(host_0, dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        host_0 = module_0.Host()
        var_0 = host_0.__hash__()
        bytes_0 = b''
        var_1 = host_0.add_group(bytes_0)
    except BaseException:
        pass

def test_case_2():
    try:
        set_0 = None
        host_0 = module_0.Host()
        host_1 = module_0.Host(host_0)
        var_0 = host_1.deserialize(set_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bool_0 = True
        bytes_0 = b'\xa7\x1f\x01T\x07\xeaS\x1d\x99\x95'
        host_0 = module_0.Host(bytes_0)
        var_0 = host_0.populate_ancestors()
        list_0 = [host_0, host_0]
        var_1 = host_0.set_variable(host_0, list_0)
        var_2 = host_0.deserialize(bool_0)
    except BaseException:
        pass

def test_case_4():
    try:
        host_0 = module_0.Host()
        var_0 = host_0.serialize()
        host_1 = module_0.Host()
        float_0 = -2089.689
        var_1 = host_0.add_group(float_0)
    except BaseException:
        pass

def test_case_5():
    try:
        host_0 = module_0.Host()
        var_0 = host_0.get_name()
        bytes_0 = b'$0\x1b;\x90z'
        tuple_0 = (bytes_0,)
        list_0 = [tuple_0, tuple_0]
        host_1 = module_0.Host(list_0)
        var_1 = host_1.get_magic_vars()
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'test'
        host_0 = module_0.Host(str_0)
        str_1 = 'key'
        str_2 = 'value'
        var_0 = host_0.set_variable(str_1, str_2)
        str_3 = 'new_value'
        var_1 = host_0.__repr__()
        var_2 = host_0.set_variable(str_1, str_3)
        str_4 = 'key2'
        var_3 = host_0.__getstate__()
        var_4 = host_0.set_variable(str_4, str_2)
        var_5 = host_0.get_vars()
        str_5 = "?'cNAsD"
        var_6 = host_0.populate_ancestors(str_5)
        var_7 = host_0.get_vars()
    except BaseException:
        pass

def test_case_7():
    try:
        int_0 = 3600
        str_0 = "wdK\\)Q>'E/2\r$"
        host_0 = module_0.Host(str_0)
        var_0 = host_0.get_name()
        list_0 = [int_0, str_0]
        str_1 = "05{gU[j\tL']NMMs7U*xj"
        var_1 = host_0.populate_ancestors(str_1)
        var_2 = host_0.__ne__(list_0)
        var_3 = host_0.__hash__()
        var_4 = host_0.__hash__()
        var_5 = host_0.populate_ancestors()
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'test_Host_remove_group'
        var_0 = print(str_0)
        str_1 = 'test_group_1'
        group_0 = module_1.Group(str_1)
        group_1 = module_1.Group(str_1)
        str_2 = '0242ac11-0014-e614-f149-00000000058e'
        str_3 = 'xogjb^sz\x0b5=-O,{V'
        dict_0 = {str_2: str_2, str_2: str_2, str_3: str_1, str_3: str_0, str_1: str_0, str_0: var_0}
        int_0 = -259
        float_0 = 976.430329
        tuple_0 = (dict_0, int_0, dict_0, float_0)
        host_0 = module_0.Host(tuple_0)
        var_1 = host_0.serialize()
        var_2 = group_1.add_child_group(group_0)
        str_4 = 'test_host'
        host_1 = module_0.Host(str_4)
        var_3 = host_1.add_group(group_0)
        var_4 = host_1.add_group(group_1)
        var_5 = host_1.remove_group(group_0)
        str_5 = '^^A_f_<gnOR[%>D'
        var_6 = host_1.populate_ancestors(str_5)
        var_7 = host_1.get_vars()
    except BaseException:
        pass