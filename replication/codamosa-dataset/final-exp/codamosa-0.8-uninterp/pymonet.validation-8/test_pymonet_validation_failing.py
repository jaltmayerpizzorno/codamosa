# Automatically generated by Pynguin.
import pymonet.validation as module_0

def test_case_0():
    try:
        str_0 = '.OMm'
        bytes_0 = b'`\xfb\xc7\\G,\x0f\x1b\x99+\xf5K\x84\xe1\xdb\x17\xd1'
        dict_0 = {}
        list_0 = []
        validation_0 = module_0.Validation(list_0, dict_0)
        var_0 = validation_0.to_try()
        validation_1 = module_0.Validation(bytes_0, dict_0)
        var_1 = validation_1.is_fail()
        var_2 = validation_1.__str__()
        set_0 = {str_0}
        list_1 = [set_0]
        validation_2 = module_0.Validation(set_0, list_1)
        var_3 = validation_2.to_maybe()
        str_1 = "DewKj\tR0U*'ZUj]#"
        tuple_0 = ()
        var_4 = validation_2.is_success()
        validation_3 = module_0.Validation(str_1, tuple_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = False
        bool_1 = False
        bool_2 = False
        list_0 = [bool_1, bool_1, bool_1, bool_2]
        validation_0 = module_0.Validation(bool_1, list_0)
        var_0 = validation_0.map(bool_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = False
        str_0 = 't\x0b\r'
        str_1 = 'D\t\x0cIk6IF'
        validation_0 = module_0.Validation(str_0, str_1)
        var_0 = validation_0.bind(bool_0)
    except BaseException:
        pass

def test_case_3():
    try:
        float_0 = 856.121
        float_1 = 143.316761
        bool_0 = False
        dict_0 = {float_0: float_1, bool_0: float_1}
        tuple_0 = (float_0, float_1, bool_0, dict_0)
        int_0 = False
        list_0 = [int_0]
        validation_0 = module_0.Validation(int_0, list_0)
        var_0 = validation_0.ap(tuple_0)
    except BaseException:
        pass

def test_case_4():
    try:
        dict_0 = {}
        bytes_0 = b'\xd4D\xc5\xb3\xac\xeb;\xa5\xd2\n\xbe\xea\xc4\xddd\xb8\xfe\xae\x8b\x04'
        str_0 = ']fp@'
        validation_0 = module_0.Validation(str_0, dict_0)
        var_0 = validation_0.to_either()
        tuple_0 = ()
        validation_1 = module_0.Validation(tuple_0, bytes_0)
        validation_2 = module_0.Validation(bytes_0, validation_1)
        var_1 = validation_2.to_maybe()
    except BaseException:
        pass

def test_case_5():
    try:
        float_0 = -6856.0
        dict_0 = {}
        dict_1 = {float_0: dict_0}
        float_1 = 531.7
        validation_0 = module_0.Validation(dict_1, float_1)
        var_0 = validation_0.to_either()
    except BaseException:
        pass

def test_case_6():
    try:
        float_0 = 1149.241
        list_0 = [float_0, float_0]
        str_0 = 'J]E8^#'
        validation_0 = module_0.Validation(list_0, str_0)
        var_0 = validation_0.__str__()
        int_0 = -2765
        tuple_0 = (float_0, list_0, int_0)
        validation_1 = module_0.Validation(str_0, tuple_0)
        var_1 = validation_1.to_maybe()
        int_1 = -1190
        tuple_1 = (int_1,)
        var_2 = validation_1.ap(tuple_1)
    except BaseException:
        pass

def test_case_7():
    try:
        float_0 = 517.0
        set_0 = {float_0, float_0}
        tuple_0 = (float_0, set_0)
        validation_0 = module_0.Validation(tuple_0, tuple_0)
        int_0 = 1113
        validation_1 = module_0.Validation(validation_0, int_0)
        var_0 = validation_1.to_try()
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = "\\R'I"
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
        bytes_0 = b'<\xd3\xaf\xed\x9f\xf0\xff\xe0\x02\x93\xe7\xf1\x0e\x88\xa85;\xf1'
        list_0 = []
        validation_0 = module_0.Validation(bytes_0, list_0)
        var_0 = validation_0.to_lazy()
        var_1 = validation_0.to_try()
        float_0 = -679.15337
        bytes_1 = b'\xa51\xa2\x92,\xdc\xd3\xc32U\x80\xd8\x93T'
        var_2 = validation_0.__eq__(dict_0)
        validation_1 = module_0.Validation(float_0, bytes_1)
        var_3 = validation_1.__str__()
        var_4 = validation_1.to_either()
        var_5 = validation_0.to_maybe()
        validation_2 = module_0.Validation(bytes_0, validation_1)
        var_6 = validation_2.to_box()
        set_0 = set()
        var_7 = validation_2.map(set_0)
    except BaseException:
        pass