# Automatically generated by Pynguin.
import pymonet.semigroups as module_0

def test_case_0():
    pass

def test_case_1():
    int_0 = 2
    min_0 = module_0.Min(int_0)

def test_case_2():
    set_0 = set()
    bool_0 = True
    first_0 = module_0.First(bool_0)
    bool_1 = True
    max_0 = module_0.Max(bool_1)
    one_0 = module_0.One(max_0)
    int_0 = True
    last_0 = module_0.Last(int_0)
    all_0 = module_0.All(first_0)
    map_0 = module_0.Map(all_0)
    str_0 = map_0.__str__()
    one_1 = module_0.One(last_0)
    map_1 = module_0.Map(one_1)
    float_0 = -1711.72
    var_0 = first_0.concat(float_0)
    one_2 = module_0.One(map_1)
    str_1 = max_0.__str__()
    tuple_0 = (last_0, one_2)
    one_3 = module_0.One(tuple_0)
    var_1 = one_3.concat(one_0)
    sum_0 = module_0.Sum(last_0)
    sum_1 = module_0.Sum(sum_0)
    var_2 = last_0.concat(sum_1)
    str_2 = ''
    one_4 = module_0.One(str_2)
    str_3 = one_4.__str__()
    var_3 = one_4.concat(first_0)
    first_1 = module_0.First(set_0)
    str_4 = sum_0.__str__()
    var_4 = one_0.concat(set_0)
    str_5 = one_1.__str__()
    var_5 = one_3.concat(max_0)

def test_case_3():
    str_0 = 'rK59.|jbr-oay\n'
    int_0 = -540
    all_0 = module_0.All(int_0)
    str_1 = all_0.__str__()
    list_0 = [all_0, int_0, int_0, str_0]
    sum_0 = module_0.Sum(list_0)
    semigroup_0 = module_0.Semigroup(sum_0)
    min_0 = module_0.Min(semigroup_0)
    last_0 = module_0.Last(min_0)
    map_0 = module_0.Map(str_0)
    str_2 = map_0.__str__()

def test_case_4():
    str_0 = 'cH'
    one_0 = module_0.One(str_0)
    all_0 = module_0.All(one_0)
    str_1 = '=rtSLnQR~'
    dict_0 = {str_1: str_1, str_1: str_1, str_1: str_1}
    all_1 = module_0.All(dict_0)
    all_2 = all_1.concat(all_0)
    float_0 = 279.9
    first_0 = module_0.First(float_0)
    first_1 = module_0.First(first_0)
    str_2 = first_1.__str__()

def test_case_5():
    complex_0 = None
    one_0 = module_0.One(complex_0)
    str_0 = one_0.__str__()
    first_0 = module_0.First(one_0)

def test_case_6():
    bytes_0 = b'\x14\xb1\xd8\x89?\xad\xbc\x84\x0e&'
    sum_0 = module_0.Sum(bytes_0)
    last_0 = module_0.Last(sum_0)
    str_0 = '!Ty`rqu;%\x0c?D=W/a<w,x'
    semigroup_0 = module_0.Semigroup(str_0)
    one_0 = module_0.One(semigroup_0)
    one_1 = module_0.One(one_0)
    var_0 = one_1.concat(last_0)

def test_case_7():
    dict_0 = {}
    map_0 = module_0.Map(dict_0)
    bytes_0 = b'(\x8e\xea]Q'
    min_0 = module_0.Min(bytes_0)
    bytes_1 = b"'\xc5"
    max_0 = module_0.Max(bytes_1)
    var_0 = max_0.concat(min_0)
    map_1 = module_0.Map(map_0)
    last_0 = module_0.Last(map_1)
    str_0 = last_0.__str__()

def test_case_8():
    int_0 = 3
    min_0 = module_0.Min(int_0)
    int_1 = 4
    min_1 = module_0.Min(int_1)
    var_0 = min_0.concat(min_1)
    min_2 = module_0.Min(int_0)
    min_3 = module_0.Min(int_1)
    min_4 = module_0.Min(int_0)
    str_0 = min_1.__str__()
    var_1 = min_3.concat(min_4)
    min_5 = module_0.Min(int_0)
    min_6 = module_0.Min(int_1)
    min_7 = module_0.Min(int_1)
    var_2 = min_6.concat(min_7)
    min_8 = module_0.Min(int_1)

def test_case_9():
    int_0 = 1
    min_0 = module_0.Min(int_0)
    int_1 = 2
    min_1 = module_0.Min(int_1)
    var_0 = min_0.concat(min_1)

def test_case_10():
    str_0 = '@0aD4}K'
    first_0 = module_0.First(str_0)
    dict_0 = {}
    map_0 = module_0.Map(dict_0)
    bytes_0 = b'(\x8e\xea]Q'
    min_0 = module_0.Min(bytes_0)
    bytes_1 = b'\xc5'
    max_0 = module_0.Max(bytes_1)
    var_0 = max_0.concat(min_0)
    last_0 = module_0.Last(map_0)
    str_1 = last_0.__str__()

def test_case_11():
    str_0 = '@0aD4}K'
    first_0 = module_0.First(str_0)
    dict_0 = {}
    map_0 = module_0.Map(dict_0)
    bytes_0 = b'(\x8e\xea]Q'
    min_0 = module_0.Min(bytes_0)
    bytes_1 = b'\xc5'
    max_0 = module_0.Max(bytes_1)
    var_0 = max_0.concat(min_0)
    map_1 = module_0.Map(map_0)
    list_0 = [str_0, map_0, var_0]
    var_1 = map_0.concat(list_0)
    last_0 = module_0.Last(map_1)
    str_1 = last_0.__str__()