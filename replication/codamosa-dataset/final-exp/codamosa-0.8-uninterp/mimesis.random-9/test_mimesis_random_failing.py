# Automatically generated by Pynguin.
import mimesis.random as module_0

def test_case_0():
    try:
        tuple_0 = None
        any_0 = module_0.get_random_item(tuple_0)
    except BaseException:
        pass

def test_case_1():
    try:
        float_0 = 3600.0
        float_1 = -2197.8117
        str_0 = 'douping'
        random_0 = module_0.Random()
        str_1 = random_0.custom_code(str_0)
        int_0 = 2630
        random_1 = module_0.Random()
        list_0 = random_1.randints(int_0)
        random_2 = module_0.Random()
        float_2 = random_2.uniform(float_0, float_1)
        str_2 = 'mLg'
        str_3 = '+256'
        str_4 = random_2.generate_string(str_3)
        str_5 = random_2.generate_string(str_2)
        dict_0 = {str_3: str_1}
        random_3 = module_0.Random(dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        random_0 = module_0.Random()
        str_0 = 'T+v_5kbr/6?&z[t\\`{~'
        int_0 = -320
        str_1 = random_0.generate_string(str_0, int_0)
        int_1 = -2737
        list_0 = random_0.randints(int_1)
    except BaseException:
        pass

def test_case_3():
    try:
        random_0 = module_0.Random()
        bytes_0 = random_0.urandom()
    except BaseException:
        pass

def test_case_4():
    try:
        random_0 = module_0.Random()
        str_0 = random_0.randstr()
        int_0 = 32
        list_0 = [int_0, str_0, str_0, random_0]
        list_1 = [random_0, int_0, int_0, list_0]
        bytes_0 = random_0.urandom(*list_1)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '422'
        str_1 = 's}Aj'
        random_0 = module_0.Random(str_0)
        float_0 = 1793.325
        str_2 = random_0.randstr(float_0)
        str_3 = random_0.custom_code(str_1, str_1)
    except BaseException:
        pass

def test_case_6():
    try:
        random_0 = module_0.Random()
        str_0 = None
        bool_0 = None
        int_0 = 6084
        str_1 = random_0.randstr(bool_0, int_0)
        list_0 = random_0.randints()
        str_2 = random_0.generate_string(str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'e'
        str_1 = '5lg'
        any_0 = module_0.get_random_item(str_0, str_1)
        random_0 = module_0.Random()
        str_2 = None
        str_3 = random_0.generate_string(str_2)
    except BaseException:
        pass

def test_case_8():
    try:
        random_0 = module_0.Random()
        str_0 = '@@@@-###-##'
        str_1 = random_0.custom_code(str_0)
        str_2 = 'PRZA-948-83'
        var_0 = str_1 == str_2
        str_3 = '@@@-@@@-####'
        str_4 = random_0.custom_code(str_3)
        str_5 = 'HVV-LWI-4557'
        var_1 = str_4 == str_5
        str_6 = '@##-@##'
        str_7 = random_0.custom_code(str_6)
        str_8 = 'P8O-W3N'
        var_2 = str_7 == str_8
        str_9 = '#'
        str_10 = '!'
        str_11 = random_0.custom_code(str_6, str_10, str_9)
        var_3 = str_11 == str_8
        str_12 = random_0.custom_code(str_6, str_10, str_10)
    except BaseException:
        pass