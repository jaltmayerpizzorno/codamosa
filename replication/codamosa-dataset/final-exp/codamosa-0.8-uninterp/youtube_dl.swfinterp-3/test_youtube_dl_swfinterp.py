# Automatically generated by Pynguin.
import youtube_dl.swfinterp as module_0

def test_case_0():
    pass

def test_case_1():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    str_0 = '72.0.3591.3'
    str_1 = '38'
    dict_0 = {str_0: bool_0, str_1: str_1, str_1: bool_0, str_1: bool_0}
    multiname_0 = module_0._Multiname(dict_0)
    a_v_m_class_0 = module_0._AVMClass(bool_0, list_0, multiname_0)
    var_0 = a_v_m_class_0.__repr__()

def test_case_2():
    int_0 = 1
    str_0 = 'test1'
    a_v_m_class_0 = module_0._AVMClass(int_0, str_0)
    str_1 = 'method1'
    int_1 = 2
    int_2 = {str_1: int_1}
    var_0 = a_v_m_class_0.register_methods(int_2)
    str_2 = 'method2'
    int_3 = {str_2: int_0}
    var_1 = a_v_m_class_0.register_methods(int_3)

def test_case_3():
    undefined_0 = module_0._Undefined()
    var_0 = undefined_0.__hash__()

def test_case_4():
    undefined_0 = module_0._Undefined()
    var_0 = undefined_0.__str__()