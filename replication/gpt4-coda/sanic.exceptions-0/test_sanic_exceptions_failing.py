# Automatically generated by Pynguin.
import sanic.exceptions as module_0

def test_case_0():
    try:
        bytes_0 = b'<\xa9\xea7E\x9e\r\xae@v'
        str_0 = 'b/}zv)9C&\r+'
        complex_0 = None
        invalid_usage_0 = None
        service_unavailable_0 = module_0.ServiceUnavailable(invalid_usage_0)
        invalid_signal_0 = module_0.InvalidSignal(service_unavailable_0)
        str_1 = 'T"VCJw\r]4w'
        header_not_found_0 = module_0.HeaderNotFound(str_1)
        bool_0 = True
        header_not_found_1 = module_0.HeaderNotFound(complex_0, str_1, bool_0)
        method_not_supported_0 = module_0.MethodNotSupported(bytes_0, str_0, header_not_found_1)
    except BaseException:
        pass

def test_case_1():
    try:
        method_not_supported_0 = None
        header_expectation_failed_0 = module_0.HeaderExpectationFailed(method_not_supported_0)
        server_error_0 = module_0.ServerError(header_expectation_failed_0)
        list_0 = [server_error_0, method_not_supported_0]
        sanic_exception_0 = None
        file_not_found_0 = module_0.FileNotFound(list_0, header_expectation_failed_0, sanic_exception_0)
        set_0 = {method_not_supported_0}
        content_range_error_0 = module_0.ContentRangeError(file_not_found_0, set_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = False
        not_found_0 = module_0.NotFound(bool_0)
        int_0 = -912
        invalid_range_type_0 = module_0.InvalidRangeType(not_found_0, int_0)
    except BaseException:
        pass

def test_case_3():
    try:
        invalid_signal_0 = None
        str_0 = 'rUsV?mP}\tY3Xz'
        header_expectation_failed_0 = module_0.HeaderExpectationFailed(str_0)
        service_unavailable_0 = module_0.ServiceUnavailable(header_expectation_failed_0)
        set_0 = {invalid_signal_0}
        header_expectation_failed_1 = None
        py_file_error_0 = module_0.PyFileError(header_expectation_failed_1)
        dict_0 = {str_0: set_0}
        unauthorized_0 = module_0.Unauthorized(str_0, set_0, header_expectation_failed_0, **dict_0)
        dict_1 = {}
        tuple_0 = (dict_1,)
        float_0 = -415.967
        sanic_exception_0 = module_0.SanicException(tuple_0, float_0)
        service_unavailable_1 = module_0.ServiceUnavailable(sanic_exception_0, dict_0)
        sanic_exception_1 = module_0.SanicException(unauthorized_0)
        list_0 = None
        payload_too_large_0 = module_0.PayloadTooLarge(service_unavailable_0, sanic_exception_1, list_0)
        bool_0 = False
        dict_2 = {}
        file_not_found_0 = module_0.FileNotFound(payload_too_large_0, bool_0, dict_2)
        method_not_supported_0 = module_0.MethodNotSupported(invalid_signal_0, file_not_found_0, header_expectation_failed_0)
    except BaseException:
        pass

def test_case_4():
    try:
        header_not_found_0 = None
        dict_0 = {header_not_found_0: header_not_found_0}
        payload_too_large_0 = module_0.PayloadTooLarge(dict_0)
        unauthorized_0 = module_0.Unauthorized(payload_too_large_0)
        request_timeout_0 = module_0.RequestTimeout(header_not_found_0, header_not_found_0)
        list_0 = []
        str_0 = 'zU7K``iJ)fZe4jw'
        forbidden_0 = module_0.Forbidden(list_0, str_0)
        str_1 = ',-}~.hb#'
        int_0 = None
        var_0 = module_0.abort(int_0, str_1)
    except BaseException:
        pass

def test_case_5():
    try:
        int_0 = 1836
        var_0 = module_0.abort(int_0)
    except BaseException:
        pass

def test_case_6():
    try:
        header_not_found_0 = None
        dict_0 = {header_not_found_0: header_not_found_0}
        payload_too_large_0 = module_0.PayloadTooLarge(dict_0)
        unauthorized_0 = module_0.Unauthorized(payload_too_large_0)
        request_timeout_0 = module_0.RequestTimeout(header_not_found_0, header_not_found_0)
        list_0 = []
        str_0 = 'zU7K``iJ)fZe4jw'
        forbidden_0 = module_0.Forbidden(list_0, str_0)
        tuple_0 = ()
        dict_1 = {}
        invalid_signal_0 = None
        not_found_0 = module_0.NotFound(invalid_signal_0)
        method_not_supported_0 = module_0.MethodNotSupported(list_0, not_found_0, tuple_0)
        invalid_signal_1 = module_0.InvalidSignal(dict_1, method_not_supported_0)
        int_0 = 308
        var_0 = module_0.abort(int_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = '_match_info'
        str_1 = ''
        load_file_exception_0 = module_0.LoadFileException(str_0, str_1)
        invalid_signal_0 = None
        str_2 = 'tO_Uw'
        list_0 = [str_2, invalid_signal_0, str_1, str_0]
        int_0 = 965
        forbidden_0 = module_0.Forbidden(int_0)
        u_r_l_build_error_0 = module_0.URLBuildError(list_0, forbidden_0)
        str_3 = None
        str_4 = '8QR*aM\\a6~\t\x0c'
        dict_0 = {str_3: str_2, str_3: forbidden_0, str_4: u_r_l_build_error_0}
        invalid_range_type_0 = None
        service_unavailable_0 = module_0.ServiceUnavailable(u_r_l_build_error_0, dict_0, invalid_range_type_0)
        request_timeout_0 = module_0.RequestTimeout(service_unavailable_0, forbidden_0)
        tuple_0 = None
        str_5 = ''
        request_timeout_1 = module_0.RequestTimeout(request_timeout_0, tuple_0, str_5)
        invalid_range_type_1 = module_0.InvalidRangeType(load_file_exception_0, invalid_signal_0)
    except BaseException:
        pass