# Automatically generated by Pynguin.
import sanic.exceptions as module_0

def test_case_0():
    try:
        float_0 = 3409.91645
        str_0 = ')WODs".P\\<R'
        py_file_error_0 = module_0.PyFileError(str_0)
        invalid_usage_0 = module_0.InvalidUsage(float_0, py_file_error_0)
        tuple_0 = ()
        list_0 = [float_0, invalid_usage_0]
        unauthorized_0 = module_0.Unauthorized(tuple_0, list_0)
        bool_0 = False
        list_1 = None
        method_not_supported_0 = module_0.MethodNotSupported(bool_0, list_1, float_0)
    except BaseException:
        pass

def test_case_1():
    try:
        content_range_error_0 = None
        float_0 = -2264.4967
        bool_0 = None
        str_0 = '1W7S'
        file_not_found_0 = module_0.FileNotFound(content_range_error_0, bool_0, str_0)
        str_1 = 'Cpb\tV~L'
        dict_0 = {str_1: float_0, str_1: content_range_error_0, str_0: str_0}
        u_r_l_build_error_0 = module_0.URLBuildError(dict_0)
        invalid_signal_0 = module_0.InvalidSignal(file_not_found_0, u_r_l_build_error_0, file_not_found_0)
        service_unavailable_0 = module_0.ServiceUnavailable(invalid_signal_0)
        server_error_0 = None
        not_found_0 = module_0.NotFound(server_error_0)
        header_expectation_failed_0 = module_0.HeaderExpectationFailed(not_found_0)
        load_file_exception_0 = module_0.LoadFileException(header_expectation_failed_0, file_not_found_0)
        method_not_supported_0 = module_0.MethodNotSupported(service_unavailable_0, float_0, file_not_found_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'nn-Mhm;e&9'
        bool_0 = True
        service_unavailable_0 = module_0.ServiceUnavailable(bool_0, str_0)
        header_not_found_0 = module_0.HeaderNotFound(service_unavailable_0)
        content_range_error_0 = module_0.ContentRangeError(str_0, header_not_found_0)
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = 405
        bytes_0 = b'\x0e:\x84cWK\xd1\xa2'
        var_0 = module_0.abort(int_0, bytes_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'pR^md\t\x0ct4.T2'
        header_not_found_0 = module_0.HeaderNotFound(str_0)
        unauthorized_0 = module_0.Unauthorized(header_not_found_0)
        int_0 = 1529
        var_0 = module_0.abort(int_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'ieQx Xq_&JR'
        invalid_signal_0 = module_0.InvalidSignal(str_0)
        str_1 = '\n        Format a part of response body in chunked encoding.\n        '
        dict_0 = {str_0: str_0, str_1: invalid_signal_0}
        unauthorized_0 = module_0.Unauthorized(str_1, **dict_0)
        var_0 = module_0.add_status_code(invalid_signal_0, unauthorized_0)
        int_0 = 405
        var_1 = module_0.abort(int_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'error message'
        int_0 = 486
        bool_0 = False
        server_error_0 = module_0.ServerError(str_0, int_0, bool_0)
        var_0 = server_error_0.message
    except BaseException:
        pass