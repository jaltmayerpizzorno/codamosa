# Automatically generated by Pynguin.
import ansible.plugins.action.debug as module_0

def test_case_0():
    try:
        bytes_0 = b'\x8b\xd5Q\x08\xb4\xf9\x8b\xe1\xb8_'
        str_0 = 'V\nSh lps'
        str_1 = 'H3p_E5NZ-t8D:C\n\t2'
        str_2 = '2b'
        float_0 = 1866.018
        str_3 = 'P+PY\n> t5'
        action_module_0 = module_0.ActionModule(bytes_0, str_0, str_1, str_2, float_0, str_3)
        var_0 = action_module_0.run()
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = False
        str_0 = 'Vlf5vG;"J\rjFo\n$i,B$W'
        complex_0 = None
        str_1 = '\x0b?#:'
        bool_1 = False
        tuple_0 = (complex_0, str_1, bool_1)
        int_0 = -2866
        dict_0 = {bool_0: int_0, tuple_0: complex_0}
        action_module_0 = module_0.ActionModule(bool_0, str_0, tuple_0, tuple_0, dict_0, str_1)
        var_0 = action_module_0.run(str_0, dict_0)
    except BaseException:
        pass