# Automatically generated by Pynguin.
import ansible.parsing.quoting as module_0

def test_case_0():
    str_0 = 'bcY\x0cm?OFd,IVT'
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
    var_0 = module_0.unquote(dict_0)

def test_case_1():
    bytes_0 = b'\x1d\xb9\x12\xd5\x02\xf1\x89\x8b[\xc7\xb3\xdeI\xfb\x8f'
    var_0 = module_0.is_quoted(bytes_0)
    str_0 = "'test'"
    var_1 = module_0.unquote(str_0)

def test_case_2():
    str_0 = ''
    var_0 = module_0.is_quoted(str_0)

def test_case_3():
    str_0 = '"test"'
    var_0 = module_0.unquote(str_0)
    str_1 = "'test'"
    var_1 = module_0.unquote(str_1)