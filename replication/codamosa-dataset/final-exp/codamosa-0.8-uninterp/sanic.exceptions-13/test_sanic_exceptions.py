# Automatically generated by Pynguin.
import sanic.exceptions as module_0

def test_case_0():
    pass

def test_case_1():
    py_file_error_0 = None
    server_error_0 = module_0.ServerError(py_file_error_0)

def test_case_2():
    str_0 = 'Auth required.'
    int_0 = 123
    unauthorized_0 = module_0.Unauthorized(str_0, int_0, str_0)

def test_case_3():
    invalid_range_type_0 = None
    py_file_error_0 = module_0.PyFileError(invalid_range_type_0)
    str_0 = '}SMS\x0bz.qfFqn{ev'
    str_1 = 'fc<9Z*6bDXo]'
    list_0 = None
    u_r_l_build_error_0 = module_0.URLBuildError(list_0)
    service_unavailable_0 = module_0.ServiceUnavailable(u_r_l_build_error_0)
    dict_0 = {str_1: str_1, str_0: str_1}
    service_unavailable_1 = module_0.ServiceUnavailable(str_0, dict_0)

def test_case_4():
    str_0 = 'pR^md\t\x0ct4.T2'
    header_not_found_0 = module_0.HeaderNotFound(str_0)
    unauthorized_0 = module_0.Unauthorized(header_not_found_0)

def test_case_5():
    str_0 = 'FIh'
    load_file_exception_0 = module_0.LoadFileException(str_0)
    not_found_0 = module_0.NotFound(load_file_exception_0)
    service_unavailable_0 = None
    str_1 = 'xo<-xokj09L'
    dict_0 = {str_1: str_1, str_0: service_unavailable_0}
    bool_0 = True
    str_2 = 'bg!'
    u_r_l_build_error_0 = module_0.URLBuildError(dict_0, bool_0, str_2)
    load_file_exception_1 = module_0.LoadFileException(not_found_0, service_unavailable_0, u_r_l_build_error_0)

def test_case_6():
    str_0 = 'Restricted Area'
    str_1 = 'Restricted Area'
    str_2 = 'Auth required.'
    str_3 = 'Rtstr%icHed Area'
    set_0 = {str_0}
    dict_0 = {str_3: str_1, str_3: str_2}
    list_0 = [str_1, str_1]
    str_4 = 'When specfyig _schee, _external must be True'
    set_1 = set()
    dict_1 = {str_4: set_1, str_2: str_4}
    unauthorized_0 = module_0.Unauthorized(set_0, dict_0, list_0, **dict_1)
    list_1 = []
    payload_too_large_0 = module_0.PayloadTooLarge(list_1)
    service_unavailable_0 = module_0.ServiceUnavailable(payload_too_large_0)
    request_timeout_0 = module_0.RequestTimeout(service_unavailable_0)