# Automatically generated by Pynguin.
import httpie.context as module_0

def test_case_0():
    try:
        str_0 = 'x/ni<'
        dict_0 = {str_0: str_0}
        environment_0 = module_0.Environment(**dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        environment_0 = module_0.Environment()
        var_0 = environment_0.__repr__()
        bytes_0 = b'n\x0c\x9b\x84\xb1\xf4\x02E\x88\xea\xff"\x0e\x9f\x7f\xd7'
        str_0 = '5{I\x0b%zhY3-p$'
        var_1 = environment_0.log_error(bytes_0, str_0)
    except BaseException:
        pass