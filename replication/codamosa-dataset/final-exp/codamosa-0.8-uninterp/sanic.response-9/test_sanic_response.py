# Automatically generated by Pynguin.
import sanic.response as module_0
import sanic.compat as module_1
import pathlib as module_2

def test_case_0():
    pass

def test_case_1():
    base_h_t_t_p_response_0 = module_0.BaseHTTPResponse()

def test_case_2():
    str_0 = 'boo'
    h_t_t_p_response_0 = module_0.json(str_0)

def test_case_3():
    str_0 = 'XOyy1gC_R fYwhA&U'
    streaming_h_t_t_p_response_0 = module_0.StreamingHTTPResponse(str_0)

def test_case_4():
    header_0 = module_1.Header()
    list_0 = [header_0, header_0, header_0, header_0]
    h_t_t_p_response_0 = module_0.empty(list_0)

def test_case_5():
    bytes_0 = b'\xc4P\x1b\xa8\xc6\x9f\xb7\xbb\x93'
    float_0 = 322.5163
    h_t_t_p_response_0 = module_0.html(bytes_0, float_0)
    str_0 = 'PLVA#\x0cCz?yB,M5(gko'
    h_t_t_p_response_1 = module_0.text(str_0)

def test_case_6():
    none_type_0 = None
    h_t_t_p_response_0 = module_0.raw(none_type_0)
    str_0 = 'Method {} not allowed for URL {}'
    pure_path_0 = module_2.PurePath()
    base_h_t_t_p_response_0 = module_0.BaseHTTPResponse()
    tuple_0 = ()
    str_1 = 'v/I6!#K[PKQi'
    tuple_1 = (base_h_t_t_p_response_0, pure_path_0, tuple_0, str_1)
    list_0 = [h_t_t_p_response_0]
    tuple_2 = (pure_path_0, tuple_1, list_0)
    header_0 = module_1.Header()
    list_1 = [header_0, header_0, header_0, h_t_t_p_response_0]
    streaming_h_t_t_p_response_0 = module_0.StreamingHTTPResponse(header_0, list_1)
    var_0 = streaming_h_t_t_p_response_0.write(tuple_2)
    h_t_t_p_response_1 = module_0.empty()
    h_t_t_p_response_2 = module_0.redirect(str_0)

def test_case_7():
    pure_path_0 = None
    var_0 = module_0.stream(pure_path_0)

def test_case_8():
    callable_0 = None
    int_0 = 2387
    var_0 = module_0.stream(callable_0, int_0)
    str_0 = None
    h_t_t_p_response_0 = module_0.html(str_0, int_0)
    str_1 = 'E\rDk{1".xDG'
    h_t_t_p_response_1 = module_0.redirect(str_1)

def test_case_9():
    var_0 = None
    int_0 = 200
    str_0 = 'text/plain; charset=utf-8'
    streaming_h_t_t_p_response_0 = module_0.StreamingHTTPResponse(var_0, int_0, var_0, str_0, str_0)

def test_case_10():
    str_0 = 'F4)sw\x0b4`6'
    callable_0 = None
    int_0 = 3021
    dict_0 = {}
    var_0 = None
    var_1 = module_0.stream(callable_0, int_0, dict_0, str_0, var_0)
    int_1 = 2170
    h_t_t_p_response_0 = module_0.html(str_0)
    h_t_t_p_response_1 = module_0.file(str_0, int_1, str_0)
    h_t_t_p_response_2 = module_0.redirect(str_0)