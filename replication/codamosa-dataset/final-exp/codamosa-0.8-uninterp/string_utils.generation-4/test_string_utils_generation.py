# Automatically generated by Pynguin.
import string_utils.generation as module_0

def test_case_0():
    str_0 = module_0.uuid()
    str_1 = module_0.uuid()

def test_case_1():
    bool_0 = True
    str_0 = module_0.uuid(bool_0)

def test_case_2():
    int_0 = 11
    str_0 = module_0.random_string(int_0)

def test_case_3():
    int_0 = 2864
    str_0 = module_0.secure_random_hex(int_0)

def test_case_4():
    int_0 = 473
    generator_0 = module_0.roman_range(int_0)

def test_case_5():
    int_0 = 6
    int_1 = 1
    int_2 = -1
    generator_0 = module_0.roman_range(int_1, int_0, int_2)
    var_0 = list(generator_0)

def test_case_6():
    int_0 = 4
    int_1 = 7
    generator_0 = module_0.roman_range(int_1, int_0)
    var_0 = [n for n in generator_0]