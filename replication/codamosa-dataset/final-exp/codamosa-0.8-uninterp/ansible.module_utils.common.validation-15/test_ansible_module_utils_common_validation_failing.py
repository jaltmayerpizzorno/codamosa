# Automatically generated by Pynguin.
import ansible.module_utils.common.validation as module_0

def test_case_0():
    try:
        str_0 = '/j'
        set_0 = None
        var_0 = module_0.check_required_one_of(str_0, set_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'\xcd|\xfb"'
        list_0 = []
        float_0 = -933.0
        var_0 = module_0.safe_eval(bytes_0, list_0, float_0)
        str_0 = ';j4x=tIO;|'
        var_1 = module_0.check_type_dict(str_0)
        bytes_1 = b':\xfb\xc7\x0b\xc0s\xcf\x1b\xe9\xf1+\xae]'
        list_1 = [var_1, bytes_1, str_0, bytes_1]
        dict_0 = {bytes_1: bytes_1}
        var_2 = module_0.check_required_one_of(bytes_1, list_1, dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = True
        float_0 = 1139.21811
        dict_0 = {bool_0: bool_0, float_0: bool_0, bool_0: bool_0}
        tuple_0 = (dict_0,)
        var_0 = module_0.check_mutually_exclusive(bool_0, float_0, tuple_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'fo_\x0bo.ar()'
        list_0 = [str_0, str_0, str_0, str_0]
        bytes_0 = b'j\x08\x86\xf3\x8a\xfc\xa0$\xb3\xfc\xbb})\xdd\xec'
        float_0 = 1200.745433
        var_0 = module_0.check_required_one_of(list_0, bytes_0, float_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '#!/usr/bin/python'
        var_0 = module_0.check_required_together(str_0, str_0)
        var_1 = module_0.check_type_float(str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bytes_0 = b';Ue\xc8\xae\xc4p\xf1\xa4\xf0Z\xc0F\xfb\xacg\xcb\xc8T'
        str_0 = ''
        var_0 = module_0.check_required_arguments(bytes_0, str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'fo_\x0bo.ar()'
        var_0 = module_0.safe_eval(str_0)
        str_1 = 'mporoo'
        var_1 = module_0.safe_eval(str_1)
        list_0 = None
        set_0 = set()
        var_2 = module_0.check_required_if(list_0, set_0)
        str_2 = '1TTv~[-\t\x0b_\\`lC})~e_='
        var_3 = module_0.check_type_dict(str_2)
        var_4 = module_0.check_type_bits(list_0)
    except BaseException:
        pass

def test_case_7():
    try:
        bytes_0 = b'\x99\x12]\xac\xf4#{\x9f\xcb\x0f\xbe\xaau\xb1\xcc\xa0\x8b'
        str_0 = 'j\nlr$=exw4=5T\tl@8\x0c\n{'
        var_0 = module_0.count_terms(bytes_0, str_0)
        dict_0 = {}
        list_0 = [dict_0, str_0]
        tuple_0 = ()
        int_0 = 989
        tuple_1 = (list_0, tuple_0, int_0)
        var_1 = module_0.check_required_arguments(dict_0, tuple_1)
        var_2 = module_0.check_type_str(int_0, dict_0)
    except BaseException:
        pass

def test_case_8():
    try:
        tuple_0 = None
        set_0 = {tuple_0, tuple_0, tuple_0}
        tuple_1 = (set_0, tuple_0)
        var_0 = module_0.check_type_list(tuple_1)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'z'
        var_0 = module_0.check_type_dict(str_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = '&>{02o{7Fu~puw'
        var_0 = module_0.check_type_bool(str_0)
    except BaseException:
        pass

def test_case_11():
    try:
        int_0 = 2
        bool_0 = True
        str_0 = ';j4x=tI;;|'
        var_0 = module_0.check_type_dict(str_0)
        tuple_0 = (bool_0,)
        var_1 = module_0.check_type_jsonarg(tuple_0)
        bool_1 = True
        tuple_1 = (int_0, bool_1)
        var_2 = module_0.check_type_bool(tuple_1)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = " >48ArMmZrH$^'/49V"
        var_0 = module_0.check_type_int(str_0)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = '#!/usr/bin/python'
        var_0 = module_0.check_type_float(str_0)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = "+(B9H;0$F$\\Aw '"
        var_0 = module_0.check_type_bytes(str_0)
    except BaseException:
        pass

def test_case_15():
    try:
        bool_0 = True
        var_0 = module_0.check_type_bits(bool_0)
    except BaseException:
        pass

def test_case_16():
    try:
        int_0 = -1896
        var_0 = module_0.check_type_jsonarg(int_0)
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = None
        var_0 = module_0.check_type_int(str_0)
    except BaseException:
        pass

def test_case_18():
    try:
        bytes_0 = b'\x83/o\xf1\xfc\x86\xc6\xde\x89\x00\x1f?3\x96\x9fu'
        bool_0 = True
        set_0 = {bytes_0, bool_0, bytes_0}
        var_0 = module_0.check_type_float(set_0)
    except BaseException:
        pass

def test_case_19():
    try:
        int_0 = 1909
        dict_0 = {int_0: int_0, int_0: int_0}
        dict_1 = {int_0: int_0, int_0: dict_0}
        bytes_0 = b'{\xd9\xf1\xb0Dd'
        var_0 = module_0.check_required_arguments(dict_1, bytes_0)
        str_0 = '.!AI#~'
        var_1 = module_0.check_type_bits(str_0)
    except BaseException:
        pass

def test_case_20():
    try:
        str_0 = "{'foo': 'bar'}"
        str_1 = "6z(h'Z]=u"
        str_2 = '&\\sWi_}64i|8=vQ[Fj2'
        str_3 = 'u'
        dict_0 = {str_0: str_2, str_0: str_2, str_1: str_0}
        set_0 = {str_3}
        var_0 = module_0.check_required_together(dict_0, set_0)
    except BaseException:
        pass

def test_case_21():
    try:
        list_0 = []
        var_0 = module_0.check_type_list(list_0)
        bool_0 = True
        var_1 = module_0.check_type_bits(bool_0)
    except BaseException:
        pass

def test_case_22():
    try:
        int_0 = 1
        var_0 = module_0.check_type_bool(int_0)
        str_0 = '8R'
        int_1 = -502
        var_1 = module_0.check_required_together(str_0, int_1)
    except BaseException:
        pass

def test_case_23():
    try:
        str_0 = '"${3f|R_/(C= 2773'
        var_0 = module_0.check_type_dict(str_0)
        dict_0 = {}
        var_1 = module_0.check_required_if(var_0, dict_0)
    except BaseException:
        pass

def test_case_24():
    try:
        bool_0 = None
        var_0 = module_0.check_required_by(bool_0, bool_0)
        str_0 = '!F'
        bytes_0 = b'\xe4Mk\x95'
        var_1 = module_0.check_mutually_exclusive(bool_0, bytes_0)
        var_2 = module_0.check_type_int(str_0)
    except BaseException:
        pass

def test_case_25():
    try:
        dict_0 = None
        var_0 = module_0.check_type_dict(dict_0)
    except BaseException:
        pass

def test_case_26():
    try:
        bool_0 = True
        str_0 = ';j4x=tIO;|'
        var_0 = module_0.check_type_dict(str_0)
        tuple_0 = (bool_0,)
        list_0 = [str_0, tuple_0, bool_0]
        str_1 = '4'
        var_1 = module_0.check_required_one_of(list_0, str_1)
    except BaseException:
        pass

def test_case_27():
    try:
        str_0 = '\r'
        complex_0 = None
        set_0 = {complex_0, complex_0, complex_0, complex_0}
        var_0 = module_0.check_required_one_of(complex_0, set_0)
        var_1 = module_0.safe_eval(str_0)
        str_1 = "6z(h'Z]=u"
        var_2 = module_0.safe_eval(str_1)
        str_2 = '&\\sWi_}64i|8=vQ[Fj2'
        str_3 = 'zu'
        dict_0 = {var_2: str_2, str_0: str_2, str_1: var_1}
        tuple_0 = (str_3,)
        var_3 = module_0.check_required_by(dict_0, tuple_0)
        var_4 = module_0.check_type_bytes(str_3)
    except BaseException:
        pass

def test_case_28():
    try:
        str_0 = '{"foo": "bar"! "fizz": "buzz"}'
        var_0 = module_0.check_type_dict(str_0)
    except BaseException:
        pass

def test_case_29():
    try:
        bool_0 = False
        var_0 = module_0.check_type_float(bool_0)
        float_0 = -1574.6
        var_1 = module_0.check_type_list(float_0)
        str_0 = '--clear-response-cache'
        var_2 = module_0.check_type_int(str_0)
    except BaseException:
        pass

def test_case_30():
    try:
        str_0 = 'fo_\x0bo.ar()'
        var_0 = module_0.safe_eval(str_0)
        str_1 = 'import oo'
        var_1 = module_0.safe_eval(str_1)
        float_0 = -300.219466
        var_2 = module_0.check_type_float(float_0)
        bytes_0 = b''
        var_3 = module_0.check_type_bytes(bytes_0)
    except BaseException:
        pass

def test_case_31():
    try:
        int_0 = None
        var_0 = module_0.check_type_raw(int_0)
        str_0 = '5|EMpBDMk+\t<41%2cjz'
        var_1 = module_0.check_missing_parameters(str_0)
        int_1 = 1032
        set_0 = {str_0, int_1, int_0}
        bytes_0 = b'c\xcc\x88;;Nb\xd61\x97u'
        dict_0 = {int_1: var_1, bytes_0: bytes_0, var_0: var_1}
        var_2 = module_0.check_required_one_of(dict_0, dict_0)
        float_0 = 462.73
        set_1 = {var_0}
        tuple_0 = (float_0, set_1)
        float_1 = -2174.5962
        tuple_1 = (set_0, tuple_0, float_1)
        bool_0 = None
        var_3 = module_0.check_required_together(tuple_1, bool_0)
    except BaseException:
        pass

def test_case_32():
    try:
        int_0 = 1031
        dict_0 = {int_0: int_0, int_0: int_0, int_0: int_0}
        str_0 = '3q@y]S:|R\\'
        var_0 = module_0.check_missing_parameters(dict_0, str_0)
    except BaseException:
        pass

def test_case_33():
    try:
        str_0 = 'Ww\rWW8d)qb'
        str_1 = '<VALMD$2n\x0cy9SpsN<ci'
        str_2 = "532'"
        list_0 = [str_0, str_2]
        var_0 = module_0.check_required_one_of(str_1, list_0)
    except BaseException:
        pass

def test_case_34():
    try:
        str_0 = 'present'
        int_0 = 99
        var_0 = dict(state=str_0, path=str_0, someint=int_0)
        str_1 = 'someint'
        var_1 = [str_1, int_0, str_1]
        var_2 = [var_0, var_1]
        var_3 = module_0.check_required_if(var_2, var_0)
    except BaseException:
        pass

def test_case_35():
    try:
        dict_0 = {}
        float_0 = 3541.128109620288
        bytes_0 = b'{8_\x9d\x9b\xee\xe5\x8a\xf9\x84%\x02\xd2\xef\xd7_\xc5'
        list_0 = [bytes_0, float_0, dict_0, bytes_0]
        tuple_0 = (list_0, float_0)
        var_0 = module_0.check_required_if(tuple_0, list_0)
    except BaseException:
        pass

def test_case_36():
    try:
        str_0 = "{'foo': 'bar'}"
        str_1 = "6z(h'Z]=u"
        var_0 = module_0.safe_eval(str_1)
        str_2 = '&\\sWi_}64i|8=vQ[Fj2'
        str_3 = 'u'
        dict_0 = {var_0: str_2, str_0: str_2, str_1: var_0}
        tuple_0 = (str_3,)
        var_1 = module_0.check_required_by(dict_0, tuple_0)
        var_2 = module_0.check_type_bytes(str_3)
    except BaseException:
        pass

def test_case_37():
    try:
        str_0 = '"${3\\f|R_/(C= 2773'
        var_0 = module_0.check_type_dict(str_0)
        dict_0 = {}
        var_1 = module_0.check_required_if(var_0, dict_0)
    except BaseException:
        pass

def test_case_38():
    try:
        str_0 = 'a'
        str_1 = 'b'
        str_2 = 'd'
        str_3 = [str_0, str_2]
        str_4 = [str_2, str_3]
        int_0 = 1
        int_1 = {str_0: int_0}
        var_0 = module_0.check_mutually_exclusive(str_1, int_1)
        int_2 = {str_0: int_0, str_1: int_0}
        var_1 = module_0.check_mutually_exclusive(str_4, int_2)
        int_3 = {str_0: int_0, str_2: int_0, str_2: int_0}
        var_2 = module_0.check_mutually_exclusive(str_4, int_3)
    except BaseException:
        pass

def test_case_39():
    try:
        str_0 = "parame'er2"
        str_1 = 'required'
        bool_0 = True
        var_0 = {str_1: str_0, str_1: bool_0}
        var_1 = {str_1: str_0, str_1: var_0, str_1: bool_0, str_1: str_0}
        var_2 = {str_1: var_0, str_0: var_1}
        str_2 = {str_0: str_0}
        var_3 = module_0.check_required_arguments(var_2, str_2)
    except BaseException:
        pass

def test_case_40():
    try:
        str_0 = 'present'
        int_0 = 99
        var_0 = dict(state=str_0, path=str_0, someint=int_0)
        str_1 = 'path'
        str_2 = (str_1,)
        bool_0 = True
        var_1 = [str_0, str_0, str_2, bool_0]
        str_3 = 'someint'
        str_4 = (str_2, str_0)
        var_2 = [str_3, int_0, str_4]
        var_3 = [var_1, var_2]
        var_4 = module_0.check_required_if(var_3, var_0)
    except BaseException:
        pass

def test_case_41():
    try:
        str_0 = ',32/'
        str_1 = 'key_2'
        str_2 = 'key_2_requirement'
        str_3 = {str_0: str_2, str_1: str_2}
        str_4 = 'FmF'
        str_5 = {str_0: str_2, str_1: str_4}
        var_0 = module_0.check_required_by(str_3, str_5)
    except BaseException:
        pass

def test_case_42():
    try:
        str_0 = 'key_1'
        str_1 = 'key_2'
        str_2 = 'key_1_requirement'
        str_3 = [str_2]
        str_4 = 'key_2_requirement'
        str_5 = {str_0: str_3, str_1: str_4}
        str_6 = 'value_2'
        str_7 = {str_0: str_4, str_1: str_6}
        var_0 = module_0.check_required_by(str_5, str_7)
    except BaseException:
        pass

def test_case_43():
    try:
        str_0 = 'key_1'
        str_1 = 'key_2'
        str_2 = 'ke_1_requirement'
        str_3 = [str_1, str_2, str_2]
        str_4 = 'key_2_requirement'
        str_5 = {str_0: str_3, str_1: str_4}
        str_6 = 'FmF'
        str_7 = {str_0: str_4, str_1: str_6}
        var_0 = module_0.check_required_by(str_5, str_7)
    except BaseException:
        pass

def test_case_44():
    try:
        str_0 = 'a'
        str_1 = 'b'
        str_2 = 'c'
        int_0 = 1
        int_1 = 2
        int_2 = 3
        int_3 = {str_0: int_0, str_1: int_1, str_2: int_2}
        str_3 = (str_0, str_1, str_2)
        str_4 = (str_0, str_1, str_2)
        str_5 = 'x'
        str_6 = 'y'
        str_7 = 'z'
        str_8 = (str_5, str_6, str_7)
        str_9 = (str_4, str_8)
        var_0 = module_0.check_required_together(str_9, int_3, str_3)
        var_1 = dict()
        var_2 = module_0.check_required_together(str_9, var_1, str_3)
        str_10 = 'a'
        int_4 = 17
        int_5 = {str_10: int_4}
        var_3 = module_0.check_required_together(str_9, int_5, str_3)
    except BaseException:
        pass

def test_case_45():
    try:
        str_0 = 'fo_\x0bo.ar()'
        var_0 = module_0.safe_eval(str_0)
        str_1 = 'import oo'
        var_1 = module_0.safe_eval(str_0, str_1, str_1)
        list_0 = None
        set_0 = set()
        var_2 = module_0.check_required_if(list_0, set_0)
        str_2 = '}T*Vh-S@WT\rKGglY~>#'
        var_3 = module_0.check_type_dict(str_2)
    except BaseException:
        pass