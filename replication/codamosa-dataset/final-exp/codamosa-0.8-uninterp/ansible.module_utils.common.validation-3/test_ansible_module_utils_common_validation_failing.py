# Automatically generated by Pynguin.
import ansible.module_utils.common.validation as module_0

def test_case_0():
    try:
        str_0 = '{0}{V/2}'
        var_0 = module_0.check_type_dict(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = None
        int_0 = None
        var_0 = module_0.check_mutually_exclusive(bool_0, int_0)
        str_0 = ''
        var_1 = module_0.check_type_dict(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = 656000
        var_0 = module_0.check_required_one_of(int_0, int_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = b'w\x07\x98Lh.\xaf\xd2\xdf\xe8\x89\xe0&U\xa4\xbc'
        str_0 = ''
        var_0 = module_0.check_required_one_of(bytes_0, str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bytes_0 = b'\xb29\xc8\x1ceKf;\xc9\xcc\xd0@\xd5\xbeo\xe8V'
        int_0 = 4099
        var_0 = module_0.check_required_by(bytes_0, int_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '{}1}/{2}'
        var_0 = module_0.check_required_if(str_0, str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        dict_0 = {}
        str_0 = '$I*Y6b,@/YP'
        var_0 = module_0.check_missing_parameters(dict_0, str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        set_0 = None
        complex_0 = None
        var_0 = module_0.check_type_str(set_0, complex_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = '$\tA\t<De\x0bFt'
        var_0 = module_0.check_type_path(str_0)
        int_0 = 642
        bytes_0 = b''
        var_1 = module_0.check_required_together(int_0, bytes_0)
    except BaseException:
        pass

def test_case_9():
    try:
        float_0 = 4594.0196
        dict_0 = {float_0: float_0}
        var_0 = module_0.check_type_list(dict_0)
    except BaseException:
        pass

def test_case_10():
    try:
        bytes_0 = b'\xddEV\xdd\xf6n\x8b\x01\xde{J\xe41u\x06'
        var_0 = module_0.check_type_dict(bytes_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = ''
        var_0 = module_0.check_type_dict(str_0)
    except BaseException:
        pass

def test_case_12():
    try:
        int_0 = 2
        var_0 = module_0.check_type_bool(int_0)
    except BaseException:
        pass

def test_case_13():
    try:
        bytes_0 = b'wA\xacd\x870\xed'
        var_0 = module_0.check_type_bool(bytes_0)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = '1sK'
        var_0 = module_0.check_type_int(str_0)
    except BaseException:
        pass

def test_case_15():
    try:
        bytes_0 = b'?u-U'
        var_0 = module_0.check_type_float(bytes_0)
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = "6Lk\njXe!{'O@C"
        var_0 = module_0.check_type_bytes(str_0)
    except BaseException:
        pass

def test_case_17():
    try:
        tuple_0 = ()
        var_0 = module_0.check_type_bits(tuple_0)
    except BaseException:
        pass

def test_case_18():
    try:
        str_0 = 'CV"BhReUt-:~'
        var_0 = module_0.check_type_bool(str_0)
    except BaseException:
        pass

def test_case_19():
    try:
        bool_0 = None
        var_0 = module_0.check_type_int(bool_0)
    except BaseException:
        pass

def test_case_20():
    try:
        bool_0 = True
        var_0 = module_0.check_missing_parameters(bool_0)
        complex_0 = None
        var_1 = module_0.check_type_float(complex_0)
    except BaseException:
        pass

def test_case_21():
    try:
        set_0 = None
        str_0 = None
        str_1 = None
        list_0 = [set_0, str_0, str_1, str_0]
        var_0 = module_0.check_type_list(list_0)
        bytes_0 = b'\xda%\x84\xda\x9eD\xf3'
        var_1 = module_0.check_type_bytes(bytes_0)
    except BaseException:
        pass

def test_case_22():
    try:
        bool_0 = None
        var_0 = module_0.check_type_jsonarg(bool_0)
    except BaseException:
        pass

def test_case_23():
    try:
        str_0 = 'a'
        str_1 = '\\^`a\t\x0b\x0c\\_g*5Rk"H=\\8'
        str_2 = 'required'
        bool_0 = True
        bool_1 = {str_2: bool_0}
        bool_2 = {str_2: bool_0}
        bool_3 = {str_0: bool_1, str_1: bool_2}
        var_0 = {}
        var_1 = module_0.check_required_arguments(bool_3, var_0)
    except BaseException:
        pass

def test_case_24():
    try:
        bytes_0 = b'\xddEV\xdd\xf6n\x8b\x01\xdeE{J\xe41u\x06'
        int_0 = 4099
        dict_0 = {int_0: bytes_0, bytes_0: bytes_0, bytes_0: int_0}
        float_0 = -59.7188
        var_0 = module_0.check_required_by(dict_0, float_0)
    except BaseException:
        pass

def test_case_25():
    try:
        str_0 = '4'
        str_1 = ",q\\V6Ep=$\ng\\'?B^F"
        var_0 = module_0.check_required_one_of(str_0, str_1)
    except BaseException:
        pass

def test_case_26():
    try:
        str_0 = "['foo', 'bar']"
        var_0 = module_0.safe_eval(str_0)
        set_0 = set()
        str_1 = 's'
        var_1 = module_0.check_required_if(set_0, str_1)
        str_2 = 'oo.bar('
        bool_0 = False
        var_2 = module_0.safe_eval(str_2, bool_0)
        str_3 = 'i8port foo'
        bool_1 = False
        var_3 = module_0.check_type_bool(bool_1)
        str_4 = 'bios_date'
        var_4 = module_0.check_required_one_of(str_3, str_4)
    except BaseException:
        pass

def test_case_27():
    try:
        str_0 = "]clLQc\t@yQ0T'x!s=a"
        dict_0 = {str_0: str_0}
        str_1 = 'yc!HTO/-htU\nN!MK/'
        var_0 = module_0.check_required_together(dict_0, str_1)
    except BaseException:
        pass

def test_case_28():
    try:
        float_0 = 0.0001
        var_0 = module_0.check_type_float(float_0)
        str_0 = 'Y\x0cf5(`:;[)~LMvw~,Z'
        tuple_0 = ()
        var_1 = module_0.check_missing_parameters(str_0, tuple_0)
        bytes_0 = b'b\r8\nw\xfa\x0b8?\xf6\xf3\x9eP\x9cu3\x8a'
        var_2 = module_0.check_type_dict(bytes_0)
    except BaseException:
        pass

def test_case_29():
    try:
        float_0 = None
        bool_0 = False
        var_0 = module_0.check_required_one_of(float_0, bool_0)
        str_0 = '{0}{Ve@}'
        var_1 = module_0.check_type_dict(str_0)
    except BaseException:
        pass

def test_case_30():
    try:
        bytes_0 = b'\x7f\xff&'
        tuple_0 = (bytes_0,)
        str_0 = 'z1]g0oI[=iq~l'
        dict_0 = {str_0: tuple_0}
        var_0 = module_0.check_required_by(dict_0, dict_0)
    except BaseException:
        pass

def test_case_31():
    try:
        bytes_0 = b'\x8a\x7f\xffl&'
        tuple_0 = (bytes_0,)
        str_0 = 'z1]g0oxI[=iq~l'
        dict_0 = {tuple_0: str_0}
        var_0 = module_0.check_required_by(dict_0, dict_0)
    except BaseException:
        pass

def test_case_32():
    try:
        bytes_0 = b'\x8a\x7f\xffl&'
        tuple_0 = (bytes_0,)
        str_0 = 'z1]g0oxI[=iq~l'
        dict_0 = {tuple_0: str_0}
        str_1 = 'p\ny#5\n&R+U_UWz'
        var_0 = module_0.check_required_by(dict_0, dict_0, str_1)
    except BaseException:
        pass

def test_case_33():
    try:
        str_0 = '{0}{Ve\x0cj'
        bool_0 = True
        bytes_0 = b'\x8c\xbf\x01\xac\xeb\xae\xb1\xedq\xd5nWh-\xf8\xb6'
        var_0 = module_0.check_type_path(bytes_0)
        int_0 = 177
        float_0 = 512.0
        dict_0 = {bool_0: int_0, int_0: str_0, str_0: float_0, str_0: bool_0}
        tuple_0 = (dict_0,)
        var_1 = module_0.check_required_if(tuple_0, str_0, int_0)
    except BaseException:
        pass

def test_case_34():
    try:
        str_0 = "]lLQc\t@KMQ0Z'x!s=a"
        bool_0 = False
        list_0 = [str_0, bool_0]
        int_0 = -1828
        set_0 = {bool_0, int_0}
        tuple_0 = (list_0, int_0, set_0, set_0)
        str_1 = '=Hx.8$\x0b'
        int_1 = -754
        tuple_1 = (tuple_0, str_1, int_1)
        str_2 = "3{F*(#B7~'iHs"
        var_0 = module_0.check_required_if(tuple_1, str_2)
    except BaseException:
        pass

def test_case_35():
    try:
        str_0 = '{0i\x0c}{Ve@}'
        list_0 = [str_0, str_0]
        dict_0 = {}
        bool_0 = True
        tuple_0 = (list_0, dict_0, bool_0)
        var_0 = module_0.check_required_one_of(tuple_0, dict_0, bool_0)
    except BaseException:
        pass

def test_case_36():
    try:
        str_0 = ')*J\r=DXE\x0b!H \x0b/<'
        var_0 = module_0.check_type_dict(str_0)
    except BaseException:
        pass

def test_case_37():
    try:
        bytes_0 = b'\x1c'
        tuple_0 = (bytes_0,)
        str_0 = 'z1]g0oxI[=iq~l'
        dict_0 = {str_0: str_0, tuple_0: tuple_0}
        var_0 = module_0.check_required_by(dict_0, dict_0)
    except BaseException:
        pass

def test_case_38():
    try:
        str_0 = "]lLQc\t@KMQ0Z'x!s=a"
        bool_0 = False
        list_0 = [str_0, bool_0]
        int_0 = -1808
        bytes_0 = None
        float_0 = -355.2236
        str_1 = 'A1Q5t5BL'
        var_0 = module_0.safe_eval(bytes_0, float_0, str_1)
        set_0 = {bool_0, int_0}
        set_1 = set()
        tuple_0 = (set_1, list_0)
        dict_0 = {int_0: tuple_0}
        var_1 = module_0.check_missing_parameters(dict_0, set_0)
    except BaseException:
        pass

def test_case_39():
    try:
        str_0 = 'state'
        str_1 = 'present'
        bool_0 = True
        var_0 = [str_0, str_1, str_1, bool_0]
        str_2 = 'bool_pa/*ram'
        var_1 = [var_0, bool_0]
        var_2 = dict(state=str_1, path=str_2)
        var_3 = [str_0]
        var_4 = module_0.check_required_if(var_1, var_2, var_3)
    except BaseException:
        pass

def test_case_40():
    try:
        str_0 = 'jFo@:Z\x0cc:;<W$G-U$Y'
        str_1 = 'present'
        str_2 = (str_1,)
        bool_0 = False
        var_0 = [str_0, str_1, str_2, bool_0]
        str_3 = 'someint'
        int_0 = 99
        str_4 = (str_0, str_3)
        var_1 = [str_3, int_0, str_4]
        var_2 = [var_0, var_1]
        var_3 = []
        var_4 = dict(state=str_1)
        var_5 = dict(someint=int_0)
        var_6 = module_0.check_required_if(var_2, var_5, var_3)
    except BaseException:
        pass

def test_case_41():
    try:
        str_0 = 'jFo@:Z\x0cc:;<W$G-U$Y'
        str_1 = 'present'
        str_2 = (str_1,)
        bool_0 = False
        var_0 = [str_0, str_1, str_2, bool_0]
        str_3 = 'someint'
        int_0 = 99
        str_4 = (str_0, str_3)
        var_1 = [var_0, int_0]
        var_2 = dict(state=str_1, path=str_4)
        var_3 = []
        var_4 = dict(state=str_1)
        var_5 = module_0.check_required_if(var_1, str_3, var_3)
    except BaseException:
        pass

def test_case_42():
    try:
        str_0 = 'r2'
        str_1 = 'required'
        str_2 = 'type'
        bool_0 = True
        str_3 = 'bool'
        var_0 = {str_1: bool_0, str_2: str_3}
        str_4 = 'str'
        str_5 = {str_2: str_4}
        var_1 = {str_3: var_0, str_0: str_5}
        bool_1 = {str_1: str_5, str_0: str_1, str_1: bool_0}
        var_2 = module_0.check_required_arguments(var_1, bool_1)
    except BaseException:
        pass

def test_case_43():
    try:
        str_0 = 'arg1'
        str_1 = 'arg2'
        str_2 = 'required'
        str_3 = 'type'
        bool_0 = True
        str_4 = 'bool'
        var_0 = {str_2: bool_0, str_3: str_4}
        str_5 = 'str'
        str_6 = {str_3: str_5}
        var_1 = {str_0: var_0, str_1: str_6}
        bool_1 = {str_0: bool_0}
        var_2 = module_0.check_required_arguments(var_1, bool_1)
        var_3 = len(var_2)
        var_4 = {}
        var_5 = module_0.check_required_arguments(var_1, var_4)
    except BaseException:
        pass

def test_case_44():
    try:
        str_0 = 'state'
        str_1 = 'present'
        str_2 = (str_1,)
        bool_0 = True
        var_0 = [str_0, str_1, str_2, bool_0]
        int_0 = 99
        str_3 = 'bool_param'
        dict_0 = {bool_0: str_1, str_1: str_3}
        float_0 = 0.0
        var_1 = module_0.check_required_one_of(dict_0, dict_0, float_0)
        var_2 = [str_0, int_0, str_2]
        var_3 = [var_0, var_2]
        str_4 = '/my/path'
        var_4 = dict(state=str_1, path=str_4)
        var_5 = []
        var_6 = module_0.check_required_if(var_3, var_4, var_5)
    except BaseException:
        pass

def test_case_45():
    try:
        str_0 = 'foo.bar()'
        bool_0 = True
        var_0 = module_0.safe_eval(str_0, bool_0)
        str_1 = 'i8port foo'
        var_1 = module_0.check_type_bytes(str_1)
    except BaseException:
        pass

def test_case_46():
    try:
        str_0 = 'b'
        str_1 = 'c'
        str_2 = [str_1, str_0, str_1]
        str_3 = [str_2]
        int_0 = 1
        int_1 = {str_0: int_0, str_0: int_0, str_1: int_0}
        var_0 = module_0.check_mutually_exclusive(str_3, int_1)
    except BaseException:
        pass

def test_case_47():
    try:
        str_0 = 'state'
        str_1 = 'present'
        str_2 = (str_1,)
        bool_0 = True
        var_0 = [str_0, str_1, str_2, bool_0]
        bool_1 = True
        dict_0 = {str_2: str_2, str_1: var_0, str_2: bool_1}
        list_0 = []
        int_0 = 384
        var_1 = module_0.check_type_int(int_0)
        var_2 = module_0.check_mutually_exclusive(dict_0, dict_0, dict_0)
        int_1 = -1389
        str_3 = 'boo_parm'
        dict_1 = {bool_0: str_1, str_1: str_3}
        float_0 = -1832.5
        var_3 = module_0.check_required_one_of(dict_1, dict_1, float_0)
        var_4 = [str_0, int_1, str_2]
        var_5 = [var_0, var_4]
        str_4 = '/my/path'
        var_6 = module_0.check_type_jsonarg(list_0)
        var_7 = dict(state=str_1, path=str_4)
        var_8 = module_0.check_required_if(var_5, var_7, int_0)
    except BaseException:
        pass

def test_case_48():
    try:
        int_0 = 1
        int_1 = 2
        var_0 = dict(param1=int_0, param2=int_1)
        str_0 = 'param2'
        str_1 = [str_0]
        str_2 = 'param4'
        str_3 = 'param5'
        str_4 = [str_2, str_3]
        var_1 = dict(param1=str_1, param3=str_4)
        var_2 = module_0.check_required_by(var_1, var_0)
        str_5 = [str_0]
        var_3 = dict(param1=str_5)
        int_2 = 3
        var_4 = dict(param1=int_0, param3=int_2)
        var_5 = module_0.check_required_by(var_1, var_4)
    except BaseException:
        pass