# Automatically generated by Pynguin.
import sanic.response as module_0
import sanic.compat as module_1
import sanic.models.protocol_types as module_2

def test_case_0():
    try:
        dict_0 = {}
        h_t_t_p_response_0 = module_0.empty(dict_0)
        callable_0 = None
        var_0 = module_0.stream(callable_0)
        int_0 = -3314
        h_t_t_p_response_1 = module_0.json(h_t_t_p_response_0, int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = None
        int_0 = 410
        h_t_t_p_response_0 = module_0.html(bytes_0, int_0)
        str_0 = '`7k3m\r`p6 U'
        int_1 = -3059
        var_0 = None
        h_t_t_p_response_1 = module_0.raw(var_0)
        base_h_t_t_p_response_0 = module_0.BaseHTTPResponse()
        base_h_t_t_p_response_0.send(h_t_t_p_response_1)
        int_2 = -741
        streaming_h_t_t_p_response_0 = module_0.file_stream(str_0, int_1, int_1, str_0, int_2, str_0)
        str_1 = 'VmfH\nwB~^!+ysY<_%'
        int_3 = -403
        h_t_t_p_response_2 = module_0.redirect(str_1, int_3)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '`7k3m\r`p6 U'
        int_0 = -3059
        int_1 = -741
        streaming_h_t_t_p_response_0 = module_0.file_stream(str_0, int_0, int_0, str_0, int_1, str_0)
        str_1 = 'VmfH\nwB~^!+ysY<_%'
        int_2 = -403
        h_t_t_p_response_0 = module_0.redirect(str_1, int_2)
    except BaseException:
        pass

def test_case_3():
    try:
        header_0 = module_1.Header()
        int_0 = -183
        streaming_h_t_t_p_response_0 = module_0.StreamingHTTPResponse(header_0, int_0, header_0)
        str_0 = 'http'
        h_t_t_p_response_0 = module_0.redirect(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '<!DOCTYPE html><html lang=en><meta charset=UTF-8><title>{title}</title>\n<style>{style}</style>\n<h1>{title}</h1><p>{text}\n{body}'
        str_1 = 'p'
        dict_0 = {str_0: str_0, str_0: str_1, str_0: str_1}
        h_t_t_p_response_0 = module_0.HTTPResponse(dict_0, str_0)
        h_t_m_l_protocol_0 = module_2.HTMLProtocol()
    except BaseException:
        pass

def test_case_5():
    try:
        callable_0 = None
        int_0 = -1052
        str_0 = '~\rF\ra:Bk17@(_{c'
        int_1 = None
        h_t_t_p_response_0 = module_0.json(callable_0, int_1)
        var_0 = module_0.stream(callable_0, int_0, str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        int_0 = 3
        h_t_t_p_response_0 = module_0.text(int_0)
    except BaseException:
        pass

def test_case_7():
    try:
        int_0 = None
        str_0 = 'vO/FRk\tK`G|V\nmT'
        list_0 = [int_0]
        streaming_h_t_t_p_response_0 = module_0.file_stream(str_0, int_0, str_0, str_0)
        var_0 = streaming_h_t_t_p_response_0.send(*list_0)
    except BaseException:
        pass

def test_case_8():
    try:
        int_0 = None
        str_0 = ''
        list_0 = [int_0]
        streaming_h_t_t_p_response_0 = module_0.file_stream(str_0, int_0, str_0, str_0)
        var_0 = streaming_h_t_t_p_response_0.send(*list_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = '{hA6^]oza\\`^h(A\n'
        float_0 = None
        str_1 = None
        str_2 = None
        dict_0 = {str_1: str_1, str_2: float_0, str_1: str_2}
        str_3 = '=DlqXYf)@'
        h_t_t_p_response_0 = module_0.raw(dict_0, str_3)
        str_4 = 'x,U-bs` ",\r`e",'
        int_0 = 404
        dict_1 = None
        str_5 = None
        set_0 = {float_0, float_0, float_0}
        var_0 = module_0.stream(str_4, int_0, dict_1, str_5, set_0)
        str_6 = "]'yn7 ]\t}.95n^n^}+^E"
        h_t_t_p_response_1 = module_0.text(str_6, str_6)
        str_7 = ',_05NR'
        h_t_t_p_response_2 = module_0.text(str_0, float_0, str_7)
    except BaseException:
        pass

def test_case_10():
    try:
        int_0 = None
        str_0 = ''
        list_0 = []
        h_t_t_p_response_0 = module_0.empty(list_0)
        h_t_t_p_response_1 = module_0.json(str_0, str_0)
        list_1 = [int_0]
        streaming_h_t_t_p_response_0 = module_0.file_stream(str_0, int_0, str_0, str_0, h_t_t_p_response_1)
        callable_0 = None
        var_0 = module_0.stream(callable_0)
        str_1 = '|L*X>o'
        bool_0 = False
        h_t_t_p_response_2 = module_0.redirect(str_1, bool_0, str_1)
        str_2 = None
        h_t_t_p_response_3 = module_0.html(str_2)
        h_t_t_p_response_4 = module_0.text(str_0)
        streaming_h_t_t_p_response_1 = module_0.StreamingHTTPResponse(callable_0, str_2)
        var_1 = streaming_h_t_t_p_response_0.send(*list_1)
    except BaseException:
        pass

def test_case_11():
    try:
        int_0 = None
        str_0 = '\n    Returns response object with body in json format.\n\n    :param body: Response data to be serialized.\n    :param status: Response code.\n    :param headers: Custom Headers.\n    :param kwargs: Remaining arguments that are passed to the json encoder.\n    '
        int_1 = None
        h_t_t_p_response_0 = module_0.redirect(str_0, int_1, str_0)
        str_1 = ''
        h_t_t_p_response_1 = module_0.json(str_1, str_1)
        list_0 = [int_0]
        streaming_h_t_t_p_response_0 = module_0.file_stream(str_1, int_0, str_1, str_1)
        callable_0 = None
        var_0 = module_0.stream(callable_0)
        str_2 = '[i,K.,}kg*<X@,'
        int_2 = 1706
        str_3 = '\\<"@M[an.>R'
        dict_0 = {str_1: int_2, str_2: str_2, str_3: list_0}
        header_0 = module_1.Header(**dict_0)
        bool_0 = True
        dict_1 = {}
        h_t_t_p_response_2 = module_0.json(str_2, int_2, header_0, str_2, bool_0, **dict_1)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = "zr@j.4aJ'Xa]f9}v9"
        range_0 = None
        h_t_t_p_response_0 = module_0.file(str_0, str_0, range_0)
        h_t_t_p_response_1 = module_0.text(str_0)
        float_0 = None
        h_t_t_p_response_0.send(float_0)
    except BaseException:
        pass