# Automatically generated by Pynguin.
import pytutils.env as module_0

def test_case_0():
    try:
        dict_0 = None
        ordered_dict_0 = module_0.load_env_file(dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'THISIS=~/a/test'
        str_1 = [str_0, str_0, str_0]
        ordered_dict_0 = module_0.load_env_file(str_1, str_0)
    except BaseException:
        pass