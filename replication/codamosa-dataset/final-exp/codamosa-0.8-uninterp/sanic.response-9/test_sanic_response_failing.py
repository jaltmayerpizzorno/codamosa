# Automatically generated by Pynguin.
import sanic.response as module_0

def test_case_0():
    try:
        int_0 = 2387
        str_0 = None
        h_t_t_p_response_0 = module_0.html(str_0, int_0)
        h_t_t_p_response_1 = module_0.redirect(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = 656
        h_t_t_p_response_0 = module_0.HTTPResponse(int_0)
        optional_0 = None
        str_0 = None
        h_t_t_p_response_1 = module_0.empty(str_0)
        h_t_t_p_response_2 = module_0.raw(optional_0)
        h_t_t_p_response_3 = module_0.text(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = 1
        h_t_t_p_response_0 = module_0.html(int_0, int_0, int_0)
    except BaseException:
        pass

def test_case_3():
    try:
        base_h_t_t_p_response_0 = module_0.BaseHTTPResponse()
        str_0 = 'server_port'
        dict_0 = {}
        var_0 = module_0.stream(str_0, dict_0, str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bytes_0 = None
        int_0 = None
        h_t_t_p_response_0 = module_0.html(bytes_0, int_0)
        int_1 = 401
        str_0 = 'n 5P]jGPw\x0bM"fR8o\tZv'
        h_t_t_p_response_1 = module_0.html(str_0)
        h_t_t_p_response_2 = module_0.redirect(str_0, int_1)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '*$r$*/|t\x0c~'
        int_0 = 2316
        list_0 = [str_0, int_0]
        str_1 = '\n    Trigger event callbacks (functions or async)\n\n    :param events: one or more sync or async functions to execute\n    :param loop: event loop\n    '
        dict_0 = {str_0: str_1, str_1: int_0}
        h_t_t_p_response_0 = module_0.json(str_0, int_0, list_0, str_1, dict_0)
    except BaseException:
        pass