# Automatically generated by Pynguin.
import ansible.module_utils.common.validation as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = '.Fq)'
    var_0 = module_0.check_required_together(str_0, str_0)

def test_case_2():
    str_0 = '.Fq)'
    var_0 = module_0.safe_eval(str_0)

def test_case_3():
    str_0 = None
    var_0 = module_0.safe_eval(str_0)

def test_case_4():
    list_0 = []
    float_0 = 0.001
    var_0 = module_0.check_mutually_exclusive(list_0, float_0)

def test_case_5():
    str_0 = '~aV:t\'i"XSz%{'
    str_1 = '-qW'
    var_0 = module_0.check_mutually_exclusive(str_0, str_1)

def test_case_6():
    str_0 = None
    list_0 = [str_0, str_0]
    var_0 = module_0.check_mutually_exclusive(str_0, list_0)
    var_1 = module_0.safe_eval(str_0)

def test_case_7():
    bool_0 = None
    dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_0, bool_0: bool_0}
    var_0 = module_0.check_required_by(dict_0, dict_0)

def test_case_8():
    dict_0 = {}
    var_0 = module_0.check_required_arguments(dict_0, dict_0)

def test_case_9():
    float_0 = 1.3704798112286913
    set_0 = set()
    var_0 = module_0.check_missing_parameters(float_0, set_0)

def test_case_10():
    bool_0 = True
    var_0 = module_0.check_missing_parameters(bool_0)

def test_case_11():
    float_0 = -2454.7511
    var_0 = module_0.check_type_path(float_0)

def test_case_12():
    float_0 = -1738.017834
    var_0 = module_0.check_type_list(float_0)

def test_case_13():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0]
    str_0 = '&_s+MHSK#(}/H;.-)\t'
    var_0 = module_0.check_type_list(str_0)
    var_1 = module_0.check_type_list(list_0)
    var_2 = module_0.check_type_bool(bool_0)

def test_case_14():
    bool_0 = False
    var_0 = module_0.check_type_int(bool_0)

def test_case_15():
    bool_0 = True
    var_0 = module_0.check_type_float(bool_0)

def test_case_16():
    list_0 = None
    var_0 = module_0.check_type_raw(list_0)

def test_case_17():
    int_0 = 0
    var_0 = module_0.check_type_bits(int_0)

def test_case_18():
    str_0 = '8}z;;4WQ=QUwL+'
    dict_0 = {str_0: str_0}
    var_0 = module_0.check_type_jsonarg(dict_0)
    var_1 = module_0.check_type_dict(str_0)

def test_case_19():
    str_0 = '8}z;;4WQ=QUwL+'
    var_0 = module_0.check_type_dict(str_0)
    var_1 = module_0.check_type_jsonarg(str_0)

def test_case_20():
    int_0 = 2278
    set_0 = {int_0, int_0}
    bytes_0 = b'\xc6\xfc'
    list_0 = []
    bytes_1 = b'\x9fz'
    var_0 = module_0.count_terms(list_0, bytes_1)
    var_1 = module_0.check_mutually_exclusive(set_0, bytes_0)

def test_case_21():
    bool_0 = False
    bytes_0 = None
    list_0 = [bytes_0, bytes_0]
    var_0 = module_0.check_required_one_of(bytes_0, list_0)
    var_1 = module_0.check_type_list(bool_0)

def test_case_22():
    str_0 = "ow=Gv6kAt'Vt[\nVt\x0c%"
    int_0 = 6002
    var_0 = module_0.check_type_raw(int_0)
    str_1 = ''
    bytes_0 = b'\xb0\x02\x8aLEo\xbf\x0c'
    var_1 = module_0.check_required_one_of(str_1, bytes_0)
    var_2 = module_0.check_type_dict(str_0)

def test_case_23():
    str_0 = '1)(`ca7\r\\\x0c>mBz'
    set_0 = {str_0, str_0}
    var_0 = module_0.check_required_together(str_0, set_0)

def test_case_24():
    bytes_0 = b'4\xbf\xc7|S3\xd9\x02'
    var_0 = module_0.safe_eval(bytes_0)
    dict_0 = {}
    bool_0 = False
    var_1 = module_0.check_type_list(bool_0)
    var_2 = module_0.check_required_arguments(dict_0, dict_0)
    int_0 = None
    var_3 = module_0.check_required_if(int_0, bool_0, bool_0)

