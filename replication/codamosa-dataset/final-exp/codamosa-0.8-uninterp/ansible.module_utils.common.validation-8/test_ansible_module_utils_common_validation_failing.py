# Automatically generated by Pynguin.
import ansible.module_utils.common.validation as module_0

def test_case_0():
    try:
        bytes_0 = b"\x14\x97\x8b\xb9`V[O\xf6\xa4\xc8\x90'\x84\x96\xdc>"
        set_0 = {bytes_0, bytes_0}
        var_0 = module_0.check_required_one_of(bytes_0, set_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'M\x10J]\xe2\x93\xca'
        float_0 = -3795.186617
        var_0 = module_0.check_required_together(bytes_0, float_0)
    except BaseException:
        pass

def test_case_2():
    try:
        var_0 = None
        var_1 = module_0.check_required_arguments(var_0, var_0)
        str_0 = 'required_one'
        list_0 = None
        var_2 = module_0.check_required_together(list_0, list_0)
        var_3 = module_0.check_type_int(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = 194
        set_0 = set()
        dict_0 = {int_0: set_0, int_0: set_0}
        var_0 = module_0.check_required_arguments(set_0, dict_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '_'
        dict_0 = {str_0: str_0}
        bytes_0 = b'N\xc2\x98\xf9\x9aQ\xe5\xb6\x1d\x92\xcb\xeam\x06\xb3\xe6'
        var_0 = module_0.check_required_arguments(dict_0, str_0, bytes_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '6'
        bytes_0 = b'\x0f\xa3+\x8e\x03('
        var_0 = module_0.check_required_if(str_0, bytes_0)
    except BaseException:
        pass

def test_case_6():
    try:
        float_0 = 2592.390429
        bytes_0 = b'\x90l\t\x9c\xc7,\xf1\x8d\xe3\xdb5yE\xdb\xfd\xc9\x01\xaa\n'
        var_0 = module_0.check_missing_parameters(float_0, bytes_0)
    except BaseException:
        pass

def test_case_7():
    try:
        dict_0 = None
        str_0 = '20[\x0c$'
        var_0 = module_0.check_type_str(dict_0, dict_0, str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        float_0 = None
        bool_0 = False
        str_0 = '`U/|:X_'
        var_0 = module_0.check_type_path(str_0)
        var_1 = module_0.check_required_if(float_0, bool_0)
        str_1 = '<#{eu@$G\\Zd'
        var_2 = module_0.check_type_dict(str_1)
    except BaseException:
        pass

def test_case_9():
    try:
        float_0 = 940.6
        var_0 = module_0.check_type_dict(float_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = '0'
        var_0 = module_0.check_type_dict(str_0)
    except BaseException:
        pass

def test_case_11():
    try:
        int_0 = 136
        var_0 = module_0.check_type_bool(int_0)
    except BaseException:
        pass

def test_case_12():
    try:
        bytes_0 = b'V\x9f\xc9\x9cG\xc7\x01\x8cu\xc5\xda\xc0`5GFn\xd4\x95'
        var_0 = module_0.check_type_bool(bytes_0)
    except BaseException:
        pass

def test_case_13():
    try:
        bytes_0 = b'\xd0'
        var_0 = module_0.check_type_int(bytes_0)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = '}a=<\'c4h\\<"`RDx'
        var_0 = module_0.check_type_int(str_0)
    except BaseException:
        pass

def test_case_15():
    try:
        bytes_0 = b'\x80\xe9x\xbb\xe2\x1ao\xbf\x03L\x02\xa0'
        var_0 = module_0.check_type_float(bytes_0)
    except BaseException:
        pass

def test_case_16():
    try:
        float_0 = None
        set_0 = {float_0, float_0, float_0, float_0}
        var_0 = module_0.check_type_raw(set_0)
        str_0 = '.EGw2%E";\t6P-W"\t\nP)K'
        var_1 = module_0.check_type_dict(str_0)
    except BaseException:
        pass

def test_case_17():
    try:
        int_0 = -3383
        var_0 = module_0.check_type_bytes(int_0)
    except BaseException:
        pass

def test_case_18():
    try:
        dict_0 = {}
        var_0 = module_0.check_type_bits(dict_0)
    except BaseException:
        pass

def test_case_19():
    try:
        int_0 = 152
        var_0 = module_0.check_type_jsonarg(int_0)
    except BaseException:
        pass

def test_case_20():
    try:
        tuple_0 = ()
        var_0 = module_0.check_type_list(tuple_0)
    except BaseException:
        pass

def test_case_21():
    try:
        str_0 = '9Q=)LM@7'
        var_0 = module_0.check_type_bool(str_0)
    except BaseException:
        pass

def test_case_22():
    try:
        list_0 = None
        var_0 = module_0.check_type_float(list_0)
    except BaseException:
        pass

def test_case_23():
    try:
        str_0 = "0(w5IAbal1V)Uo\x0c8'-"
        complex_0 = None
        list_0 = [str_0, str_0, str_0]
        var_0 = module_0.check_required_arguments(complex_0, list_0)
        var_1 = module_0.check_type_list(str_0)
        set_0 = None
        var_2 = module_0.check_type_bits(set_0)
    except BaseException:
        pass

def test_case_24():
    try:
        str_0 = "d86qAH6'w\\uQ; "
        var_0 = module_0.check_type_jsonarg(str_0)
        bytes_0 = b'\xae'
        int_0 = 1871
        tuple_0 = (bytes_0, int_0)
        str_1 = ''
        bool_0 = True
        int_1 = 3067
        bool_1 = None
        str_2 = None
        var_1 = module_0.check_required_arguments(bool_1, str_2)
        float_0 = 1718.0
        var_2 = module_0.safe_eval(bool_0, int_1, float_0)
        var_3 = module_0.check_required_together(tuple_0, str_1)
    except BaseException:
        pass

def test_case_25():
    try:
        str_0 = '}a=<\'c4h\\<"`RDx'
        str_1 = None
        str_2 = 'u&>I'
        var_0 = module_0.check_required_arguments(str_1, str_2)
        var_1 = module_0.check_type_dict(str_0)
        var_2 = module_0.check_type_int(str_2)
    except BaseException:
        pass

def test_case_26():
    try:
        str_0 = "{('N_`O{3YN?V]aVF2/W"
        var_0 = module_0.check_type_dict(str_0)
    except BaseException:
        pass

def test_case_27():
    try:
        complex_0 = None
        var_0 = module_0.check_mutually_exclusive(complex_0, complex_0)
        str_0 = 'P'
        var_1 = module_0.check_type_int(str_0)
    except BaseException:
        pass

def test_case_28():
    try:
        str_0 = '}a=<\'c4h\\<"`RDx'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
        var_0 = module_0.check_required_by(dict_0, dict_0)
        set_0 = set()
        var_1 = module_0.check_missing_parameters(set_0)
        dict_1 = {}
        str_1 = 'h'
        var_2 = module_0.check_required_one_of(dict_1, dict_0, str_1)
        str_2 = '\\^o65&p\rhF<'
        var_3 = module_0.check_type_dict(str_2)
    except BaseException:
        pass

def test_case_29():
    try:
        int_0 = -3347
        list_0 = [int_0, int_0]
        float_0 = 498.534
        var_0 = module_0.check_required_one_of(list_0, list_0, float_0)
        str_0 = 'fcinfo'
        str_1 = '0Ra4`\n\x0chD5'
        set_0 = {str_0, str_1}
        var_1 = module_0.check_required_arguments(str_0, set_0)
    except BaseException:
        pass

def test_case_30():
    try:
        bytes_0 = b"'\x8f["
        int_0 = 29
        tuple_0 = (bytes_0, int_0)
        int_1 = -4981
        var_0 = module_0.check_required_if(tuple_0, int_1)
    except BaseException:
        pass

def test_case_31():
    try:
        str_0 = 'Q^<+9`'
        bytes_0 = b'\xa8\xc1\x07\x1a\xfe'
        set_0 = {str_0, bytes_0, str_0}
        var_0 = module_0.check_required_one_of(str_0, bytes_0, set_0)
    except BaseException:
        pass

def test_case_32():
    try:
        str_0 = 'XJn6ZKOCO}"|6;'
        bytes_0 = None
        bool_0 = None
        bytes_1 = b'\xf7'
        var_0 = module_0.check_required_by(bytes_0, bool_0, bytes_1)
        var_1 = module_0.check_type_int(str_0)
    except BaseException:
        pass

def test_case_33():
    try:
        str_0 = ' l4b^S]m =T'
        var_0 = module_0.check_type_dict(str_0)
    except BaseException:
        pass

def test_case_34():
    try:
        tuple_0 = ()
        str_0 = 'rV5\x0b\x0cHt=f"7D$\x0c5z/4'
        var_0 = module_0.check_required_one_of(str_0, tuple_0)
    except BaseException:
        pass

def test_case_35():
    try:
        int_0 = 1
        int_1 = 2
        int_2 = 3
        var_0 = dict(one=int_0, two=int_1, three=int_2)
        str_0 = 'one'
        str_1 = 'two'
        str_2 = [str_0, str_1]
        str_3 = [str_2]
        var_1 = module_0.check_mutually_exclusive(str_3, var_0)
    except BaseException:
        pass

def test_case_36():
    try:
        str_0 = 'a'
        str_1 = 'b'
        str_2 = [str_0]
        int_0 = 1
        int_1 = 2
        int_2 = {str_0: int_0, str_1: int_1}
        var_0 = module_0.check_mutually_exclusive(str_2, int_2)
        str_3 = [str_0, str_1]
        str_4 = [str_3]
        int_3 = {str_0: int_0, str_1: int_1}
        str_5 = 'key1'
        str_6 = 'key2'
        str_7 = [str_5, str_6]
        var_1 = module_0.check_mutually_exclusive(str_4, int_3, str_7)
    except BaseException:
        pass

def test_case_37():
    try:
        str_0 = 'ne'
        str_1 = '_Qther'
        str_2 = (str_0, str_1)
        str_3 = 'xxx'
        str_4 = [str_2, str_3]
        str_5 = 'other1'
        str_6 = {str_1: str_5}
        var_0 = module_0.check_required_together(str_4, str_6)
    except BaseException:
        pass

def test_case_38():
    try:
        str_0 = 'g)3\tvI\nYb'
        str_1 = 'bool_param'
        bool_0 = True
        var_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_1: bool_0, str_0: str_0}
        var_1 = [str_0, str_0, str_0, bool_0]
        var_2 = [var_1, var_0]
        var_3 = module_0.check_required_if(var_2, var_0)
    except BaseException:
        pass

def test_case_39():
    try:
        str_0 = 'g)3\tvI\nYb'
        str_1 = 'bool_param'
        bool_0 = True
        int_0 = -1148
        var_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_1: bool_0, str_0: str_0}
        var_1 = [str_0, str_0, str_0, bool_0]
        var_2 = [str_0, int_0, str_0, bool_0]
        var_3 = [var_1, var_2]
        var_4 = module_0.check_required_if(var_3, var_0)
    except BaseException:
        pass

def test_case_40():
    try:
        str_0 = 'g)3\tvI\nYb'
        str_1 = 'path'
        str_2 = 'bool_param'
        str_3 = 'present'
        bool_0 = True
        var_0 = {str_0: str_3, str_1: str_2, str_1: str_2, str_2: bool_0, str_2: str_2}
        var_1 = [str_0, str_3, str_3, bool_0]
        str_4 = 'someint'
        int_0 = 80
        str_5 = (str_2, str_4)
        var_2 = [str_4, int_0, str_5]
        str_6 = (str_2, str_4)
        bool_1 = False
        var_3 = [str_4, int_0, str_6, bool_1]
        var_4 = [var_1, var_2, var_3]
        var_5 = module_0.check_required_if(var_4, var_0)
    except BaseException:
        pass

def test_case_41():
    try:
        var_0 = {}
        str_0 = 'y'
        str_1 = ')_O&`!oT'
        str_2 = {}
        var_1 = module_0.check_required_by(str_2, var_0)
        str_3 = {str_0: str_1}
        var_2 = {str_0: var_1}
        var_3 = module_0.check_required_by(str_3, var_2)
    except BaseException:
        pass

def test_case_42():
    try:
        str_0 = 'req!ired_one'
        str_1 = 'required_two'
        str_2 = 'required'
        bool_0 = True
        bool_1 = {str_2: bool_0}
        bool_2 = {str_2: bool_0}
        bool_3 = {str_0: bool_1, str_1: bool_2}
        var_0 = module_0.check_required_arguments(bool_3, str_0)
    except BaseException:
        pass

def test_case_43():
    try:
        var_0 = {}
        str_0 = 'test16'
        var_1 = module_0.check_missing_parameters(var_0, str_0)
    except BaseException:
        pass

def test_case_44():
    try:
        var_0 = None
        var_1 = {}
        var_2 = module_0.check_required_by(var_0, var_1)
        str_0 = 'key'
        str_1 = ')_O&`!oT'
        str_2 = {str_0: str_1}
        var_3 = module_0.check_type_jsonarg(str_2)
        str_3 = {str_0: str_1}
        var_4 = {str_0: var_0}
        var_5 = module_0.check_required_by(str_3, var_4)
        str_4 = {str_0: str_1}
        str_5 = {}
        var_6 = module_0.check_required_by(str_4, str_5)
        str_6 = {str_0: str_1}
        str_7 = 'other'
        str_8 = {str_0: str_1, str_1: str_7}
        var_7 = module_0.check_required_by(str_6, str_8)
        str_9 = {str_0: str_1}
        str_10 = {str_0: str_7}
        var_8 = module_0.check_required_by(str_9, str_10)
    except BaseException:
        pass

def test_case_45():
    try:
        str_0 = 'a'
        str_1 = {str_0: str_0}
        var_0 = None
        var_1 = module_0.check_missing_parameters(str_1, var_0)
        str_2 = {str_0: str_0}
        str_3 = [str_0]
        var_2 = module_0.check_missing_parameters(str_2, str_3)
        str_4 = {str_0: str_0}
        str_5 = 'b'
        str_6 = [str_0, str_5]
        var_3 = module_0.check_missing_parameters(str_4, str_6)
    except BaseException:
        pass

def test_case_46():
    try:
        str_0 = 'a'
        str_1 = 'b'
        str_2 = {str_0: str_1}
        var_0 = module_0.check_type_dict(str_2)
        str_3 = '{"a": "b"}'
        var_1 = module_0.check_type_dict(str_3)
        str_4 = ' a=b,  c = d'
        var_2 = module_0.check_type_dict(str_4)
    except BaseException:
        pass