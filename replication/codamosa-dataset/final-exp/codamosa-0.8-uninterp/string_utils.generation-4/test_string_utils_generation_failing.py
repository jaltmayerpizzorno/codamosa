# Automatically generated by Pynguin.
import string_utils.generation as module_0

def test_case_0():
    try:
        int_0 = -4435
        generator_0 = module_0.roman_range(int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = None
        str_0 = module_0.random_string(int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = None
        str_0 = module_0.secure_random_hex(int_0)
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = 8
        int_1 = 7
        generator_0 = module_0.roman_range(int_0, int_1)
        var_0 = list(generator_0)
        generator_1 = module_0.roman_range(int_0, int_1, int_0)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = None
        generator_0 = module_0.roman_range(int_0, int_0, int_0)
    except BaseException:
        pass

def test_case_5():
    try:
        int_0 = 2093
        str_0 = module_0.secure_random_hex(int_0)
        int_1 = -1773
        int_2 = 1348
        generator_0 = module_0.roman_range(int_2)
        str_1 = module_0.random_string(int_1)
    except BaseException:
        pass

def test_case_6():
    try:
        int_0 = 3
        generator_0 = module_0.roman_range(int_0)
        var_0 = list(generator_0)
        int_1 = -8
        str_0 = module_0.secure_random_hex(int_1)
    except BaseException:
        pass

def test_case_7():
    try:
        int_0 = 3
        generator_0 = module_0.roman_range(int_0)
        var_0 = list(generator_0)
        int_1 = 36
        int_2 = 13
        generator_1 = module_0.roman_range(int_0, int_1, int_2)
    except BaseException:
        pass

def test_case_8():
    try:
        int_0 = 757
        str_0 = module_0.uuid()
        int_1 = 9
        generator_0 = module_0.roman_range(int_0, int_1)
        int_2 = 5818
        generator_1 = module_0.roman_range(int_2)
    except BaseException:
        pass

def test_case_9():
    try:
        int_0 = 3
        generator_0 = module_0.roman_range(int_0)
        var_0 = list(generator_0)
        int_1 = 11
        int_2 = 7
        generator_1 = module_0.roman_range(int_1, int_2)
        var_1 = list(generator_1)
        int_3 = -1
        generator_2 = module_0.roman_range(int_1, int_2, int_3)
    except BaseException:
        pass

def test_case_10():
    try:
        int_0 = 3
        generator_0 = module_0.roman_range(int_0)
        var_0 = list(generator_0)
        int_1 = 11
        var_1 = list(generator_0)
        int_2 = -1
        generator_1 = module_0.roman_range(int_1, int_1, int_2)
    except BaseException:
        pass