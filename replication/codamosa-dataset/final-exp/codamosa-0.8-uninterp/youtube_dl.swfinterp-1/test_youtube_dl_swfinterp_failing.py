# Automatically generated by Pynguin.
import youtube_dl.swfinterp as module_0

def test_case_0():
    try:
        bytes_0 = b'a\xc1;C=[v'
        s_w_f_interpreter_0 = module_0.SWFInterpreter(bytes_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b']\xe3\x06\xf7\x0c\xda\x9cql\xb2\x96\x1c'
        a_v_m_class__object_0 = module_0._AVMClass_Object(bytes_0)
        var_0 = a_v_m_class__object_0.__repr__()
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'\xe4t\x10\x7f4\x01/'
        multiname_0 = module_0._Multiname(bytes_0)
        scope_dict_0 = module_0._ScopeDict(multiname_0)
        var_0 = scope_dict_0.__repr__()
    except BaseException:
        pass

def test_case_3():
    try:
        bool_0 = True
        multiname_0 = module_0._Multiname(bool_0)
        multiname_1 = module_0._Multiname(multiname_0)
        a_v_m_class__object_0 = module_0._AVMClass_Object(multiname_1)
        a_v_m_class_0 = module_0._AVMClass(multiname_1, a_v_m_class__object_0)
        scope_dict_0 = module_0._ScopeDict(a_v_m_class_0)
        var_0 = a_v_m_class_0.make_object()
        var_1 = scope_dict_0.__repr__()
    except BaseException:
        pass

def test_case_4():
    try:
        dict_0 = {}
        scope_dict_0 = module_0._ScopeDict(dict_0)
        undefined_0 = module_0._Undefined()
        a_v_m_class_0 = module_0._AVMClass(dict_0, undefined_0)
        var_0 = a_v_m_class_0.make_object()
        var_1 = scope_dict_0.__repr__()
    except BaseException:
        pass

def test_case_5():
    try:
        undefined_0 = module_0._Undefined()
        var_0 = undefined_0.__bool__()
        undefined_1 = module_0._Undefined()
        var_1 = undefined_1.__bool__()
        a_v_m_class_0 = None
        int_0 = 2559
        a_v_m_class_1 = module_0._AVMClass(int_0, undefined_1)
        str_0 = '*\rf;IoK '
        dict_0 = {str_0: int_0}
        var_2 = a_v_m_class_0.__repr__()
        str_1 = '&d::S]{R)L2g8,\t1o'
        tuple_0 = (a_v_m_class_1, dict_0, str_1)
        s_w_f_interpreter_0 = module_0.SWFInterpreter(tuple_0)
    except BaseException:
        pass

def test_case_6():
    try:
        undefined_0 = module_0._Undefined()
        var_0 = undefined_0.__hash__()
        bool_0 = False
        str_0 = 't\x0cYsw wL6v!4'
        a_v_m_class_0 = module_0._AVMClass(undefined_0, str_0)
        var_1 = a_v_m_class_0.register_methods(bool_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = None
        str_1 = 'Q'
        str_2 = '#~bxF6'
        dict_0 = {str_0: str_0, str_1: str_1, str_2: str_2}
        str_3 = 'C|+?~sd\r'
        float_0 = 3109.1683
        a_v_m_class_0 = module_0._AVMClass(str_3, float_0)
        var_0 = a_v_m_class_0.register_methods(dict_0)
        undefined_0 = module_0._Undefined()
        var_1 = undefined_0.__bool__()
    except BaseException:
        pass

def test_case_8():
    try:
        undefined_0 = module_0._Undefined()
        var_0 = undefined_0.__bool__()
        bytes_0 = b'\x12e\xd1#\xde\x03\xf6\xdc,0P\t\x9a\xac\x04w7\x19\x85'
        s_w_f_interpreter_0 = module_0.SWFInterpreter(bytes_0)
    except BaseException:
        pass

def test_case_9():
    try:
        undefined_0 = module_0._Undefined()
        var_0 = undefined_0.__hash__()
        undefined_1 = module_0._Undefined()
        var_1 = undefined_1.__bool__()
        bytes_0 = b'a\xc1;C=\xf2[y/v'
        s_w_f_interpreter_0 = module_0.SWFInterpreter(bytes_0)
    except BaseException:
        pass