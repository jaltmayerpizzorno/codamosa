# Automatically generated by Pynguin.
import pymonet.semigroups as module_0

def test_case_0():
    try:
        list_0 = None
        float_0 = 1482.0
        semigroup_0 = module_0.Semigroup(float_0)
        bool_0 = semigroup_0.__eq__(list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'\xd1\xc0\x92p'
        float_0 = 185.2651
        map_0 = module_0.Map(float_0)
        list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
        max_0 = module_0.Max(list_0)
        map_1 = module_0.Map(max_0)
        semigroup_0 = module_0.Semigroup(map_1)
        var_0 = semigroup_0.fold(map_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = True
        sum_0 = module_0.Sum(bool_0)
        str_0 = "+'Z*'X!Hi"
        last_0 = module_0.Last(str_0)
        all_0 = module_0.All(last_0)
        sum_1 = module_0.Sum(all_0)
        sum_2 = sum_1.concat(sum_0)
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = 1972
        int_1 = 1387
        tuple_0 = (int_1,)
        first_0 = module_0.First(tuple_0)
        var_0 = first_0.concat(int_0)
        dict_0 = {tuple_0: int_0, int_1: int_1}
        one_0 = module_0.One(dict_0)
        semigroup_0 = module_0.Semigroup(one_0)
        list_0 = []
        str_0 = one_0.__str__()
        map_0 = module_0.Map(list_0)
        var_1 = map_0.concat(semigroup_0)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = 3193
        set_0 = set()
        last_0 = module_0.Last(set_0)
        var_0 = last_0.concat(int_0)
    except BaseException:
        pass

def test_case_5():
    try:
        dict_0 = {}
        float_0 = 2043.904051547627
        min_0 = module_0.Min(float_0)
        float_1 = -3948.409
        min_1 = module_0.Min(float_1)
        var_0 = min_1.concat(min_0)
        first_0 = module_0.First(dict_0)
        sum_0 = module_0.Sum(first_0)
        bool_0 = True
        semigroup_0 = module_0.Semigroup(bool_0)
        last_0 = module_0.Last(semigroup_0)
        str_0 = min_1.__str__()
        sum_1 = module_0.Sum(last_0)
        sum_2 = sum_1.concat(sum_0)
    except BaseException:
        pass

def test_case_6():
    try:
        dict_0 = {}
        float_0 = -3948.409
        min_0 = module_0.Min(float_0)
        var_0 = min_0.concat(min_0)
        bool_0 = False
        semigroup_0 = module_0.Semigroup(bool_0)
        last_0 = module_0.Last(semigroup_0)
        sum_0 = module_0.Sum(last_0)
        float_1 = 2761.71
        max_0 = module_0.Max(float_1)
        str_0 = max_0.__str__()
        first_0 = module_0.First(float_0)
        str_1 = first_0.__str__()
        set_0 = None
        one_0 = module_0.One(set_0)
        one_1 = module_0.One(max_0)
        var_1 = one_1.concat(dict_0)
        str_2 = one_1.__str__()
        list_0 = None
        one_2 = module_0.One(list_0)
        int_0 = -1415
        var_2 = one_0.concat(int_0)
    except BaseException:
        pass