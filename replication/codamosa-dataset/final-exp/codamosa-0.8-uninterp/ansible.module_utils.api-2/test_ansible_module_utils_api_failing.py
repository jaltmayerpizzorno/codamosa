# Automatically generated by Pynguin.
import ansible.module_utils.api as module_0

def test_case_0():
    try:
        bool_0 = True
        var_0 = module_0.rate_limit_argument_spec(bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        var_0 = module_0.retry_argument_spec()
        set_0 = set()
        var_1 = module_0.generate_jittered_backoff(set_0)
        var_2 = module_0.basic_auth_argument_spec()
        var_3 = module_0.retry_argument_spec()
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'\x81\x07?WK7.\xd8\x1e \xa3\x9a\xa5\xc3\xbc\x08'
        var_0 = module_0.rate_limit_argument_spec()
        var_1 = module_0.retry_with_delays_and_condition(bytes_0)
        bytes_1 = b'Gl<\x8c~\x8b\xd8>\x8a#\x08\x01e\x88*'
        var_2 = module_0.retry_argument_spec(bytes_1)
    except BaseException:
        pass

def test_case_3():
    try:
        var_0 = module_0.basic_auth_argument_spec()
        str_0 = '\x0b&'
        var_1 = module_0.basic_auth_argument_spec(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        float_0 = 1101.22256
        var_0 = module_0.retry_with_delays_and_condition(float_0)
        float_1 = -95.0
        var_1 = module_0.rate_limit(float_1)
        tuple_0 = None
        str_0 = ' 8$LoyD47v'
        tuple_1 = (str_0,)
        list_0 = [str_0, float_0]
        tuple_2 = (tuple_0, tuple_1, list_0, list_0)
        var_2 = module_0.retry_never(tuple_2)
        bytes_0 = b'\xf5F\x16\xff'
        str_1 = ''
        var_3 = module_0.rate_limit(bytes_0, str_1)
    except BaseException:
        pass