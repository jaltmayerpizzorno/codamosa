# Automatically generated by Pynguin.
import ansible.module_utils.common.validation as module_0

def test_case_0():
    try:
        str_0 = '?z @'
        tuple_0 = ()
        var_0 = module_0.check_required_one_of(str_0, tuple_0)
    except BaseException:
        pass

def test_case_1():
    try:
        dict_0 = None
        bool_0 = True
        str_0 = '1^XRZ>Bmy=;j+a'
        var_0 = module_0.safe_eval(dict_0, bool_0, str_0)
        list_0 = []
        var_1 = module_0.check_type_bool(list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = None
        set_0 = {bool_0}
        var_0 = module_0.check_required_one_of(bool_0, set_0)
        bytes_0 = b'I\xf1\xfa\xc3\x12\xdck\xbe\xcb\xed\x83'
        var_1 = module_0.check_type_dict(bytes_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'eU\n|2<l\rm)Mcuht%H)j'
        dict_0 = {}
        var_0 = module_0.check_required_by(str_0, dict_0)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = -1189
        bool_0 = None
        var_0 = module_0.check_required_arguments(int_0, bool_0)
    except BaseException:
        pass

def test_case_5():
    try:
        float_0 = -374.27508
        list_0 = [float_0, float_0]
        bool_0 = True
        var_0 = module_0.check_required_if(list_0, bool_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '9z5\x0b\\:4i0\x0c'
        var_0 = module_0.check_missing_parameters(str_0, str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        tuple_0 = None
        list_0 = []
        var_0 = module_0.check_type_str(tuple_0, list_0)
    except BaseException:
        pass

def test_case_8():
    try:
        bytes_0 = b'\x1fT\xce\xec\xa38\xd2\xa7\xa4I\x14\xdd\x9b'
        var_0 = module_0.check_type_list(bytes_0)
    except BaseException:
        pass

def test_case_9():
    try:
        float_0 = -1948.781411
        var_0 = module_0.check_type_list(float_0)
        str_0 = 'f.'
        var_1 = module_0.check_type_list(str_0)
        set_0 = None
        var_2 = module_0.check_type_dict(set_0)
    except BaseException:
        pass

def test_case_10():
    try:
        float_0 = -374.27508
        var_0 = module_0.check_type_dict(float_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = 'r^qv7\x0bc+H!!A]v1\\;q'
        var_0 = module_0.check_type_int(str_0)
    except BaseException:
        pass

def test_case_12():
    try:
        dict_0 = {}
        var_0 = module_0.check_type_float(dict_0)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = '9z5\x0b\\:4i0\x0c'
        var_0 = module_0.check_type_float(str_0)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = ']#TJQ,~I'
        var_0 = module_0.check_type_bytes(str_0)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = 'B8S'
        var_0 = module_0.check_type_bits(str_0)
    except BaseException:
        pass

def test_case_16():
    try:
        dict_0 = {}
        var_0 = module_0.check_type_dict(dict_0)
        complex_0 = None
        bytes_0 = b'\xa8\xd6\xf4\xdd\x0f\xe2\x8d\x99\xff\xe8l^\xaf\x84'
        list_0 = [bytes_0, complex_0]
        var_1 = module_0.check_mutually_exclusive(bytes_0, list_0)
        bool_0 = None
        var_2 = module_0.check_type_raw(bool_0)
        float_0 = -622.377
        var_3 = module_0.check_type_jsonarg(float_0)
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = '\x0bKGBk#\x0cx<}4r7M'
        var_0 = module_0.check_required_together(str_0, str_0)
        str_1 = 'exec_wrapper'
        float_0 = None
        bytes_0 = b'r\xb2\xc6V'
        str_2 = ''
        dict_0 = {float_0: float_0}
        var_1 = module_0.check_type_jsonarg(dict_0)
        set_0 = {float_0, bytes_0, str_2, str_1}
        var_2 = module_0.check_type_path(set_0)
        dict_1 = {}
        str_3 = 'y"K8&?|sB|x1'
        var_3 = module_0.check_required_by(dict_1, str_3)
        str_4 = 'Blm'
        var_4 = module_0.check_required_if(float_0, str_4)
        tuple_0 = (str_4, bytes_0)
        var_5 = module_0.check_type_dict(tuple_0)
    except BaseException:
        pass

def test_case_18():
    try:
        str_0 = 'AlmaLinux'
        list_0 = [str_0, str_0, str_0, str_0]
        dict_0 = {str_0: list_0}
        var_0 = module_0.check_type_int(dict_0)
    except BaseException:
        pass

def test_case_19():
    try:
        set_0 = None
        bool_0 = False
        var_0 = module_0.check_mutually_exclusive(set_0, bool_0)
        str_0 = "\r\x0cG25Wa]3\nF,z0S'e%E"
        var_1 = module_0.safe_eval(str_0)
        tuple_0 = ()
        var_2 = module_0.check_type_bits(tuple_0)
    except BaseException:
        pass

def test_case_20():
    try:
        int_0 = 126
        var_0 = module_0.check_type_bool(int_0)
    except BaseException:
        pass

def test_case_21():
    try:
        str_0 = '$l2BO|*$>M:\x0b+zPqG'
        var_0 = module_0.check_type_bool(str_0)
    except BaseException:
        pass

def test_case_22():
    try:
        float_0 = 1.0
        dict_0 = {float_0: float_0}
        list_0 = [dict_0, dict_0, dict_0, dict_0]
        int_0 = 2962
        var_0 = module_0.check_required_arguments(dict_0, list_0, int_0)
    except BaseException:
        pass

def test_case_23():
    try:
        str_0 = 'P('
        var_0 = module_0.check_type_dict(str_0)
    except BaseException:
        pass

def test_case_24():
    try:
        str_0 = ' searches for roles on the Ansible Galaxy server'
        str_1 = '|QD5%d;|/P9.}w9]66t'
        set_0 = {str_0, str_1}
        var_0 = module_0.check_required_if(str_1, str_1, set_0)
    except BaseException:
        pass

def test_case_25():
    try:
        str_0 = 'q5dAET|y7q'
        var_0 = module_0.check_required_together(str_0, str_0)
        bytes_0 = b'`'
        var_1 = module_0.check_type_dict(bytes_0)
    except BaseException:
        pass

def test_case_26():
    try:
        bool_0 = False
        bytes_0 = b'd\x19\x1a\x1e5'
        var_0 = module_0.count_terms(bool_0, bytes_0)
        int_0 = 437
        bytes_1 = b'\x87'
        list_0 = [bool_0, int_0, bytes_1]
        var_1 = module_0.check_type_list(list_0)
        str_0 = '3NEz~Gm_iwdL;*I'
        bool_1 = True
        var_2 = module_0.check_required_arguments(str_0, bool_1)
    except BaseException:
        pass

def test_case_27():
    try:
        str_0 = '4V(>Gf(|sw)&'
        bool_0 = False
        str_1 = '}]G'
        var_0 = module_0.safe_eval(str_0, bool_0, str_1)
        tuple_0 = None
        str_2 = '\'iie-U"\'.`0CCx'
        var_1 = module_0.check_required_by(tuple_0, str_2)
    except BaseException:
        pass

def test_case_28():
    try:
        str_0 = 'AlmaLinux'
        bytes_0 = b'\xa1E@\'\x17\xefJ\xc1"br'
        list_0 = [str_0, str_0, bytes_0]
        int_0 = 1697
        list_1 = [list_0, list_0, int_0]
        tuple_0 = None
        var_0 = module_0.check_required_if(list_1, tuple_0)
    except BaseException:
        pass

def test_case_29():
    try:
        str_0 = '(=F'
        var_0 = module_0.check_type_dict(str_0)
        var_1 = module_0.safe_eval(str_0, str_0)
        list_0 = []
        str_1 = 'path'
        bool_0 = True
        set_0 = {bool_0, var_1, bool_0, str_1}
        var_2 = module_0.check_required_if(set_0, list_0)
    except BaseException:
        pass

def test_case_30():
    try:
        dict_0 = {}
        str_0 = 'u]%o4\\,[@li@'
        var_0 = module_0.check_required_one_of(dict_0, str_0)
        bool_0 = False
        float_0 = 512.0
        var_1 = module_0.check_required_arguments(bool_0, float_0)
    except BaseException:
        pass

def test_case_31():
    try:
        str_0 = 'pMh:]*8EKu<;\x0c)'
        str_1 = 'A)$- n$:&v#d'
        list_0 = [str_1]
        var_0 = module_0.check_required_together(list_0, str_0)
    except BaseException:
        pass

def test_case_32():
    try:
        str_0 = 'test'
        str_1 = '\x0c#h1OC6 dE`\x0c'
        str_2 = 'test_3'
        str_3 = {str_1, str_2}
        var_0 = dict(test_1=str_3)
        str_4 = 'Test'
        var_1 = dict(test_1=str_4, test_3=str_0)
        var_2 = module_0.check_required_by(var_0, var_1)
    except BaseException:
        pass

def test_case_33():
    try:
        int_0 = -1092
        var_0 = module_0.check_missing_parameters(int_0)
        str_0 = 'GI|B@vzTzVWp61N?J'
        var_1 = module_0.safe_eval(str_0, str_0)
        set_0 = {var_1}
        dict_0 = {}
        bool_0 = False
        bytes_0 = b'\xe7\x93'
        str_1 = '>\nGBFb"[s{q(\x0b;}~0'
        tuple_0 = (bool_0, set_0, bytes_0, str_1)
        var_2 = module_0.check_required_one_of(set_0, dict_0, tuple_0)
    except BaseException:
        pass

def test_case_34():
    try:
        str_0 = "Q}'WT4)G={t#_U_RG"
        var_0 = module_0.check_type_dict(str_0)
        float_0 = -315.09
        var_1 = module_0.safe_eval(float_0)
        var_2 = module_0.check_type_int(str_0)
    except BaseException:
        pass

def test_case_35():
    try:
        str_0 = 'p.^mk4R?pQk\x0c_'
        bytes_0 = b'\x13w\x1c_-\xbb\x0e8\xd4\x85\xc8/3\x86'
        var_0 = module_0.check_required_one_of(bytes_0, bytes_0)
        var_1 = module_0.check_type_bytes(str_0)
    except BaseException:
        pass

def test_case_36():
    try:
        str_0 = 'test_arg1'
        str_1 = 'test_arg2'
        str_2 = 'test_arg3'
        str_3 = 'test_arg4'
        str_4 = (str_2, str_3)
        str_5 = [str_0, str_1, str_4]
        str_6 = [str_5]
        str_7 = {str_0: str_1}
        var_0 = module_0.check_required_if(str_6, str_7)
    except BaseException:
        pass

def test_case_37():
    try:
        str_0 = "{m_'^^Q{:NQeW84(4#]J"
        var_0 = module_0.check_type_dict(str_0)
    except BaseException:
        pass

def test_case_38():
    try:
        str_0 = '{"key1":"value1", "key2":"value2"}'
        var_0 = module_0.check_type_dict(str_0)
        dict_0 = {}
        var_1 = module_0.check_type_bytes(dict_0)
    except BaseException:
        pass

def test_case_39():
    try:
        str_0 = 'Test check_mutually_exclusive function'
        int_0 = -24
        str_1 = 'q'
        str_2 = [str_0]
        int_1 = {str_1: int_0}
        var_0 = module_0.check_mutually_exclusive(str_2, int_1)
        str_3 = 'p'
        str_4 = 'q'
        str_5 = [str_3, str_4]
        str_6 = [str_5]
        int_2 = {str_3: int_0, str_4: int_0}
        var_1 = module_0.check_mutually_exclusive(str_6, int_2)
    except BaseException:
        pass

def test_case_40():
    try:
        str_0 = '<<'
        str_1 = 'key2'
        str_2 = 'value'
        str_3 = [str_2, str_2]
        str_4 = 'value2'
        str_5 = [str_4, str_4]
        str_6 = {str_0: str_3, str_1: str_5}
        str_7 = {str_0: str_2, str_1: str_4}
        str_8 = [str_2]
        var_0 = module_0.check_required_by(str_6, str_7, str_8)
    except BaseException:
        pass

def test_case_41():
    try:
        str_0 = 'arg1'
        str_1 = 'arg2'
        str_2 = 'arg3'
        str_3 = 'required'
        bool_0 = True
        bool_1 = {str_3: bool_0}
        bool_2 = False
        bool_3 = {str_3: bool_2}
        bool_4 = {str_0: bool_1, str_1: bool_3, str_2: bool_1}
        str_4 = 'val1'
        str_5 = {str_1: str_4}
        var_0 = module_0.check_required_arguments(bool_4, str_5)
    except BaseException:
        pass

def test_case_42():
    try:
        str_0 = 'param1'
        var_0 = {}
        var_1 = module_0.check_missing_parameters(var_0, str_0)
    except BaseException:
        pass

def test_case_43():
    try:
        str_0 = 'param1'
        str_1 = 'required'
        bool_0 = True
        bool_1 = {str_1: bool_0}
        bool_2 = {str_0: bool_1}
        var_0 = module_0.check_required_arguments(bool_2, str_0)
        bool_3 = {str_1: bool_0}
        bool_4 = {str_0: bool_3}
        var_1 = {}
        var_2 = module_0.check_required_arguments(bool_4, var_1)
    except BaseException:
        pass

def test_case_44():
    try:
        str_0 = 'U9QS1N`~\nZ'
        str_1 = 'path'
        bool_0 = True
        var_0 = [str_0, str_1, str_1, bool_0]
        str_2 = 'someint'
        int_0 = 99
        str_3 = 'bool_param'
        str_4 = 'string_param'
        str_5 = (str_3, str_4)
        var_1 = [str_2, int_0, str_5]
        var_2 = [var_0, var_1]
        var_3 = {str_2: int_0, str_3: bool_0}
        var_4 = module_0.check_required_if(var_2, var_3)
    except BaseException:
        pass

def test_case_45():
    try:
        str_0 = 'path'
        bool_0 = True
        var_0 = [str_0, str_0, str_0, bool_0]
        str_1 = 'oment'
        int_0 = 99
        str_2 = 'string_param'
        str_3 = (str_2, str_2)
        var_1 = [str_1, int_0, str_3]
        var_2 = [var_0, var_1]
        var_3 = {str_1: int_0, str_0: bool_0}
        var_4 = module_0.check_required_if(var_2, var_3)
    except BaseException:
        pass

def test_case_46():
    try:
        str_0 = '/tmp/test.txt'
        str_1 = [str_0]
        str_2 = 'present'
        var_0 = dict(paths=str_1, state=str_2)
        str_3 = 'paths'
        str_4 = [str_0]
        str_5 = 'state'
        str_6 = 'owner'
        str_7 = [str_5, str_6]
        bool_0 = True
        var_1 = [str_3, str_4, str_7, bool_0]
        var_2 = [var_1]
        var_3 = module_0.check_required_if(var_2, var_0)
        str_8 = [str_0]
        bool_1 = False
        var_4 = [str_3, str_8, str_3, bool_1]
        var_5 = [var_4]
        var_6 = module_0.check_required_if(var_5, var_0)
    except BaseException:
        pass

def test_case_47():
    try:
        str_0 = 'arg1'
        str_1 = '123'
        str_2 = {str_0: str_1}
        str_3 = 'arg2'
        str_4 = 'arg3'
        str_5 = [str_0, str_3, str_4]
        var_0 = module_0.check_missing_parameters(str_2, str_5)
    except BaseException:
        pass

def test_case_48():
    try:
        str_0 = 'test'
        var_0 = module_0.safe_eval(str_0)
        str_1 = 'None'
        var_1 = module_0.safe_eval(str_1)
        str_2 = 'test.method()'
        var_2 = module_0.safe_eval(str_2)
        int_0 = 0
        bool_0 = True
        var_3 = safe_eval(str_2, include_exceptions=bool_0)[int_0]
    except BaseException:
        pass