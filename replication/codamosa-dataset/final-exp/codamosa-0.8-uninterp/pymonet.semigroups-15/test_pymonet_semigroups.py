# Automatically generated by Pynguin.
import pymonet.semigroups as module_0

def test_case_0():
    pass

def test_case_1():
    int_0 = None
    last_0 = module_0.Last(int_0)

def test_case_2():
    set_0 = set()
    max_0 = module_0.Max(set_0)
    first_0 = module_0.First(set_0)
    str_0 = max_0.__str__()
    bool_0 = False
    min_0 = module_0.Min(set_0)
    var_0 = max_0.concat(min_0)
    sum_0 = module_0.Sum(bool_0)
    str_1 = sum_0.__str__()
    sum_1 = module_0.Sum(set_0)
    str_2 = 'q!=<|*_?|^X2SQ'
    map_0 = module_0.Map(str_2)
    sum_2 = sum_0.concat(sum_0)

def test_case_3():
    int_0 = 2585
    sum_0 = module_0.Sum(int_0)
    last_0 = module_0.Last(sum_0)
    bool_0 = True
    set_0 = {bool_0, bool_0, bool_0}
    max_0 = module_0.Max(set_0)
    max_1 = module_0.Max(max_0)
    last_1 = module_0.Last(max_1)
    int_1 = -3316
    tuple_0 = (bool_0, last_1, int_1)
    max_2 = module_0.Max(tuple_0)
    one_0 = module_0.One(max_2)
    var_0 = one_0.concat(last_0)

def test_case_4():
    str_0 = " _5'cWY&uHKTp5"
    first_0 = module_0.First(str_0)
    str_1 = '\n    Perform left-to-right function composition.\n\n    :param value: argument of first applied function\n    :type value: Any\n    :param functions: list of functions to applied from left-to-right\n    :type functions: List[Function]\n    :returns: result of all functions\n    :rtype: Any\n    '
    complex_0 = None
    one_0 = module_0.One(complex_0)
    first_1 = module_0.First(one_0)
    min_0 = module_0.Min(first_1)
    min_1 = module_0.Min(min_0)
    var_0 = first_0.concat(min_1)
    var_1 = first_0.concat(str_1)
    str_2 = first_0.__str__()
    bytes_0 = b'\x1f\xea\xd1\xa8\x00?I`\xc5\x87\xa1U3\xb6('
    last_0 = module_0.Last(first_0)
    map_0 = module_0.Map(last_0)
    str_3 = map_0.__str__()
    min_2 = module_0.Min(bytes_0)

def test_case_5():
    str_0 = 'a'
    int_0 = 1
    sum_0 = module_0.Sum(int_0)
    sum_1 = {str_0: sum_0}
    map_0 = module_0.Map(sum_1)
    int_1 = 2
    sum_2 = module_0.Sum(int_1)
    sum_3 = {str_0: sum_2}
    map_1 = module_0.Map(sum_3)
    var_0 = map_0.concat(map_1)
    int_2 = 3
    sum_4 = module_0.Sum(int_2)
    sum_5 = {str_0: sum_4}
    map_2 = module_0.Map(sum_5)

def test_case_6():
    int_0 = 4
    max_0 = module_0.Max(int_0)
    int_1 = 3
    max_1 = module_0.Max(int_1)
    var_0 = max_0.concat(max_1)
    var_1 = print(var_0)

def test_case_7():
    str_0 = '\tyH}]L9^HW+C#Thlm'
    str_1 = '\n        Transform Validation to Maybe.\n\n        :returns: Maybe with Validation Value when Validation has no errors, in other case empty Maybe\n        :rtype: Maybe[A | None]\n        '
    last_0 = module_0.Last(str_1)
    int_0 = -1689
    one_0 = module_0.One(int_0)
    tuple_0 = (str_0, last_0, one_0)
    max_0 = module_0.Max(tuple_0)
    min_0 = module_0.Min(max_0)
    str_2 = min_0.__str__()

def test_case_8():
    int_0 = 1
    max_0 = module_0.Max(int_0)
    int_1 = 2
    max_1 = module_0.Max(int_1)
    var_0 = max_0.concat(max_1)
    max_2 = module_0.Max(int_1)

def test_case_9():
    bool_0 = False
    set_0 = set()
    max_0 = module_0.Max(set_0)
    first_0 = module_0.First(set_0)
    str_0 = max_0.__str__()
    sum_0 = module_0.Sum(bool_0)
    min_0 = module_0.Min(set_0)
    var_0 = max_0.concat(min_0)
    map_0 = None
    semigroup_0 = module_0.Semigroup(map_0)
    one_0 = module_0.One(sum_0)
    str_1 = one_0.__str__()
    str_2 = one_0.__str__()
    map_1 = module_0.Map(one_0)
    var_1 = min_0.concat(min_0)
    float_0 = -975.0
    max_1 = module_0.Max(float_0)
    sum_1 = sum_0.concat(sum_0)