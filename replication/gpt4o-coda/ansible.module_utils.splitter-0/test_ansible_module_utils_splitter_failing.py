# Automatically generated by Pynguin.
import ansible.module_utils.splitter as module_0

def test_case_0():
    try:
        str_0 = ''
        var_0 = module_0.split_args(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b''
        var_0 = module_0.split_args(bytes_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = None
        var_0 = module_0.is_quoted(bytes_0)
    except BaseException:
        pass