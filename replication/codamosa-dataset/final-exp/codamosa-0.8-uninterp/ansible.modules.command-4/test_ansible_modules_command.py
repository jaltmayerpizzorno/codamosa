# Automatically generated by Pynguin.
import ansible.modules.command as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = '1'
    var_0 = module_0.check_command(str_0, str_0)

def test_case_2():
    var_0 = module_0.main()

def test_case_3():
    str_0 = 'l'
    list_0 = [str_0]
    var_0 = module_0.check_command(list_0, list_0)
    var_1 = module_0.check_command(str_0, str_0)
    var_2 = module_0.main()