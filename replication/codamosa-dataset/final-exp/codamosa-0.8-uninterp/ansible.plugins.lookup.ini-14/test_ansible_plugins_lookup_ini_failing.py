# Automatically generated by Pynguin.
import ansible.plugins.lookup.ini as module_0

def test_case_0():
    try:
        lookup_module_0 = module_0.LookupModule()
        bool_0 = False
        var_0 = lookup_module_0.get_value(lookup_module_0, lookup_module_0, bool_0, bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = -181
        bytes_0 = b'}\x12yZ\xa8\x8a\xaeq\xb7\xf5\xd6\xc6\x02r\xd2\x93C\xa9qv'
        set_0 = {bytes_0, bytes_0, int_0, bytes_0}
        lookup_module_0 = module_0.LookupModule()
        var_0 = lookup_module_0.get_value(int_0, int_0, set_0, set_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = False
        tuple_0 = (bool_0,)
        lookup_module_0 = module_0.LookupModule()
        list_0 = None
        bytes_0 = b'Ce$'
        str_0 = 'Secret'
        str_1 = '\x0bT_'
        dict_0 = {str_0: bytes_0, str_1: str_0}
        lookup_module_1 = module_0.LookupModule(bytes_0, **dict_0)
        var_0 = lookup_module_1.run(tuple_0, list_0)
    except BaseException:
        pass