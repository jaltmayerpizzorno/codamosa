# Automatically generated by Pynguin.
import ansible.module_utils.api as module_0

def test_case_0():
    try:
        var_0 = module_0.retry_argument_spec()
        var_1 = module_0.generate_jittered_backoff()
        str_0 = 'b'
        var_2 = module_0.rate_limit_argument_spec(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        var_0 = module_0.retry()
        var_1 = module_0.retry()
        float_0 = 5384.64703
        var_2 = module_0.retry_never(float_0)
        set_0 = {var_1, var_1, var_1, var_1}
        var_3 = module_0.retry_with_delays_and_condition(set_0)
        var_4 = module_0.generate_jittered_backoff()
        var_5 = module_0.retry_argument_spec(float_0)
    except BaseException:
        pass

def test_case_2():
    try:
        float_0 = -1970.0
        var_0 = module_0.basic_auth_argument_spec(float_0)
    except BaseException:
        pass

def test_case_3():
    try:
        var_0 = module_0.retry_argument_spec()
        var_1 = module_0.generate_jittered_backoff()
        var_2 = module_0.generate_jittered_backoff()
        bytes_0 = b'\x84'
        var_3 = module_0.rate_limit(bytes_0, bytes_0)
    except BaseException:
        pass