# Automatically generated by Pynguin.
import string_utils.generation as module_0

def test_case_0():
    try:
        int_0 = -1513
        str_0 = module_0.random_string(int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = -539
        str_0 = module_0.secure_random_hex(int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = 1281
        generator_0 = module_0.roman_range(int_0, int_0)
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = 8
        int_1 = -185
        generator_0 = module_0.roman_range(int_0, int_1)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = None
        int_1 = 3621
        generator_0 = module_0.roman_range(int_0, int_1)
    except BaseException:
        pass

def test_case_5():
    try:
        bool_0 = False
        int_0 = 1156
        generator_0 = module_0.roman_range(int_0)
        str_0 = module_0.uuid(bool_0)
        int_1 = None
        str_1 = module_0.random_string(int_1)
    except BaseException:
        pass

def test_case_6():
    try:
        int_0 = 485
        str_0 = module_0.secure_random_hex(int_0)
        str_1 = module_0.uuid()
        str_2 = module_0.uuid()
        int_1 = None
        str_3 = module_0.secure_random_hex(int_1)
    except BaseException:
        pass

def test_case_7():
    try:
        int_0 = 688
        int_1 = 1281
        generator_0 = module_0.roman_range(int_0, int_1)
    except BaseException:
        pass

def test_case_8():
    try:
        int_0 = 4260
        int_1 = 159
        generator_0 = module_0.roman_range(int_0, int_1)
    except BaseException:
        pass

def test_case_9():
    try:
        int_0 = 7
        generator_0 = module_0.roman_range(int_0)
        var_0 = list(generator_0)
        int_1 = 2
        generator_1 = module_0.roman_range(int_0, int_1)
        var_1 = list(generator_1)
        int_2 = 18
        int_3 = -4
        generator_2 = module_0.roman_range(int_2, int_0, int_3)
    except BaseException:
        pass