# Automatically generated by Pynguin.
import ansible.template.safe_eval as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'U^a'
    var_0 = module_0.safe_eval(str_0)

def test_case_2():
    bytes_0 = b'oy\x88\xa8'
    var_0 = module_0.safe_eval(bytes_0)

def test_case_3():
    int_0 = 5181
    float_0 = None
    var_0 = module_0.safe_eval(float_0)
    float_1 = 1757.51
    str_0 = 'tSkJ~Q\x0b?"|p,)xK9'
    bytes_0 = b'\x04'
    int_1 = -3721
    var_1 = module_0.safe_eval(str_0, bytes_0, int_1)
    var_2 = module_0.safe_eval(float_1)
    int_2 = -2635
    tuple_0 = (int_2,)
    dict_0 = {tuple_0: int_2}
    var_3 = module_0.safe_eval(tuple_0, dict_0)
    var_4 = module_0.safe_eval(int_0)
    list_0 = []
    set_0 = set()
    list_1 = [int_1, float_0, int_1, var_4]
    var_5 = module_0.safe_eval(list_1)
    var_6 = module_0.safe_eval(set_0)
    var_7 = module_0.safe_eval(list_0)

def test_case_4():
    int_0 = 2868
    var_0 = module_0.safe_eval(int_0)
    str_0 = 'IE>\\!'
    var_1 = module_0.safe_eval(str_0)

def test_case_5():
    str_0 = 'Ua'
    var_0 = module_0.safe_eval(str_0)

def test_case_6():
    str_0 = 'foo'
    str_1 = 'bar'
    str_2 = {str_0: str_1}
    str_3 = 'az7'
    str_4 = 'quux'
    str_5 = {str_3: str_4}
    var_0 = module_0.safe_eval(str_0, str_2, str_5)
    var_1 = module_0.safe_eval(str_3, str_2, str_5)
    str_6 = 'foo and baz'
    var_2 = module_0.safe_eval(str_6, str_2, str_5)
    str_7 = 'foo and baz and None'
    var_3 = module_0.safe_eval(str_7, str_2, str_5)
    str_8 = '[1,2,3,4]'
    var_4 = module_0.safe_eval(str_8, str_2, str_5)
    str_9 = 'None in bar'
    var_5 = module_0.safe_eval(str_9, str_2, str_5)

def test_case_7():
    int_0 = 729
    dict_0 = {int_0: int_0, int_0: int_0, int_0: int_0}
    str_0 = 'QD@^L-!'
    float_0 = -924.24117
    bool_0 = False
    str_1 = ''
    tuple_0 = (bool_0, str_1, str_0, dict_0)
    var_0 = module_0.safe_eval(tuple_0)
    var_1 = module_0.safe_eval(dict_0, str_0, float_0)

def test_case_8():
    float_0 = -558.0
    set_0 = {float_0}
    str_0 = ';NiB|L'
    bool_0 = False
    var_0 = module_0.safe_eval(set_0, str_0, bool_0)

def test_case_9():
    str_0 = '5\r'
    var_0 = module_0.safe_eval(str_0)