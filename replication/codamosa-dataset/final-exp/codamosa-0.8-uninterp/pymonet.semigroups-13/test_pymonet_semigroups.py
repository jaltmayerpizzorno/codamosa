# Automatically generated by Pynguin.
import pymonet.semigroups as module_0

def test_case_0():
    bytes_0 = b'J\xfe\x9c{P\x03R\xea'
    sum_0 = module_0.Sum(bytes_0)

def test_case_1():
    str_0 = 'XtJUH|%5'
    all_0 = module_0.All(str_0)
    str_1 = "['H+3L-C1Wtp$>"
    tuple_0 = ()
    first_0 = module_0.First(tuple_0)
    str_2 = first_0.__str__()
    one_0 = module_0.One(str_1)
    min_0 = module_0.Min(first_0)
    all_1 = all_0.concat(all_0)
    str_3 = one_0.__str__()
    sum_0 = module_0.Sum(all_1)
    sum_1 = module_0.Sum(sum_0)
    max_0 = module_0.Max(sum_1)
    str_4 = max_0.__str__()

def test_case_2():
    bool_0 = False
    min_0 = module_0.Min(bool_0)
    all_0 = module_0.All(min_0)
    str_0 = all_0.__str__()
    dict_0 = None
    max_0 = module_0.Max(dict_0)

def test_case_3():
    bytes_0 = b''
    dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0}
    int_0 = -3054
    min_0 = module_0.Min(int_0)
    one_0 = module_0.One(min_0)
    var_0 = one_0.concat(dict_0)

def test_case_4():
    bytes_0 = b' O\xd7\xbd'
    last_0 = module_0.Last(bytes_0)
    min_0 = module_0.Min(last_0)
    first_0 = module_0.First(min_0)
    str_0 = first_0.__str__()

def test_case_5():
    list_0 = []
    dict_0 = {}
    max_0 = module_0.Max(dict_0)
    str_0 = max_0.__str__()
    map_0 = module_0.Map(list_0)
    str_1 = map_0.__str__()
    str_2 = map_0.__str__()

def test_case_6():
    str_0 = '\n        Transform Maybe to Try.\n\n        :returns: successfully Try with previous value when Maybe is not empty, othercase not successfully Try with None\n        :rtype: Try[A]\n        '
    all_0 = module_0.All(str_0)
    str_1 = '\n        Transform Validation to Try.\n\n        :returns: successfully Try with Validation value value. Try is successful when Validation has no errors\n        :rtype: Try[A]\n        '
    all_1 = module_0.All(str_1)
    bytes_0 = b'2\x839$\xbb\xea\xd8$H\xcdFJ'
    all_2 = module_0.All(bytes_0)
    all_3 = module_0.All(all_2)
    all_4 = module_0.All(all_3)
    list_0 = [all_2, all_3]
    last_0 = module_0.Last(list_0)
    all_5 = module_0.All(last_0)
    bool_0 = False
    all_6 = module_0.All(bool_0)
    all_7 = all_6.concat(all_4)
    all_8 = all_7.concat(all_1)
    all_9 = all_8.concat(all_0)

def test_case_7():
    int_0 = 1
    int_1 = 2
    sum_0 = module_0.Sum(int_0)
    sum_1 = module_0.Sum(int_1)
    sum_2 = {int_0: sum_0, int_1: sum_1}
    map_0 = module_0.Map(sum_2)
    sum_3 = module_0.Sum(int_0)
    sum_4 = module_0.Sum(int_1)
    sum_5 = {int_0: sum_3, int_1: sum_4}
    map_1 = module_0.Map(sum_5)
    var_0 = map_0.concat(map_1)
    sum_6 = module_0.Sum(int_1)
    int_2 = 4
    sum_7 = module_0.Sum(int_2)
    sum_8 = {int_0: sum_6, int_1: sum_7}
    map_2 = module_0.Map(sum_8)

def test_case_8():
    float_0 = 1551.816
    min_0 = module_0.Min(float_0)
    max_0 = module_0.Max(float_0)
    var_0 = max_0.concat(min_0)
    bool_0 = False
    tuple_0 = (bool_0,)
    semigroup_0 = module_0.Semigroup(tuple_0)
    map_0 = module_0.Map(float_0)
    bool_1 = True
    first_0 = module_0.First(bool_1)
    str_0 = first_0.__str__()

def test_case_9():
    int_0 = 2
    max_0 = module_0.Max(int_0)
    int_1 = 1
    max_1 = module_0.Max(int_1)
    var_0 = max_0.concat(max_1)
    var_1 = var_0.value
    int_2 = 10
    max_2 = module_0.Max(int_2)
    int_3 = 11
    max_3 = module_0.Max(int_3)
    var_2 = max_2.concat(max_3)
    var_3 = var_2.value
    int_4 = 100
    max_4 = module_0.Max(int_4)
    max_5 = module_0.Max(int_4)
    var_4 = max_4.concat(max_5)
    var_5 = var_4.value