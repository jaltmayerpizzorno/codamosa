# Automatically generated by Pynguin.
import youtube_dl.swfinterp as module_0

def test_case_0():
    undefined_0 = module_0._Undefined()

def test_case_1():
    bool_0 = False
    float_0 = 26.0
    a_v_m_class_0 = module_0._AVMClass(bool_0, float_0)
    set_0 = {a_v_m_class_0, float_0}
    str_0 = 'http://njpwworld.com/p/s_series_00155_1_9/'
    a_v_m_class__object_0 = module_0._AVMClass_Object(str_0)
    a_v_m_class_1 = module_0._AVMClass(bool_0, set_0, a_v_m_class__object_0)
    var_0 = a_v_m_class_1.make_object()

def test_case_2():
    str_0 = 'N\t7EkxT;'
    multiname_0 = None
    dict_0 = {str_0: str_0, str_0: multiname_0}
    scope_dict_0 = module_0._ScopeDict(dict_0)
    bytes_0 = b'\xf3'
    str_1 = 'site_name'
    a_v_m_class_0 = module_0._AVMClass(bytes_0, str_1)
    var_0 = a_v_m_class_0.register_methods(scope_dict_0)

def test_case_3():
    int_0 = 846
    multiname_0 = module_0._Multiname(int_0)

def test_case_4():
    undefined_0 = module_0._Undefined()
    var_0 = undefined_0.__bool__()

def test_case_5():
    list_0 = []
    undefined_0 = module_0._Undefined(*list_0)
    var_0 = undefined_0.__str__()