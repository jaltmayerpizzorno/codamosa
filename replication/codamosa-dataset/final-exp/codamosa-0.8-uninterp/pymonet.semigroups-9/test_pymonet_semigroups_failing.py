# Automatically generated by Pynguin.
import pymonet.semigroups as module_0

def test_case_0():
    try:
        last_0 = None
        list_0 = []
        first_0 = module_0.First(list_0)
        semigroup_0 = module_0.Semigroup(first_0)
        bool_0 = semigroup_0.__eq__(last_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = False
        first_0 = None
        tuple_0 = (first_0,)
        max_0 = module_0.Max(tuple_0)
        str_0 = max_0.__str__()
        semigroup_0 = module_0.Semigroup(bool_0)
        var_0 = semigroup_0.fold(semigroup_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'xH<\\A/8ehmTA9T}opJ'
        str_1 = '\n        Take mapper function and return value of Left.\n\n        :returns: Stored value\n        :rtype: A\n        '
        int_0 = 2245
        str_2 = 'afI\\w[mAo;q22[9Qb+'
        bool_0 = True
        first_0 = module_0.First(bool_0)
        var_0 = first_0.concat(str_2)
        first_1 = module_0.First(int_0)
        bool_1 = True
        semigroup_0 = module_0.Semigroup(bool_1)
        var_1 = first_1.concat(semigroup_0)
        var_2 = first_1.concat(str_1)
        last_0 = module_0.Last(str_0)
        str_3 = first_1.__str__()
        str_4 = last_0.__str__()
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'V~^n\nw=zw5n_&W'
        max_0 = module_0.Max(str_0)
        first_0 = module_0.First(max_0)
        float_0 = 2674.0
        map_0 = module_0.Map(float_0)
        var_0 = map_0.concat(first_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '\n        Return monad value when is successfully.\n        Othercase return default_value argument.\n\n        :params default_value: value to return when monad is not successfully.\n        :type default_value: B\n        :returns: monad value\n        :rtype: A | B\n        '
        dict_0 = {str_0: str_0}
        map_0 = module_0.Map(dict_0)
        float_0 = -4681.93139
        set_0 = {str_0}
        last_0 = module_0.Last(set_0)
        all_0 = module_0.All(last_0)
        last_1 = module_0.Last(all_0)
        str_1 = last_1.__str__()
        map_1 = module_0.Map(float_0)
        max_0 = module_0.Max(map_0)
        semigroup_0 = module_0.Semigroup(float_0)
        sum_0 = module_0.Sum(semigroup_0)
        var_0 = map_0.concat(sum_0)
    except BaseException:
        pass