# Automatically generated by Pynguin.
import ansible.modules.replace as module_0

def test_case_0():
    try:
        str_0 = '5L\r\x0cA<1*7}&\\'
        tuple_0 = (str_0,)
        float_0 = 2.0
        str_1 = 'Running %s as the backend for the yum action plugin'
        tuple_1 = (str_1,)
        var_0 = module_0.write_changes(tuple_0, float_0, tuple_1)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'JE\t\r}>Ny?6|b[`6B'
        int_0 = None
        dict_0 = {str_0: str_0, str_0: int_0}
        var_0 = module_0.check_file_attrs(str_0, int_0, dict_0)
    except BaseException:
        pass