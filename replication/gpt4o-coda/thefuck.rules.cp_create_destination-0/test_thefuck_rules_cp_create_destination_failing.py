# Automatically generated by Pynguin.
import thefuck.rules.cp_create_destination as module_0

def test_case_0():
    try:
        str_0 = 'git branch --delete list'
        var_0 = module_0.match(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = -136
        var_0 = module_0.get_new_command(int_0)
    except BaseException:
        pass