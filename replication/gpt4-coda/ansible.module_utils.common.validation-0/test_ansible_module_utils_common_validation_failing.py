# Automatically generated by Pynguin.
import ansible.module_utils.common.validation as module_0

def test_case_0():
    try:
        str_0 = 'OPsqU\nk^Ru5)uI'
        bytes_0 = b'\xc7[\x1b'
        var_0 = module_0.check_required_one_of(str_0, bytes_0)
    except BaseException:
        pass

def test_case_1():
    try:
        complex_0 = None
        tuple_0 = None
        var_0 = module_0.check_required_together(complex_0, tuple_0)
        str_0 = ';'
        var_1 = module_0.check_type_dict(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '0bDFo&iki8w\\ZMH\r'
        var_0 = module_0.check_required_by(str_0, str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        float_0 = -924.5
        set_0 = {float_0, float_0}
        bool_0 = False
        var_0 = module_0.check_required_arguments(set_0, bool_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'L7Rf1Z'
        dict_0 = {str_0: str_0, str_0: str_0}
        int_0 = 2205
        var_0 = module_0.check_required_arguments(dict_0, int_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '{'
        bool_0 = False
        tuple_0 = None
        var_0 = module_0.check_required_arguments(tuple_0, str_0)
        var_1 = module_0.check_type_int(bool_0)
        var_2 = module_0.check_type_dict(str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'q\x0b@-xFEjJ^tw?V|'
        var_0 = module_0.check_required_if(str_0, str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        int_0 = -151
        str_0 = 'failed to copy: {0} and {1} are the same'
        var_0 = module_0.count_terms(int_0, str_0)
        str_1 = None
        var_1 = module_0.check_type_list(str_1)
    except BaseException:
        pass

def test_case_8():
    try:
        list_0 = []
        var_0 = module_0.check_type_dict(list_0)
    except BaseException:
        pass

def test_case_9():
    try:
        list_0 = None
        var_0 = module_0.check_type_bool(list_0)
    except BaseException:
        pass

def test_case_10():
    try:
        float_0 = -2232.0
        var_0 = module_0.check_type_bool(float_0)
    except BaseException:
        pass

def test_case_11():
    try:
        bytes_0 = b'\xe3\xdet\xd0q\x8b\x9e\x9buu""\xae\xe8\x96\x18O\xc0@'
        var_0 = module_0.check_type_int(bytes_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = ''
        var_0 = module_0.check_type_int(str_0)
    except BaseException:
        pass

def test_case_13():
    try:
        bytes_0 = b'I\x02\xccR\x99\x03\xa6\x98*\xe3\xfd\xcc\xd7\xa0b(l\x04\xa4'
        var_0 = module_0.check_type_float(bytes_0)
    except BaseException:
        pass

def test_case_14():
    try:
        list_0 = None
        var_0 = module_0.check_type_bytes(list_0)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = '{YPe*kS~>.p\n*cZ'
        var_0 = module_0.check_type_bits(str_0)
    except BaseException:
        pass

def test_case_16():
    try:
        set_0 = set()
        bool_0 = True
        var_0 = module_0.safe_eval(bool_0)
        var_1 = module_0.check_type_jsonarg(set_0)
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = 'ESUr)MwuL#IvUtW[\n]Tu'
        var_0 = module_0.check_type_path(str_0)
        var_1 = module_0.check_type_bool(str_0)
    except BaseException:
        pass

def test_case_18():
    try:
        str_0 = ']L3KWmZ7u\t'
        var_0 = module_0.check_required_together(str_0, str_0)
        tuple_0 = None
        var_1 = module_0.check_type_float(tuple_0)
    except BaseException:
        pass

def test_case_19():
    try:
        bool_0 = False
        bytes_0 = b'd\xd0\xac\xad\x1fDCv7>\xca\xaa\x17\xd6'
        list_0 = [bytes_0, bool_0, bool_0]
        complex_0 = None
        dict_0 = {bool_0: bool_0, bytes_0: complex_0, bool_0: list_0, complex_0: list_0, bytes_0: bytes_0}
        var_0 = module_0.check_required_by(dict_0, list_0)
    except BaseException:
        pass

def test_case_20():
    try:
        str_0 = '8tka4'
        var_0 = module_0.check_type_dict(str_0)
    except BaseException:
        pass

def test_case_21():
    try:
        bytes_0 = b'\x0c\\d'
        set_0 = set()
        list_0 = [bytes_0, set_0]
        var_0 = module_0.check_required_if(list_0, list_0)
    except BaseException:
        pass

def test_case_22():
    try:
        set_0 = set()
        int_0 = 1277
        tuple_0 = (int_0,)
        var_0 = module_0.check_required_if(set_0, tuple_0)
        set_1 = set()
        bytes_0 = b'\xbbK\xe0\xc5^\x00\xad)\\A\x96Z'
        list_0 = [bytes_0, set_1]
        float_0 = 0.0
        var_1 = module_0.check_type_str(list_0, float_0)
    except BaseException:
        pass

def test_case_23():
    try:
        str_0 = '{'
        int_0 = 29
        var_0 = module_0.check_type_list(int_0)
        bool_0 = False
        int_1 = 2104
        var_1 = module_0.check_type_int(int_1)
        tuple_0 = None
        bytes_0 = b'\x00l\xb8\x05!\x01\x80\x96/\xcd\xee7\xc3\xff'
        var_2 = module_0.check_required_if(tuple_0, bytes_0)
        var_3 = module_0.check_required_arguments(tuple_0, str_0)
        var_4 = module_0.check_type_int(bool_0)
        str_1 = '[sudo via ansible, key=%s] password:'
        var_5 = module_0.check_type_dict(str_1)
    except BaseException:
        pass

def test_case_24():
    try:
        float_0 = 3154.591
        float_1 = -3669.810215
        var_0 = module_0.check_type_list(float_1)
        int_0 = 92
        var_1 = module_0.check_type_list(int_0)
        str_0 = 'Vyp>&JgaYwW'
        var_2 = module_0.check_type_bits(float_0)
        bytes_0 = b'[@\xc2\x9f\xb6\x1e\x1d\xb5\x01\\\x16'
        var_3 = module_0.check_required_arguments(str_0, bytes_0)
    except BaseException:
        pass

def test_case_25():
    try:
        bool_0 = False
        bytes_0 = b'r\x9f\xa5Z\xc82\xe2m\xacx\xbd=\xdb\x8f}+\xbc\x1c\xfe\xa6'
        var_0 = module_0.safe_eval(bool_0, bool_0, bytes_0)
        str_0 = '}BWBwd@d,'
        list_0 = [bytes_0, bytes_0, bool_0]
        var_1 = module_0.check_type_jsonarg(list_0)
        var_2 = module_0.check_type_int(str_0)
    except BaseException:
        pass

def test_case_26():
    try:
        tuple_0 = ()
        var_0 = module_0.check_type_str(tuple_0)
        bool_0 = True
        var_1 = module_0.safe_eval(bool_0)
        str_0 = '(GWaHzy}>o'
        list_0 = [str_0, var_1, var_1]
        float_0 = -1108.80034
        var_2 = module_0.check_required_one_of(str_0, list_0, float_0)
    except BaseException:
        pass

def test_case_27():
    try:
        bytes_0 = b'\xbbK\xe0\xc5^\x00\xad)\\A\x96Z'
        str_0 = 'Invalid type supplied for source option, it must be a string'
        bytes_1 = b'y\xcfy\x11\nB\xd7$\xc0\xee\xe12f\xbd'
        list_0 = [bytes_1, bytes_0, str_0]
        var_0 = module_0.check_type_list(list_0)
        str_1 = '\td^Y[W:~9'
        var_1 = module_0.safe_eval(str_1)
        int_0 = 3045
        dict_0 = {var_1: bytes_0}
        var_2 = module_0.check_required_by(int_0, dict_0)
    except BaseException:
        pass

def test_case_28():
    try:
        bool_0 = False
        tuple_0 = None
        str_0 = 'eRKb3BNUOBA0'
        bytes_0 = b'\x00l\xb8\x05!\x01\x80\x96/\xcd\xee7\xc3\xff'
        var_0 = module_0.check_required_if(tuple_0, bytes_0)
        var_1 = module_0.check_required_arguments(tuple_0, str_0)
        var_2 = module_0.check_type_int(bool_0)
        str_1 = '[sudo via ansible, key=%s] password:'
        var_3 = module_0.check_type_dict(str_1)
    except BaseException:
        pass

def test_case_29():
    try:
        str_0 = '0bDFo&iki8w\\ZMH\r'
        set_0 = {str_0, str_0}
        var_0 = module_0.check_missing_parameters(set_0, str_0)
    except BaseException:
        pass

def test_case_30():
    try:
        bytes_0 = b'\x0c\xe7\\d'
        set_0 = set()
        bool_0 = False
        var_0 = module_0.safe_eval(bool_0)
        float_0 = 999.5093907242075
        str_0 = ''
        bytes_1 = b'1\x98\x96\x0c\xab_\x869>\xe5,OqsI+\xd8\xde}'
        bool_1 = False
        var_1 = module_0.check_type_int(bool_1)
        tuple_0 = (float_0, str_0, bytes_1)
        var_2 = module_0.check_required_together(set_0, tuple_0)
        list_0 = [bytes_0, bool_1, set_0, var_0]
        var_3 = module_0.check_required_if(list_0, list_0)
    except BaseException:
        pass

def test_case_31():
    try:
        bytes_0 = b'\x0c\\d'
        set_0 = set()
        list_0 = [bytes_0, set_0]
        var_0 = module_0.check_required_if(list_0, bytes_0)
    except BaseException:
        pass

def test_case_32():
    try:
        str_0 = '{'
        var_0 = module_0.check_type_dict(str_0)
    except BaseException:
        pass

def test_case_33():
    try:
        int_0 = -3043
        dict_0 = {int_0: int_0, int_0: int_0}
        var_0 = module_0.check_missing_parameters(dict_0, dict_0)
        float_0 = -294.36648771732325
        list_0 = []
        var_1 = module_0.check_required_arguments(float_0, list_0)
    except BaseException:
        pass

def test_case_34():
    try:
        str_0 = '^eK#Lw.+'
        list_0 = []
        var_0 = module_0.check_type_list(list_0)
        var_1 = module_0.check_type_jsonarg(str_0)
        bool_0 = True
        var_2 = module_0.check_type_str(bool_0)
        bytes_0 = b'\x0c\\d'
        str_1 = '<pR'
        str_2 = '3axom`C='
        float_0 = -335.8
        var_3 = module_0.check_type_float(float_0)
        set_0 = {str_1, bool_0, str_2, str_2}
        str_3 = "(QpMzLsAyk\x0bJb6c?\n'[="
        var_4 = module_0.count_terms(bytes_0, str_3)
        bool_1 = True
        list_1 = [set_0, set_0, bytes_0, bool_1, set_0, set_0]
        var_5 = module_0.check_required_if(list_1, list_1)
    except BaseException:
        pass

def test_case_35():
    try:
        str_0 = "{'key': 'value'}"
        str_1 = '[1, 2, 3]'
        dict_0 = {}
        float_0 = -200.91
        list_0 = [dict_0, dict_0, dict_0, str_1]
        var_0 = module_0.check_mutually_exclusive(str_0, dict_0)
        list_1 = [list_0]
        tuple_0 = (float_0, list_1, float_0)
        var_1 = module_0.check_type_str(tuple_0)
        var_2 = module_0.check_missing_parameters(dict_0)
        bool_0 = False
        var_3 = module_0.check_required_arguments(dict_0, tuple_0, bool_0)
        bytes_0 = b'}O\xb6\x91\x03\xac<\xa5\n\xc8G\xef'
        var_4 = module_0.check_type_float(float_0)
        var_5 = module_0.check_type_bits(bytes_0)
    except BaseException:
        pass

def test_case_36():
    try:
        str_0 = 'state'
        str_1 = 'enabled'
        str_2 = 'test'
        bool_0 = True
        var_0 = {str_2: str_2, str_0: str_2, str_1: bool_0}
        var_1 = None
        var_2 = module_0.check_required_together(var_1, var_0)
        var_3 = module_0.check_required_together(str_1, var_0)
        str_3 = 'name'
        str_4 = 'missing'
        str_5 = [str_3, str_4, str_0]
        str_6 = [str_5]
        var_4 = module_0.check_required_together(str_6, var_0)
    except BaseException:
        pass

def test_case_37():
    try:
        str_0 = 'Mtest'
        str_1 = 'value1'
        str_2 = {str_0: str_1}
        str_3 = {str_0: str_1}
        var_0 = module_0.check_required_by(str_2, str_3)
    except BaseException:
        pass

def test_case_38():
    try:
        str_0 = 'g'
        str_1 = 'c} A,\\^l'
        str_2 = [str_0, str_1, str_1]
        var_0 = [str_2, str_2]
        str_3 = {str_0: str_1}
        var_1 = module_0.check_required_if(var_0, str_3)
    except BaseException:
        pass

def test_case_39():
    try:
        var_0 = None
        var_1 = {}
        var_2 = module_0.check_required_if(var_0, var_1)
        str_0 = 'state'
        str_1 = 'present'
        str_2 = 'path'
        str_3 = [str_0, str_1, str_0]
        str_4 = 'someint'
        int_0 = 99
        str_5 = 'bool_param'
        str_6 = [str_5, str_2]
        var_3 = [str_4, int_0, str_6]
        var_4 = [str_2, str_3, str_3, var_3]
        var_5 = {}
        var_6 = module_0.check_required_if(var_4, var_5)
        str_7 = {str_0: str_1}
        var_7 = module_0.check_required_if(var_4, str_7)
    except BaseException:
        pass

def test_case_40():
    try:
        str_0 = ''
        str_1 = 'c} A,\\^l'
        str_2 = [str_0, str_1]
        str_3 = [str_0, str_1, str_2]
        var_0 = [str_3, str_3]
        str_4 = {str_0: str_1}
        var_1 = module_0.check_required_if(var_0, str_4)
    except BaseException:
        pass

def test_case_41():
    try:
        str_0 = 'name'
        str_1 = 'state'
        str_2 = ';'
        str_3 = {str_0: str_2, str_1: str_1}
        var_0 = module_0.check_mutually_exclusive(str_1, str_3)
        str_4 = {str_0: str_2, str_1: str_0}
        str_5 = [str_0, str_1]
        str_6 = [str_5]
        var_1 = module_0.check_mutually_exclusive(str_6, str_4)
    except BaseException:
        pass

def test_case_42():
    try:
        str_0 = 'name'
        str_1 = 'state'
        str_2 = 'enabled'
        str_3 = 'required'
        str_4 = 'type'
        bool_0 = True
        var_0 = {str_3: bool_0, str_4: str_0}
        str_5 = 'default'
        bool_1 = False
        str_6 = 'present'
        var_1 = {str_3: bool_1, str_4: str_2, str_5: str_6}
        var_2 = {str_3: bool_0, str_4: str_5}
        var_3 = {str_0: var_0, str_1: var_1, str_2: var_2}
        str_7 = 'test'
        var_4 = {str_0: str_7, str_2: bool_0}
        var_5 = module_0.check_required_arguments(var_3, var_4)
        str_8 = {str_0: str_7}
        var_6 = module_0.check_required_arguments(var_3, str_8)
    except BaseException:
        pass

def test_case_43():
    try:
        str_0 = 'param1'
        str_1 = 'value1'
        str_2 = {str_0: str_1}
        var_0 = module_0.check_missing_parameters(str_2)
        str_3 = {str_0: str_1}
        str_4 = [str_0]
        var_1 = module_0.check_missing_parameters(str_3, str_4)
        str_5 = 'param1'
        str_6 = 'value1'
        str_7 = {str_5: str_6}
        str_8 = 'param2'
        str_9 = [str_8]
        var_2 = module_0.check_missing_parameters(str_7, str_9)
    except BaseException:
        pass

def test_case_44():
    try:
        str_0 = 'name'
        str_1 = 'state'
        str_2 = 'enabled'
        str_3 = 'config'
        str_4 = 'test'
        str_5 = 'present'
        bool_0 = True
        var_0 = None
        var_1 = {str_0: str_4, str_1: str_5, str_2: bool_0, str_3: var_0}
        str_6 = [str_0]
        str_7 = {str_1: str_6}
        var_2 = module_0.check_required_by(str_7, var_1)
        str_8 = {str_1: str_3}
        var_3 = module_0.check_required_by(str_8, var_1)
    except BaseException:
        pass

def test_case_45():
    try:
        str_0 = 'g'
        str_1 = 'c} A,\\^l'
        str_2 = [str_0, str_1]
        str_3 = [str_0, str_1, str_2]
        var_0 = [str_3, str_3]
        str_4 = {str_0: str_1}
        bool_0 = False
        var_1 = module_0.safe_eval(bool_0)
        var_2 = module_0.check_required_if(var_0, str_4, str_1)
    except BaseException:
        pass