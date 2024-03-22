# Automatically generated by Pynguin.
import ansible.module_utils.common.validation as module_0

def test_case_0():
    str_0 = 'M0jw.\\&"~.Wj"3liv,/s'
    var_0 = module_0.check_type_path(str_0)

def test_case_1():
    str_0 = 'files'
    var_0 = module_0.check_mutually_exclusive(str_0, str_0)

def test_case_2():
    str_0 = 'Unexpected failure!'
    var_0 = module_0.safe_eval(str_0, str_0)

def test_case_3():
    set_0 = set()
    var_0 = module_0.safe_eval(set_0)

def test_case_4():
    str_0 = "'"
    str_1 = ", 'N=nS`M@3E&Wfe5&"
    int_0 = 17
    list_0 = [str_1, str_1, str_1, int_0]
    bool_0 = True
    var_0 = module_0.check_required_together(str_0, list_0, bool_0)

def test_case_5():
    dict_0 = {}
    float_0 = 0.2
    str_0 = 'se0s[s#)|vd '
    var_0 = module_0.check_required_together(dict_0, float_0, str_0)

def test_case_6():
    float_0 = -298.01441
    var_0 = module_0.check_missing_parameters(float_0)

def test_case_7():
    str_0 = 'auto_silent'
    var_0 = module_0.check_type_list(str_0)

def test_case_8():
    float_0 = 2889.02943
    var_0 = module_0.check_type_list(float_0)

def test_case_9():
    float_0 = 2.0
    var_0 = module_0.check_type_float(float_0)

def test_case_10():
    str_0 = 'i g:'
    var_0 = module_0.check_type_raw(str_0)

def test_case_11():
    list_0 = []
    var_0 = module_0.check_type_jsonarg(list_0)

def test_case_12():
    str_0 = 'x/9'
    var_0 = module_0.check_type_jsonarg(str_0)

def test_case_13():
    str_0 = '88'
    var_0 = module_0.safe_eval(str_0)
    dict_0 = {}
    var_1 = module_0.check_type_dict(dict_0)

def test_case_14():
    int_0 = 248
    int_1 = None
    var_0 = module_0.check_type_raw(int_0)
    str_0 = '|`p`8ljiAMbz50NZqyg'
    var_1 = module_0.check_required_together(str_0, str_0)
    var_2 = module_0.check_type_raw(int_1)

def test_case_15():
    dict_0 = None
    bool_0 = False
    bytes_0 = b'BP\xee\x91\x07R\x14_U\xad1E{\xc5\xfaW\xe0\x92'
    tuple_0 = (bytes_0, bool_0)
    var_0 = module_0.check_mutually_exclusive(dict_0, bool_0, tuple_0)

def test_case_16():
    int_0 = 70
    float_0 = -1329.122788
    var_0 = module_0.check_missing_parameters(float_0)
    str_0 = '9+'
    var_1 = module_0.check_type_int(int_0)
    var_2 = module_0.check_type_bits(str_0)
    var_3 = module_0.check_type_float(int_0)

def test_case_17():
    str_0 = "I^'=Z+2"
    var_0 = module_0.check_type_dict(str_0)

def test_case_18():
    str_0 = ''
    int_0 = 1176
    var_0 = module_0.check_required_if(str_0, int_0)

def test_case_19():
    bytes_0 = b'\xa6\xc1\xbbaU_~\xf6\x8a\xdf\x97\xb0uc\x141\x9a'
    float_0 = -487.2
    set_0 = {bytes_0, float_0, bytes_0}
    dict_0 = {}
    var_0 = module_0.check_missing_parameters(set_0, dict_0)

def test_case_20():
    str_0 = '8'
    var_0 = module_0.safe_eval(str_0)

def test_case_21():
    str_0 = '\\q(ie=0!S<(I^w\nVD'
    var_0 = module_0.check_type_dict(str_0)
    complex_0 = None
    float_0 = 4480.26
    int_0 = -1929
    tuple_0 = (complex_0, float_0, int_0)
    var_1 = module_0.check_type_raw(tuple_0)

def test_case_22():
    str_0 = '88'
    var_0 = module_0.safe_eval(str_0)
    dict_0 = {}
    list_0 = [str_0, str_0, str_0, dict_0]
    var_1 = module_0.check_required_by(dict_0, list_0)

def test_case_23():
    str_0 = 'P'
    str_1 = 'baz'
    str_2 = 'quuz'
    str_3 = [str_2, str_0, str_1]
    str_4 = {str_0: str_1, str_1: str_3, str_2: str_3}
    bool_0 = False
    bool_1 = {str_0: bool_0, str_2: bool_0, str_1: bool_0, str_2: bool_0, str_2: bool_0}
    var_0 = module_0.check_required_by(str_4, bool_1)

def test_case_24():
    str_0 = 'a'
    str_1 = 'b'
    str_2 = 'c'
    str_3 = 'd'
    str_4 = [str_2, str_3]
    str_5 = [str_0, str_1, str_4]
    str_6 = [str_5]
    str_7 = {str_0: str_1, str_2: str_2, str_3: str_3}
    var_0 = module_0.check_required_if(str_6, str_7)

def test_case_25():
    str_0 = "ansible.module_utils.six.text_type(a=Rb')"
    var_0 = module_0.safe_eval(str_0)

def test_case_26():
    str_0 = 'import os'
    var_0 = module_0.safe_eval(str_0)

def test_case_27():
    str_0 = '{"foo":"bar", "baz":"faz"}'
    var_0 = module_0.check_type_dict(str_0)
    str_1 = 'foo=bar, baz=faz'
    var_1 = module_0.check_type_dict(str_1)
    str_2 = 'foo'
    str_3 = 'baz'
    str_4 = 'When doing an --list, represent in a way that is optimized for export,not as an accurate representation of how Ansible has processed it'
    str_5 = 'faz'
    str_6 = {str_2: str_4, str_3: str_5}
    var_2 = module_0.check_type_dict(str_6)