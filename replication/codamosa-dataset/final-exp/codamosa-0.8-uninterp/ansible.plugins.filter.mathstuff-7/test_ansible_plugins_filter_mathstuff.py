# Automatically generated by Pynguin.
import ansible.plugins.filter.mathstuff as module_0

def test_case_0():
    pass

def test_case_1():
    tuple_0 = ()
    str_0 = 'ansible_pos can only be set with a tuple/list of three values: source, line number, column number'
    var_0 = module_0.unique(tuple_0, str_0)

def test_case_2():
    str_0 = '5aq^]P^54EjZ\\Fc\\'
    set_0 = {str_0, str_0}
    var_0 = module_0.intersect(str_0, str_0, set_0)

def test_case_3():
    dict_0 = {}
    list_0 = [dict_0]
    list_1 = []
    var_0 = module_0.difference(dict_0, list_0, list_1)

def test_case_4():
    float_0 = -2666.0
    list_0 = [float_0, float_0]
    list_1 = [list_0, float_0, float_0, list_0]
    var_0 = module_0.symmetric_difference(float_0, list_0, list_1)

def test_case_5():
    bytes_0 = b'\x92iv\x9a"\x01\x80\x8dE\x85\x06\xec\x9e'
    list_0 = [bytes_0, bytes_0]
    var_0 = module_0.max(bytes_0, list_0)

def test_case_6():
    filter_module_0 = module_0.FilterModule()
    var_0 = filter_module_0.filters()

def test_case_7():
    str_0 = ' Test ansible.utils.min'
    set_0 = set()
    list_0 = [str_0, str_0, set_0]
    var_0 = module_0.unique(set_0, list_0)

def test_case_8():
    float_0 = None
    list_0 = []
    bytes_0 = b'\xd1\xcbe+\xda_,\x0e\xbdM\xb7\xdc'
    var_0 = module_0.difference(float_0, list_0, bytes_0)
    filter_module_0 = module_0.FilterModule()
    str_0 = '/%'
    list_1 = []
    var_1 = module_0.difference(str_0, list_1, list_1)
    var_2 = filter_module_0.filters()
    list_2 = []
    dict_0 = {str_0: list_1}
    var_3 = module_0.rekey_on_member(list_2, dict_0)

def test_case_9():
    str_0 = '$<\n@p}#xEau-Ic'
    dict_0 = {str_0: str_0}
    var_0 = module_0.intersect(dict_0, dict_0, dict_0)
    filter_module_0 = module_0.FilterModule()

def test_case_10():
    float_0 = 2.0
    var_0 = module_0.logarithm(float_0)
    int_0 = 100
    int_1 = 10
    var_1 = module_0.logarithm(int_0, int_1)