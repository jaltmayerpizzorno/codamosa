# Automatically generated by Pynguin.
import sanic.exceptions as module_0

def test_case_0():
    try:
        list_0 = []
        list_1 = [list_0]
        payload_too_large_0 = module_0.PayloadTooLarge(list_0, list_1)
        str_0 = 'N'
        py_file_error_0 = module_0.PyFileError(str_0)
        str_1 = 'F'
        sanic_exception_0 = module_0.SanicException(str_1)
        tuple_0 = ()
        dict_0 = {str_1: sanic_exception_0}
        request_timeout_0 = module_0.RequestTimeout(dict_0)
        method_not_supported_0 = module_0.MethodNotSupported(tuple_0, request_timeout_0, sanic_exception_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = "\n        Register a root to serve files from. The input can either be a\n        file or a directory. This method will enable an easy and simple way\n        to setup the :class:`Route` necessary to serve the static files.\n\n        :param uri: URL path to be used for serving static content\n        :param file_or_directory: Path for the Static file/directory with\n            static files\n        :param pattern: Regex Pattern identifying the valid static files\n        :param use_modified_since: If true, send file modified time, and return\n            not modified if the browser's matches the server's\n        :param use_content_range: If true, process header for range requests\n            and sends the file part that is requested\n        :param stream_large_files: If true, use the\n            :func:`StreamingHTTPResponse.file_stream` handler rather\n            than the :func:`HTTPResponse.file` handler to send the file.\n            If this is an integer, this represents the threshold size to\n            switch to :func:`StreamingHTTPResponse.file_stream`\n        :param name: user defined name used for url_for\n        :param host: Host IP or FQDN for the service to use\n        :param strict_slashes: Instruct :class:`Sanic` to check if the request\n            URLs need to terminate with a */*\n        :param content_type: user defined content type for header\n        :return: routes registered on the router\n        :rtype: List[sanic.router.Route]\n        "
        request_timeout_0 = module_0.RequestTimeout(str_0)
        str_1 = '`v;^+8L[\r08dwaQ'
        dict_0 = None
        list_0 = [str_1, str_1, dict_0]
        unauthorized_0 = module_0.Unauthorized(list_0)
        invalid_usage_0 = module_0.InvalidUsage(request_timeout_0)
        not_found_0 = None
        set_0 = {not_found_0, unauthorized_0}
        bytes_0 = b'\x81]?I\xba6'
        float_0 = 2819.98
        u_r_l_build_error_0 = module_0.URLBuildError(float_0)
        tuple_0 = (set_0, bytes_0, u_r_l_build_error_0)
        header_expectation_failed_0 = None
        file_not_found_0 = module_0.FileNotFound(not_found_0, tuple_0, header_expectation_failed_0)
        str_2 = 'attachment; filename="'
        dict_1 = {str_2: request_timeout_0}
        service_unavailable_0 = module_0.ServiceUnavailable(dict_1)
        method_not_supported_0 = module_0.MethodNotSupported(header_expectation_failed_0, dict_1, service_unavailable_0)
    except BaseException:
        pass

def test_case_2():
    try:
        float_0 = -1411.0
        load_file_exception_0 = module_0.LoadFileException(float_0)
        tuple_0 = ()
        file_not_found_0 = None
        content_range_error_0 = module_0.ContentRangeError(tuple_0, file_not_found_0)
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = -15
        bytes_0 = b'TIZY\xfe'
        u_r_l_build_error_0 = None
        invalid_signal_0 = None
        list_0 = [int_0, bytes_0]
        py_file_error_0 = module_0.PyFileError(list_0)
        service_unavailable_0 = module_0.ServiceUnavailable(invalid_signal_0, bytes_0)
        invalid_usage_0 = module_0.InvalidUsage(service_unavailable_0)
        forbidden_0 = module_0.Forbidden(u_r_l_build_error_0)
        u_r_l_build_error_1 = module_0.URLBuildError(forbidden_0, forbidden_0)
        sanic_exception_0 = module_0.SanicException(u_r_l_build_error_1)
        var_0 = module_0.abort(int_0, bytes_0)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = 2
        var_0 = module_0.abort(int_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '{!s}="{!s}"'
        service_unavailable_0 = module_0.ServiceUnavailable(str_0)
        float_0 = 408.5094
        list_0 = [str_0, service_unavailable_0, float_0, str_0]
        int_0 = 403
        invalid_usage_0 = module_0.InvalidUsage(service_unavailable_0, int_0)
        invalid_usage_1 = module_0.InvalidUsage(list_0, invalid_usage_0, float_0)
        py_file_error_0 = module_0.PyFileError(service_unavailable_0)
        var_0 = module_0.abort(int_0)
    except BaseException:
        pass

def test_case_6():
    try:
        bytes_0 = b'\nJ\xc8E\xe5'
        bool_0 = True
        payload_too_large_0 = module_0.PayloadTooLarge(bool_0)
        service_unavailable_0 = module_0.ServiceUnavailable(bytes_0, payload_too_large_0)
        tuple_0 = ()
        py_file_error_0 = module_0.PyFileError(tuple_0)
        header_expectation_failed_0 = module_0.HeaderExpectationFailed(py_file_error_0)
        method_not_supported_0 = None
        set_0 = {payload_too_large_0, payload_too_large_0}
        not_found_0 = module_0.NotFound(method_not_supported_0, set_0)
        request_timeout_0 = module_0.RequestTimeout(not_found_0)
        float_0 = 3397.0
        dict_0 = {}
        forbidden_0 = module_0.Forbidden(request_timeout_0, float_0, dict_0)
        unauthorized_0 = module_0.Unauthorized(py_file_error_0)
        content_range_error_0 = module_0.ContentRangeError(forbidden_0, unauthorized_0)
    except BaseException:
        pass