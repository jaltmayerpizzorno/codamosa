# Automatically generated by Pynguin.
import ansible.modules.expect as module_0

def test_case_0():
    pass

def test_case_1():
    int_0 = 2775
    int_1 = None
    set_0 = {int_0, int_0, int_0, int_1}
    str_0 = 'Mx*R-w#Bz#'
    str_1 = 'Directory %s already exists, but not as a regular file\n'
    var_0 = module_0.response_closure(set_0, str_0, str_1)
    var_1 = module_0.main()
    var_2 = module_0.main()

def test_case_2():
    var_0 = module_0.main()