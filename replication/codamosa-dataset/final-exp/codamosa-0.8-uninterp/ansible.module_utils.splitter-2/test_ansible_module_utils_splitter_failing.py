# Automatically generated by Pynguin.
import ansible.module_utils.splitter as module_0

def test_case_0():
    try:
        float_0 = 689.61
        var_0 = module_0.split_args(float_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'&\x1e\xde\xb1E\x8e\x01\xc8'
        var_0 = module_0.split_args(bytes_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'key1=val1  key2="{{foo}} bar {{baz}}"  key3=\'{{fie}} Zar {{fum}}\''
        var_0 = module_0.split_args(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        tuple_0 = None
        var_0 = module_0.is_quoted(tuple_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = ' unquote should remove first and last quote from a string '
        str_1 = '"abc"'
        var_0 = module_0.unquote(str_1)
        str_2 = "'abc'"
        var_1 = module_0.unquote(str_2)
        str_3 = 'abc'
        dict_0 = {str_3: str_3, str_1: str_3, str_0: str_0, var_1: str_2}
        var_2 = module_0.split_args(dict_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'peer'
        bytes_0 = b'\xcd\xda\x9f\xe6:#\x18\xfa\xafU'
        str_1 = '"kj[fU*'
        var_0 = module_0.is_quoted(str_1)
        var_1 = module_0.unquote(str_0)
        var_2 = module_0.split_args(bytes_0)
    except BaseException:
        pass