# Automatically generated by Pynguin.
import ansible.template.safe_eval as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'qoGpLJ.b>ZmAP68S'
    var_0 = module_0.safe_eval(str_0)

def test_case_2():
    str_0 = None
    var_0 = module_0.safe_eval(str_0)

def test_case_3():
    str_0 = '1'
    var_0 = module_0.safe_eval(str_0)
    str_1 = 'foo'
    var_1 = module_0.safe_eval(str_1)
    int_0 = -1116
    dict_0 = {int_0: str_1}
    var_2 = module_0.safe_eval(dict_0)
    str_2 = '/{.*;Tgb~Q'
    str_3 = '?rhw@'
    var_3 = module_0.safe_eval(str_2, int_0, str_3)
    int_1 = -1424
    var_4 = module_0.safe_eval(int_1)
    set_0 = {int_1, int_0}
    bool_0 = True
    var_5 = module_0.safe_eval(set_0, bool_0)

def test_case_4():
    str_0 = '#vj:(vU9,pBm.w<'
    var_0 = module_0.safe_eval(str_0)
    int_0 = 6
    var_1 = module_0.safe_eval(int_0)

def test_case_5():
    str_0 = 't'
    var_0 = module_0.safe_eval(str_0)

def test_case_6():
    str_0 = 'NM#qQK1DI=t}me3UO$[d'
    dict_0 = {}
    int_0 = 605
    var_0 = module_0.safe_eval(str_0, dict_0, int_0)
    float_0 = -49.96421
    var_1 = module_0.safe_eval(float_0)

def test_case_7():
    dict_0 = None
    bool_0 = True
    list_0 = [bool_0]
    var_0 = module_0.safe_eval(dict_0, bool_0, list_0)

def test_case_8():
    str_0 = 'o'
    var_0 = module_0.safe_eval(str_0, str_0)

def test_case_9():
    str_0 = '00000000000000000000000000000000'
    var_0 = module_0.safe_eval(str_0)

def test_case_10():
    str_0 = '["foo", "bar"]'
    var_0 = dict()
    bool_0 = True
    var_1 = module_0.safe_eval(str_0, var_0, bool_0)
    var_2 = dict()
    bool_1 = False
    var_3 = module_0.safe_eval(str_0, var_2, bool_1)
    str_1 = 'foo'
    str_2 = 'bar'
    var_4 = dict(foo=str_2)
    var_5 = module_0.safe_eval(str_1, var_4, bool_0)
    var_6 = dict(foo=str_2)
    var_7 = module_0.safe_eval(str_1, var_6, bool_1)