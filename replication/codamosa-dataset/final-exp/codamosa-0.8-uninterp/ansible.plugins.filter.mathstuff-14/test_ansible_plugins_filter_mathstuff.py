# Automatically generated by Pynguin.
import ansible.plugins.filter.mathstuff as module_0
import ansible.utils.display as module_1

def test_case_0():
    filter_module_0 = module_0.FilterModule()

def test_case_1():
    set_0 = set()
    str_0 = ' p4Uyh'
    var_0 = module_0.unique(set_0, str_0)

def test_case_2():
    display_0 = module_1.Display()
    list_0 = [display_0, display_0]
    var_0 = module_0.intersect(display_0, list_0, list_0)

def test_case_3():
    float_0 = 2.718281828459045
    list_0 = [float_0]
    var_0 = module_0.symmetric_difference(float_0, list_0, list_0)

def test_case_4():
    str_0 = ''
    list_0 = [str_0]
    list_1 = [list_0, list_0, str_0]
    var_0 = module_0.union(str_0, list_0, list_1)

def test_case_5():
    filter_module_0 = module_0.FilterModule()
    var_0 = filter_module_0.filters()

def test_case_6():
    int_0 = 1
    str_0 = 'z'
    str_1 = 'overwrite'
    var_0 = dict(z=int_0)
    var_1 = dict(z=int_0)
    var_2 = [var_1, var_1]
    var_3 = module_0.rekey_on_member(var_2, str_0, str_1)