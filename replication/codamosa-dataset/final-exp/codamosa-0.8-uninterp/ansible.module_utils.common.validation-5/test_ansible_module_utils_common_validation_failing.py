# Automatically generated by Pynguin.
import ansible.module_utils.common.validation as module_0

def test_case_0():
    try:
        bytes_0 = b'~'
        var_0 = module_0.check_type_bits(bytes_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '{"a":I1, "b":|2}'
        var_0 = module_0.check_type_dict(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '-[/N:'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
        var_0 = module_0.check_required_one_of(str_0, dict_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = b'\x05\xcc\x1b\xf4B\xfc\xc9\x02^]\x07\x17(\xef'
        bool_0 = True
        tuple_0 = (bytes_0, bool_0)
        var_0 = module_0.check_required_together(tuple_0, tuple_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '\t1als%6y;Jr~=j!M|eqm'
        int_0 = -952
        dict_0 = {str_0: str_0, str_0: str_0, str_0: int_0, str_0: str_0}
        tuple_0 = ()
        var_0 = module_0.check_required_by(dict_0, tuple_0)
        str_1 = None
        var_1 = module_0.check_type_list(str_1)
    except BaseException:
        pass

def test_case_5():
    try:
        bool_0 = True
        var_0 = module_0.check_required_by(bool_0, bool_0)
    except BaseException:
        pass

def test_case_6():
    try:
        bool_0 = True
        var_0 = dict(required=bool_0)
        bool_1 = False
        var_1 = dict(required=bool_1)
        var_2 = dict(test_parameter=var_0, test_parameter_false=var_1)
        var_3 = dict()
        var_4 = module_0.check_required_arguments(var_2, var_3)
    except BaseException:
        pass

def test_case_7():
    try:
        bytes_0 = b'"$0\x80\x1a\xf1\xa6T\xa5\x8c\x08\xf0\x84\x1c"\\;`*'
        float_0 = -207.0
        int_0 = None
        str_0 = ';('
        tuple_0 = (float_0, str_0, int_0, str_0)
        tuple_1 = (bytes_0, bytes_0, tuple_0)
        dict_0 = {tuple_1: str_0, str_0: bytes_0}
        var_0 = module_0.check_required_if(dict_0, tuple_0)
    except BaseException:
        pass

def test_case_8():
    try:
        bytes_0 = b'z\xa1\ty\xef\x88\xa6\xd3E\x92\x10\xc9\xb1'
        str_0 = 'nMqw9fX+h{\rDh7qQ9*s'
        var_0 = module_0.check_required_if(bytes_0, str_0, str_0)
    except BaseException:
        pass

def test_case_9():
    try:
        set_0 = set()
        str_0 = ',z_X-TiG5@-f^i3wnpDi'
        var_0 = module_0.check_missing_parameters(set_0, str_0)
    except BaseException:
        pass

def test_case_10():
    try:
        bytes_0 = b'\x05\xcc\x1b\xf4B\xfc\xc9\x02^]\x07\x17(\xef'
        float_0 = 1356.8207
        var_0 = module_0.check_type_path(float_0)
        bool_0 = True
        tuple_0 = (bytes_0, bool_0)
        var_1 = module_0.check_required_together(tuple_0, tuple_0)
    except BaseException:
        pass

def test_case_11():
    try:
        int_0 = -3139
        var_0 = module_0.check_type_dict(int_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = 'x-7co2hj\tk'
        var_0 = module_0.check_type_bool(str_0)
    except BaseException:
        pass

def test_case_13():
    try:
        bytes_0 = b'\xd9]\xd4'
        var_0 = module_0.check_type_raw(bytes_0)
        str_0 = 'S'
        str_1 = {str_0: str_0}
        str_2 = "{'a':'b','c':'d'}"
        var_1 = module_0.check_type_dict(str_2)
        set_0 = None
        list_0 = [var_0, set_0, bytes_0]
        var_2 = module_0.check_mutually_exclusive(str_1, list_0)
        set_1 = set()
        var_3 = module_0.check_type_bool(set_1)
    except BaseException:
        pass

def test_case_14():
    try:
        bytes_0 = b'\x14Rdb2~\x84\xf4x\x08\x08\xdc\xcb\x19=P\xe3\x14\x96'
        var_0 = module_0.check_type_int(bytes_0)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = '2.SgQy6cbJ[;5tly0%Zg'
        var_0 = module_0.check_type_int(str_0)
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = '%'
        var_0 = module_0.safe_eval(str_0)
        str_1 = None
        list_0 = [str_1, str_1]
        str_2 = 'c{eS~}f}\\p0Lt_\n;>Vo8'
        int_0 = 1000
        var_1 = module_0.check_type_int(int_0)
        var_2 = module_0.check_required_by(list_0, str_1, str_2)
    except BaseException:
        pass

def test_case_17():
    try:
        tuple_0 = None
        var_0 = module_0.check_type_float(tuple_0)
    except BaseException:
        pass

def test_case_18():
    try:
        bytes_0 = b'Ia2\x1e\xa3\x81\xc9\xf4\xd2\x8a\x11Q\xc1\xeb\x95\x0b\x17\xda$\xb0'
        var_0 = module_0.check_type_float(bytes_0)
    except BaseException:
        pass

def test_case_19():
    try:
        float_0 = -840.98785
        var_0 = module_0.check_type_bytes(float_0)
    except BaseException:
        pass

def test_case_20():
    try:
        int_0 = 1248
        var_0 = module_0.check_type_jsonarg(int_0)
    except BaseException:
        pass

def test_case_21():
    try:
        bytes_0 = b'"$0\x80\x1a\xf1\xa6T\xa5\x8c\x08\xf0\x84\x1c"\\;`*'
        float_0 = -207.0
        str_0 = 'IAaG.Y\x0c5{aK3`X'
        int_0 = None
        tuple_0 = (float_0, str_0, int_0, str_0)
        tuple_1 = (bytes_0, bytes_0, tuple_0)
        dict_0 = {tuple_1: str_0, str_0: bytes_0}
        var_0 = module_0.check_required_if(dict_0, tuple_1)
    except BaseException:
        pass

def test_case_22():
    try:
        int_0 = 41
        var_0 = module_0.check_type_bool(int_0)
    except BaseException:
        pass

def test_case_23():
    try:
        bool_0 = False
        var_0 = module_0.check_missing_parameters(bool_0)
        int_0 = -518
        dict_0 = {}
        set_0 = set()
        tuple_0 = (int_0, dict_0, set_0)
        tuple_1 = (tuple_0,)
        list_0 = [var_0, tuple_1]
        bool_1 = None
        var_1 = module_0.check_required_one_of(tuple_1, list_0, bool_1)
    except BaseException:
        pass

def test_case_24():
    try:
        str_0 = 'foo'
        var_0 = module_0.safe_eval(str_0)
        str_1 = '[1,2,3]'
        var_1 = module_0.safe_eval(str_1)
        list_0 = []
        var_2 = module_0.check_type_list(list_0)
        str_2 = "{'aV: !1, 'b': 2}"
        var_3 = module_0.safe_eval(str_2)
        str_3 = 'bar.update(baz)'
        var_4 = module_0.safe_eval(str_3)
        float_0 = 1730.61869
        var_5 = module_0.check_type_dict(float_0)
    except BaseException:
        pass

def test_case_25():
    try:
        str_0 = '{"":9I1, "bi:|2}'
        set_0 = {str_0, str_0, str_0, str_0}
        var_0 = module_0.check_required_together(set_0, set_0)
        var_1 = module_0.check_type_dict(str_0)
    except BaseException:
        pass

def test_case_26():
    try:
        int_0 = 291
        var_0 = module_0.safe_eval(int_0)
        bool_0 = False
        int_1 = 3168
        var_1 = module_0.check_type_str(int_1)
        str_0 = '%s (%s) is not a text_type'
        var_2 = module_0.count_terms(bool_0, str_0)
        set_0 = None
        var_3 = module_0.check_required_together(set_0, set_0)
        float_0 = 0.1
        var_4 = module_0.check_required_if(float_0, str_0)
    except BaseException:
        pass

def test_case_27():
    try:
        str_0 = '{"":9I1, "bi:|2}'
        float_0 = None
        tuple_0 = ()
        dict_0 = {float_0: tuple_0}
        var_0 = module_0.check_required_by(float_0, dict_0)
        var_1 = module_0.check_type_dict(str_0)
    except BaseException:
        pass

def test_case_28():
    try:
        bytes_0 = b'"$0\x80\x1a\xf1\xa6T\xa5\x8c\x08\xf0\x84\x1c"\\;`*'
        float_0 = -207.0
        str_0 = 'IAaG.Y\x0c5{aK3`X'
        int_0 = None
        tuple_0 = (float_0, str_0, int_0, str_0)
        dict_0 = {tuple_0: str_0, str_0: bytes_0}
        bool_0 = True
        list_0 = []
        var_0 = module_0.check_required_if(dict_0, bool_0, list_0)
    except BaseException:
        pass

def test_case_29():
    try:
        bool_0 = False
        var_0 = module_0.check_type_list(bool_0)
        str_0 = "i'\x0b&~b\x0cO^9}y7\\"
        var_1 = module_0.check_type_int(str_0)
    except BaseException:
        pass

def test_case_30():
    try:
        bytes_0 = b'"$0\x80\x1a\xf1\xa6T\xa5\x8c\x08\xf0\x84\x1c"\\;`*'
        float_0 = -207.0
        str_0 = 'IAaG.Y\x0c5{aK3`X'
        set_0 = None
        var_0 = module_0.check_required_one_of(set_0, str_0)
        int_0 = None
        str_1 = ';('
        tuple_0 = (float_0, str_0, int_0, str_1)
        var_1 = module_0.check_type_list(float_0)
        tuple_1 = (bytes_0, bytes_0, tuple_0)
        dict_0 = {tuple_1: str_0, str_1: bytes_0}
        bool_0 = True
        var_2 = module_0.check_missing_parameters(bool_0)
        var_3 = module_0.check_required_if(dict_0, tuple_0)
    except BaseException:
        pass

def test_case_31():
    try:
        dict_0 = None
        set_0 = None
        str_0 = ';#~8p7@.Nsw@'
        var_0 = module_0.check_required_arguments(set_0, str_0)
        var_1 = module_0.check_mutually_exclusive(set_0, dict_0)
        float_0 = 2829.8
        var_2 = module_0.check_required_if(set_0, set_0, float_0)
        var_3 = module_0.check_type_bytes(str_0)
    except BaseException:
        pass

def test_case_32():
    try:
        bool_0 = True
        var_0 = module_0.check_type_str(bool_0)
        tuple_0 = None
        str_0 = "-g1Q)'Lq\n~@["
        dict_0 = {tuple_0: str_0}
        bytes_0 = b'\xb7\xb0w\xc1X\x1b\xe1\x88K\xb3\xbb\xfb\xaa\xa9'
        var_1 = module_0.check_missing_parameters(dict_0, bytes_0)
    except BaseException:
        pass

def test_case_33():
    try:
        dict_0 = None
        float_0 = 1426.0
        var_0 = module_0.check_required_by(dict_0, float_0)
        bytes_0 = b'>\xbd6\x94@\x1exV\x84>\xe9'
        tuple_0 = None
        var_1 = module_0.check_type_str(bytes_0, tuple_0)
    except BaseException:
        pass

def test_case_34():
    try:
        complex_0 = None
        str_0 = 'egIIY\x0cQ[70'
        bool_0 = True
        var_0 = module_0.check_required_one_of(complex_0, str_0, bool_0)
        str_1 = '{"N:9I5,%"bi:|2}'
        var_1 = module_0.check_type_dict(str_1)
    except BaseException:
        pass

def test_case_35():
    try:
        str_0 = 'a'
        str_1 = {str_0: str_0}
        var_0 = module_0.check_type_dict(str_1)
        str_2 = '|=b,c=d'
        var_1 = module_0.check_type_dict(str_2)
        bool_0 = None
        var_2 = module_0.check_type_dict(bool_0)
    except BaseException:
        pass

def test_case_36():
    try:
        str_0 = '{"a":I1, "b":|2}'
        tuple_0 = None
        var_0 = module_0.check_required_arguments(tuple_0, str_0)
        float_0 = 419.62299
        var_1 = module_0.check_type_float(float_0)
        var_2 = module_0.check_type_dict(str_0)
    except BaseException:
        pass

def test_case_37():
    try:
        str_0 = ''
        var_0 = module_0.check_type_dict(str_0)
    except BaseException:
        pass

def test_case_38():
    try:
        bytes_0 = b'\x14Rdb2~\x84\xf4x\x08\x08\xdc\xcb\x19=P\xe3\x14\x96'
        set_0 = set()
        dict_0 = {}
        tuple_0 = None
        var_0 = module_0.check_required_one_of(set_0, dict_0, tuple_0)
        var_1 = module_0.check_type_int(bytes_0)
    except BaseException:
        pass

def test_case_39():
    try:
        str_0 = "=W@(RC'l"
        var_0 = module_0.check_type_dict(str_0)
        var_1 = module_0.safe_eval(str_0)
        tuple_0 = ()
        float_0 = None
        var_2 = module_0.check_required_together(tuple_0, float_0)
        var_3 = module_0.check_required_one_of(str_0, str_0)
        var_4 = module_0.check_type_int(str_0)
    except BaseException:
        pass

def test_case_40():
    try:
        str_0 = "=W@(RC'l"
        var_0 = module_0.check_type_dict(str_0)
        str_1 = 'C\\R\tU'
        var_1 = module_0.safe_eval(str_1)
        tuple_0 = ()
        float_0 = None
        dict_0 = {str_1: str_0, var_1: tuple_0}
        var_2 = module_0.safe_eval(float_0, str_0, dict_0)
        var_3 = module_0.check_required_together(tuple_0, float_0)
        var_4 = module_0.check_type_int(str_0)
    except BaseException:
        pass

def test_case_41():
    try:
        str_0 = None
        str_1 = 'foo'
        str_2 = [str_1, str_1]
        str_3 = {str_1: str_2}
        var_0 = {str_1: str_1, str_0: str_2}
        var_1 = module_0.check_required_by(str_3, var_0)
        str_4 = 'foo'
        str_5 = 'bar'
        str_6 = 'baz'
        str_7 = [str_5, str_6]
        str_8 = {str_4: str_7}
        var_2 = None
        var_3 = {str_4: str_4, str_6: var_2}
        var_4 = module_0.check_required_by(str_8, var_3)
    except BaseException:
        pass

def test_case_42():
    try:
        str_0 = "=W@(RC'l"
        var_0 = module_0.check_type_dict(str_0)
        str_1 = 'C\\R\tU'
        var_1 = module_0.safe_eval(str_1)
        str_2 = 'M9\t2TMx'
        str_3 = ')<%F.:g7'
        str_4 = 'bQN\n'
        var_2 = module_0.check_required_one_of(str_2, str_3, str_4)
    except BaseException:
        pass

def test_case_43():
    try:
        str_0 = 'a'
        str_1 = ''
        int_0 = 1
        int_1 = {str_0: int_0, str_1: int_0}
        str_2 = [str_0, str_1]
        str_3 = [str_2]
        var_0 = module_0.check_mutually_exclusive(str_3, int_1)
    except BaseException:
        pass

def test_case_44():
    try:
        str_0 = 'present'
        str_1 = 'overridden_value_1'
        str_2 = 'default_value_1'
        var_0 = dict(state=str_0, name=str_1, want_value=str_1, default_value=str_2)
        str_3 = 'default_value'
        str_4 = [str_0, str_3]
        str_5 = [str_4]
        var_1 = module_0.check_required_together(str_5, var_0)
    except BaseException:
        pass

def test_case_45():
    try:
        str_0 = 'something_extra'
        str_1 = 'something_required'
        str_2 = {str_0: str_1}
        str_3 = 'foo'
        str_4 = {str_0: str_3}
        var_0 = module_0.check_required_by(str_2, str_4)
    except BaseException:
        pass

def test_case_46():
    try:
        str_0 = 'staote'
        str_1 = 'present'
        str_2 = (str_1,)
        bool_0 = True
        var_0 = [str_0, str_1, str_2, bool_0]
        int_0 = 99
        bool_1 = None
        str_3 = 'string_paraP'
        var_1 = [var_0, bool_1]
        var_2 = {str_0: str_1, str_3: int_0}
        var_3 = module_0.check_required_if(var_1, var_2)
    except BaseException:
        pass

def test_case_47():
    try:
        str_0 = 'state'
        str_1 = 'present'
        str_2 = 'port'
        bool_0 = True
        var_0 = [str_0, str_1, str_2, bool_0]
        var_1 = [var_0]
        str_3 = '80'
        str_4 = {str_0: str_1, str_2: str_3}
        var_2 = module_0.check_required_if(var_1, str_4)
    except BaseException:
        pass

def test_case_48():
    try:
        str_0 = 'state'
        str_1 = (str_0,)
        bool_0 = True
        var_0 = [str_0, str_0, str_1, bool_0]
        int_0 = 99
        str_2 = '07"XS{jVIL'
        str_3 = 'string_param'
        str_4 = (str_2, str_3)
        var_1 = [str_2, int_0, str_4]
        var_2 = [var_0, var_1]
        var_3 = {str_0: str_3, str_3: int_0}
        var_4 = module_0.check_required_if(var_2, var_3)
        int_1 = {str_0: int_0}
        var_5 = module_0.check_required_if(int_0, int_1)
    except BaseException:
        pass

def test_case_49():
    try:
        str_0 = 'state'
        str_1 = 'present'
        str_2 = (str_1,)
        bool_0 = True
        var_0 = [str_0, str_1, str_2, bool_0]
        str_3 = 'someint'
        int_0 = 99
        bool_1 = None
        var_1 = module_0.check_type_path(bool_1)
        str_4 = 'string_param'
        str_5 = (str_0, str_4)
        var_2 = [str_3, int_0, str_5]
        var_3 = [var_0, var_2]
        var_4 = {str_0: str_1, str_3: int_0}
        var_5 = module_0.check_required_if(var_3, var_4)
    except BaseException:
        pass

def test_case_50():
    try:
        float_0 = 1.0
        str_0 = 'C@=xk'
        var_0 = module_0.count_terms(float_0, str_0)
        float_1 = 3299.0
        dict_0 = {float_1: float_1, float_1: float_1, float_1: float_1}
        str_1 = '4'
        tuple_0 = (str_1, float_1)
        var_1 = module_0.check_missing_parameters(dict_0, tuple_0)
    except BaseException:
        pass

def test_case_51():
    try:
        bool_0 = True
        str_0 = 'str'
        var_0 = dict(required=bool_0, type=str_0)
        var_1 = dict(required=bool_0, type=str_0)
        var_2 = dict(required=bool_0, type=str_0)
        var_3 = dict(required_arg_1=var_0, required_arg_2=var_1, required_arg_3=var_2)
        str_1 = 'This is arg2'
        var_4 = dict(required_arg_2=str_1)
        var_5 = module_0.check_required_arguments(var_3, var_4)
    except BaseException:
        pass