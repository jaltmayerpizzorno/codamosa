# Automatically generated by Pynguin.
import sanic.exceptions as module_0

def test_case_0():
    pass

def test_case_1():
    bool_0 = True
    invalid_signal_0 = module_0.InvalidSignal(bool_0)

def test_case_2():
    service_unavailable_0 = None
    float_0 = 1583.105583
    header_expectation_failed_0 = module_0.HeaderExpectationFailed(service_unavailable_0, float_0)

def test_case_3():
    list_0 = []
    py_file_error_0 = module_0.PyFileError(list_0)

def test_case_4():
    list_0 = []
    not_found_0 = module_0.NotFound(list_0)
    py_file_error_0 = module_0.PyFileError(not_found_0)
    dict_0 = {not_found_0: list_0, py_file_error_0: py_file_error_0, py_file_error_0: list_0, not_found_0: py_file_error_0}
    unauthorized_0 = module_0.Unauthorized(dict_0)
    header_expectation_failed_0 = module_0.HeaderExpectationFailed(py_file_error_0, unauthorized_0)
    server_error_0 = None
    sanic_exception_0 = None
    float_0 = 3244.0
    int_0 = 412
    forbidden_0 = module_0.Forbidden(float_0, server_error_0, int_0)
    invalid_signal_0 = module_0.InvalidSignal(server_error_0, sanic_exception_0, forbidden_0)
    dict_1 = {}
    forbidden_1 = module_0.Forbidden(dict_1)
    forbidden_2 = module_0.Forbidden(header_expectation_failed_0, forbidden_1)

def test_case_5():
    int_0 = 403
    list_0 = [int_0, int_0]
    int_1 = -725
    load_file_exception_0 = module_0.LoadFileException(int_1)
    sanic_exception_0 = module_0.SanicException(list_0, load_file_exception_0)
    header_not_found_0 = module_0.HeaderNotFound(sanic_exception_0)
    unauthorized_0 = None
    dict_0 = {}
    payload_too_large_0 = module_0.PayloadTooLarge(unauthorized_0, dict_0)
    sanic_exception_1 = None
    invalid_signal_0 = None
    sanic_exception_2 = module_0.SanicException(sanic_exception_1, invalid_signal_0)
    not_found_0 = module_0.NotFound(unauthorized_0, payload_too_large_0, sanic_exception_2)
    dict_1 = {}
    py_file_error_0 = module_0.PyFileError(dict_1)

def test_case_6():
    str_0 = 'upgrade_websocket'
    float_0 = -838.0
    header_not_found_0 = module_0.HeaderNotFound(str_0, float_0)
    str_1 = 'AL1K\\""CPa ,'
    str_2 = 'Chfn$P?)'
    str_3 = 'iVQEI(i:`Tk!fTv7n9'
    str_4 = '&hszTh pH1OkJQ\\'
    dict_0 = {str_1: header_not_found_0, str_2: header_not_found_0, str_3: str_2, str_4: float_0}
    float_1 = -1136.33
    request_timeout_0 = module_0.RequestTimeout(float_1)
    u_r_l_build_error_0 = module_0.URLBuildError(request_timeout_0)
    server_error_0 = module_0.ServerError(u_r_l_build_error_0)
    unauthorized_0 = module_0.Unauthorized(header_not_found_0, str_1, header_not_found_0, **dict_0)
    dict_1 = {unauthorized_0: dict_0, str_1: header_not_found_0, str_4: float_0}
    sanic_exception_0 = None
    set_0 = {u_r_l_build_error_0}
    header_expectation_failed_0 = module_0.HeaderExpectationFailed(set_0)
    tuple_0 = ()
    int_0 = None
    load_file_exception_0 = module_0.LoadFileException(int_0)
    u_r_l_build_error_1 = module_0.URLBuildError(load_file_exception_0, tuple_0)
    not_found_0 = module_0.NotFound(tuple_0, u_r_l_build_error_1)
    request_timeout_1 = module_0.RequestTimeout(request_timeout_0, header_not_found_0)
    invalid_usage_0 = module_0.InvalidUsage(dict_1, sanic_exception_0, not_found_0)
    bool_0 = None
    var_0 = module_0.add_status_code(bool_0)