# Automatically generated by Pynguin.
import pymonet.semigroups as module_0

def test_case_0():
    pass

def test_case_1():
    dict_0 = {}
    semigroup_0 = module_0.Semigroup(dict_0)

def test_case_2():
    str_0 = '\n    Min is a Monoid that will combines 2 numbers, resulting in the smallest of the two.\n    '
    sum_0 = module_0.Sum(str_0)
    str_1 = sum_0.__str__()

def test_case_3():
    int_0 = 790
    all_0 = module_0.All(int_0)
    int_1 = 3056
    float_0 = -1144.6143
    sum_0 = module_0.Sum(float_0)
    str_0 = all_0.__str__()
    sum_1 = module_0.Sum(int_1)
    all_1 = all_0.concat(all_0)
    sum_2 = sum_0.concat(sum_0)
    str_1 = all_1.__str__()
    float_1 = 267.82332
    set_0 = {float_1, float_1, float_1}
    one_0 = module_0.One(set_0)
    int_2 = -40
    sum_3 = sum_1.concat(sum_1)
    semigroup_0 = module_0.Semigroup(int_2)
    one_1 = module_0.One(one_0)
    bool_0 = False
    first_0 = module_0.First(bool_0)
    str_2 = first_0.__str__()
    all_2 = module_0.All(one_1)
    all_3 = all_2.concat(all_2)
    str_3 = all_3.__str__()

def test_case_4():
    str_0 = 'a'
    str_1 = 'b'
    int_0 = 1
    sum_0 = module_0.Sum(int_0)
    bool_0 = True
    all_0 = module_0.All(bool_0)
    var_0 = {str_0: sum_0, str_1: all_0}
    map_0 = module_0.Map(var_0)
    str_2 = 'c'
    bool_1 = True
    all_1 = module_0.All(bool_1)
    bool_2 = False
    one_0 = module_0.One(bool_2)
    var_1 = {str_0: sum_0, str_1: all_1, str_2: one_0}
    map_1 = module_0.Map(var_1)
    var_2 = map_0.concat(map_1)
    int_1 = 3
    sum_1 = module_0.Sum(int_1)
    bool_3 = True
    all_2 = module_0.All(bool_3)
    one_1 = module_0.One(bool_2)
    map_2 = module_0.Map(str_1)

def test_case_5():
    dict_0 = {}
    float_0 = 2043.519
    min_0 = module_0.Min(float_0)
    float_1 = -3948.409
    min_1 = module_0.Min(float_1)
    var_0 = min_1.concat(min_0)
    float_2 = 2761.71
    max_0 = module_0.Max(float_2)
    str_0 = max_0.__str__()
    first_0 = module_0.First(float_1)
    str_1 = first_0.__str__()
    set_0 = None
    one_0 = module_0.One(set_0)
    one_1 = module_0.One(max_0)
    var_1 = one_1.concat(dict_0)
    str_2 = one_1.__str__()
    bool_0 = False
    all_0 = module_0.All(bool_0)
    str_3 = all_0.__str__()
    bytes_0 = b'&\xed\r1\xad\x1c\x9au\x82/\x1e\xff'
    semigroup_0 = module_0.Semigroup(bytes_0)
    all_1 = module_0.All(semigroup_0)
    var_2 = max_0.concat(first_0)

def test_case_6():
    set_0 = set()
    max_0 = module_0.Max(set_0)
    all_0 = module_0.All(max_0)
    min_0 = None
    int_0 = True
    sum_0 = None
    one_0 = module_0.One(sum_0)
    map_0 = module_0.Map(one_0)
    first_0 = module_0.First(max_0)
    str_0 = first_0.__str__()
    one_1 = module_0.One(map_0)
    sum_1 = module_0.Sum(one_1)
    min_1 = module_0.Min(int_0)
    first_1 = module_0.First(min_1)
    var_0 = first_1.concat(min_0)
    bytes_0 = b'\x87[\xca`\xb1\x7f>v0\xe2)\x0bp\xb3'
    str_1 = map_0.__str__()
    var_1 = first_1.concat(bytes_0)
    map_1 = module_0.Map(all_0)

