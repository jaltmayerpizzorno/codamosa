# Automatically generated by Pynguin.
import ansible.module_utils.common.validation as module_0

def test_case_0():
    pass

def test_case_1():
    bytes_0 = b'\xdb\x0c:\xd8\xdcO=\x12\xb5'
    str_0 = '&'
    var_0 = module_0.check_mutually_exclusive(bytes_0, str_0)

def test_case_2():
    tuple_0 = ()
    var_0 = module_0.safe_eval(tuple_0)

def test_case_3():
    dict_0 = {}
    int_0 = -4436
    var_0 = module_0.check_mutually_exclusive(dict_0, int_0)

def test_case_4():
    set_0 = set()
    int_0 = 1395
    list_0 = [int_0, int_0]
    var_0 = module_0.check_required_together(set_0, int_0, list_0)

def test_case_5():
    str_0 = '\\{or>-pzi`*SyK-['
    bytes_0 = b'\xc5'
    var_0 = module_0.check_required_together(str_0, bytes_0)

def test_case_6():
    dict_0 = {}
    var_0 = module_0.check_required_by(dict_0, dict_0)

def test_case_7():
    list_0 = []
    var_0 = module_0.check_required_if(list_0, list_0)

def test_case_8():
    str_0 = '{"a": 1, "b": "two", "c": \'three\'}'
    var_0 = module_0.check_type_dict(str_0)
    list_0 = None
    var_1 = module_0.check_required_if(list_0, list_0)

def test_case_9():
    bytes_0 = None
    var_0 = module_0.check_type_str(bytes_0)

def test_case_10():
    bool_0 = False
    var_0 = module_0.check_type_list(bool_0)

def test_case_11():
    bool_0 = True
    var_0 = module_0.check_type_path(bool_0)
    str_0 = '-;uueB2eF/7s\x0b-w'
    var_1 = module_0.check_type_list(str_0)

def test_case_12():
    dict_0 = {}
    var_0 = module_0.check_type_dict(dict_0)

def test_case_13():
    bool_0 = True
    var_0 = module_0.check_type_bool(bool_0)

def test_case_14():
    int_0 = 14
    var_0 = module_0.check_type_path(int_0)

def test_case_15():
    bytes_0 = b'z\xd2Q\x1a\xbal\xf2\x86\xe5\x80\xa3_ :C\x96'
    var_0 = module_0.check_type_raw(bytes_0)

def test_case_16():
    bool_0 = False
    bytes_0 = b'\xe1r\xa3k\xe8\xd4'
    var_0 = module_0.check_type_jsonarg(bytes_0)
    var_1 = module_0.check_type_float(bool_0)

def test_case_17():
    str_0 = '{"a": 1, "b": "two", "c": \'three\'}'
    var_0 = module_0.check_type_dict(str_0)

def test_case_18():
    str_0 = '?%|0m!C'
    var_0 = module_0.check_type_path(str_0)

def test_case_19():
    str_0 = 'sjP59sc\x0b'
    dict_0 = {str_0: str_0}
    var_0 = module_0.safe_eval(str_0, dict_0)

def test_case_20():
    str_0 = "5:761'/Q8t0B!=x`^\t3"
    var_0 = module_0.check_type_dict(str_0)

def test_case_21():
    bytes_0 = b'\xc5'
    set_0 = {bytes_0}
    var_0 = module_0.check_required_together(set_0, bytes_0)

def test_case_22():
    str_0 = '\t47~z-#M'
    int_0 = 4473
    set_0 = {str_0, str_0, int_0, str_0}
    var_0 = module_0.safe_eval(int_0, set_0, int_0)
    bytes_0 = b''
    list_0 = []
    var_1 = module_0.check_required_if(bytes_0, list_0)

def test_case_23():
    str_0 = '1,2,3]'
    var_0 = module_0.safe_eval(str_0)
    str_1 = '"foo(bar)"'
    var_1 = module_0.safe_eval(str_1)
    str_2 = 'import foo'
    var_2 = module_0.safe_eval(str_2)

def test_case_24():
    str_0 = 'hz'
    str_1 = 'c'
    var_0 = None
    var_1 = {str_0: str_0, str_1: var_0}
    str_2 = {str_1: str_1, str_1: str_1}
    var_2 = module_0.check_required_by(str_2, var_1)

def test_case_25():
    str_0 = 'a'
    str_1 = 'b'
    var_0 = None
    var_1 = {str_0: str_1, str_0: var_0}
    str_2 = 'd'
    str_3 = {str_0: str_0, str_2: str_1}
    var_2 = module_0.check_required_by(str_3, var_1)

def test_case_26():
    str_0 = '1Mb'
    var_0 = module_0.check_type_bits(str_0)
    dict_0 = {}
    var_1 = module_0.check_required_arguments(dict_0, str_0)

def test_case_27():
    str_0 = '{"a": 1, "b": "two", "c": \'three\'}'
    var_0 = module_0.check_type_dict(str_0)
    str_1 = 'a=1, b="two", c=\'three\''
    var_1 = module_0.check_type_dict(str_1)

def test_case_28():
    str_0 = 'import foo'
    var_0 = module_0.safe_eval(str_0)

def test_case_29():
    str_0 = 'foo'
    str_1 = 'bar'
    bool_0 = True
    bool_1 = {str_0: bool_0}
    bool_2 = False
    bool_3 = {str_0: bool_2}
    bool_4 = {str_0: bool_1, str_1: bool_3}
    var_0 = module_0.check_required_arguments(bool_4, str_0)
    str_2 = {str_1: str_1}
    var_1 = module_0.check_required_arguments(bool_4, str_2)

def test_case_30():
    str_0 = '3'
    var_0 = module_0.safe_eval(str_0)
    str_1 = 'foo'
    var_1 = module_0.safe_eval(str_1)
    str_2 = '["foo", "bar"]'
    var_2 = module_0.safe_eval(str_2)
    str_3 = '{"foo": "bar"}'
    var_3 = module_0.safe_eval(str_3)
    str_4 = '{"foo": {"bar": "baz"}}'
    var_4 = module_0.safe_eval(str_4)
    str_5 = 'foo.bar()'
    var_5 = module_0.safe_eval(str_5)
    str_6 = 'import foo'
    var_6 = module_0.safe_eval(str_6)