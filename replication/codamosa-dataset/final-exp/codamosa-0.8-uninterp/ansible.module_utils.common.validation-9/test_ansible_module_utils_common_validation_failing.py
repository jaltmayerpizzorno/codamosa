# Automatically generated by Pynguin.
import ansible.module_utils.common.validation as module_0

def test_case_0():
    try:
        bytes_0 = b']D\xa7\xe7\\O'
        list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
        float_0 = 2432.0
        var_0 = module_0.check_required_one_of(bytes_0, list_0, float_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'D#9VE;'
        list_0 = [str_0, str_0]
        var_0 = module_0.check_required_by(str_0, list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'\x98g\xebl\xac\xdd\xfe\x1f\xa6'
        bytes_1 = b'\xee\x91\x19\x1ds\xc8~\x9f\xc9S\x7f\x89XN|\x88'
        var_0 = module_0.check_required_arguments(bytes_0, bytes_1)
    except BaseException:
        pass

def test_case_3():
    try:
        var_0 = None
        str_0 = 'foo'
        str_1 = 'bar'
        str_2 = [str_0, str_1]
        var_1 = module_0.check_required_arguments(var_0, str_1, str_2)
        str_3 = 'test_param_required'
        str_4 = 'required'
        bool_0 = True
        bool_1 = {str_4: bool_0}
        bool_2 = {str_3: bool_1}
        var_2 = module_0.check_required_arguments(bool_2, str_2, str_2)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'nr\x0b1hEP]Zu&n~w(}ZYnh'
        str_1 = 'SPQ_>eDCp\nz9JSi'
        dict_0 = {str_0: str_0, str_1: str_1}
        var_0 = module_0.check_required_if(str_1, dict_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bool_0 = False
        float_0 = None
        var_0 = module_0.check_type_str(bool_0, bool_0, float_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'p{_O'
        var_0 = module_0.check_type_path(str_0)
        tuple_0 = ()
        var_1 = module_0.check_missing_parameters(tuple_0)
        var_2 = module_0.check_type_bits(tuple_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'QDbD.\n\x0b&=GXL8DC/]DXG'
        set_0 = {str_0, str_0, str_0, str_0}
        float_0 = -134.25178
        var_0 = module_0.check_type_list(float_0)
        var_1 = module_0.check_type_list(set_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = '[d'
        var_0 = module_0.check_type_dict(str_0)
    except BaseException:
        pass

def test_case_9():
    try:
        int_0 = 50
        var_0 = module_0.check_type_dict(int_0)
    except BaseException:
        pass

def test_case_10():
    try:
        float_0 = -3400.82
        var_0 = module_0.check_type_bool(float_0)
    except BaseException:
        pass

def test_case_11():
    try:
        int_0 = None
        bool_0 = False
        set_0 = {int_0, bool_0}
        var_0 = module_0.check_type_bool(set_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = 'g'
        var_0 = module_0.check_type_int(str_0)
    except BaseException:
        pass

def test_case_13():
    try:
        bytes_0 = None
        var_0 = module_0.check_type_float(bytes_0)
    except BaseException:
        pass

def test_case_14():
    try:
        bytes_0 = b'\t{z\xea\x1fG*y\x01d'
        var_0 = module_0.check_type_bytes(bytes_0)
    except BaseException:
        pass

def test_case_15():
    try:
        int_0 = -727
        var_0 = module_0.check_type_bits(int_0)
    except BaseException:
        pass

def test_case_16():
    try:
        bytes_0 = b'\xfd\x95\xd7\t}\x8eu\x92dNt\x87'
        var_0 = module_0.check_type_path(bytes_0)
        int_0 = None
        var_1 = module_0.check_type_jsonarg(int_0)
    except BaseException:
        pass

def test_case_17():
    try:
        set_0 = set()
        tuple_0 = (set_0,)
        var_0 = module_0.check_mutually_exclusive(tuple_0, set_0)
        bool_0 = True
        var_1 = module_0.check_type_list(bool_0)
        str_0 = 'Irl=u|5,:w\tRfP27\x0c\n5'
        var_2 = module_0.check_type_dict(str_0)
    except BaseException:
        pass

def test_case_18():
    try:
        str_0 = ''
        var_0 = module_0.check_type_path(str_0)
        str_1 = 'b'
        var_1 = module_0.check_type_bool(str_1)
    except BaseException:
        pass

def test_case_19():
    try:
        bool_0 = True
        var_0 = module_0.check_type_float(bool_0)
        set_0 = {bool_0, bool_0}
        str_0 = ')}H\\^#Iew'
        list_0 = [set_0, str_0]
        var_1 = module_0.check_type_int(list_0)
    except BaseException:
        pass

def test_case_20():
    try:
        str_0 = 'M'
        var_0 = module_0.check_type_float(str_0)
    except BaseException:
        pass

def test_case_21():
    try:
        str_0 = 'x{RC'
        bool_0 = False
        var_0 = module_0.check_required_together(str_0, str_0, bool_0)
        complex_0 = None
        var_1 = module_0.check_type_bits(complex_0)
    except BaseException:
        pass

def test_case_22():
    try:
        float_0 = 244.0
        set_0 = {float_0, float_0}
        bytes_0 = b'\xd2N\xc0\xad\x1fi\x11'
        var_0 = module_0.safe_eval(set_0, bytes_0)
        set_1 = {float_0, float_0, float_0, float_0}
        str_0 = '\x0b*\t@bY'
        var_1 = module_0.check_missing_parameters(set_1, str_0)
    except BaseException:
        pass

def test_case_23():
    try:
        str_0 = 'nr\x0b1hEP]Zu&n~w(}ZYnh'
        str_1 = "Zv1'5'ZfN']o*HMaIDa~"
        var_0 = module_0.check_type_list(str_1)
        var_1 = module_0.check_type_float(str_0)
    except BaseException:
        pass

def test_case_24():
    try:
        str_0 = 'Completely failed to parse inventory source %s'
        float_0 = 2777.979
        bool_0 = True
        tuple_0 = (str_0, float_0, bool_0)
        int_0 = 4379
        var_0 = module_0.check_required_one_of(tuple_0, str_0, int_0)
    except BaseException:
        pass

def test_case_25():
    try:
        str_0 = '/v3/'
        set_0 = set()
        dict_0 = {str_0: str_0, str_0: str_0, str_0: set_0}
        var_0 = module_0.check_required_one_of(str_0, dict_0)
    except BaseException:
        pass

def test_case_26():
    try:
        str_0 = 'value1'
        str_1 = 'value3'
        var_0 = dict(param1=str_0, param3=str_1)
        str_2 = 'param1'
        str_3 = 'param2'
        str_4 = 'param3'
        str_5 = [str_2, str_3, str_4]
        var_1 = module_0.check_missing_parameters(var_0, str_5)
    except BaseException:
        pass

def test_case_27():
    try:
        var_0 = dict()
        var_1 = dict()
        bool_0 = None
        var_2 = module_0.check_missing_parameters(bool_0, var_0)
        var_3 = dict()
        var_4 = module_0.check_required_by(var_1, var_0)
        str_0 = 'param1'
        var_5 = dict()
        var_6 = dict(requirement1=str_0, requirement2=var_1)
        str_1 = [str_0]
        str_2 = [str_0]
        var_7 = dict(requirement1=str_1, requirement2=str_2)
        var_8 = module_0.check_required_by(var_6, var_7)
    except BaseException:
        pass

def test_case_28():
    try:
        float_0 = -1767.5802
        int_0 = -925
        tuple_0 = (int_0, float_0)
        tuple_1 = (tuple_0,)
        set_0 = {int_0, float_0, tuple_1}
        var_0 = module_0.check_required_one_of(tuple_1, set_0)
        set_1 = {float_0}
        var_1 = module_0.check_type_dict(set_1)
    except BaseException:
        pass

def test_case_29():
    try:
        int_0 = 860
        tuple_0 = None
        bool_0 = True
        var_0 = module_0.check_required_one_of(tuple_0, bool_0)
        var_1 = module_0.check_missing_parameters(tuple_0)
        bool_1 = True
        var_2 = module_0.check_required_by(int_0, bool_1)
    except BaseException:
        pass

def test_case_30():
    try:
        bool_0 = False
        var_0 = module_0.check_type_list(bool_0)
        str_0 = '`C#\n8NjjW(Wj}tI"'
        dict_0 = {str_0: str_0, bool_0: bool_0}
        list_0 = [str_0, var_0]
        var_1 = module_0.check_type_list(list_0)
        list_1 = [dict_0, var_0, var_0]
        var_2 = module_0.check_type_list(list_1)
    except BaseException:
        pass

def test_case_31():
    try:
        str_0 = '{wHk-X\r!j\tP95c'
        var_0 = module_0.check_type_dict(str_0)
    except BaseException:
        pass

def test_case_32():
    try:
        str_0 = 'key'
        str_1 = 'state'
        str_2 = 'val'
        str_3 = '/path/to/file'
        str_4 = 'present'
        str_5 = {str_0: str_2, str_1: str_3, str_1: str_4}
        bool_0 = False
        var_0 = [str_1, str_4, str_0, bool_0]
        var_1 = [var_0]
        var_2 = module_0.check_required_if(var_1, str_5)
    except BaseException:
        pass

def test_case_33():
    try:
        bytes_0 = b'J\xbfT\xac\x18+~"\x8a\xc6\x0c\\\xb9\xbe'
        str_0 = '7G@ 2Lx]z'
        float_0 = 2374.8
        tuple_0 = (str_0, str_0, bytes_0, float_0)
        dict_0 = {str_0: tuple_0, float_0: bytes_0}
        list_0 = [tuple_0, dict_0]
        var_0 = module_0.check_required_by(dict_0, list_0)
        var_1 = module_0.check_missing_parameters(bytes_0, tuple_0)
    except BaseException:
        pass

def test_case_34():
    try:
        str_0 = ' #P*\x0b.r9pAoa/g9K'
        var_0 = dict(requirement1=str_0, requirement2=str_0)
        var_1 = module_0.check_required_by(var_0, var_0)
    except BaseException:
        pass

def test_case_35():
    try:
        str_0 = 'Irl=u|5,:w\tRfP27\x0c\n5'
        var_0 = module_0.check_type_dict(str_0)
    except BaseException:
        pass

def test_case_36():
    try:
        str_0 = 'test-key'
        str_1 = 'test-key2'
        str_2 = [str_0, str_1]
        str_3 = 'test-key3'
        str_4 = 'test-key4'
        str_5 = [str_3, str_4]
        str_6 = [str_2, str_5]
        str_7 = 'test'
        str_8 = 'test2'
        str_9 = {str_0: str_7, str_1: str_8}
        str_10 = 'tst-key'
        str_11 = 'tst-key2'
        str_12 = [str_10, str_11]
        var_0 = module_0.check_mutually_exclusive(str_6, str_9, str_12)
    except BaseException:
        pass

def test_case_37():
    try:
        str_0 = 'foo'
        str_1 = 'ar'
        str_2 = [str_0, str_1]
        var_0 = module_0.check_mutually_exclusive(str_2, str_1)
        str_3 = [str_0, str_1]
        str_4 = [str_3]
        var_1 = module_0.check_mutually_exclusive(str_4, str_2)
    except BaseException:
        pass

def test_case_38():
    try:
        var_0 = dict()
        str_0 = 'param1'
        var_1 = dict(requirement1=var_0, requirement2=str_0)
        var_2 = dict(requirement1=str_0, requirement2=var_1)
        var_3 = module_0.check_required_by(var_1, var_2)
    except BaseException:
        pass

def test_case_39():
    try:
        str_0 = "{'1':2,'2':3}"
        str_1 = '1'
        int_0 = 2
        var_0 = module_0.check_type_dict(str_0)
        str_2 = '1=2,2=3'
        var_1 = module_0.check_type_dict(str_2)
        int_1 = {str_1: int_0}
        var_2 = module_0.check_type_dict(int_1)
        str_3 = "'1':2"
        var_3 = module_0.check_type_dict(str_3)
    except BaseException:
        pass

def test_case_40():
    try:
        str_0 = 'a'
        str_1 = 'b'
        str_2 = (str_0, str_1)
        str_3 = [str_2, str_1]
        var_0 = module_0.check_required_together(str_3, str_1)
    except BaseException:
        pass

def test_case_41():
    try:
        str_0 = "{'1':2,'2':3}"
        str_1 = '1'
        float_0 = 2098.24047
        var_0 = module_0.check_type_float(float_0)
        var_1 = module_0.check_missing_parameters(str_0)
        int_0 = 3
        str_2 = 'w;5'
        var_2 = module_0.check_mutually_exclusive(str_2, str_2)
        var_3 = module_0.check_type_dict(str_0)
        str_3 = '1=,'
        var_4 = module_0.check_type_dict(str_3)
        int_1 = {str_1: int_0}
        var_5 = module_0.check_type_dict(int_1)
        int_2 = -1224
        var_6 = module_0.check_required_one_of(int_2, int_0)
    except BaseException:
        pass

def test_case_42():
    try:
        str_0 = '1'
        str_1 = '2'
        dict_0 = {}
        bool_0 = False
        var_0 = module_0.check_required_by(dict_0, bool_0)
        float_0 = 2098.24047
        var_1 = module_0.check_type_float(float_0)
        str_2 = 'ovTcDCI\tj*e)\x0b"F.LI'
        dict_1 = {str_1: var_1, str_2: dict_0, str_2: var_1, str_0: dict_0}
        str_3 = '=\\.ep'
        var_2 = module_0.check_type_str(dict_1, str_3)
        str_4 = "Virrc[sB@'$-W)RQ"
        var_3 = module_0.check_mutually_exclusive(str_4, str_4)
        var_4 = module_0.check_type_dict(str_3)
        list_0 = []
        var_5 = module_0.check_type_bytes(list_0)
    except BaseException:
        pass