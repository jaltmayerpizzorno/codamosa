# Automatically generated by Pynguin.
import ansible.module_utils.splitter as module_0

def test_case_0():
    try:
        tuple_0 = None
        var_0 = module_0.split_args(tuple_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'J '
        var_0 = module_0.split_args(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'\xbbP\xa8AL\x95?j\xa0+\xef\xa9yO'
        var_0 = module_0.split_args(bytes_0)
    except BaseException:
        pass

def test_case_3():
    try:
        float_0 = 0.2
        var_0 = module_0.unquote(float_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '"hello world"'
        var_0 = module_0.unquote(str_0)
        str_1 = "'hello world'"
        var_1 = module_0.unquote(str_1)
        str_2 = "'hello world"
        var_2 = module_0.unquote(str_2)
        var_3 = module_0.split_args(str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bytes_0 = b'\x1eYg|'
        str_0 = 'dDD%C3X'
        var_0 = module_0.unquote(bytes_0)
        var_1 = module_0.is_quoted(str_0)
        str_1 = '"J'
        var_2 = module_0.is_quoted(str_1)
        list_0 = []
        var_3 = module_0.is_quoted(list_0)
        var_4 = module_0.split_args(bytes_0)
    except BaseException:
        pass