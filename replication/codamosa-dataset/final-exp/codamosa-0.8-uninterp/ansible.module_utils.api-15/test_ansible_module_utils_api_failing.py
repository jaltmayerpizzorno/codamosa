# Automatically generated by Pynguin.
import ansible.module_utils.api as module_0

def test_case_0():
    try:
        bytes_0 = None
        list_0 = [bytes_0, bytes_0]
        var_0 = module_0.rate_limit_argument_spec(list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'\xc3\xd8\x01\xceJ4\x97K\x1a#\x19$\xa2\x81l\x83'
        var_0 = module_0.retry_argument_spec(bytes_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = 493
        var_0 = module_0.basic_auth_argument_spec(int_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = ''
        var_0 = module_0.basic_auth_argument_spec(str_0)
        var_1 = module_0.retry_argument_spec()
        bool_0 = False
        float_0 = -647.0669
        var_2 = module_0.rate_limit(bool_0, float_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '&.1cL:Z'
        dict_0 = {str_0: str_0}
        var_0 = module_0.retry_with_delays_and_condition(dict_0)
        float_0 = 5857.53
        var_1 = module_0.basic_auth_argument_spec()
        var_2 = module_0.retry_argument_spec()
        var_3 = module_0.retry_with_delays_and_condition(str_0, float_0)
        var_4 = module_0.rate_limit()
        var_5 = module_0.rate_limit_argument_spec()
        str_1 = 'Oj<y`cu[\x0cAO$9>d!<?'
        var_6 = module_0.basic_auth_argument_spec(str_1)
    except BaseException:
        pass

def test_case_5():
    try:
        bytes_0 = b"\xe3\xc2\xb5\x1at\xfc\x15\xbd\xae\xc3\x93\xf6\xb3\xc66h'\x92\xf5"
        str_0 = '{+>a1aN\t9+pz'
        var_0 = module_0.retry_with_delays_and_condition(bytes_0, str_0)
        int_0 = 9
        var_1 = module_0.retry_never(int_0)
        var_2 = module_0.rate_limit()
        var_3 = module_0.generate_jittered_backoff()
        float_0 = -2152.0
        bytes_1 = b'-\x17_H\x8e\xeb\xfa\xcb\xf1\xb2'
        var_4 = module_0.generate_jittered_backoff(float_0, bytes_1)
        var_5 = module_0.generate_jittered_backoff()
        var_6 = module_0.basic_auth_argument_spec()
        var_7 = module_0.retry()
        tuple_0 = ()
        var_8 = module_0.retry_with_delays_and_condition(tuple_0)
        str_1 = '$KNY6P>B\rQ4,$i\t0'
        var_9 = module_0.retry(str_1)
        list_0 = [var_5, var_5, var_3, var_2]
        var_10 = module_0.rate_limit_argument_spec(list_0)
    except BaseException:
        pass