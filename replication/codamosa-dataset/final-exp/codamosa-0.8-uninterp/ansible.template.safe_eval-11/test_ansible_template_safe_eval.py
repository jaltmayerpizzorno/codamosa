# Automatically generated by Pynguin.
import ansible.template.safe_eval as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'x+2'
    var_0 = module_0.safe_eval(str_0)

def test_case_2():
    set_0 = set()
    var_0 = module_0.safe_eval(set_0)

def test_case_3():
    bool_0 = True
    var_0 = module_0.safe_eval(bool_0)
    str_0 = "4 '2/"
    bytes_0 = None
    str_1 = 'ALwrW]jy=?jU/9Z-'
    var_1 = module_0.safe_eval(str_0, bytes_0, str_1)

def test_case_4():
    str_0 = '[]'
    var_0 = module_0.safe_eval(str_0)

def test_case_5():
    str_0 = "'abc'"
    var_0 = module_0.safe_eval(str_0)
    str_1 = '123'
    var_1 = module_0.safe_eval(str_1)
    str_2 = 'true'
    var_2 = module_0.safe_eval(str_2)
    str_3 = "{'a': 'b'}"
    var_3 = module_0.safe_eval(str_3)
    str_4 = 'Repo: %s/%s'
    var_4 = module_0.safe_eval(str_4)

def test_case_6():
    str_0 = 'svc'
    str_1 = '[(<)}u{rr^0JZ!'
    int_0 = 9
    set_0 = None
    list_0 = [int_0, str_1, set_0]
    int_1 = None
    var_0 = module_0.safe_eval(set_0, list_0, int_1)
    bytes_0 = b'%\x9e1\x1f\x112\x18i\xb3\x83\xa9\xc2\xa8\xe0\xc4\xf3\x94M'
    float_0 = 3128.8671
    tuple_0 = (int_0, bytes_0, float_0, str_1)
    var_1 = module_0.safe_eval(str_0, str_1, tuple_0)

def test_case_7():
    set_0 = set()
    bool_0 = True
    var_0 = module_0.safe_eval(set_0, bool_0, bool_0)

def test_case_8():
    str_0 = '+2'
    var_0 = module_0.safe_eval(str_0)

def test_case_9():
    str_0 = 'TS2'
    var_0 = module_0.safe_eval(str_0, str_0)

def test_case_10():
    str_0 = '""'
    var_0 = module_0.safe_eval(str_0)
    str_1 = '42'
    var_1 = module_0.safe_eval(str_1)
    str_2 = '42.0'
    var_2 = module_0.safe_eval(str_2)
    var_3 = module_0.safe_eval(str_0)
    str_3 = 'false'
    var_4 = module_0.safe_eval(str_3)
    str_4 = 'null'
    var_5 = module_0.safe_eval(str_4)
    str_5 = '[]'
    var_6 = module_0.safe_eval(str_5)
    str_6 = 'a_list_variable'
    var_7 = module_0.safe_eval(str_6)
    set_0 = set()
    tuple_0 = ()
    tuple_1 = (tuple_0, set_0)
    var_8 = module_0.safe_eval(str_1, set_0, tuple_1)
    bool_0 = True
    var_9 = module_0.safe_eval(bool_0)
    list_0 = [str_5]
    bool_1 = True
    var_10 = module_0.safe_eval(list_0, bool_1)