# Automatically generated by Pynguin.
import pymonet.semigroups as module_0

def test_case_0():
    int_0 = -435
    semigroup_0 = module_0.Semigroup(int_0)

def test_case_1():
    int_0 = 1
    min_0 = module_0.Min(int_0)
    int_1 = 2
    min_1 = module_0.Min(int_1)
    var_0 = min_0.concat(min_1)
    min_2 = module_0.Min(int_0)
    var_1 = var_0 == min_2

def test_case_2():
    bool_0 = True
    first_0 = module_0.First(bool_0)
    bytes_0 = b'*'
    last_0 = module_0.Last(bytes_0)
    str_0 = last_0.__str__()
    bool_1 = False
    max_0 = module_0.Max(bool_1)
    var_0 = max_0.concat(max_0)
    str_1 = "|d2O#'D4\t8]nlsQ"
    map_0 = module_0.Map(str_1)
    bool_2 = True
    all_0 = module_0.All(bool_2)
    int_0 = 1209
    sum_0 = module_0.Sum(int_0)
    str_2 = sum_0.__str__()
    all_1 = all_0.concat(all_0)

def test_case_3():
    int_0 = 1
    int_1 = 2
    sum_0 = module_0.Sum(int_0)
    bool_0 = True
    all_0 = module_0.All(bool_0)
    var_0 = {int_0: sum_0, int_1: all_0}
    map_0 = module_0.Map(var_0)
    int_2 = 5
    sum_1 = module_0.Sum(int_2)
    bool_1 = False
    all_1 = module_0.All(bool_1)
    var_1 = {bool_0: sum_1, int_1: all_1}
    map_1 = module_0.Map(var_1)
    var_2 = map_0.concat(map_1)

def test_case_4():
    int_0 = -435
    map_0 = module_0.Map(int_0)
    all_0 = module_0.All(map_0)
    all_1 = all_0.concat(all_0)

def test_case_5():
    dict_0 = {}
    one_0 = module_0.One(dict_0)
    one_1 = module_0.One(one_0)
    last_0 = module_0.Last(one_1)
    int_0 = -435
    map_0 = module_0.Map(int_0)
    all_0 = module_0.All(map_0)
    first_0 = module_0.First(last_0)
    all_1 = all_0.concat(all_0)
    one_2 = module_0.One(last_0)
    first_1 = module_0.First(one_2)
    str_0 = first_1.__str__()

def test_case_6():
    str_0 = '9>;E)Ty\r&4Qgl9\tI(r'
    one_0 = module_0.One(str_0)
    str_1 = one_0.__str__()
    last_0 = module_0.Last(str_0)
    first_0 = module_0.First(one_0)
    str_2 = last_0.__str__()
    map_0 = module_0.Map(last_0)
    str_3 = map_0.__str__()
    var_0 = one_0.concat(map_0)
    str_4 = first_0.__str__()
    str_5 = last_0.__str__()
    int_0 = 1334
    map_1 = module_0.Map(int_0)
    str_6 = 'e:z*a7;o'
    sum_0 = module_0.Sum(str_6)
    all_0 = module_0.All(sum_0)
    all_1 = all_0.concat(all_0)

def test_case_7():
    float_0 = None
    list_0 = [float_0]
    semigroup_0 = module_0.Semigroup(list_0)
    bytes_0 = b'\x17g\xe8\xccU!\xb6!\xfb\x91+\x18\xceh'
    first_0 = module_0.First(bytes_0)
    int_0 = None
    first_1 = module_0.First(int_0)
    var_0 = first_0.concat(semigroup_0)

def test_case_8():
    bool_0 = False
    map_0 = module_0.Map(bool_0)
    bytes_0 = b'u\xc6\x0f}j\xc4H\xe5\xb2\xaa\x14\x96&EM'
    dict_0 = {bytes_0: bytes_0, bytes_0: map_0}
    last_0 = module_0.Last(dict_0)
    one_0 = module_0.One(last_0)
    semigroup_0 = module_0.Semigroup(bytes_0)
    str_0 = last_0.__str__()
    bool_1 = semigroup_0.__eq__(map_0)

def test_case_9():
    float_0 = None
    semigroup_0 = module_0.Semigroup(float_0)
    bool_0 = True
    last_0 = module_0.Last(bool_0)
    last_1 = module_0.Last(last_0)
    var_0 = last_1.concat(semigroup_0)

def test_case_10():
    bool_0 = True
    max_0 = module_0.Max(bool_0)
    max_1 = module_0.Max(bool_0)
    var_0 = max_1.concat(max_0)
    str_0 = "|d2O='D4\t8]nlsQ"
    map_0 = module_0.Map(str_0)
    str_1 = map_0.__str__()

def test_case_11():
    first_0 = None
    tuple_0 = None
    int_0 = True
    list_0 = []
    tuple_1 = (tuple_0, int_0, list_0)
    max_0 = module_0.Max(tuple_1)
    last_0 = module_0.Last(max_0)
    str_0 = last_0.__str__()
    first_1 = module_0.First(first_0)

def test_case_12():
    float_0 = 1332.3752
    bool_0 = False
    max_0 = module_0.Max(bool_0)
    var_0 = max_0.concat(max_0)
    sum_0 = module_0.Sum(float_0)

def test_case_13():
    int_0 = 1
    min_0 = module_0.Min(int_0)
    int_1 = 3
    min_1 = module_0.Min(int_1)
    str_0 = 'min_a='
    var_0 = print(str_0, min_0)
    var_1 = print(str_0, min_1)
    var_2 = min_0.concat(min_1)
    var_3 = print(str_0, var_2)

def test_case_14():
    int_0 = 2
    min_0 = module_0.Min(int_0)
    var_0 = min_0.concat(min_0)
    var_1 = var_0.value

def test_case_15():
    int_0 = 1
    sum_0 = module_0.Sum(int_0)
    bool_0 = True
    all_0 = module_0.All(bool_0)
    var_0 = {int_0: sum_0, int_0: all_0}
    map_0 = module_0.Map(var_0)
    int_1 = 5
    sum_1 = module_0.Sum(int_1)
    bool_1 = False
    all_1 = module_0.All(bool_1)
    var_1 = {bool_0: sum_1, int_1: all_1}
    map_1 = module_0.Map(var_1)
    var_2 = map_0.concat(map_1)

def test_case_16():
    int_0 = 1
    min_0 = module_0.Min(int_0)
    int_1 = 5
    min_1 = module_0.Min(int_1)
    var_0 = min_0.concat(min_1)
    var_1 = var_0.value
    min_2 = module_0.Min(int_1)
    min_3 = module_0.Min(int_0)
    var_2 = min_2.concat(min_3)
    var_3 = var_2.value