# Automatically generated by Pynguin.
import ansible.module_utils.api as module_0

def test_case_0():
    pass

def test_case_1():
    set_0 = set()
    var_0 = module_0.retry_with_delays_and_condition(set_0)
    var_1 = module_0.rate_limit_argument_spec()
    var_2 = module_0.basic_auth_argument_spec()
    var_3 = module_0.retry_argument_spec()
    var_4 = module_0.generate_jittered_backoff()

def test_case_2():
    str_0 = None
    var_0 = module_0.retry_argument_spec(str_0)

def test_case_3():
    bool_0 = True
    int_0 = 1600
    str_0 = '(Z=!/.;;ck4q{G*42'
    var_0 = module_0.retry_never(str_0)
    var_1 = module_0.rate_limit(bool_0, int_0)
    str_1 = '/\n'
    var_2 = module_0.retry_with_delays_and_condition(str_1)
    var_3 = module_0.retry_argument_spec()
    var_4 = module_0.rate_limit_argument_spec()
    list_0 = [bool_0, var_1]
    str_2 = ';~0LY"`,L)4_}5'
    var_5 = module_0.generate_jittered_backoff(str_2)
    var_6 = module_0.retry()
    bytes_0 = b'\xcb\xe1\xc4\x17g'
    var_7 = module_0.retry_with_delays_and_condition(bytes_0)
    float_0 = None
    set_0 = {str_1, str_2, var_6}
    str_3 = 'id_like'
    var_8 = module_0.retry_with_delays_and_condition(str_3)
    var_9 = module_0.retry_with_delays_and_condition(set_0)
    int_1 = -1689
    var_10 = module_0.rate_limit(int_1)
    var_11 = module_0.generate_jittered_backoff(float_0)
    str_4 = 'g!'
    var_12 = module_0.retry(str_4)
    var_13 = module_0.retry_never(list_0)
    var_14 = module_0.retry_with_delays_and_condition(list_0)
    set_1 = None
    tuple_0 = (set_1,)
    var_15 = module_0.retry_never(tuple_0)
    var_16 = module_0.basic_auth_argument_spec()

def test_case_4():
    var_0 = module_0.rate_limit()

def test_case_5():
    var_0 = module_0.retry()

def test_case_6():
    bytes_0 = b''
    var_0 = module_0.rate_limit()
    var_1 = module_0.retry_never(bytes_0)

def test_case_7():
    dict_0 = None
    var_0 = module_0.retry_with_delays_and_condition(dict_0)

def test_case_8():
    bool_0 = False
    bool_1 = True
    bool_2 = False
    var_0 = module_0.retry_with_delays_and_condition(bool_1, bool_2)
    bool_3 = True
    var_1 = module_0.rate_limit()
    var_2 = module_0.basic_auth_argument_spec()
    dict_0 = {bool_0: bool_0, bool_0: bool_3}
    var_3 = module_0.retry_never(dict_0)
    bytes_0 = b'\xe3\x8e\x87'
    var_4 = module_0.retry_never(bytes_0)