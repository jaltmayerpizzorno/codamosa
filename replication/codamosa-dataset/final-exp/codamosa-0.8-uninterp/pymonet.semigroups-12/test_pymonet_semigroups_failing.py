# Automatically generated by Pynguin.
import pymonet.semigroups as module_0

def test_case_0():
    try:
        list_0 = []
        str_0 = '\n        Returns failed Validation with None as value and errors list.\n\n        :params errors: list of errors to store\n        :type value: List[E]\n        :returns: Failed Validation\n        :rtype: Validation[None, List[E]]\n        '
        semigroup_0 = module_0.Semigroup(str_0)
        bool_0 = semigroup_0.__eq__(list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'j@w>K9D'
        str_1 = 'W$)lAUt;3'
        set_0 = {str_1, str_0, str_0, str_0}
        max_0 = module_0.Max(set_0)
        str_2 = max_0.__str__()
        list_0 = [str_0, str_0]
        tuple_0 = (list_0,)
        list_1 = []
        semigroup_0 = module_0.Semigroup(list_1)
        var_0 = semigroup_0.fold(tuple_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'{T\xaf\xb9/G'
        sum_0 = module_0.Sum(bytes_0)
        str_0 = sum_0.__str__()
        list_0 = None
        str_1 = 'w!l)EtetyWj|gSg\x0ch$)/'
        min_0 = module_0.Min(str_1)
        var_0 = min_0.concat(list_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '>JI'
        sum_0 = module_0.Sum(str_0)
        bytes_0 = b'\xf1\x12\x9f\xe0I\nrY|A\xcc\xcbk\xb7\xaa\xf3\xe7rt'
        sum_1 = module_0.Sum(bytes_0)
        sum_2 = sum_1.concat(sum_0)
    except BaseException:
        pass

def test_case_4():
    try:
        all_0 = None
        bytes_0 = b'<\x9a\xf4S\xf0\xfa\xcb\x11"r\x94"}\xb7\x0c\x9b\x85'
        all_1 = module_0.All(bytes_0)
        all_2 = all_1.concat(all_0)
    except BaseException:
        pass

def test_case_5():
    try:
        max_0 = None
        str_0 = '\n        :returns: False\n        :rtype: Boolean\n        '
        last_0 = module_0.Last(str_0)
        tuple_0 = (last_0,)
        int_0 = -460
        one_0 = module_0.One(int_0)
        var_0 = one_0.concat(tuple_0)
        str_1 = one_0.__str__()
        semigroup_0 = module_0.Semigroup(last_0)
        min_0 = module_0.Min(semigroup_0)
        var_1 = min_0.concat(max_0)
    except BaseException:
        pass

def test_case_6():
    try:
        last_0 = None
        list_0 = []
        last_1 = module_0.Last(list_0)
        var_0 = last_1.concat(last_0)
    except BaseException:
        pass

def test_case_7():
    try:
        list_0 = []
        list_1 = []
        max_0 = module_0.Max(list_1)
        map_0 = module_0.Map(max_0)
        var_0 = map_0.concat(list_0)
    except BaseException:
        pass

def test_case_8():
    try:
        int_0 = -2524
        max_0 = module_0.Max(int_0)
        list_0 = [int_0]
        all_0 = module_0.All(list_0)
        all_1 = module_0.All(max_0)
        all_2 = all_1.concat(all_0)
        str_0 = all_2.__str__()
        str_1 = '+AF kz*-"\'J3%W&iQ'
        all_3 = module_0.All(str_1)
        all_4 = module_0.All(all_3)
        all_5 = all_4.concat(all_2)
        all_6 = all_5.concat(all_0)
        var_0 = max_0.concat(all_5)
    except BaseException:
        pass