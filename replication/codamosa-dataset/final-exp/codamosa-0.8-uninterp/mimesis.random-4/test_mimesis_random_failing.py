# Automatically generated by Pynguin.
import mimesis.random as module_0

def test_case_0():
    try:
        random_0 = module_0.Random()
        random_1 = module_0.Random()
        list_0 = random_0.randints()
        any_0 = module_0.get_random_item(random_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = -2069
        random_0 = module_0.Random()
        list_0 = random_0.randints(int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        random_0 = module_0.Random()
        bytes_0 = random_0.urandom()
    except BaseException:
        pass

def test_case_3():
    try:
        random_0 = module_0.Random()
        str_0 = random_0.randstr()
        random_1 = module_0.Random()
        float_0 = 10.0
        float_1 = 547.8
        float_2 = random_1.uniform(float_0, float_1)
        any_0 = module_0.get_random_item(random_1)
    except BaseException:
        pass

def test_case_4():
    try:
        float_0 = 0.0
        int_0 = 1217
        random_0 = module_0.Random()
        int_1 = 306
        list_0 = random_0.randints(int_1)
        str_0 = random_0.randstr()
        str_1 = random_0.randstr(int_0)
        list_1 = random_0.randints()
        any_0 = module_0.get_random_item(float_0, random_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '{l4\x0c =.B!1'
        random_0 = module_0.Random()
        str_1 = random_0.generate_string(str_0)
        str_2 = random_0.generate_string(str_1)
        any_0 = module_0.get_random_item(random_0, random_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '/;y'
        random_0 = module_0.Random()
        int_0 = 2508
        int_1 = -2424
        list_0 = random_0.randints(int_0, int_1)
        bool_0 = True
        bool_1 = False
        str_1 = random_0.randstr(bool_1, int_1)
        str_2 = random_0.generate_string(str_0)
        random_1 = module_0.Random(bool_0)
        str_3 = random_1.randstr()
        list_1 = random_0.randints()
        any_0 = module_0.get_random_item(list_1)
        any_1 = module_0.get_random_item(bool_0, random_1)
    except BaseException:
        pass

def test_case_7():
    try:
        bytes_0 = b'\x99\x0f\xa0'
        str_0 = '.Qw&,fP)I@kq'
        int_0 = -302
        str_1 = '=HaS"XC\tJ7TY0`'
        str_2 = 'w*'
        any_0 = module_0.get_random_item(bytes_0, str_2)
        random_0 = module_0.Random()
        str_3 = random_0.custom_code()
        random_1 = module_0.Random(str_1)
        str_4 = random_1.generate_string(str_0, int_0)
        bytes_1 = random_1.urandom()
    except BaseException:
        pass

def test_case_8():
    try:
        random_0 = module_0.Random()
        str_0 = random_0.custom_code()
        str_1 = '@###'
        str_2 = '@'
        str_3 = random_0.custom_code(str_1, str_2)
        str_4 = '@###@'
        str_5 = random_0.custom_code(str_4, str_2)
        str_6 = '@'
        str_7 = random_0.custom_code(str_1, str_6, str_6)
    except BaseException:
        pass