# Automatically generated by Pynguin.
import mimesis.random as module_0

def test_case_0():
    try:
        str_0 = 'kH#a'
        random_0 = module_0.Random()
        str_1 = random_0.custom_code(str_0)
        int_0 = -962
        list_0 = random_0.randints(int_0, int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        random_0 = module_0.Random()
        bytes_0 = random_0.urandom()
    except BaseException:
        pass

def test_case_2():
    try:
        random_0 = module_0.Random()
        str_0 = 'seahorse'
        str_1 = random_0.generate_string(str_0)
        str_2 = None
        str_3 = random_0.custom_code(str_2)
    except BaseException:
        pass

def test_case_3():
    try:
        random_0 = module_0.Random()
        float_0 = None
        int_0 = 1806
        str_0 = random_0.randstr()
        float_1 = random_0.uniform(float_0, float_0, int_0)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = 142
        random_0 = module_0.Random()
        str_0 = '5\r&w%k]A*%'
        str_1 = random_0.generate_string(str_0)
        random_1 = module_0.Random()
        float_0 = 563.48
        float_1 = random_1.uniform(float_0, float_0)
        any_0 = module_0.get_random_item(int_0, random_1)
    except BaseException:
        pass

def test_case_5():
    try:
        int_0 = 202
        random_0 = module_0.Random()
        list_0 = random_0.randints(int_0)
        any_0 = module_0.get_random_item(random_0)
    except BaseException:
        pass

def test_case_6():
    try:
        int_0 = 20
        float_0 = -3309.5073
        any_0 = module_0.get_random_item(int_0, float_0)
    except BaseException:
        pass