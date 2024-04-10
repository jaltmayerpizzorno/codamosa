# Automatically generated by Pynguin.
import sanic.exceptions as module_0

def test_case_0():
    pass

def test_case_1():
    list_0 = []
    invalid_signal_0 = module_0.InvalidSignal(list_0)

def test_case_2():
    dict_0 = {}
    load_file_exception_0 = module_0.LoadFileException(dict_0)
    bool_0 = None
    header_not_found_0 = module_0.HeaderNotFound(bool_0, load_file_exception_0)
    str_0 = None
    bytes_0 = b'V\xe0\xbe\xc3\xc2\x9d\xaa'
    tuple_0 = (header_not_found_0, str_0, bytes_0)
    request_timeout_0 = module_0.RequestTimeout(load_file_exception_0, tuple_0)

def test_case_3():
    str_0 = '\n        :return: Incoming cookies on the request\n        :rtype: Dict[str, str]\n        '
    str_1 = 'B@ltxbZ'
    payload_too_large_0 = module_0.PayloadTooLarge(str_1)
    header_not_found_0 = None
    list_0 = [str_0, payload_too_large_0]
    forbidden_0 = module_0.Forbidden(list_0)
    py_file_error_0 = module_0.PyFileError(forbidden_0)
    dict_0 = {str_1: payload_too_large_0, py_file_error_0: str_0, header_not_found_0: str_1, forbidden_0: list_0}
    bool_0 = False
    not_found_0 = module_0.NotFound(header_not_found_0)
    not_found_1 = module_0.NotFound(bool_0, not_found_0)
    file_not_found_0 = module_0.FileNotFound(header_not_found_0, dict_0, not_found_1)
    file_not_found_1 = module_0.FileNotFound(str_0, payload_too_large_0, file_not_found_0)
    float_0 = 1737.48
    header_not_found_1 = module_0.HeaderNotFound(file_not_found_1, float_0)

def test_case_4():
    load_file_exception_0 = None
    float_0 = 506.6
    unauthorized_0 = module_0.Unauthorized(float_0)
    service_unavailable_0 = module_0.ServiceUnavailable(load_file_exception_0)
    str_0 = '\n        Close the connection if a request is not being sent or received\n\n        :return: boolean - True if closed, false if staying open\n        '
    not_found_0 = module_0.NotFound(str_0)
    var_0 = module_0.add_status_code(not_found_0)
    bytes_0 = b'\x99\xb5:\xa5\xf5\x0b\x06\x8e\x17'
    forbidden_0 = module_0.Forbidden(bytes_0)

def test_case_5():
    str_0 = 'Co8SM;#sqE{'
    py_file_error_0 = module_0.PyFileError(str_0)
    u_r_l_build_error_0 = module_0.URLBuildError(py_file_error_0)
    payload_too_large_0 = None
    set_0 = {str_0, py_file_error_0}
    float_0 = 0.001
    server_error_0 = module_0.ServerError(float_0, u_r_l_build_error_0)
    forbidden_0 = module_0.Forbidden(set_0, server_error_0)
    dict_0 = {str_0: server_error_0, str_0: payload_too_large_0}
    file_not_found_0 = module_0.FileNotFound(payload_too_large_0, forbidden_0, dict_0)
    list_0 = [dict_0]
    sanic_exception_0 = module_0.SanicException(file_not_found_0, list_0, u_r_l_build_error_0)
    str_1 = "\n        Register a root to serve files from. The input can either be a\n        file or a directory. This method will enable an easy and simple way\n        to setup the :class:`Route` necessary to serve the static files.\n\n        :param uri: URL path to be used for serving static content\n        :param file_or_directory: Path for the Static file/directory with\n            static files\n        :param pattern: Regex Pattern identifying the valid static files\n        :param use_modified_since: If true, send file modified time, and return\n            not modified if the browser's matches the server's\n        :param use_content_range: If true, process header for range requests\n            and sends the file part that is requested\n        :param stream_large_files: If true, use the\n            :func:`StreamingHTTPResponse.file_stream` handler rather\n            than the :func:`HTTPResponse.file` handler to send the file.\n            If this is an integer, this represents the threshold size to\n            switch to :func:`StreamingHTTPResponse.file_stream`\n        :param name: user defined name used for url_for\n        :param host: Host IP or FQDN for the service to use\n        :param strict_slashes: Instruct :class:`Sanic` to check if the request\n            URLs need to terminate with a */*\n        :param content_type: user defined content type for header\n        :return: routes registered on the router\n        :rtype: List[sanic.router.Route]\n        "
    server_error_1 = module_0.ServerError(u_r_l_build_error_0, sanic_exception_0, str_1)
    float_1 = 15.0
    forbidden_1 = module_0.Forbidden(float_1)