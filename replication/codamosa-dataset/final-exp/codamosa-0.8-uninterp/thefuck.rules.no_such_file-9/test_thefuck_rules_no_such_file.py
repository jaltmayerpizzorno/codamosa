# Automatically generated by Pynguin.
import thefuck.rules.no_such_file as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = ''
    var_0 = ()
    str_1 = 'script'
    str_2 = 'output'
    str_3 = 'mv file.txt test/'
    str_4 = "mv: cannot move 'file.txt' to 'test/': No such file or directory"
    str_5 = {str_1: str_3, str_2: str_4}
    var_1 = type(str_0, var_0, str_5)
    var_2 = module_0.get_new_command(var_1)
    var_3 = ()
    str_6 = 'cp file.txt test/'
    str_7 = {str_1: str_6, str_2: str_0}
    var_4 = type(str_0, var_3, str_7)
    var_5 = module_0.get_new_command(var_4)