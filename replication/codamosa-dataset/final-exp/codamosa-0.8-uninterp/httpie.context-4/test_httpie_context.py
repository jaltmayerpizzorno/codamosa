# Automatically generated by Pynguin.
import httpie.context as module_0

def test_case_0():
    environment_0 = module_0.Environment()

def test_case_1():
    environment_0 = module_0.Environment()
    var_0 = environment_0.__repr__()

def test_case_2():
    environment_0 = module_0.Environment()
    var_0 = environment_0.__repr__()
    int_0 = -2560
    var_1 = environment_0.log_error(int_0)

def test_case_3():
    environment_0 = module_0.Environment()
    var_0 = environment_0.__str__()
    var_1 = environment_0.__str__()
    var_2 = environment_0.__repr__()
    int_0 = -662
    environment_1 = module_0.Environment(int_0)
    var_3 = environment_1.__str__()

def test_case_4():
    environment_0 = module_0.Environment()
    var_0 = environment_0.devnull

def test_case_5():
    environment_0 = module_0.Environment()
    str_0 = 'stdout_encoding'
    dict_0 = {str_0: str_0, str_0: str_0}
    environment_1 = module_0.Environment(**dict_0)

def test_case_6():
    str_0 = 'O@=\t4Rh\x0cmBe"h?0r'
    bool_0 = True
    dict_0 = {}
    environment_0 = module_0.Environment(bool_0, **dict_0)
    var_0 = environment_0.__str__()
    var_1 = environment_0.log_error(str_0)
    environment_1 = module_0.Environment()
    var_2 = environment_0.__repr__()
    var_3 = environment_1.is_windows
    environment_2 = module_0.Environment()
    environment_3 = module_0.Environment()
    var_4 = environment_3.stdin
    environment_4 = module_0.Environment()
    var_5 = environment_4.stdin_isatty
    environment_5 = module_0.Environment()
    var_6 = environment_5.stdin_encoding
    var_7 = environment_1.stdout
    environment_6 = module_0.Environment()
    var_8 = environment_6.stdout_isatty
    environment_7 = module_0.Environment()
    var_9 = environment_7.stdout_encoding
    environment_8 = module_0.Environment()
    var_10 = environment_8.stderr
    environment_9 = module_0.Environment()
    var_11 = environment_9.stderr_isatty
    environment_10 = module_0.Environment()
    var_12 = environment_10.colors
    environment_11 = module_0.Environment()
    var_13 = environment_11.program_name
    environment_12 = module_0.Environment()
    var_14 = environment_12.config
    var_15 = environment_2.__str__()
    var_16 = environment_0.devnull
    environment_13 = module_0.Environment()
    var_17 = environment_13._orig_stderr
    environment_14 = module_0.Environment()
    var_18 = environment_14._devnull