# Automatically generated by Pynguin.
import youtube_dl.swfinterp as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'HzR7qWVfvOO3'
    bytes_0 = b'\xc1\xfb\xb8[\xfb\x18\xd9uN\xf5'
    a_v_m_class_0 = module_0._AVMClass(str_0, bytes_0)
    var_0 = a_v_m_class_0.make_object()

def test_case_2():
    str_0 = 'SomeClass'
    int_0 = 0
    a_v_m_class_0 = module_0._AVMClass(str_0, int_0)
    str_1 = 'method_1'
    str_2 = 'method_2'
    str_3 = 'method_3'
    int_1 = 1
    int_2 = 2
    int_3 = 3
    int_4 = {str_1: int_1, str_2: int_2, str_3: int_3}
    var_0 = a_v_m_class_0.register_methods(int_4)

def test_case_3():
    undefined_0 = module_0._Undefined()
    var_0 = undefined_0.__hash__()

def test_case_4():
    int_0 = 1350194821
    undefined_0 = module_0._Undefined()
    var_0 = undefined_0.__str__()
    a_v_m_class_0 = module_0._AVMClass(int_0, undefined_0)
    var_1 = undefined_0.__str__()
    str_0 = ''
    a_v_m_class__object_0 = module_0._AVMClass_Object(str_0)
    a_v_m_class_1 = module_0._AVMClass(a_v_m_class_0, a_v_m_class__object_0)
    var_2 = a_v_m_class_1.make_object()