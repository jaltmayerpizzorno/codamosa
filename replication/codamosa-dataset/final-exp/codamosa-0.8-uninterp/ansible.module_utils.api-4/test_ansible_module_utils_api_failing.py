# Automatically generated by Pynguin.
import ansible.module_utils.api as module_0

def test_case_0():
    try:
        str_0 = None
        var_0 = module_0.retry_never(str_0)
        var_1 = module_0.retry()
        list_0 = None
        var_2 = module_0.retry_never(list_0)
        var_3 = module_0.retry_argument_spec(list_0)
        var_4 = module_0.retry()
        str_1 = '2.12.1'
        var_5 = module_0.rate_limit_argument_spec(str_1)
    except BaseException:
        pass

def test_case_1():
    try:
        list_0 = None
        var_0 = module_0.rate_limit(list_0)
        var_1 = module_0.retry()
        str_0 = '\rt\x0b1/W!xVGWqcU+7hP&'
        var_2 = module_0.retry_argument_spec(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'\xbd\xce\xc4N\x95\xce\xa1E\x97\xc5\x8d\xb77\xbb\x0b\x96\xdf\xee'
        complex_0 = None
        var_0 = module_0.basic_auth_argument_spec()
        tuple_0 = (complex_0,)
        var_1 = module_0.retry_with_delays_and_condition(bytes_0, tuple_0)
        int_0 = 1394
        var_2 = module_0.retry_never(int_0)
        var_3 = module_0.basic_auth_argument_spec(tuple_0)
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = 1213
        dict_0 = {int_0: int_0, int_0: int_0, int_0: int_0, int_0: int_0}
        tuple_0 = ()
        bool_0 = True
        var_0 = module_0.retry_with_delays_and_condition(tuple_0, bool_0)
        set_0 = set()
        tuple_1 = ()
        var_1 = module_0.basic_auth_argument_spec(tuple_1)
        list_0 = None
        tuple_2 = (set_0, list_0)
        bool_1 = None
        float_0 = -1420.4614
        var_2 = module_0.retry_with_delays_and_condition(bool_1, float_0)
        var_3 = module_0.rate_limit(dict_0, tuple_2)
    except BaseException:
        pass

def test_case_4():
    try:
        var_0 = module_0.basic_auth_argument_spec()
        var_1 = module_0.rate_limit()
        var_2 = module_0.generate_jittered_backoff()
        set_0 = {var_1, var_2}
        bytes_0 = b'\xba\xf0Ah\x86\x80\x95J\xb8'
        var_3 = module_0.retry()
        dict_0 = {var_2: set_0, var_2: set_0}
        bool_0 = False
        tuple_0 = (bytes_0, dict_0, bool_0, bool_0)
        bytes_1 = b'\x1ak\\\x8d\xe5'
        var_4 = module_0.retry(bytes_1)
        var_5 = module_0.retry_argument_spec()
        var_6 = module_0.retry(set_0, tuple_0)
        var_7 = module_0.generate_jittered_backoff()
        var_8 = module_0.retry_argument_spec()
        var_9 = module_0.retry()
        var_10 = module_0.basic_auth_argument_spec(set_0)
    except BaseException:
        pass