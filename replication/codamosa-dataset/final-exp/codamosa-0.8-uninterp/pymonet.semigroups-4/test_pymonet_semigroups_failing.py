# Automatically generated by Pynguin.
import pymonet.semigroups as module_0

def test_case_0():
    try:
        float_0 = 898.21838
        dict_0 = {}
        semigroup_0 = module_0.Semigroup(dict_0)
        var_0 = semigroup_0.fold(float_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = None
        list_0 = [bool_0, bool_0]
        last_0 = module_0.Last(list_0)
        str_0 = last_0.__str__()
        str_1 = '\n        :param constructor_fn: function to call during fold method call\n        :type constructor_fn: Function() -> A\n        '
        sum_0 = module_0.Sum(str_1)
        list_1 = []
        first_0 = module_0.First(list_1)
        int_0 = 2350
        var_0 = first_0.concat(int_0)
        sum_1 = module_0.Sum(first_0)
        sum_2 = sum_1.concat(sum_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = None
        last_0 = module_0.Last(int_0)
        semigroup_0 = module_0.Semigroup(last_0)
        min_0 = module_0.Min(semigroup_0)
        semigroup_1 = module_0.Semigroup(min_0)
        all_0 = module_0.All(semigroup_1)
        float_0 = 2800.79
        all_1 = all_0.concat(all_0)
        first_0 = module_0.First(all_1)
        var_0 = last_0.concat(first_0)
        all_2 = module_0.All(float_0)
        list_0 = [float_0]
        sum_0 = module_0.Sum(list_0)
        one_0 = None
        var_1 = min_0.concat(one_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = b'\xaf\xd8(\xf1s\xec\xe3xV\x0b\xaf:\x1e\xc5\x07\xda\xc2'
        map_0 = module_0.Map(bytes_0)
        str_0 = map_0.__str__()
    except BaseException:
        pass

def test_case_4():
    try:
        float_0 = 572.181
        map_0 = module_0.Map(float_0)
        str_0 = map_0.__str__()
        min_0 = module_0.Min(map_0)
        one_0 = module_0.One(map_0)
        bytes_0 = b'e\xf6If*\xd7\x08\xc9\xafpl%\x98\xcb\xb4'
        str_1 = map_0.__str__()
        max_0 = module_0.Max(bytes_0)
        var_0 = map_0.concat(max_0)
    except BaseException:
        pass

def test_case_5():
    try:
        float_0 = -1774.8
        first_0 = module_0.First(float_0)
        str_0 = 'hA6o&.GT'
        bool_0 = True
        one_0 = module_0.One(bool_0)
        str_1 = one_0.__str__()
        max_0 = module_0.Max(str_0)
        str_2 = max_0.__str__()
        float_1 = 2580.9045
        var_0 = first_0.concat(float_1)
        sum_0 = None
        float_2 = -810.36329
        semigroup_0 = module_0.Semigroup(float_2)
        var_1 = semigroup_0.fold(sum_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'qB6\x0czH[\tqhxab972<Ki'
        semigroup_0 = module_0.Semigroup(str_0)
        all_0 = module_0.All(str_0)
        str_1 = '\\Ue\\N54m/m4'
        all_1 = module_0.All(str_1)
        all_2 = all_1.concat(all_0)
        bool_0 = semigroup_0.__eq__(all_2)
        str_2 = '_sPxNvx)[yk|ETll]'
        min_0 = module_0.Min(str_2)
        var_0 = min_0.concat(semigroup_0)
        str_3 = ''
        one_0 = module_0.One(str_3)
        str_4 = one_0.__str__()
        int_0 = 3518
        map_0 = module_0.Map(int_0)
        map_1 = module_0.Map(map_0)
        str_5 = map_1.__str__()
        bool_1 = False
        sum_0 = None
        set_0 = {sum_0, bool_1}
        var_1 = one_0.concat(set_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = '1~uVB\tflHPjr\\pY`l'
        dict_0 = {str_0: str_0}
        map_0 = module_0.Map(dict_0)
        first_0 = module_0.First(map_0)
        set_0 = {str_0, str_0}
        str_1 = map_0.__str__()
        str_2 = 'FS[C>8B'
        first_1 = None
        float_0 = -2134.8
        tuple_0 = (set_0, str_2, first_1, float_0)
        one_0 = module_0.One(set_0)
        var_0 = map_0.concat(tuple_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = '1~uVB\tflHPjr\\pY`l'
        dict_0 = {}
        map_0 = module_0.Map(dict_0)
        first_0 = module_0.First(map_0)
        set_0 = {str_0, str_0}
        str_1 = first_0.__str__()
        str_2 = map_0.__str__()
        var_0 = map_0.concat(set_0)
        str_3 = 'FS[C>8B'
        first_1 = None
        bool_0 = False
        var_1 = map_0.concat(bool_0)
        float_0 = -2134.8
        tuple_0 = (set_0, str_3, first_1, float_0)
        one_0 = module_0.One(set_0)
        var_2 = map_0.concat(tuple_0)
        str_4 = one_0.__str__()
        max_0 = module_0.Max(tuple_0)
        var_3 = max_0.concat(first_0)
    except BaseException:
        pass