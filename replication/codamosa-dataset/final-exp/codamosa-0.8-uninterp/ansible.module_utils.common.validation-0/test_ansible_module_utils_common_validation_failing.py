# Automatically generated by Pynguin.
import ansible.module_utils.common.validation as module_0

def test_case_0():
    try:
        str_0 = '_=3W%;~QjYRJ+,e\r8P<'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
        var_0 = module_0.check_required_one_of(str_0, dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = "{6'BHf:@!]t@)5_;D"
        var_0 = module_0.check_type_dict(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        dict_0 = {}
        bytes_0 = b'\xc8\xee\xfd\xfbU\xfb\x18):'
        var_0 = module_0.check_required_one_of(dict_0, bytes_0)
        list_0 = []
        var_1 = module_0.check_type_bits(list_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'L^U_f,\x0ct&.F7M\\'
        bytes_0 = b'\x1f\xc4\xe6 \xd0W\xfe\xaf\xeb\xe7'
        var_0 = module_0.check_required_together(bytes_0, str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bool_0 = False
        list_0 = []
        bytes_0 = b'\xa0\xdf\x9a\xbby/'
        var_0 = module_0.check_required_together(list_0, bytes_0)
        int_0 = -3047
        var_1 = module_0.count_terms(bool_0, int_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bytes_0 = b'\xdcZ\x9d\xcd\x92_\x05\xa6G\xeb*\x88\xa5\xb1\xda\xaf\xce'
        list_0 = []
        var_0 = module_0.check_required_by(bytes_0, list_0)
    except BaseException:
        pass

def test_case_6():
    try:
        bytes_0 = b'\xb0\xb3\x8b\xbe\xcb&Q\xe0\xf8KB\x81{\x98T\xfd'
        dict_0 = {bytes_0: bytes_0}
        var_0 = module_0.check_required_arguments(dict_0, dict_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = '8H;1BDbGE['
        str_1 = 'value1'
        str_2 = 'pram3'
        str_3 = [str_2, str_1]
        str_4 = [str_0, str_1, str_3]
        str_5 = [str_0, str_1, str_3]
        str_6 = [str_5, str_4]
        str_7 = {str_0: str_1, str_2: str_0}
        var_0 = module_0.check_required_if(str_6, str_7)
    except BaseException:
        pass

def test_case_8():
    try:
        bool_0 = True
        var_0 = module_0.check_type_list(bool_0)
        bytes_0 = b'\xa7'
        var_1 = module_0.check_type_bytes(bytes_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = '"uK*CzDxzvPv)^2)kQ'
        list_0 = [str_0, str_0, str_0]
        var_0 = module_0.safe_eval(list_0)
        var_1 = module_0.check_type_list(list_0)
        bytes_0 = b'\xdc}\x89\x94\x8d\xd81\x020V]\x89=\x08'
        var_2 = module_0.check_type_list(bytes_0)
    except BaseException:
        pass

def test_case_10():
    try:
        bytes_0 = b'\xdc}\x89\x94\x8d\xd81\x020V]\x89=\x08'
        var_0 = module_0.check_type_list(bytes_0)
    except BaseException:
        pass

def test_case_11():
    try:
        list_0 = None
        var_0 = module_0.check_type_dict(list_0)
    except BaseException:
        pass

def test_case_12():
    try:
        int_0 = 1
        str_0 = 'import foo'
        bool_0 = False
        bytes_0 = b'*=\xf1\xdf\x9a\xe3\x89\xb2Fc\xb5\xaf_\x0f:"\xc3'
        set_0 = {int_0, str_0, str_0}
        list_0 = [bytes_0, int_0, str_0, int_0]
        tuple_0 = (list_0,)
        float_0 = -391.0
        var_0 = module_0.check_type_str(tuple_0, float_0)
        var_1 = module_0.safe_eval(str_0, bytes_0, set_0)
        var_2 = module_0.safe_eval(str_0, bool_0)
        var_3 = module_0.check_type_bool(set_0)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = 'v]f\t'
        var_0 = module_0.check_type_bool(str_0)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = '<u{\nqReMcJ^9Pv`"k:'
        str_1 = 'value1'
        str_2 = 'pram3'
        str_3 = [str_2, str_1]
        bool_0 = False
        var_0 = module_0.check_type_bool(bool_0)
        str_4 = [str_0, str_1, str_3]
        str_5 = [str_0, str_1, str_3]
        str_6 = [str_5, str_4]
        str_7 = {str_0: str_1, str_2: str_0}
        var_1 = module_0.check_required_if(str_6, str_7)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = 'a1="b2",a2="b2"'
        var_0 = module_0.check_type_int(str_0)
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = 'zH'
        var_0 = module_0.check_type_float(str_0)
    except BaseException:
        pass

def test_case_17():
    try:
        bool_0 = True
        var_0 = module_0.check_type_bytes(bool_0)
    except BaseException:
        pass

def test_case_18():
    try:
        float_0 = -3045.0
        var_0 = module_0.check_type_bits(float_0)
    except BaseException:
        pass

def test_case_19():
    try:
        int_0 = 511
        var_0 = module_0.check_type_raw(int_0)
        float_0 = -1193.715081
        var_1 = module_0.check_type_jsonarg(float_0)
    except BaseException:
        pass

def test_case_20():
    try:
        bytes_0 = None
        float_0 = -1156.7385
        tuple_0 = (bytes_0, float_0)
        set_0 = {tuple_0, bytes_0, bytes_0, tuple_0}
        str_0 = 'IrJ_'
        var_0 = module_0.check_required_one_of(set_0, str_0)
    except BaseException:
        pass

def test_case_21():
    try:
        float_0 = -2635.2
        var_0 = module_0.check_type_bool(float_0)
    except BaseException:
        pass

def test_case_22():
    try:
        dict_0 = {}
        var_0 = module_0.check_type_dict(dict_0)
        bytes_0 = b'\xd3x\x12 '
        var_1 = module_0.check_type_int(bytes_0)
    except BaseException:
        pass

def test_case_23():
    try:
        str_0 = "a1='b2',a2='b2'"
        var_0 = module_0.check_type_dict(str_0)
        var_1 = module_0.check_type_dict(str_0)
        set_0 = set()
        var_2 = module_0.check_type_float(set_0)
    except BaseException:
        pass

def test_case_24():
    try:
        str_0 = '*jiad'
        bytes_0 = b'\xab\xe1s\xa62!\x80\x15\xfc\xc6\x90\xbe\xb6'
        dict_0 = {str_0: str_0, str_0: str_0, bytes_0: bytes_0}
        var_0 = module_0.check_required_one_of(str_0, bytes_0, dict_0)
    except BaseException:
        pass

def test_case_25():
    try:
        str_0 = 'state=bsent'
        set_0 = None
        bool_0 = True
        var_0 = module_0.check_required_arguments(set_0, bool_0)
        set_1 = {str_0}
        var_1 = module_0.check_type_int(set_1)
    except BaseException:
        pass

def test_case_26():
    try:
        str_0 = 'h'
        var_0 = module_0.check_type_dict(str_0)
    except BaseException:
        pass

def test_case_27():
    try:
        str_0 = 'WC*arMjIwq4@t?^$b{'
        str_1 = 'e|c\n[GD3^'
        var_0 = module_0.check_required_one_of(str_0, str_1)
    except BaseException:
        pass

def test_case_28():
    try:
        bytes_0 = None
        var_0 = module_0.safe_eval(bytes_0)
        tuple_0 = ()
        var_1 = module_0.check_missing_parameters(tuple_0, tuple_0)
        str_0 = 'state=absent'
        var_2 = module_0.check_type_dict(str_0)
        var_3 = module_0.check_type_float(str_0)
    except BaseException:
        pass

def test_case_29():
    try:
        float_0 = -198.5998
        var_0 = module_0.safe_eval(float_0)
        bytes_0 = b'1C\xc3w\xd9Kk\xe6\xb4i\xa9!'
        bool_0 = False
        set_0 = {bytes_0}
        var_1 = module_0.check_missing_parameters(bool_0, set_0)
    except BaseException:
        pass

def test_case_30():
    try:
        str_0 = 'OEL'
        list_0 = [str_0, str_0]
        var_0 = module_0.check_type_jsonarg(list_0)
        float_0 = 1000.0
        tuple_0 = (str_0,)
        var_1 = module_0.check_type_float(float_0)
        var_2 = module_0.check_required_if(list_0, tuple_0, tuple_0)
        var_3 = module_0.check_type_bits(tuple_0)
    except BaseException:
        pass

def test_case_31():
    try:
        bytes_0 = None
        var_0 = module_0.safe_eval(bytes_0)
        str_0 = 'MIm"`+IJR9)&)[0q'
        var_1 = module_0.check_required_together(str_0, str_0)
        var_2 = module_0.check_type_dict(str_0)
    except BaseException:
        pass

def test_case_32():
    try:
        str_0 = '`uo7m1\nm\\0vz.=2'
        var_0 = module_0.check_type_dict(str_0)
        str_1 = 's'
        var_1 = module_0.check_type_int(str_1)
    except BaseException:
        pass

def test_case_33():
    try:
        str_0 = '0My3P$T+0AW+A_'
        int_0 = 1432
        var_0 = module_0.safe_eval(str_0, int_0)
        list_0 = None
        bool_0 = True
        var_1 = module_0.check_type_str(bool_0, list_0)
    except BaseException:
        pass

def test_case_34():
    try:
        str_0 = ''
        str_1 = 'b'
        str_2 = (str_0, str_1)
        str_3 = [str_2]
        str_4 = 'foo'
        str_5 = 'bar'
        str_6 = {str_0: str_4, str_1: str_5}
        var_0 = module_0.check_required_together(str_3, str_6)
        str_7 = (str_0, str_1)
        str_8 = (str_0, str_6)
        str_9 = [str_7, str_8]
        list_0 = [str_7, str_0, str_9]
        var_1 = module_0.check_type_path(list_0)
        float_0 = 2905.608199
        var_2 = module_0.check_type_list(float_0)
        str_10 = {str_0: str_4}
        var_3 = module_0.check_required_together(str_9, str_10)
    except BaseException:
        pass

def test_case_35():
    try:
        tuple_0 = None
        float_0 = None
        set_0 = {float_0, tuple_0}
        var_0 = module_0.check_required_together(tuple_0, float_0, set_0)
        int_0 = -294
        var_1 = module_0.check_type_float(int_0)
        bytes_0 = b'\x87\xd0\x1f\xb4_\x9b\xee\x1d\x05\xbf8\xb3VE\xb0\x89\x92'
        var_2 = module_0.check_type_bytes(bytes_0)
    except BaseException:
        pass

def test_case_36():
    try:
        set_0 = set()
        dict_0 = {}
        var_0 = module_0.check_required_together(set_0, dict_0)
        tuple_0 = ()
        var_1 = module_0.check_required_arguments(dict_0, set_0, tuple_0)
        bool_0 = True
        var_2 = module_0.check_type_dict(bool_0)
    except BaseException:
        pass

def test_case_37():
    try:
        str_0 = '/$H!TqIC~l5T!<'
        var_0 = module_0.safe_eval(str_0)
        str_1 = 'P`S;E)$tpRxI'
        list_0 = None
        str_2 = "7gl0s5-'7Ah"
        var_1 = module_0.check_required_one_of(list_0, str_2)
        var_2 = module_0.check_type_int(str_1)
    except BaseException:
        pass

def test_case_38():
    try:
        str_0 = 'Test for function check_required_by'
        dict_0 = {str_0: str_0, str_0: str_0}
        var_0 = module_0.check_missing_parameters(dict_0, dict_0)
    except BaseException:
        pass

def test_case_39():
    try:
        bytes_0 = None
        var_0 = module_0.safe_eval(bytes_0)
        set_0 = set()
        var_1 = module_0.check_required_if(set_0, set_0)
        str_0 = "{6'Hf:@!]t@)5_;D"
        bool_0 = True
        dict_0 = {bool_0: str_0, str_0: bytes_0}
        str_1 = 'CgF!S&ddB_7o'
        var_2 = module_0.check_missing_parameters(dict_0, str_1)
    except BaseException:
        pass

def test_case_40():
    try:
        bytes_0 = None
        var_0 = module_0.safe_eval(bytes_0)
        bool_0 = True
        str_0 = 'size_available'
        dict_0 = {bytes_0: str_0}
        tuple_0 = (str_0,)
        var_1 = module_0.check_required_by(dict_0, tuple_0)
        dict_1 = None
        float_0 = 3624.30789
        tuple_1 = ()
        tuple_2 = (float_0, tuple_1, bool_0, float_0)
        tuple_3 = (tuple_2,)
        tuple_4 = (dict_1, tuple_3)
        var_2 = module_0.check_type_int(tuple_4)
    except BaseException:
        pass

def test_case_41():
    try:
        str_0 = 'b'
        str_1 = 'foo'
        str_2 = (str_1, str_0)
        str_3 = [str_2, str_2]
        str_4 = {str_1: str_1}
        var_0 = module_0.check_required_together(str_3, str_4)
    except BaseException:
        pass

def test_case_42():
    try:
        str_0 = 'firsag'
        str_1 = 'required'
        bool_0 = True
        bool_1 = {str_1: bool_0}
        bool_2 = {str_1: bool_0}
        bool_3 = {str_0: bool_1, str_1: bool_1, str_1: bool_2, str_1: bool_1}
        str_2 = {}
        var_0 = module_0.check_required_arguments(bool_3, str_2)
    except BaseException:
        pass

def test_case_43():
    try:
        str_0 = 'thirdarg'
        bool_0 = True
        bool_1 = {str_0: bool_0}
        bool_2 = False
        bool_3 = {str_0: bool_2}
        bool_4 = {str_0: bool_0}
        bool_5 = {str_0: bool_2}
        bool_6 = {str_0: bool_1, str_0: bool_3, str_0: bool_4, str_0: bool_5}
        var_0 = {}
        var_1 = module_0.check_required_arguments(bool_6, var_0)
    except BaseException:
        pass

def test_case_44():
    try:
        str_0 = 'firstarg'
        str_1 = 'thirdarg'
        str_2 = 'fourtharg'
        str_3 = 'required'
        bool_0 = True
        bool_1 = {str_3: bool_0}
        bool_2 = {str_3: bool_0}
        bool_3 = {str_3: bool_0}
        bool_4 = {str_3: bool_0}
        bool_5 = {str_0: bool_1, str_2: bool_2, str_1: bool_3, str_2: bool_4}
        str_4 = 'firstarg'
        str_5 = {str_4: str_4}
        var_0 = module_0.check_required_arguments(bool_5, str_5)
    except BaseException:
        pass

def test_case_45():
    try:
        str_0 = 'foo'
        str_1 = 'bar'
        var_0 = None
        var_1 = {str_0: str_1, str_1: var_0}
        str_2 = {str_0: str_1}
        var_2 = module_0.check_required_by(str_2, var_1)
    except BaseException:
        pass

def test_case_46():
    try:
        str_0 = 'required_by_test'
        str_1 = 'param_one'
        str_2 = [str_1, str_1]
        str_3 = {str_0: str_2}
        str_4 = 'param_value'
        str_5 = {str_0: str_4}
        var_0 = module_0.check_required_by(str_3, str_5)
    except BaseException:
        pass

def test_case_47():
    try:
        str_0 = 'foo'
        str_1 = 'bar'
        var_0 = {str_0: str_1}
        str_2 = {str_0: str_1}
        var_1 = module_0.check_required_by(str_2, var_0)
    except BaseException:
        pass

def test_case_48():
    try:
        str_0 = 'state'
        str_1 = (str_0,)
        bool_0 = True
        var_0 = [str_0, str_1, str_1, bool_0]
        str_2 = 'someint'
        int_0 = 99
        str_3 = 'bool_param'
        str_4 = 'string_param'
        str_5 = (str_3, str_4)
        var_1 = [str_2, int_0, str_5]
        var_2 = [var_0, var_1]
        str_6 = '/tmp/bar'
        bool_1 = False
        var_3 = {str_0: str_0, str_2: int_0, str_5: str_6, str_3: bool_1}
        var_4 = module_0.check_required_if(var_2, var_3)
    except BaseException:
        pass

def test_case_49():
    try:
        str_0 = ''
        str_1 = 'a'
        str_2 = 'B'
        str_3 = {str_2: str_1, str_1: str_2, str_2: str_2, str_0: str_1}
        str_4 = [str_0, str_2]
        str_5 = [str_1, str_0]
        str_6 = [str_4, str_5, str_1]
        var_0 = module_0.check_mutually_exclusive(str_6, str_3)
    except BaseException:
        pass

def test_case_50():
    try:
        str_0 = 'None'
        var_0 = module_0.safe_eval(str_0)
        var_1 = module_0.safe_eval(str_0, var_0, str_0)
        str_1 = 'Fale'
        var_2 = module_0.safe_eval(str_1)
        str_2 = 'I'
        var_3 = module_0.safe_eval(str_2)
        str_3 = '[1, 2, 3]'
        bool_0 = False
        var_4 = module_0.check_type_raw(bool_0)
        var_5 = module_0.safe_eval(str_3)
        dict_0 = {}
        str_4 = "\t)$:r<2\rNh {'a5\t"
        var_6 = module_0.check_required_one_of(dict_0, str_4)
        var_7 = module_0.safe_eval(var_2)
        str_5 = 'None.foo(/'
        var_8 = module_0.safe_eval(str_5)
        str_6 = 'import json'
        var_9 = module_0.safe_eval(str_6)
        bytes_0 = b'\xb5\xacQI!\xbc\xc3\x97s\xc3\xc7 \x17o\xbbe\xce'
        set_0 = {bytes_0, bytes_0}
        var_10 = module_0.check_type_path(set_0)
        dict_1 = {str_3: var_3}
        var_11 = module_0.check_type_str(bytes_0, dict_1)
        var_12 = module_0.check_type_dict(str_4)
    except BaseException:
        pass

def test_case_51():
    try:
        str_0 = '8Hk1DbG![W'
        str_1 = 'va.e1'
        str_2 = 'pram3'
        str_3 = [str_0, str_1, str_0]
        str_4 = [str_2, str_0, str_1, str_3]
        str_5 = [str_0, str_1, str_4]
        str_6 = [str_2, str_0, str_3, str_4]
        str_7 = [str_6, str_5]
        str_8 = {str_0: str_1, str_2: str_0}
        var_0 = module_0.check_required_if(str_7, str_8)
    except BaseException:
        pass