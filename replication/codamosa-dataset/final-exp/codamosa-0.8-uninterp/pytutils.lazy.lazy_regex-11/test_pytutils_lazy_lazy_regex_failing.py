# Automatically generated by Pynguin.
import pytutils.lazy.lazy_regex as module_0

def test_case_0():
    try:
        str_0 = '8>{B\nA\x0b\\8"@5'
        invalid_pattern_0 = module_0.InvalidPattern(str_0)
        var_0 = invalid_pattern_0.__repr__()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '8>{B\nA\x0b\\8"@5'
        invalid_pattern_0 = module_0.InvalidPattern(str_0)
        var_0 = invalid_pattern_0.__unicode__()
    except BaseException:
        pass

def test_case_2():
    try:
        list_0 = []
        invalid_pattern_0 = module_0.InvalidPattern(list_0)
        bytes_0 = b'\xe0\xc2S=&/~'
        invalid_pattern_1 = module_0.InvalidPattern(bytes_0)
        var_0 = invalid_pattern_1.__eq__(invalid_pattern_0)
        str_0 = '_real_obj'
        invalid_pattern_2 = module_0.InvalidPattern(str_0)
        var_1 = invalid_pattern_2.__str__()
    except BaseException:
        pass

def test_case_3():
    try:
        set_0 = set()
        invalid_pattern_0 = module_0.InvalidPattern(set_0)
        var_0 = invalid_pattern_0.__eq__(set_0)
        var_1 = invalid_pattern_0.__unicode__()
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '^\\w+$'
        str_1 = (str_0,)
        var_0 = {}
        lazy_regex_0 = module_0.LazyRegex(str_1, var_0)
        var_1 = lazy_regex_0.attr_name
    except BaseException:
        pass

def test_case_5():
    try:
        bool_0 = None
        lazy_regex_0 = module_0.LazyRegex()
        var_0 = lazy_regex_0.__getattr__(bool_0)
    except BaseException:
        pass

def test_case_6():
    try:
        lazy_regex_0 = module_0.LazyRegex()
        var_0 = lazy_regex_0.__getstate__()
        int_0 = -649
        var_1 = module_0.finditer_public(lazy_regex_0, int_0)
    except BaseException:
        pass

def test_case_7():
    try:
        dict_0 = None
        str_0 = 'utf8'
        var_0 = module_0.finditer_public(dict_0, str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        lazy_regex_0 = module_0.LazyRegex()
        int_0 = -615
        var_0 = module_0.finditer_public(lazy_regex_0, int_0)
    except BaseException:
        pass

def test_case_9():
    try:
        var_0 = module_0.install_lazy_compile()
        bytes_0 = None
        invalid_pattern_0 = module_0.InvalidPattern(bytes_0)
        str_0 = '{J\tPMB-\\c8x\rK\\Y9{3i5'
        set_0 = {str_0, str_0, str_0}
        lazy_regex_0 = module_0.LazyRegex(set_0)
        var_1 = lazy_regex_0.__getattr__(invalid_pattern_0)
    except BaseException:
        pass