# Automatically generated by Pynguin.
import string_utils.generation as module_0

def test_case_0():
    try:
        int_0 = 11
        generator_0 = module_0.roman_range(int_0)
        bool_0 = True
        str_0 = module_0.uuid(bool_0)
        str_1 = module_0.uuid()
        int_1 = -3843
        str_2 = module_0.random_string(int_1)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = -2698
        str_0 = module_0.random_string(int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = 971
        str_0 = module_0.random_string(int_0)
        str_1 = module_0.secure_random_hex(int_0)
        str_2 = module_0.uuid()
        int_1 = -4417
        str_3 = module_0.random_string(int_1)
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = -1365
        str_0 = module_0.secure_random_hex(int_0)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = 852
        generator_0 = module_0.roman_range(int_0, int_0, int_0)
    except BaseException:
        pass

def test_case_5():
    try:
        int_0 = -2750
        int_1 = 1754
        generator_0 = module_0.roman_range(int_0, int_1, int_0)
    except BaseException:
        pass

def test_case_6():
    try:
        int_0 = None
        generator_0 = module_0.roman_range(int_0, int_0)
    except BaseException:
        pass

def test_case_7():
    try:
        int_0 = 715
        str_0 = module_0.uuid()
        int_1 = 320
        str_1 = module_0.random_string(int_1)
        generator_0 = module_0.roman_range(int_1)
        generator_1 = module_0.roman_range(int_0)
        generator_2 = module_0.roman_range(int_1)
        int_2 = None
        str_2 = module_0.random_string(int_2)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = module_0.uuid()
        int_0 = None
        str_1 = module_0.secure_random_hex(int_0)
    except BaseException:
        pass

def test_case_9():
    try:
        int_0 = 852
        int_1 = -34
        generator_0 = module_0.roman_range(int_0, int_0, int_1)
    except BaseException:
        pass

def test_case_10():
    try:
        int_0 = 7
        generator_0 = module_0.roman_range(int_0)
        int_1 = 1
        var_0 = list(generator_0)
        int_2 = 8
        generator_1 = module_0.roman_range(int_1, int_2)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = module_0.uuid()
        str_1 = module_0.uuid()
        bool_0 = True
        str_2 = module_0.uuid(bool_0)
        str_3 = module_0.uuid()
        int_0 = 4626
        generator_0 = module_0.roman_range(int_0)
    except BaseException:
        pass

def test_case_12():
    try:
        int_0 = 7
        generator_0 = module_0.roman_range(int_0)
        var_0 = list(generator_0)
        int_1 = 25
        int_2 = -1
        generator_1 = module_0.roman_range(int_1, int_0, int_2)
    except BaseException:
        pass

def test_case_13():
    try:
        int_0 = 2
        generator_0 = module_0.roman_range(int_0)
        var_0 = next(generator_0)
        var_1 = next(generator_0)
        var_2 = next(generator_0)
    except BaseException:
        pass