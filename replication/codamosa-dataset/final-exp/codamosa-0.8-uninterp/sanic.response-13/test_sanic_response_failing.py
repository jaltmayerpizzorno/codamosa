# Automatically generated by Pynguin.
import sanic.response as module_0
import sanic.models.protocol_types as module_1
import sanic.compat as module_2
import pathlib as module_3

def test_case_0():
    try:
        float_0 = 0.001
        dict_0 = {}
        var_0 = module_0.stream(float_0, dict_0)
        h_t_m_l_protocol_0 = module_1.HTMLProtocol()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '1'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
        list_0 = [dict_0, str_0, str_0]
        list_1 = [list_0, list_0, list_0]
        h_t_t_p_response_0 = module_0.html(str_0)
        h_t_t_p_response_1 = module_0.empty()
        float_0 = 1042.3
        int_0 = 248
        tuple_0 = (list_1, h_t_t_p_response_0, float_0, int_0)
        int_1 = 2032
        streaming_h_t_t_p_response_0 = module_0.StreamingHTTPResponse(tuple_0, int_1, str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b"f'x\x05\x85M\x8f\xe2\xe1N\xe2g\xa7-\xc9"
        int_0 = 1435
        none_type_0 = None
        str_0 = '\nKebd'
        h_t_t_p_response_0 = module_0.json(bytes_0, int_0, none_type_0, str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '1'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
        list_0 = [dict_0, str_0, str_0]
        h_t_t_p_response_0 = module_0.html(str_0)
        int_0 = -679
        h_t_t_p_response_1 = module_0.json(list_0, int_0)
        header_0 = module_2.Header()
        h_t_m_l_protocol_0 = module_1.HTMLProtocol()
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = 8192
        bool_0 = True
        h_t_t_p_response_0 = module_0.HTTPResponse(int_0, bool_0)
        str_0 = None
        h_t_t_p_response_1 = module_0.text(str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '('
        int_0 = 2979
        h_t_t_p_response_0 = module_0.redirect(str_0, int_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '1'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
        list_0 = [dict_0, str_0, str_0]
        list_1 = [list_0, list_0, list_0]
        list_2 = [list_1, str_0, dict_0]
        h_t_t_p_response_0 = module_0.html(str_0)
        float_0 = 1042.3
        int_0 = 248
        tuple_0 = (list_2, h_t_t_p_response_0, float_0, int_0)
        int_1 = 2032
        streaming_h_t_t_p_response_0 = module_0.StreamingHTTPResponse(tuple_0, int_1, str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        callable_0 = None
        str_0 = '" not found.'
        str_1 = '\n    Render a response for the default FALLBACK exception handler.\n    '
        str_2 = '[!I!0e1phUVO^:I?'
        str_3 = 'q.H\x0cK'
        set_0 = None
        h_t_t_p_response_0 = module_0.empty(set_0)
        dict_0 = {str_0: str_0, str_1: str_0, str_2: str_1, str_3: callable_0}
        str_4 = '_&UL@%e+%c62(."@#JP'
        str_5 = '|}z.#e>rrz_H \'\\"'
        str_6 = '+<*kA\\U?YWJ*\n\x0b#;c\n'
        str_7 = '5'
        str_8 = 'xt'
        str_9 = 'zWg125'
        none_type_0 = None
        base_h_t_t_p_response_0 = module_0.BaseHTTPResponse()
        str_10 = None
        h_t_t_p_response_1 = module_0.raw(none_type_0, base_h_t_t_p_response_0, str_10)
        dict_1 = {str_4: str_5, str_9: str_6, str_7: str_4, str_8: str_9}
        h_t_t_p_response_2 = module_0.json(dict_0, dict_1)
        int_0 = -2091
        bytes_0 = b'\xad\x9c\xd1\xb4\xc3\xdb\n\xdb\xdf\xd4\x9b\xfbB\xe6\xc4`\xc8Z\xb7\x19'
        str_11 = '\t\x0c\tKPwKT/`'
        str_12 = 'My.0'
        dict_2 = {str_11: h_t_t_p_response_2, str_12: str_10}
        h_t_t_p_response_3 = module_0.json(str_0, int_0, dict_1, str_3, bytes_0, **dict_2)
    except BaseException:
        pass

def test_case_8():
    try:
        bool_0 = None
        list_0 = [bool_0]
        pure_path_0 = module_3.PurePath()
        int_0 = -324
        streaming_h_t_t_p_response_0 = module_0.file_stream(pure_path_0, int_0)
        var_0 = streaming_h_t_t_p_response_0.send(*list_0)
    except BaseException:
        pass

def test_case_9():
    try:
        bool_0 = None
        list_0 = [bool_0]
        pure_path_0 = module_3.PurePath()
        int_0 = -324
        str_0 = "4uu*.[r7^h0qUc#\x0c'.1"
        str_1 = ':\\JeqXd'
        dict_0 = {str_0: str_0, str_0: str_1}
        streaming_h_t_t_p_response_0 = module_0.file_stream(pure_path_0, int_0, dict_0, list_0)
        var_0 = streaming_h_t_t_p_response_0.send(*list_0)
    except BaseException:
        pass