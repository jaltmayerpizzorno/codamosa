# Automatically generated by Pynguin.
import sanic.response as module_0
import pathlib as module_1

def test_case_0():
    try:
        str_0 = 'Bad body type. Expected str, got '
        str_1 = '+P@AiOi!+$PV`7y|%&t'
        str_2 = ' AZ:-mOk'
        dict_0 = {str_0: str_1, str_2: str_0}
        h_t_t_p_response_0 = module_0.empty(dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        none_type_0 = None
        h_t_t_p_response_0 = module_0.empty(none_type_0)
        h_t_t_p_response_1 = module_0.empty()
        int_0 = None
        h_t_t_p_response_2 = module_0.empty()
        str_0 = None
        h_t_t_p_response_3 = module_0.json(int_0)
        h_t_t_p_response_4 = module_0.text(str_0, h_t_t_p_response_3)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'Js'
        h_t_t_p_response_0 = module_0.text(str_0)
        str_1 = 'wzQn'
        h_t_t_p_response_1 = module_0.text(str_1)
        h_t_t_p_response_2 = module_0.text(str_0)
        int_0 = 2430
        h_t_t_p_response_3 = module_0.HTTPResponse(int_0, int_0)
        h_t_t_p_response_4 = module_0.html(str_1)
        h_t_t_p_response_5 = module_0.json(int_0)
        dict_0 = None
        list_0 = [dict_0]
        list_1 = []
        pure_path_0 = module_1.PurePath(*list_1)
        str_2 = '&sBh,$pD21*'
        h_t_t_p_response_6 = module_0.HTTPResponse()
        range_0 = None
        str_3 = '?BJQnhKZIvOYO}:pG-|d'
        tuple_0 = (range_0, str_3)
        streaming_h_t_t_p_response_0 = module_0.file_stream(str_0, int_0, int_0, tuple_0, str_2)
        h_t_t_p_response_7 = module_0.empty()
        var_0 = streaming_h_t_t_p_response_0.send(*list_0)
    except BaseException:
        pass

def test_case_3():
    try:
        float_0 = 183.17425
        str_0 = 'yHqfl'
        str_1 = None
        str_2 = '1'
        str_3 = 'awu! \n\x0b:|p^A>B['
        dict_0 = {str_0: str_0, str_1: str_2, str_0: str_0, str_3: str_2}
        str_4 = '~_~Uo`t6Z?\x0cg,S>{)'
        none_type_0 = None
        h_t_t_p_response_0 = module_0.json(float_0, dict_0, str_4, none_type_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'bAR7'
        h_t_t_p_response_0 = module_0.text(str_0)
        h_t_t_p_response_1 = module_0.html(str_0)
        dict_0 = None
        list_0 = [dict_0]
        list_1 = []
        pure_path_0 = module_1.PurePath(*list_1)
        str_1 = '&sBh,$pD21*'
        streaming_h_t_t_p_response_0 = module_0.file_stream(pure_path_0, str_1)
        var_0 = streaming_h_t_t_p_response_0.send(*list_0)
    except BaseException:
        pass

def test_case_5():
    try:
        callable_0 = None
        int_0 = 451
        int_1 = -2691
        str_0 = 'server_port'
        list_0 = []
        var_0 = module_0.stream(callable_0, int_0, int_1, str_0, list_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'wzQn'
        h_t_t_p_response_0 = module_0.text(str_0)
        str_1 = 'bAR7'
        h_t_t_p_response_1 = module_0.text(str_1)
        int_0 = 2428
        h_t_t_p_response_2 = module_0.HTTPResponse(int_0, int_0)
        h_t_t_p_response_3 = module_0.html(str_0)
        h_t_t_p_response_4 = module_0.json(int_0)
        dict_0 = None
        list_0 = [dict_0]
        list_1 = []
        pure_path_0 = module_1.PurePath(*list_1)
        h_t_t_p_response_5 = module_0.HTTPResponse(int_0)
        int_1 = -1738
        str_2 = ':1\\8f v5h5ENzbKARV`'
        streaming_h_t_t_p_response_0 = module_0.file_stream(pure_path_0, int_1, str_1, str_2)
        h_t_t_p_response_6 = module_0.empty()
        var_0 = streaming_h_t_t_p_response_0.send(*list_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'wzQn'
        int_0 = -562
        h_t_t_p_response_0 = module_0.html(str_0, int_0)
        h_t_t_p_response_1 = module_0.text(str_0)
        str_1 = 'bAR7'
        int_1 = 2430
        h_t_t_p_response_2 = module_0.HTTPResponse(int_1, int_1)
        h_t_t_p_response_3 = module_0.html(str_1)
        h_t_t_p_response_4 = module_0.json(str_1)
        dict_0 = None
        list_0 = [dict_0]
        base_h_t_t_p_response_0 = module_0.BaseHTTPResponse()
        streaming_h_t_t_p_response_0 = module_0.StreamingHTTPResponse(base_h_t_t_p_response_0)
        list_1 = []
        pure_path_0 = module_1.PurePath(*list_1)
        base_h_t_t_p_response_1 = module_0.BaseHTTPResponse()
        h_t_t_p_response_5 = module_0.HTTPResponse()
        str_2 = '$otsbN`PB>u'
        int_2 = -1169
        streaming_h_t_t_p_response_1 = module_0.file_stream(str_1, int_2, int_2, str_1, str_1, pure_path_0)
        str_3 = 'ay3djjwYJ6zGjBk#zOV'
        dict_1 = {str_2: str_3}
        h_t_t_p_response_6 = module_0.empty(dict_1)
        var_0 = streaming_h_t_t_p_response_1.send(*list_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'wzQn'
        h_t_t_p_response_0 = module_0.text(str_0)
        str_1 = 'bAR7'
        int_0 = 2430
        h_t_t_p_response_1 = module_0.HTTPResponse(int_0, int_0)
        str_2 = None
        h_t_t_p_response_2 = module_0.html(str_2)
        h_t_t_p_response_3 = module_0.file(str_1, int_0)
        h_t_t_p_response_4 = module_0.json(int_0)
        dict_0 = None
        list_0 = [dict_0]
        list_1 = []
        pure_path_0 = module_1.PurePath(*list_1)
        base_h_t_t_p_response_0 = module_0.BaseHTTPResponse()
        dict_1 = {}
        h_t_t_p_response_5 = module_0.html(str_1, int_0, dict_1)
        h_t_t_p_response_6 = module_0.HTTPResponse()
        str_3 = '$otsbN`PB>u'
        int_1 = None
        str_4 = '!g>8Y:q45/"PrP"#!A\r'
        str_5 = 'lC#.2SZ-qm;'
        str_6 = None
        str_7 = ''
        dict_2 = {str_4: str_5, str_6: str_7}
        streaming_h_t_t_p_response_0 = module_0.file_stream(str_2, int_0, int_1, str_3, dict_2, str_0)
        bool_0 = True
        h_t_t_p_response_7 = module_0.empty(bool_0, dict_1)
        var_0 = streaming_h_t_t_p_response_0.send(*list_0)
    except BaseException:
        pass