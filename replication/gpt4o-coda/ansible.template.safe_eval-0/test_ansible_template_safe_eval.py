# Automatically generated by Pynguin.
import ansible.template.safe_eval as module_0

def test_case_0():
    str_0 = None
    var_0 = module_0.safe_eval(str_0)

def test_case_1():
    str_0 = '+ 1'
    var_0 = module_0.safe_eval(str_0)

def test_case_2():
    int_0 = 4611
    list_0 = [int_0]
    bool_0 = False
    var_0 = module_0.safe_eval(bool_0)
    str_0 = 'C78${VJ\x0bAk~^>?i'
    dict_0 = {}
    str_1 = '\tu/\tB'
    var_1 = module_0.safe_eval(str_0, dict_0, str_1)
    float_0 = 2717.614
    bytes_0 = b'\xd0A\xf0\xdd\x81p<L\xa4\x9cxe\x89\x9a4\x0b\xfe'
    bytes_1 = b'{\xc4\xf1\x13\x14\x9d\x17\xd7#\t\x00\xec'
    var_2 = module_0.safe_eval(bytes_1)
    float_1 = -770.38
    var_3 = module_0.safe_eval(bool_0, bytes_0, float_1)
    var_4 = module_0.safe_eval(list_0, float_0)
    str_2 = None
    dict_1 = {}
    var_5 = module_0.safe_eval(str_2, dict_1)

def test_case_3():
    str_0 = '1 + 1'
    var_0 = module_0.safe_eval(str_0)

def test_case_4():
    str_0 = '+1)\x0b'
    var_0 = module_0.safe_eval(str_0)

def test_case_5():
    str_0 = 'FYsrVle-fife'
    var_0 = module_0.safe_eval(str_0)
    list_0 = [var_0]
    bool_0 = False
    var_1 = module_0.safe_eval(list_0, bool_0, list_0)

def test_case_6():
    int_0 = -1307
    var_0 = module_0.safe_eval(int_0, int_0)

def test_case_7():
    str_0 = '--role-filfe'
    var_0 = module_0.safe_eval(str_0)

def test_case_8():
    str_0 = '-roJ-filf'
    bytes_0 = b'\r\x96\xb2\x85!\xb6x@'
    int_0 = 12
    var_0 = module_0.safe_eval(str_0, bytes_0, int_0)