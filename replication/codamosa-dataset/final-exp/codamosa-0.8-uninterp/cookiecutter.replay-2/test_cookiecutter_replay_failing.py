# Automatically generated by Pynguin.
import cookiecutter.replay as module_0

def test_case_0():
    try:
        str_0 = '\n    Exception for incompatible modes.\n\n    Raised when cookiecutter is called with both `no_input==True` and\n    `replay==True` at the same time.\n    '
        var_0 = module_0.load(str_0, str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = ''
        int_0 = -2133
        float_0 = -83.0
        var_0 = module_0.dump(str_0, int_0, float_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'ODjx:\x0cK\rOy6q'
        bool_0 = False
        set_0 = {str_0, str_0, str_0}
        var_0 = module_0.dump(str_0, bool_0, set_0)
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = 3
        float_0 = -1908.0
        var_0 = module_0.load(int_0, float_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'cohokiecutter'
        str_1 = {str_0: str_0}
        var_0 = module_0.dump(str_0, str_0, str_1)
    except BaseException:
        pass

def test_case_5():
    try:
        bytes_0 = b':\x11\xa1L\n'
        str_0 = 'hu3FHYK@5>\r0<YpL'
        float_0 = 2070.044
        var_0 = module_0.dump(bytes_0, str_0, float_0)
    except BaseException:
        pass

def test_case_6():
    try:
        float_0 = -576.6
        str_0 = '.json'
        var_0 = module_0.load(float_0, str_0)
    except BaseException:
        pass