def test_case_7():
    int_0 = 573
    last_0 = module_0.Last(int_0)
    map_0 = module_0.Map(last_0)
    first_0 = module_0.First(map_0)
    max_0 = module_0.Max(last_0)
    var_0 = first_0.concat(max_0)

def test_case_8():
    float_0 = 2043.519
    min_0 = module_0.Min(float_0)
    float_1 = -3948.409
    min_1 = module_0.Min(float_1)
    var_0 = min_1.concat(min_0)
    bool_0 = False
    semigroup_0 = module_0.Semigroup(bool_0)
    last_0 = module_0.Last(semigroup_0)
    sum_0 = module_0.Sum(last_0)
    float_2 = 2761.71
    max_0 = module_0.Max(float_2)
    str_0 = max_0.__str__()
    str_1 = max_0.__str__()
    var_1 = max_0.concat(max_0)
    str_2 = sum_0.__str__()

def test_case_9():
    str_0 = 'huMB9t#v#J"9^J!i('
    map_0 = module_0.Map(str_0)
    str_1 = map_0.__str__()
    list_0 = [map_0]
    first_0 = module_0.First(list_0)
    semigroup_0 = module_0.Semigroup(first_0)

def test_case_10():
    float_0 = 2043.519
    min_0 = module_0.Min(float_0)
    var_0 = min_0.concat(min_0)
    float_1 = 2761.71
    max_0 = module_0.Max(float_1)
    str_0 = max_0.__str__()
    str_1 = max_0.__str__()
    var_1 = max_0.concat(max_0)

def test_case_11():
    int_0 = 2
    min_0 = module_0.Min(int_0)
    int_1 = 1
    min_1 = module_0.Min(int_1)
    var_0 = min_0.concat(min_1)
    min_2 = module_0.Min(int_1)

def test_case_12():
    int_0 = 2
    min_0 = module_0.Min(int_0)
    int_1 = 1
    min_1 = module_0.Min(int_1)
    var_0 = min_0.concat(min_1)
    var_1 = min_0.concat(min_0)
    list_0 = [var_1, var_0, min_0, int_1]
    min_2 = module_0.Min(list_0)

def test_case_13():
    dict_0 = {}
    float_0 = 2043.519
    min_0 = module_0.Min(float_0)
    float_1 = -3948.409
    min_1 = module_0.Min(float_1)
    var_0 = min_1.concat(min_0)
    bool_0 = False
    semigroup_0 = module_0.Semigroup(bool_0)
    last_0 = module_0.Last(semigroup_0)
    sum_0 = module_0.Sum(last_0)
    float_2 = 2761.71
    max_0 = module_0.Max(float_2)
    str_0 = max_0.__str__()
    first_0 = module_0.First(float_1)
    str_1 = first_0.__str__()
    set_0 = None
    one_0 = module_0.One(set_0)
    one_1 = module_0.One(max_0)
    var_1 = one_1.concat(dict_0)
    str_2 = one_1.__str__()
    bool_1 = False
    all_0 = module_0.All(bool_1)
    str_3 = all_0.__str__()
    bool_2 = False
    str_4 = one_1.__str__()
    first_1 = module_0.First(bool_2)
    str_5 = first_1.__str__()
    str_6 = '\n        Returns new ImmutableList with argument value on the begin of list\n        and other list elements after it\n\n        :param new_element: element to append on the begin of list\n        :type fn: A\n        :returns: ImmutableList[A]\n        '
    all_1 = module_0.All(str_6)
    all_2 = all_0.concat(all_0)
    str_7 = all_2.__str__()

def test_case_14():
    str_0 = 'a'
    str_1 = 'b'
    int_0 = 1
    sum_0 = module_0.Sum(int_0)
    sum_1 = module_0.Sum(int_0)
    sum_2 = {str_0: sum_0, str_1: sum_1}
    map_0 = module_0.Map(sum_2)
    sum_3 = module_0.Sum(int_0)
    sum_4 = module_0.Sum(int_0)
    sum_5 = {str_0: sum_3, str_1: sum_4}
    map_1 = module_0.Map(sum_5)
    var_0 = map_0.concat(map_1)
    var_1 = var_0.value
    int_1 = 2
    sum_6 = module_0.Sum(int_1)
    sum_7 = module_0.Sum(int_1)