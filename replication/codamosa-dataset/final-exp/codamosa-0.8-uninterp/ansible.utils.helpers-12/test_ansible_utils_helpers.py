# Automatically generated by Pynguin.
import ansible.utils.helpers as module_0

def test_case_0():
    str_0 = '10%'
    int_0 = 100
    var_0 = module_0.pct_to_int(str_0, int_0)
    int_1 = -976
    var_1 = module_0.pct_to_int(str_0, int_1)

def test_case_1():
    str_0 = 'toa5d 8MN\tet-aKi'
    var_0 = module_0.object_to_dict(str_0)

def test_case_2():
    str_0 = '(Iy|3tI:fQMv oZ0U{'
    var_0 = module_0.deduplicate_list(str_0)

def test_case_3():
    int_0 = 5
    int_1 = 200
    var_0 = module_0.pct_to_int(int_0, int_1)
    var_1 = module_0.pct_to_int(int_0, int_1, int_0)
    int_2 = 0
    var_2 = module_0.pct_to_int(int_0, int_2)
    var_3 = module_0.pct_to_int(int_0, int_2, int_0)
    int_3 = 100
    var_4 = module_0.pct_to_int(int_0, int_3)
    var_5 = module_0.pct_to_int(int_0, int_3, int_0)
    str_0 = '5%'
    var_6 = module_0.pct_to_int(str_0, int_3)
    var_7 = module_0.pct_to_int(str_0, int_3, int_0)
    var_8 = module_0.pct_to_int(str_0, int_2)
    var_9 = module_0.pct_to_int(str_0, int_2, int_0)