# Automatically generated by Pynguin.
import mimesis.random as module_0

def test_case_0():
    try:
        random_0 = module_0.Random()
        bytes_0 = b'\x8d\xcby'
        random_1 = module_0.Random()
        any_0 = module_0.get_random_item(bytes_0)
        int_0 = 3117
        str_0 = random_1.randstr(int_0)
        int_1 = -644
        list_0 = random_1.randints(int_1)
    except BaseException:
        pass

def test_case_1():
    try:
        dict_0 = {}
        bool_0 = False
        random_0 = module_0.Random(bool_0)
        bytes_0 = random_0.urandom(**dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        random_0 = module_0.Random()
        str_0 = random_0.randstr()
        any_0 = module_0.get_random_item(str_0)
        bool_0 = True
        int_0 = None
        str_1 = random_0.randstr(bool_0, int_0)
        bytes_0 = random_0.urandom()
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = ' \x0bm'
        tuple_0 = None
        random_0 = module_0.Random(tuple_0)
        any_0 = module_0.get_random_item(str_0, random_0)
        dict_0 = {str_0: str_0, str_0: any_0}
        bytes_0 = random_0.urandom(**dict_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bytes_0 = b'\xeeX\xab\x16T\x8eN\xe8P\xf7;\xd7'
        any_0 = module_0.get_random_item(bytes_0)
        set_0 = {bytes_0}
        random_0 = module_0.Random(set_0)
    except BaseException:
        pass

def test_case_5():
    try:
        random_0 = module_0.Random()
        bool_0 = True
        str_0 = random_0.randstr(bool_0)
        random_1 = module_0.Random()
        random_2 = module_0.Random()
        bool_1 = False
        str_1 = random_2.randstr(bool_1, random_0)
    except BaseException:
        pass

def test_case_6():
    try:
        random_0 = module_0.Random()
        str_0 = random_0.custom_code()
        str_1 = 'AA#'
        var_0 = [c.isupper() or c.isdigit() for c in str_0]
        var_1 = all(var_0)
        any_0 = module_0.get_random_item(str_1)
        bytes_0 = b'B\xac\xe7\x08\xb5{\xa2\xc1"\t\xc7c\xf9\xda\x0f;Ub\xef\xa9'
        random_1 = module_0.Random(bytes_0)
        str_2 = 'A'
        str_3 = 'YC\x0bat0E'
        int_0 = -998
        str_4 = random_1.generate_string(str_3, int_0)
        str_5 = random_0.custom_code(str_1, str_2, str_2)
    except BaseException:
        pass