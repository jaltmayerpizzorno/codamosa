# Automatically generated by Pynguin.
import pytutils.env as module_0

def test_case_0():
    generator_0 = module_0.parse_env_file_contents()

def test_case_1():
    str_0 = '\x0cCp:?'
    str_1 = module_0.expand(str_0)

def test_case_2():
    str_0 = ' $+m\n^Jg"'
    generator_0 = module_0.parse_env_file_contents()
    list_0 = [str_0, generator_0, str_0]
    ordered_dict_0 = module_0.load_env_file(str_0, list_0)

def test_case_3():
    str_0 = 'THISIS=~/a/test'
    str_1 = 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'
    str_2 = [str_1, str_0, str_1]
    var_0 = None
    ordered_dict_0 = module_0.load_env_file(str_2, var_0)

def test_case_4():
    str_0 = "TEST='${HOME}/yeee'"
    str_1 = 'TEST2=${HOME}/yeee'
    str_2 = 'THISIS="~/a/test"'
    str_3 = 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'
    str_4 = [str_0, str_1, str_2, str_3]
    generator_0 = module_0.parse_env_file_contents(str_4)
    var_0 = dict(generator_0)