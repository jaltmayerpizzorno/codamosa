# Automatically generated by Pynguin.
import pytutils.env as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = '\n    Write `contents` to `filename`.\n    '
    str_1 = module_0.expand(str_0)

def test_case_2():
    str_0 = 'THI3=~/Wf//.t{st'
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    ordered_dict_0 = module_0.load_env_file(dict_0)

def test_case_3():
    str_0 = "Return a member from the proxied regex object.\n\n        If the regex hasn't been compiled yet, compile it\n        "
    ordered_dict_0 = module_0.load_env_file(str_0)
    str_1 = 'D-\rfb'
    generator_0 = module_0.parse_env_file_contents(str_1)

def test_case_4():
    str_0 = 'THISIS=~/a/test'
    str_1 = [str_0, str_0, str_0]
    str_2 = None
    ordered_dict_0 = module_0.load_env_file(str_1, str_2)