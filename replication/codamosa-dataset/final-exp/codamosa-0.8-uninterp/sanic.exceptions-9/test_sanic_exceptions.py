# Automatically generated by Pynguin.
import sanic.exceptions as module_0

def test_case_0():
    pass

def test_case_1():
    int_0 = 3436
    sanic_exception_0 = module_0.SanicException(int_0)

def test_case_2():
    str_0 = 'IpJU+v}M\n*>`d'
    set_0 = {str_0}
    bytes_0 = b'\x9bk\xd9RrS9\xf2\xe5A\xean\x98_\xad'
    service_unavailable_0 = module_0.ServiceUnavailable(bytes_0)
    forbidden_0 = module_0.Forbidden(set_0, service_unavailable_0)
    file_not_found_0 = module_0.FileNotFound(str_0, forbidden_0, set_0)
    bool_0 = True
    payload_too_large_0 = module_0.PayloadTooLarge(bool_0)
    dict_0 = None
    request_timeout_0 = module_0.RequestTimeout(payload_too_large_0, dict_0)
    float_0 = -727.927106
    service_unavailable_1 = module_0.ServiceUnavailable(float_0)
    complex_0 = None
    header_expectation_failed_0 = module_0.HeaderExpectationFailed(complex_0)

def test_case_3():
    forbidden_0 = None
    py_file_error_0 = module_0.PyFileError(forbidden_0)

def test_case_4():
    float_0 = -2000.015
    invalid_usage_0 = module_0.InvalidUsage(float_0)
    str_0 = "&`b\tsY>oCpl'"
    server_error_0 = module_0.ServerError(str_0)
    forbidden_0 = module_0.Forbidden(invalid_usage_0, server_error_0)
    str_1 = 'q(*c7t FP\rB\x0c'
    tuple_0 = (forbidden_0, str_1)
    service_unavailable_0 = module_0.ServiceUnavailable(tuple_0)
    unauthorized_0 = module_0.Unauthorized(service_unavailable_0)
    set_0 = {unauthorized_0}
    py_file_error_0 = module_0.PyFileError(set_0)

def test_case_5():
    int_0 = 405
    float_0 = -3621.894501
    forbidden_0 = module_0.Forbidden(float_0)
    dict_0 = None
    unauthorized_0 = module_0.Unauthorized(dict_0)
    tuple_0 = None
    bytes_0 = b'\x93\xb0K(\xed\xf4\x19\x98\xd5\x99Z\xc7\xe5\x02\x12\xe5\x8d\x87z\xfb'
    not_found_0 = module_0.NotFound(tuple_0, bytes_0)
    file_not_found_0 = module_0.FileNotFound(int_0, int_0, not_found_0)
    dict_1 = {}
    request_timeout_0 = module_0.RequestTimeout(dict_1, forbidden_0)
    bool_0 = False
    unauthorized_1 = module_0.Unauthorized(file_not_found_0, request_timeout_0, bool_0)

def test_case_6():
    tuple_0 = ()
    str_0 = '\x0bu'
    str_1 = 'k"5.LD*C-KU\t1}(!^C'
    str_2 = 'JW7`\x0bP+J6$C2a'
    dict_0 = {str_1: str_1, str_2: str_2, str_0: str_0}
    str_3 = 'rp9$lvE6^I*'
    request_timeout_0 = module_0.RequestTimeout(str_0, dict_0, str_3)
    forbidden_0 = None
    payload_too_large_0 = module_0.PayloadTooLarge(forbidden_0, forbidden_0)
    header_expectation_failed_0 = module_0.HeaderExpectationFailed(payload_too_large_0)
    load_file_exception_0 = module_0.LoadFileException(request_timeout_0, header_expectation_failed_0)
    service_unavailable_0 = module_0.ServiceUnavailable(tuple_0, load_file_exception_0)

def test_case_7():
    str_0 = '__html__'
    sanic_exception_0 = module_0.SanicException(str_0)
    int_0 = 405
    header_not_found_0 = None
    float_0 = -3621.894501
    forbidden_0 = module_0.Forbidden(float_0)
    str_1 = ''
    header_not_found_1 = module_0.HeaderNotFound(header_not_found_0, forbidden_0, str_1)
    tuple_0 = None
    bytes_0 = b'\x93\xb0K(\xed\xf4\x19\x98\xd5\x99Z\xc7\xe5\x02\x12\xe5\x8d\x87z\xfb'
    not_found_0 = module_0.NotFound(tuple_0, bytes_0)
    file_not_found_0 = module_0.FileNotFound(int_0, header_not_found_1, not_found_0)
    dict_0 = {}
    request_timeout_0 = module_0.RequestTimeout(dict_0, forbidden_0)
    bool_0 = False
    unauthorized_0 = module_0.Unauthorized(file_not_found_0, request_timeout_0, bool_0)
    str_2 = ''
    header_not_found_2 = module_0.HeaderNotFound(sanic_exception_0)
    file_not_found_1 = module_0.FileNotFound(str_2, str_2, header_not_found_2)
    load_file_exception_0 = module_0.LoadFileException(unauthorized_0)

def test_case_8():
    bytes_0 = b'\x0e\xebH\xd1[I\x05\x02'
    str_0 = '__html__'
    sanic_exception_0 = module_0.SanicException(str_0)
    int_0 = 405
    header_not_found_0 = None
    float_0 = -3621.894501
    forbidden_0 = module_0.Forbidden(float_0)
    str_1 = 'B.c<TOZBv'
    header_not_found_1 = module_0.HeaderNotFound(header_not_found_0, forbidden_0, str_1)
    tuple_0 = None
    bytes_1 = b'\x93\xb0K(\xed\xf4\x19\x98\xd5\x99Z\xc7\xe5\x02\x12\xe5\x8d\x87z\xfb'
    list_0 = []
    u_r_l_build_error_0 = module_0.URLBuildError(list_0)
    not_found_0 = module_0.NotFound(tuple_0, bytes_1)
    file_not_found_0 = module_0.FileNotFound(int_0, header_not_found_1, not_found_0)
    dict_0 = {}
    request_timeout_0 = module_0.RequestTimeout(dict_0, forbidden_0)
    bool_0 = False
    unauthorized_0 = module_0.Unauthorized(file_not_found_0, request_timeout_0, bool_0)
    bytes_2 = b'[\x04\x97\x9a\xfa\x94MrU]\xf4-\x18\x8c\xf5\xd0\x8fU\xfa\xb1'
    invalid_signal_0 = None
    header_expectation_failed_0 = module_0.HeaderExpectationFailed(invalid_signal_0)
    dict_1 = {file_not_found_0: bytes_2, bytes_2: dict_0}
    request_timeout_1 = module_0.RequestTimeout(header_expectation_failed_0, dict_1)
    list_1 = [bytes_0, header_expectation_failed_0, invalid_signal_0, bool_0]
    payload_too_large_0 = module_0.PayloadTooLarge(list_1, unauthorized_0)
    bytes_3 = b'+Y\xb3~\x16R\x83(\xd2e\x81\x8e\xdb\xa4v\x8da'
    bool_1 = True
    server_error_0 = module_0.ServerError(bool_1)
    header_expectation_failed_1 = module_0.HeaderExpectationFailed(forbidden_0)
    str_2 = "=G#u aBM'JL@\x0b0PkD5-"
    str_3 = "v9il0q7H`;#'"
    dict_2 = {str_1: forbidden_0}
    unauthorized_1 = module_0.Unauthorized(str_2, bytes_3, str_3, **dict_2)
    forbidden_1 = module_0.Forbidden(unauthorized_1, invalid_signal_0, header_expectation_failed_0)