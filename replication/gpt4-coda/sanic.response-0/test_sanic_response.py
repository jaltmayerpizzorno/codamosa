# Automatically generated by Pynguin.
import sanic.response as module_0

def test_case_0():
    pass

def test_case_1():
    h_t_t_p_response_0 = module_0.empty()

def test_case_2():
    str_0 = None
    h_t_t_p_response_0 = module_0.html(str_0)

def test_case_3():
    bytes_0 = b'+\xe1\xb4I\x08\xde|\\\xe5\x908'
    streaming_h_t_t_p_response_0 = module_0.StreamingHTTPResponse(bytes_0)

def test_case_4():
    int_0 = 211
    h_t_t_p_response_0 = module_0.json(int_0)

def test_case_5():
    callable_0 = None
    var_0 = module_0.stream(callable_0)

def test_case_6():
    base_h_t_t_p_response_0 = module_0.BaseHTTPResponse()
    str_0 = ':\\\x0c]$#t\x0c\rz8\nPz'
    str_1 = 'RW'
    dict_0 = {str_0: str_1, str_1: str_0}
    int_0 = -1264
    h_t_t_p_response_0 = module_0.redirect(str_0, dict_0, int_0)
    str_2 = '_<>u1Y'
    int_1 = 4722
    list_0 = [int_1]
    list_1 = [str_2, list_0, str_1, str_0]
    h_t_t_p_response_1 = module_0.file(str_0, list_1)
    base_h_t_t_p_response_0.send()