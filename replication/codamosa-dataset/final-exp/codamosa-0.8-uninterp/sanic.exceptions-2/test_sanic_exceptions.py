# Automatically generated by Pynguin.
import sanic.exceptions as module_0

def test_case_0():
    pass

def test_case_1():
    bool_0 = False
    invalid_usage_0 = module_0.InvalidUsage(bool_0)

def test_case_2():
    bool_0 = True
    set_0 = {bool_0}
    float_0 = -3545.0
    py_file_error_0 = module_0.PyFileError(float_0)
    unauthorized_0 = module_0.Unauthorized(set_0, py_file_error_0, py_file_error_0)

def test_case_3():
    payload_too_large_0 = None
    request_timeout_0 = None
    str_0 = 'wc'
    list_0 = None
    bytes_0 = b'\xb8I\xaf\xcf>'
    dict_0 = {}
    file_not_found_0 = module_0.FileNotFound(list_0, bytes_0, dict_0)
    header_not_found_0 = module_0.HeaderNotFound(file_not_found_0)
    dict_1 = {str_0: header_not_found_0}
    unauthorized_0 = module_0.Unauthorized(payload_too_large_0, request_timeout_0, **dict_1)
    sanic_exception_0 = module_0.SanicException(unauthorized_0)

def test_case_4():
    bool_0 = False
    header_not_found_0 = None
    u_r_l_build_error_0 = module_0.URLBuildError(bool_0)
    bool_1 = True
    str_0 = ',}Cdkpm<b\rv=t8'
    str_1 = '8i.\r\nj.K|])B!g\n'
    dict_0 = {}
    str_2 = '\ny !2:F'
    dict_1 = {str_0: u_r_l_build_error_0, str_1: dict_0, str_1: str_0, str_2: header_not_found_0}
    unauthorized_0 = module_0.Unauthorized(header_not_found_0, u_r_l_build_error_0, bool_1, **dict_1)
    py_file_error_0 = module_0.PyFileError(unauthorized_0)
    int_0 = 207
    unauthorized_1 = module_0.Unauthorized(int_0, **dict_1)