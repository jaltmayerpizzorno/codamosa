# Automatically generated by Pynguin.
import sanic.exceptions as module_0

def test_case_0():
    try:
        float_0 = 1383.3
        set_0 = {float_0, float_0, float_0, float_0}
        invalid_range_type_0 = module_0.InvalidRangeType(float_0, set_0)
    except BaseException:
        pass

def test_case_1():
    try:
        invalid_range_type_0 = None
        py_file_error_0 = None
        forbidden_0 = module_0.Forbidden(py_file_error_0)
        py_file_error_1 = module_0.PyFileError(forbidden_0)
        invalid_range_type_1 = module_0.InvalidRangeType(invalid_range_type_0, py_file_error_1)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = ':%yW*mXZ{'
        dict_0 = {str_0: str_0, str_0: str_0}
        unauthorized_0 = module_0.Unauthorized(dict_0)
        sanic_exception_0 = module_0.SanicException(unauthorized_0)
        int_0 = 528
        var_0 = module_0.abort(int_0)
    except BaseException:
        pass

def test_case_3():
    try:
        invalid_usage_0 = None
        float_0 = -76.309113
        load_file_exception_0 = module_0.LoadFileException(float_0)
        dict_0 = {invalid_usage_0: invalid_usage_0}
        header_expectation_failed_0 = None
        header_expectation_failed_1 = module_0.HeaderExpectationFailed(header_expectation_failed_0)
        header_not_found_0 = module_0.HeaderNotFound(header_expectation_failed_1)
        u_r_l_build_error_0 = module_0.URLBuildError(dict_0, header_not_found_0)
        bool_0 = False
        unauthorized_0 = module_0.Unauthorized(bool_0)
        not_found_0 = module_0.NotFound(unauthorized_0)
        header_expectation_failed_2 = module_0.HeaderExpectationFailed(not_found_0)
        forbidden_0 = module_0.Forbidden(bool_0, header_expectation_failed_1)
        var_0 = module_0.add_status_code(header_expectation_failed_2)
        int_0 = 502
        set_0 = {forbidden_0}
        list_0 = [header_not_found_0, not_found_0]
        invalid_signal_0 = module_0.InvalidSignal(list_0, forbidden_0)
        server_error_0 = module_0.ServerError(invalid_usage_0, invalid_signal_0)
        u_r_l_build_error_1 = module_0.URLBuildError(set_0, server_error_0)
        var_1 = module_0.abort(int_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bool_0 = None
        bytes_0 = b'\x9cY-D\xe0\x89T5b)B\xf8\xd9\xdfX\xe9\x92'
        header_expectation_failed_0 = module_0.HeaderExpectationFailed(bool_0, bytes_0)
        payload_too_large_0 = module_0.PayloadTooLarge(header_expectation_failed_0)
        int_0 = 485
        var_0 = module_0.abort(int_0, bytes_0)
    except BaseException:
        pass

def test_case_5():
    try:
        header_not_found_0 = None
        payload_too_large_0 = module_0.PayloadTooLarge(header_not_found_0)
        str_0 = 'v>B~Nu/FObf_:E2g*O'
        py_file_error_0 = module_0.PyFileError(str_0)
        int_0 = -2493
        tuple_0 = (py_file_error_0, int_0)
        bool_0 = False
        service_unavailable_0 = module_0.ServiceUnavailable(payload_too_large_0, tuple_0, bool_0)
        dict_0 = {str_0: service_unavailable_0}
        bool_1 = False
        dict_1 = {service_unavailable_0: int_0}
        load_file_exception_0 = None
        not_found_0 = module_0.NotFound(load_file_exception_0)
        float_0 = -346.126783
        forbidden_0 = module_0.Forbidden(dict_1, float_0)
        bytes_0 = b'^ UT\xda\xbc'
        header_expectation_failed_0 = module_0.HeaderExpectationFailed(bytes_0)
        unauthorized_0 = module_0.Unauthorized(not_found_0, forbidden_0, header_expectation_failed_0, **dict_0)
        forbidden_1 = module_0.Forbidden(py_file_error_0, dict_1, unauthorized_0)
        invalid_range_type_0 = module_0.InvalidRangeType(dict_0, bool_1)
    except BaseException:
        pass