# Automatically generated by Pynguin.
import string_utils.generation as module_0

def test_case_0():
    int_0 = 167
    str_0 = module_0.secure_random_hex(int_0)

def test_case_1():
    str_0 = module_0.uuid()
    str_1 = module_0.uuid()
    str_2 = module_0.uuid()
    str_3 = module_0.uuid()

def test_case_2():
    int_0 = 2
    generator_0 = module_0.roman_range(int_0)
    var_0 = next(generator_0)