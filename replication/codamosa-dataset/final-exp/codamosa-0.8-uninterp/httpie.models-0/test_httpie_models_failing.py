# Automatically generated by Pynguin.
import httpie.models as module_0

def test_case_0():
    try:
        int_0 = 100
        set_0 = set()
        h_t_t_p_request_0 = module_0.HTTPRequest(set_0)
        h_t_t_p_message_0 = module_0.HTTPMessage(h_t_t_p_request_0)
        iterable_0 = h_t_t_p_message_0.iter_body(int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = 16
        str_0 = 'jQ'
        h_t_t_p_message_0 = module_0.HTTPMessage(str_0)
        iterable_0 = h_t_t_p_message_0.iter_lines(int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        tuple_0 = ()
        float_0 = 446.52
        h_t_t_p_response_0 = module_0.HTTPResponse(float_0)
        var_0 = h_t_t_p_response_0.iter_body(tuple_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '"6)@w#;`nHeJ7n\\p'
        str_1 = 'bold'
        h_t_t_p_request_0 = module_0.HTTPRequest(str_1)
        h_t_t_p_response_0 = module_0.HTTPResponse(str_0)
        var_0 = h_t_t_p_response_0.iter_lines(h_t_t_p_response_0)
    except BaseException:
        pass

def test_case_4():
    try:
        var_0 = None
        h_t_t_p_request_0 = module_0.HTTPRequest(var_0)
        var_1 = h_t_t_p_request_0.body
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'abc'
        h_t_t_p_request_0 = module_0.HTTPRequest(str_0)
        int_0 = 1
        var_0 = h_t_t_p_request_0.iter_body(int_0)
        var_1 = list(var_0)
    except BaseException:
        pass