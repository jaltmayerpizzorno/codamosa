# Automatically generated by Pynguin.
import httpie.context as module_0

def test_case_0():
    pass

def test_case_1():
    environment_0 = module_0.Environment()

def test_case_2():
    environment_0 = module_0.Environment()
    var_0 = environment_0.__str__()

def test_case_3():
    environment_0 = module_0.Environment()
    var_0 = environment_0.__repr__()

def test_case_4():
    environment_0 = module_0.Environment()
    var_0 = environment_0.log_error(environment_0)

def test_case_5():
    str_0 = 'stdin'
    dict_0 = {str_0: str_0, str_0: str_0}
    environment_0 = module_0.Environment(dict_0, **dict_0)

def test_case_6():
    environment_0 = module_0.Environment()
    var_0 = environment_0.__repr__()
    var_1 = environment_0.__repr__()

def test_case_7():
    str_0 = '/dev/null'
    str_1 = 'stdin'
    str_2 = 'stdout'
    dict_0 = {str_0: str_1, str_1: str_0}
    dict_1 = {str_2: str_2}
    environment_0 = module_0.Environment(dict_0, **dict_1)

def test_case_8():
    str_0 = '/root'
    str_1 = 'stdin'
    bool_0 = False
    str_2 = 'stdin_encoding'
    str_3 = 'stdout'
    str_4 = 'stdout_encoding'
    str_5 = 'stderr'
    str_6 = 'program_name'
    var_0 = dict(config_dir=str_0, stdin=str_1, stdin_isatty=bool_0, stdin_encoding=str_2, stdout=str_3, stdout_isatty=bool_0, stdout_encoding=str_4, stderr=str_5, stderr_isatty=bool_0, colors=bool_0, program_name=str_6)
    environment_0 = module_0.Environment(**var_0)
    var_1 = environment_0.__dict__
    var_2 = dict(var_1)
    str_7 = '_orig_stderr'
    var_3 = var_2[str_7]
    str_8 = '_devnull'
    var_4 = var_2[str_8]

def test_case_9():
    bool_0 = False
    str_0 = '/'
    environment_0 = module_0.Environment()
    var_0 = environment_0.__str__()
    var_1 = print(var_0)
    var_2 = environment_0.__repr__()
    var_3 = print(var_2)
    var_4 = environment_0.devnull
    var_5 = print(var_4)