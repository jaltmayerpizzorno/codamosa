# Automatically generated by Pynguin.
import mimesis.random as module_0

def test_case_0():
    random_0 = module_0.Random()

def test_case_1():
    random_0 = module_0.Random()
    list_0 = random_0.randints()

def test_case_2():
    str_0 = None
    int_0 = -364
    random_0 = module_0.Random()
    str_1 = random_0.generate_string(str_0, int_0)

def test_case_3():
    random_0 = module_0.Random()
    str_0 = random_0.custom_code()

def test_case_4():
    str_0 = 'JPQ[r5f-<`3m'
    random_0 = module_0.Random()
    str_1 = random_0.generate_string(str_0)
    str_2 = 'H?VF)20'
    str_3 = random_0.custom_code(str_2)

def test_case_5():
    float_0 = -1253.947382
    random_0 = module_0.Random()
    float_1 = random_0.uniform(float_0, float_0)
    random_1 = module_0.Random()
    str_0 = random_1.randstr()

def test_case_6():
    bool_0 = False
    random_0 = module_0.Random()
    str_0 = random_0.randstr(bool_0)
    int_0 = 416
    int_1 = 3536
    list_0 = random_0.randints(int_0, int_1)