# Automatically generated by Pynguin.
import ansible.utils.py3compat as module_0

def test_case_0():
    pass

def test_case_1():
    text_environ_0 = module_0._TextEnviron()

def test_case_2():
    bool_0 = False
    str_0 = 'y8#*,c~<'
    text_environ_0 = module_0._TextEnviron(str_0)
    var_0 = text_environ_0.__getitem__(bool_0)

def test_case_3():
    bool_0 = False
    str_0 = 'y8#*,c~<'
    text_environ_0 = module_0._TextEnviron(str_0)
    var_0 = text_environ_0.__getitem__(bool_0)
    var_1 = text_environ_0.__iter__()

def test_case_4():
    text_environ_0 = module_0._TextEnviron()
    var_0 = text_environ_0.__len__()