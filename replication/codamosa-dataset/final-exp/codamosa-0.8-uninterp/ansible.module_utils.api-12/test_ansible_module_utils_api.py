# Automatically generated by Pynguin.
import ansible.module_utils.api as module_0

def test_case_0():
    pass

def test_case_1():
    var_0 = module_0.rate_limit_argument_spec()

def test_case_2():
    var_0 = module_0.retry_argument_spec()

def test_case_3():
    var_0 = module_0.basic_auth_argument_spec()

def test_case_4():
    var_0 = module_0.rate_limit()

def test_case_5():
    var_0 = module_0.retry()

def test_case_6():
    int_0 = -1622
    dict_0 = {int_0: int_0, int_0: int_0, int_0: int_0, int_0: int_0}
    tuple_0 = (dict_0,)
    var_0 = module_0.retry_never(tuple_0)

def test_case_7():
    str_0 = 'v2_playbook_on_vars_prompt'
    var_0 = module_0.retry_with_delays_and_condition(str_0)

def test_case_8():
    int_0 = 404
    var_0 = module_0.rate_limit(int_0)

def test_case_9():
    float_0 = None
    list_0 = [float_0, float_0, float_0, float_0]
    str_0 = 'EjP'
    var_0 = module_0.retry_with_delays_and_condition(list_0, str_0)
    var_1 = module_0.retry_argument_spec()
    var_2 = module_0.generate_jittered_backoff()
    dict_0 = {var_2: var_2, var_2: var_2, var_2: var_2}
    var_3 = module_0.rate_limit(dict_0)
    set_0 = {var_2, var_2, var_2}
    var_4 = module_0.retry()
    var_5 = module_0.retry_never(set_0)
    complex_0 = None
    var_6 = module_0.basic_auth_argument_spec()
    var_7 = module_0.retry(complex_0)
    var_8 = module_0.basic_auth_argument_spec()
    str_1 = 'ax/s'
    var_9 = module_0.retry_never(str_1)
    var_10 = module_0.basic_auth_argument_spec()
    var_11 = module_0.rate_limit_argument_spec()
    var_12 = module_0.retry_argument_spec()