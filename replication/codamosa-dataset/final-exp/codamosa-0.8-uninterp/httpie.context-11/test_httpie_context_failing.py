# Automatically generated by Pynguin.
import httpie.context as module_0

def test_case_0():
    try:
        str_0 = 'h'
        dict_0 = {str_0: str_0}
        environment_0 = module_0.Environment(str_0, **dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = False
        float_0 = -2078.0
        environment_0 = module_0.Environment()
        var_0 = environment_0.log_error(bool_0, float_0)
    except BaseException:
        pass