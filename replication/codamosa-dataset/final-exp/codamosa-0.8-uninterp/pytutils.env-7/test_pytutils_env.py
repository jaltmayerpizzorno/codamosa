# Automatically generated by Pynguin.
import pytutils.env as module_0

def test_case_0():
    generator_0 = module_0.parse_env_file_contents()

def test_case_1():
    str_0 = 'tE\n'
    str_1 = module_0.expand(str_0)

def test_case_2():
    str_0 = " qeB=%:a 9B[CXS`',q\x0b"
    ordered_dict_0 = module_0.load_env_file(str_0)

def test_case_3():
    str_0 = 'key1=value1'
    str_1 = (str_0, str_0)
    generator_0 = module_0.parse_env_file_contents(str_1)
    var_0 = next(generator_0)

def test_case_4():
    str_0 = 'TEST=${HOME}/yeee'
    str_1 = "THISIS='~/a/test'"
    str_2 = 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'
    str_3 = [str_0, str_1, str_2]
    generator_0 = module_0.parse_env_file_contents(str_3)
    var_0 = dict(generator_0)
    str_4 = 'TEST'
    var_1 = var_0[str_4]
    str_5 = 'THISIS'
    var_2 = var_0[str_5]
    str_6 = 'YOLO'
    var_3 = var_0[str_6]

def test_case_5():
    str_0 = 'TEST="hello there"'
    str_1 = [str_0]
    generator_0 = module_0.parse_env_file_contents(str_1)
    var_0 = list(generator_0)
    str_2 = "TEST='hello'"
    str_3 = [str_2]
    generator_1 = module_0.parse_env_file_contents(str_3)
    var_1 = list(generator_1)
    str_4 = 'TEST="hello\nthere"'
    str_5 = [str_4]
    generator_2 = module_0.parse_env_file_contents(str_5)
    var_2 = list(generator_2)
    str_6 = 'TEST=hello there'
    str_7 = [str_6]
    generator_3 = module_0.parse_env_file_contents(str_7)
    var_3 = list(generator_3)