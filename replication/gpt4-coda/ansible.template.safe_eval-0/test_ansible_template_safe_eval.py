# Automatically generated by Pynguin.
import ansible.template.safe_eval as module_0

def test_case_0():
    str_0 = 'E 80W\x0cYFN*][k]N5T:'
    var_0 = module_0.safe_eval(str_0)

def test_case_1():
    str_0 = 'F'
    var_0 = module_0.safe_eval(str_0)

def test_case_2():
    int_0 = 511
    var_0 = module_0.safe_eval(int_0)

def test_case_3():
    str_0 = 'Evaluated conditional (%s): %s'
    float_0 = -1834.003706
    var_0 = module_0.safe_eval(str_0, float_0)
    var_1 = module_0.safe_eval(str_0, float_0)
    bool_0 = None
    var_2 = module_0.safe_eval(float_0, bool_0)
    str_1 = 'secontext'
    set_0 = set()
    var_3 = module_0.safe_eval(str_1, str_0, set_0)
    set_1 = {str_0}
    var_4 = module_0.safe_eval(str_0, set_1, set_1)
    str_2 = '-V$9xu|,nX~'
    var_5 = module_0.safe_eval(bool_0, str_2)
    str_3 = 'B;r\t\x0c58UL,y6>,:nS,'
    var_6 = module_0.safe_eval(str_3)

def test_case_4():
    bool_0 = True
    var_0 = module_0.safe_eval(bool_0, bool_0)
    dict_0 = {bool_0: bool_0}
    var_1 = module_0.safe_eval(dict_0)
    set_0 = None
    float_0 = 0.2
    str_0 = '3kC5U5/uAk"xXk8YvV^'
    var_2 = module_0.safe_eval(set_0, float_0, str_0)
    dict_1 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_0}
    tuple_0 = ()
    var_3 = module_0.safe_eval(tuple_0)
    var_4 = module_0.safe_eval(bool_0, dict_1)

def test_case_5():
    str_0 = '"'
    var_0 = module_0.safe_eval(str_0, str_0)

def test_case_6():
    str_0 = 'wXNTMS^djEZH'
    var_0 = module_0.safe_eval(str_0)

def test_case_7():
    str_0 = '"virtual collection namespace"'
    var_0 = module_0.safe_eval(str_0)