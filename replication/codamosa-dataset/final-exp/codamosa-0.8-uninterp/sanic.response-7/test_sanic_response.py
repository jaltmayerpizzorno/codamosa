# Automatically generated by Pynguin.
import sanic.response as module_0

def test_case_0():
    pass

def test_case_1():
    base_h_t_t_p_response_0 = module_0.BaseHTTPResponse()

def test_case_2():
    str_0 = 'h3W8%b~'
    h_t_t_p_response_0 = module_0.text(str_0, str_0)

def test_case_3():
    h_t_m_l_protocol_0 = None
    h_t_t_p_response_0 = module_0.html(h_t_m_l_protocol_0)

def test_case_4():
    str_0 = 'deprecated'
    var_0 = module_0.stream(str_0)

def test_case_5():
    str_0 = 'v,LBg'
    var_0 = module_0.stream(str_0)
    h_t_t_p_response_0 = module_0.HTTPResponse()
    set_0 = None
    pure_path_0 = None
    h_t_t_p_response_1 = module_0.empty(set_0, pure_path_0)

def test_case_6():
    int_0 = 1842
    h_t_t_p_response_0 = module_0.json(int_0)

def test_case_7():
    str_0 = '.NoA#P0\n+X'
    streaming_h_t_t_p_response_0 = module_0.file_stream(str_0, str_0)
    base_h_t_t_p_response_0 = module_0.BaseHTTPResponse()
    int_0 = None
    int_1 = 2095
    callable_0 = None
    streaming_h_t_t_p_response_1 = module_0.StreamingHTTPResponse(callable_0, str_0)
    set_0 = {str_0, int_0, base_h_t_t_p_response_0}
    streaming_h_t_t_p_response_2 = module_0.file_stream(str_0, int_0, int_1, str_0, set_0)
    h_t_t_p_response_0 = module_0.redirect(str_0)

def test_case_8():
    h_t_m_l_protocol_0 = None
    int_0 = -1539
    str_0 = None
    str_1 = '\tWE{'
    dict_0 = {str_1: str_0, str_1: str_1}
    h_t_t_p_response_0 = module_0.html(h_t_m_l_protocol_0, int_0, dict_0)

def test_case_9():
    str_0 = '<=\x0b6T2*R]JUx%I$&!'
    h_t_t_p_response_0 = module_0.html(str_0)
    base_h_t_t_p_response_0 = module_0.BaseHTTPResponse()