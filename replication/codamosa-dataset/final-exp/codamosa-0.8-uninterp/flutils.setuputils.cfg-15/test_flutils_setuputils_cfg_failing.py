# Automatically generated by Pynguin.
import flutils.setuputils.cfg as module_0

def test_case_0():
    try:
        str_0 = '../..'
        generator_0 = module_0.each_sub_command_config(str_0)
        var_0 = next(generator_0)
    except BaseException:
        pass

def test_case_1():
    try:
        generator_0 = module_0.each_sub_command_config()
        var_0 = next(generator_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'Ci8ePashKb\t'
        generator_0 = module_0.each_sub_command_config(str_0)
        var_0 = next(generator_0)
    except BaseException:
        pass