def test_case_25():
    str_0 = '8}z;;4WQ=QUwL+'
    var_0 = module_0.check_type_dict(str_0)

def test_case_26():
    set_0 = set()
    str_0 = 'wM(!I'
    var_0 = module_0.check_required_if(set_0, str_0)

def test_case_27():
    dict_0 = {}
    var_0 = module_0.check_required_arguments(dict_0, dict_0)
    var_1 = module_0.check_type_dict(dict_0)

def test_case_28():
    str_0 = '6'
    var_0 = module_0.safe_eval(str_0)

def test_case_29():
    str_0 = 'l~h'
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
    set_0 = {str_0, str_0}
    var_0 = module_0.check_missing_parameters(dict_0, set_0)

def test_case_30():
    str_0 = 'present'
    str_1 = 'path'
    str_2 = (str_1,)
    bool_0 = True
    var_0 = [str_1, str_0, str_2, bool_0]
    str_3 = 'someint'
    int_0 = 99
    var_1 = [str_3, int_0, str_2]
    var_2 = [var_0, var_1]
    str_4 = '/'
    str_5 = {str_4: str_0, str_1: str_4}
    var_3 = module_0.check_required_if(var_2, str_5)
    str_6 = ''
    str_7 = {str_4: str_0, str_1: str_6}
    var_4 = module_0.check_required_if(var_2, str_7)

def test_case_31():
    str_0 = 'L-)"]@s19@ZZ\tL+1*7'
    set_0 = None
    str_1 = [str_0]
    str_2 = {str_0: str_1}
    var_0 = module_0.safe_eval(set_0)
    var_1 = module_0.check_required_by(str_2, str_2)

def test_case_32():
    var_0 = dict()
    bool_0 = True
    var_1 = dict(parameter1=var_0, parameter2=var_0)
    var_2 = dict()
    var_3 = dict(required=bool_0)
    var_4 = dict(parameter1=var_2, parameter2=var_3)
    str_0 = 'test'
    var_5 = dict(parameter2=str_0)
    var_6 = module_0.check_required_arguments(var_1, var_5)

def test_case_33():
    str_0 = '[1, 2]'
    var_0 = None
    var_1 = module_0.safe_eval(str_0, var_0)
    bool_0 = True
    var_2 = module_0.safe_eval(str_0, var_0, bool_0)
    str_1 = 'foo'
    var_3 = module_0.safe_eval(str_1)
    var_4 = module_0.safe_eval(str_1, var_0, bool_0)
    str_2 = 'import foo'
    var_5 = module_0.safe_eval(str_2)
    var_6 = module_0.safe_eval(str_2, var_0, bool_0)
    str_3 = 'foo.bar()'
    var_7 = module_0.safe_eval(str_3)
    var_8 = module_0.safe_eval(str_3, var_0, bool_0)

def test_case_34():
    str_0 = '"str"=str,"str2"=str2,"str3"=str3'
    var_0 = module_0.check_type_dict(str_0)
    str_1 = "{'json_str':'json_str'}"
    var_1 = module_0.check_type_dict(str_1)
    var_2 = module_0.check_type_dict(str_1)

def test_case_35():
    var_0 = None
    bool_0 = True
    str_0 = 'foo'
    var_1 = module_0.safe_eval(str_0)
    var_2 = module_0.safe_eval(str_0, var_0, bool_0)
    str_1 = 'import foo'
    var_3 = module_0.safe_eval(str_1)
    var_4 = module_0.safe_eval(str_1, var_0, bool_0)
    str_2 = 'foo.bar()'
    var_5 = module_0.safe_eval(str_2)

def test_case_36():
    str_0 = '{"foo": "bar"}'
    var_0 = module_0.check_type_dict(str_0)
    str_1 = 'foo=bar'
    var_1 = module_0.check_type_dict(str_1)
    var_2 = module_0.check_type_dict(str_1)
    str_2 = '"foo"=bar'
    var_3 = module_0.check_type_dict(str_2)
    str_3 = '"foo bar"=bar'
    var_4 = module_0.check_type_dict(str_3)
    str_4 = 'foo="bar"'
    var_5 = module_0.check_type_dict(str_4)
    str_5 = 'foo="bar\nbaz"'
    var_6 = module_0.check_type_dict(str_5)
    str_6 = 'foo="bar\\nbaz"'
    var_7 = module_0.check_type_dict(str_6)