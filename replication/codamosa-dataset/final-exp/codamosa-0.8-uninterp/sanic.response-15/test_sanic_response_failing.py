# Automatically generated by Pynguin.
import sanic.response as module_0
import pathlib as module_1
import sanic.models.protocol_types as module_2

def test_case_0():
    try:
        str_0 = 'ROZBSP'
        int_0 = -2649
        h_t_t_p_response_0 = module_0.json(str_0, int_0)
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
        var_0 = None
        streaming_h_t_t_p_response_0 = module_0.file_stream(str_0, str_0)
        var_1 = module_0.stream(dict_0, var_0)
        dict_1 = None
        streaming_h_t_t_p_response_1 = module_0.file_stream(str_0, dict_1)
        str_1 = 'do'
        optional_0 = None
        h_t_t_p_response_1 = module_0.raw(optional_0)
        h_t_t_p_response_2 = module_0.html(str_1)
        h_t_t_p_response_3 = module_0.text(str_1, int_0, dict_1)
        pure_path_0 = module_1.PurePath(**dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        base_h_t_t_p_response_0 = module_0.BaseHTTPResponse()
        str_0 = '"'
        list_0 = []
        int_0 = 3537
        h_t_t_p_response_0 = module_0.redirect(str_0, list_0, int_0)
        str_1 = None
        int_1 = 475
        h_t_t_p_response_1 = module_0.text(str_1, int_1)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'r~fZ\t'
        int_0 = 1203
        h_t_t_p_response_0 = module_0.raw(str_0, int_0, str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '\n        A handler that catches specific exceptions and outputs a response.\n\n        :param request: The current request object\n        :type request: :class:`SanicASGITestClient`\n        :param exception: The exception that was raised\n        :type exception: BaseException\n        :raises ServerError: response 500\n        '
        h_t_t_p_response_0 = module_0.redirect(str_0)
        str_1 = '^[/]*'
        int_0 = -2081
        h_t_t_p_response_1 = module_0.redirect(str_1, int_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bytes_0 = b'\x8f\xf4*\xac\xc5\x88l\xb0\xa0\xa3\xba'
        dict_0 = {}
        h_t_t_p_response_0 = module_0.html(bytes_0, dict_0)
        range_0 = module_2.Range()
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'ROZBSY'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
        var_0 = None
        streaming_h_t_t_p_response_0 = module_0.file_stream(str_0, str_0)
        var_1 = module_0.stream(dict_0, var_0)
        str_1 = 'd'
        h_t_t_p_response_0 = module_0.raw(var_0)
        h_t_t_p_response_1 = module_0.html(str_1)
        dict_1 = {}
        streaming_h_t_t_p_response_1 = module_0.StreamingHTTPResponse(dict_0, dict_1, str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '\\H!i$rfxR\\TTA'
        int_0 = 2549
        h_t_t_p_response_0 = module_0.html(str_0, int_0)
        int_1 = 416
        h_t_t_p_response_1 = module_0.raw(str_0, int_1, str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        callable_0 = None
        int_0 = 2066
        base_h_t_t_p_response_0 = module_0.BaseHTTPResponse()
        str_0 = 'before_start'
        list_0 = [str_0, callable_0]
        var_0 = module_0.stream(callable_0, int_0, base_h_t_t_p_response_0, str_0, list_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'WiZBSP'
        var_0 = None
        list_0 = [var_0]
        dict_0 = {}
        streaming_h_t_t_p_response_0 = module_0.file_stream(str_0, str_0)
        var_1 = streaming_h_t_t_p_response_0.send(*list_0, **dict_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'WiZBSP'
        int_0 = -2678
        h_t_t_p_response_0 = module_0.json(str_0, int_0)
        pure_path_0 = module_1.PurePath()
        streaming_h_t_t_p_response_0 = module_0.file_stream(pure_path_0, str_0, str_0)
        var_0 = None
        h_t_t_p_response_1 = module_0.raw(var_0)
        var_1 = None
        str_1 = None
        h_t_t_p_response_2 = module_0.html(str_1)
        int_1 = 1823
        var_2 = module_0.stream(h_t_t_p_response_2, int_1)
        list_0 = [var_1]
        dict_0 = {}
        h_t_t_p_response_3 = module_0.HTTPResponse()
        int_2 = -670
        bytes_0 = b'\xb7PSQ\xe8t\xd3E\xd6\xb1\x07\x9f\x0b\xf8\xfcB\x14\xd2'
        streaming_h_t_t_p_response_1 = module_0.file_stream(pure_path_0, int_2, int_0, str_0, bytes_0)
        var_3 = streaming_h_t_t_p_response_1.send(*list_0, **dict_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = ':\n2;59OM'
        int_0 = -532
        h_t_t_p_response_0 = module_0.file(str_0, int_0, str_0, str_0)
        int_1 = None
        h_t_t_p_response_0.send(int_1)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = 'deprecated'
        h_t_t_p_response_0 = module_0.file(str_0, str_0)
        none_type_0 = None
        h_t_t_p_response_0.send(none_type_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = 'WiZBSP'
        int_0 = -2649
        h_t_t_p_response_0 = module_0.json(str_0, int_0)
        callable_0 = None
        streaming_h_t_t_p_response_0 = module_0.StreamingHTTPResponse(callable_0)
        var_0 = None
        int_1 = 16384
        list_0 = [callable_0, streaming_h_t_t_p_response_0, callable_0, callable_0]
        h_t_t_p_response_1 = module_0.file(str_0, int_1, str_0, list_0, str_0)
        h_t_t_p_response_1.send(var_0)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = 'WiZBSP'
        int_0 = -2678
        h_t_t_p_response_0 = module_0.json(str_0, int_0)
        var_0 = None
        optional_0 = None
        h_t_t_p_response_1 = module_0.empty(optional_0)
        h_t_t_p_response_2 = module_0.raw(var_0)
        var_1 = None
        str_1 = None
        h_t_t_p_response_3 = module_0.html(str_1)
        int_1 = 1823
        var_2 = module_0.stream(h_t_t_p_response_3, int_1)
        list_0 = [var_1]
        dict_0 = {}
        h_t_t_p_response_4 = module_0.HTTPResponse(var_1)
        int_2 = -4980
        str_2 = 'Dez\\'
        str_3 = '*:oR^Q3I=,&~m"'
        str_4 = 'deprecated'
        str_5 = ''
        dict_1 = {str_3: str_3, str_3: str_2, str_4: str_5}
        streaming_h_t_t_p_response_0 = module_0.file_stream(str_1, int_2, int_1, str_2, dict_1, str_2)
        var_3 = streaming_h_t_t_p_response_0.send(*list_0, **dict_0)
    except BaseException:
        pass