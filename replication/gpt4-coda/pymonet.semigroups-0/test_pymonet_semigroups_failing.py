# Automatically generated by Pynguin.
import pymonet.semigroups as module_0

def test_case_0():
    try:
        tuple_0 = ()
        bytes_0 = b'<\x01n\x0b'
        semigroup_0 = module_0.Semigroup(bytes_0)
        bool_0 = semigroup_0.__eq__(tuple_0)
    except BaseException:
        pass

def test_case_1():
    try:
        float_0 = None
        int_0 = 3994
        dict_0 = {float_0: int_0, float_0: int_0}
        max_0 = module_0.Max(dict_0)
        sum_0 = module_0.Sum(max_0)
        one_0 = module_0.One(int_0)
        semigroup_0 = module_0.Semigroup(one_0)
        var_0 = semigroup_0.fold(float_0)
    except BaseException:
        pass

def test_case_2():
    try:
        dict_0 = {}
        sum_0 = module_0.Sum(dict_0)
        last_0 = module_0.Last(sum_0)
        float_0 = 4189.120823
        str_0 = last_0.__str__()
        str_1 = '"fNi<l*"#E\x0c'
        map_0 = module_0.Map(str_1)
        var_0 = map_0.concat(float_0)
    except BaseException:
        pass

def test_case_3():
    try:
        float_0 = -4863.0
        sum_0 = module_0.Sum(float_0)
        sum_1 = sum_0.concat(sum_0)
        first_0 = module_0.First(sum_0)
        str_0 = 'MK7D\n\x0bp6DXo>&'
        semigroup_0 = module_0.Semigroup(str_0)
        bool_0 = semigroup_0.__eq__(first_0)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = -1993
        bool_0 = False
        one_0 = module_0.One(bool_0)
        str_0 = one_0.__str__()
        sum_0 = module_0.Sum(int_0)
        last_0 = module_0.Last(sum_0)
        list_0 = None
        var_0 = last_0.concat(list_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bytes_0 = b'\x19\xecT\xa5\xbe\t\xde\x92\x8a'
        int_0 = True
        dict_0 = {int_0: int_0, int_0: int_0}
        last_0 = module_0.Last(dict_0)
        var_0 = last_0.concat(bytes_0)
    except BaseException:
        pass

def test_case_6():
    try:
        list_0 = None
        list_1 = [list_0]
        map_0 = module_0.Map(list_1)
        last_0 = module_0.Last(map_0)
        semigroup_0 = module_0.Semigroup(last_0)
        str_0 = "gR'z?\r5h6M^s"
        first_0 = module_0.First(str_0)
        min_0 = module_0.Min(first_0)
        min_1 = module_0.Min(min_0)
        one_0 = module_0.One(min_1)
        var_0 = one_0.concat(semigroup_0)
        bytes_0 = b'shK\xb4\x12\x9a\x07\x81\xe5\xe0\x00\x14\xf9\x05\x11\x93\xdf'
        map_1 = module_0.Map(bytes_0)
        str_1 = map_1.__str__()
        str_2 = map_1.__str__()
        str_3 = map_1.__str__()
        bool_0 = True
        var_1 = min_0.concat(bool_0)
    except BaseException:
        pass

def test_case_7():
    try:
        bool_0 = True
        map_0 = module_0.Map(bool_0)
        var_0 = map_0.concat(bool_0)
    except BaseException:
        pass

def test_case_8():
    try:
        float_0 = -897.38
        int_0 = 1722
        one_0 = module_0.One(int_0)
        last_0 = module_0.Last(one_0)
        last_1 = module_0.Last(last_0)
        max_0 = module_0.Max(last_1)
        var_0 = max_0.concat(float_0)
    except BaseException:
        pass

def test_case_9():
    try:
        list_0 = None
        list_1 = [list_0]
        map_0 = module_0.Map(list_1)
        last_0 = module_0.Last(map_0)
        bool_0 = False
        sum_0 = module_0.Sum(bool_0)
        first_0 = module_0.First(sum_0)
        str_0 = first_0.__str__()
        semigroup_0 = module_0.Semigroup(last_0)
        str_1 = "gR'z?\r5h6M^s"
        first_1 = module_0.First(str_1)
        min_0 = module_0.Min(first_1)
        min_1 = module_0.Min(min_0)
        one_0 = module_0.One(min_1)
        var_0 = one_0.concat(semigroup_0)
        bool_1 = True
        var_1 = min_0.concat(bool_1)
    except BaseException:
        pass

def test_case_10():
    try:
        complex_0 = None
        dict_0 = {complex_0: complex_0, complex_0: complex_0, complex_0: complex_0}
        map_0 = module_0.Map(dict_0)
        bytes_0 = b'\xf7\xc1s\xca\x1eQ\xd1MW\xd9\x06F\x0em'
        var_0 = map_0.concat(bytes_0)
    except BaseException:
        pass

def test_case_11():
    try:
        float_0 = 1241.7081
        max_0 = module_0.Max(float_0)
        semigroup_0 = module_0.Semigroup(max_0)
        bool_0 = True
        all_0 = module_0.All(bool_0)
        map_0 = module_0.Map(all_0)
        str_0 = map_0.__str__()
        list_0 = []
        map_1 = module_0.Map(list_0)
        str_1 = all_0.__str__()
        bytes_0 = b'\xf4 \x87!)\xa6u\x93\xe3\xd5BAzp\x08'
        last_0 = module_0.Last(bytes_0)
        var_0 = max_0.concat(max_0)
    except BaseException:
        pass

def test_case_12():
    try:
        bool_0 = True
        map_0 = module_0.Map(bool_0)
        min_0 = module_0.Min(map_0)
        last_0 = module_0.Last(min_0)
        first_0 = module_0.First(last_0)
        complex_0 = None
        last_1 = module_0.Last(complex_0)
        all_0 = module_0.All(last_1)
        bool_1 = False
        all_1 = module_0.All(bool_1)
        all_2 = all_1.concat(all_0)
        float_0 = 2003.132
        min_1 = module_0.Min(float_0)
        str_0 = last_1.__str__()
        all_3 = module_0.All(min_1)
        str_1 = 'MK7D\n\x0bp6DXo>&'
        max_0 = module_0.Max(str_1)
        all_4 = module_0.All(max_0)
        all_5 = all_4.concat(all_3)
        all_6 = all_5.concat(all_2)
        str_2 = 'E/-\x0c7 V)I'
        sum_0 = module_0.Sum(str_2)
        map_1 = module_0.Map(sum_0)
        var_0 = map_1.concat(last_1)
    except BaseException:
        pass