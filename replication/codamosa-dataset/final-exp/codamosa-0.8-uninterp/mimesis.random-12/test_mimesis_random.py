# Automatically generated by Pynguin.
import mimesis.random as module_0

def test_case_0():
    random_0 = module_0.Random()

def test_case_1():
    float_0 = 10.0
    float_1 = -548.5939
    random_0 = module_0.Random()
    float_2 = 2.0
    int_0 = 556
    float_3 = random_0.uniform(float_0, float_2, int_0)
    float_4 = random_0.uniform(float_0, float_1)

def test_case_2():
    str_0 = 'ceBdbin4.bg'
    int_0 = 5636
    random_0 = module_0.Random()
    str_1 = random_0.generate_string(str_0, int_0)

def test_case_3():
    bool_0 = False
    str_0 = '4'
    random_0 = module_0.Random()
    int_0 = 1114
    random_1 = module_0.Random()
    float_0 = 1445.0423
    bytes_0 = b'b\xbf2W7\tm\xc4s\x14\x99\xbdy\xcc('
    random_2 = module_0.Random(bytes_0)
    float_1 = -1387.2
    float_2 = random_0.uniform(float_0, float_1)
    str_1 = random_0.randstr(bool_0, int_0)
    str_2 = random_0.custom_code(str_1, str_0)
    str_3 = '6600'
    str_4 = random_2.custom_code(str_3)