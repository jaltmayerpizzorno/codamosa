# Automatically generated by Pynguin.
import httpie.models as module_0

def test_case_0():
    try:
        int_0 = -1026
        bytes_0 = b'\xb9P\xbd\xa1\xfe\x16\xa4\xbd0Su\xf1w~\x8e'
        h_t_t_p_message_0 = module_0.HTTPMessage(bytes_0)
        iterable_0 = h_t_t_p_message_0.iter_body(int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = -396
        dict_0 = {}
        h_t_t_p_message_0 = module_0.HTTPMessage(dict_0)
        h_t_t_p_message_1 = module_0.HTTPMessage(h_t_t_p_message_0)
        iterable_0 = h_t_t_p_message_1.iter_lines(int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b''
        h_t_t_p_response_0 = module_0.HTTPResponse(bytes_0)
        var_0 = h_t_t_p_response_0.iter_body()
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = b''
        h_t_t_p_response_0 = module_0.HTTPResponse(bytes_0)
        var_0 = h_t_t_p_response_0.iter_lines(bytes_0)
    except BaseException:
        pass