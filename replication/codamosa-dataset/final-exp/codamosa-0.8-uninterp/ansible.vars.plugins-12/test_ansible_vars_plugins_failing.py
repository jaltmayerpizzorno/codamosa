# Automatically generated by Pynguin.
import ansible.vars.plugins as module_0
import ansible.inventory.host as module_1

def test_case_0():
    try:
        var_0 = None
        var_1 = module_0.get_vars_from_path(var_0, var_0, var_0, var_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'task_messages'
        bytes_0 = b'\x8a'
        list_0 = [bytes_0]
        var_0 = module_0.get_plugin_vars(str_0, str_0, bytes_0, list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = 3244
        str_0 = ',^oi3<t~Kl/bE(S0],U'
        var_0 = module_0.get_vars_from_inventory_sources(int_0, str_0, int_0, str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = b'\xfd\xc0\xfc\xecQ\xe3\x92%\x85\xbc\x19\x830\xcc\xefe_\x83\n\xbd'
        str_0 = ''
        bool_0 = False
        int_0 = 1908
        var_0 = module_0.get_plugin_vars(bytes_0, str_0, bool_0, int_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '_n'
        dict_0 = {}
        set_0 = set()
        tuple_0 = (str_0, str_0, set_0)
        bytes_0 = b'\x8eGYS\x96\x17_\x17'
        var_0 = module_0.get_plugin_vars(dict_0, tuple_0, bytes_0, set_0)
        str_1 = 'bu\t/M N!kH\x0cml'
        tuple_1 = (str_1,)
        str_2 = '/6'
        var_1 = module_0.get_vars_from_inventory_sources(set_0, tuple_0, tuple_1, str_2)
    except BaseException:
        pass

def test_case_5():
    try:
        dict_0 = {}
        str_0 = '77\t-_vji'
        set_0 = set()
        tuple_0 = (str_0, str_0, set_0)
        bytes_0 = b'\x8eGYS\x96\x17_\x17'
        list_0 = [bytes_0]
        bool_0 = False
        str_1 = 'inventory'
        var_0 = module_0.get_vars_from_path(list_0, set_0, bool_0, str_1)
        var_1 = module_0.get_plugin_vars(dict_0, tuple_0, bytes_0, set_0)
        str_2 = 'bu\t/M N!kH\x0cml'
        tuple_1 = (str_2,)
        float_0 = None
        var_2 = module_0.get_vars_from_inventory_sources(str_2, tuple_1, float_0, float_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '/foo/bar'
        bool_0 = True
        int_0 = -2253
        var_0 = module_0.get_vars_from_inventory_sources(bool_0, str_0, int_0, int_0)
    except BaseException:
        pass

def test_case_7():
    try:
        bytes_0 = b'\x8eGYS\x96\x17_\x17'
        host_0 = module_1.Host()
        set_0 = set()
        bytes_1 = b'~\x8c\x9a\x03\xecYN\x9fr\x0ct\x02\x99F'
        list_0 = [host_0, bytes_0]
        var_0 = module_0.get_plugin_vars(host_0, set_0, bytes_1, list_0)
    except BaseException:
        pass