# Automatically generated by Pynguin.
import sty.primitive as module_0
import sty.rendertype as module_1

def test_case_0():
    try:
        register_0 = module_0.Register()
        str_0 = None
        style_0 = module_0.Style()
        var_0 = register_0.__setattr__(str_0, style_0)
    except BaseException:
        pass

def test_case_1():
    try:
        register_0 = module_0.Register()
        register_0.unmute()
        str_0 = ')\x0c`zoQt&ROTK{3x-Z'
        list_0 = [str_0, str_0]
        style_0 = module_0.Style(*list_0)
        var_0 = register_0.__setattr__(str_0, style_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = None
        list_0 = [bool_0, bool_0]
        register_0 = module_0.Register()
        register_1 = register_0.copy()
        register_2 = register_1.copy()
        register_2.set_eightbit_call(list_0)
    except BaseException:
        pass

def test_case_3():
    try:
        list_0 = []
        list_1 = [list_0, list_0]
        list_2 = [list_1, list_0, list_0]
        register_0 = module_0.Register()
        register_1 = register_0.copy()
        register_2 = register_1.copy()
        register_2.set_rgb_call(list_2)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = ')|A['
        style_0 = None
        register_0 = module_0.Register()
        var_0 = register_0.__setattr__(str_0, style_0)
        register_0.mute()
        register_1 = register_0.copy()
        str_1 = register_1.__call__()
        dict_0 = {}
        dict_1 = register_1.as_dict()
        dict_2 = register_1.as_dict()
        style_1 = module_0.Style(**dict_0)
        var_1 = register_1.__setattr__(str_0, style_1)
        type_0 = None
        register_1.set_rgb_call(type_0)
    except BaseException:
        pass

def test_case_5():
    try:
        register_0 = module_0.Register()
        register_0.mute()
        register_1 = module_0.Register()
        register_1.mute()
        dict_0 = register_1.as_dict()
        register_2 = register_0.copy()
        var_0 = register_1.as_namedtuple()
        str_0 = 'PM\x0bZS4Sor+L\r; pIOWw?'
        style_0 = module_0.Style()
        var_1 = register_0.__setattr__(str_0, style_0)
        register_3 = module_0.Register()
        register_1.unmute()
        type_0 = None
        dict_1 = register_0.as_dict()
        style_1 = module_0.Style()
        register_1.set_rgb_call(type_0)
    except BaseException:
        pass

def test_case_6():
    try:
        register_0 = module_0.Register()
        str_0 = register_0.__call__()
        register_1 = module_0.Register()
        register_2 = module_0.Register()
        str_1 = register_2.__call__()
        dict_0 = {}
        dict_1 = register_2.as_dict()
        str_2 = '/\t!EC^|bV@%|'
        style_0 = module_0.Style()
        var_0 = register_0.__setattr__(str_2, style_0)
        dict_2 = register_2.as_dict()
        register_0.unmute()
        style_1 = module_0.Style(**dict_0)
        style_2 = module_0.Style()
        str_3 = 'VKZFeVY&hU'
        style_3 = module_0.Style()
        var_1 = register_2.__setattr__(str_3, style_3)
        type_0 = None
        register_3 = register_2.copy()
        register_3.set_rgb_call(type_0)
    except BaseException:
        pass

def test_case_7():
    try:
        register_0 = module_0.Register()
        str_0 = '@5E],FnO'
        style_0 = module_0.Style()
        var_0 = register_0.__setattr__(str_0, style_0)
        type_0 = None
        callable_0 = None
        register_0.set_renderfunc(type_0, callable_0)
        type_1 = None
        register_0.set_eightbit_call(type_1)
        str_1 = register_0.__call__()
        dict_0 = register_0.as_dict()
        register_1 = register_0.copy()
        register_0.mute()
        bytes_0 = b'\xbf9p\xf0\xa1\x86'
        list_0 = [style_0, style_0, style_0]
        style_1 = style_0.__new__(bytes_0, *list_0)
    except BaseException:
        pass

def test_case_8():
    try:
        register_0 = module_0.Register()
        str_0 = register_0.__call__()
        register_1 = module_0.Register()
        list_0 = [register_0, str_0, register_1]
        style_0 = module_0.Style(*list_0)
        bytes_0 = b'12\x03\xf4\x87.\xb9\xa1.Ahs\xaf\x9e\x1f`\x98C\xec'
        register_0.set_renderfunc(style_0, bytes_0)
        list_1 = [str_0]
        str_1 = register_0.__call__(*list_1)
    except BaseException:
        pass

def test_case_9():
    try:
        register_0 = module_0.Register()
        register_1 = register_0.copy()
        register_1.mute()
        dict_0 = {}
        render_type_0 = module_1.RenderType(**dict_0)
        register_2 = module_0.Register()
        str_0 = "Parameter 'rules' must be of type Iterable[Rule]."
        list_0 = [render_type_0]
        style_0 = module_0.Style(*list_0)
        register_3 = register_2.copy()
        var_0 = register_3.__setattr__(str_0, style_0)
    except BaseException:
        pass