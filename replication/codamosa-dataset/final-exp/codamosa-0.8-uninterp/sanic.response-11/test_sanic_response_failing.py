# Automatically generated by Pynguin.
import sanic.response as module_0
import sanic.compat as module_1
import pathlib as module_2
import sanic.models.protocol_types as module_3

def test_case_0():
    try:
        str_0 = '\n        Sanitize the Blueprint Entity to override the Version and strict slash\n        behaviors as required.\n\n        :param bp: Sanic Blueprint entity Object\n        :return: Modified Blueprint\n        '
        str_1 = None
        h_t_t_p_response_0 = module_0.html(str_1)
        var_0 = None
        bytes_0 = b"\xae\xee\x8ca$YB\x1bg7'R%"
        dict_0 = {str_0: h_t_t_p_response_0, str_0: h_t_t_p_response_0}
        header_0 = module_1.Header(**dict_0)
        tuple_0 = (h_t_t_p_response_0, var_0, bytes_0, header_0)
        h_t_t_p_response_1 = module_0.empty(tuple_0)
        dict_1 = None
        list_0 = [dict_1]
        streaming_h_t_t_p_response_0 = module_0.file_stream(str_0)
        var_1 = streaming_h_t_t_p_response_0.send(*list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        base_h_t_t_p_response_0 = module_0.BaseHTTPResponse()
        base_h_t_t_p_response_0.send()
        list_0 = []
        pure_path_0 = module_2.PurePath(*list_0)
        str_0 = "'pWM2"
        h_t_t_p_response_0 = module_0.json(pure_path_0, str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'hello'
        callable_0 = None
        dict_0 = None
        var_0 = module_0.stream(callable_0, dict_0)
        str_1 = 'world'
        str_2 = {str_0: str_1}
        str_3 = [str_0, str_1]
        bool_0 = False
        h_t_t_p_response_0 = module_0.json(str_3)
        h_t_t_p_response_1 = module_0.redirect(str_2)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = ''
        h_t_t_p_response_0 = module_0.text(str_0)
        range_0 = module_3.Range()
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'Z2=a-T\rK'
        int_0 = -1292
        h_t_t_p_response_0 = module_0.redirect(str_0, int_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = ''
        str_1 = 'zk'
        h_t_t_p_response_0 = module_0.redirect(str_1)
        h_t_t_p_response_1 = module_0.text(str_0)
        streaming_h_t_t_p_response_0 = module_0.file_stream(str_0)
        h_t_t_p_response_2 = module_0.html(str_0)
        h_t_t_p_response_3 = module_0.html(str_0)
        dict_0 = {}
        pure_path_0 = module_2.PurePath(**dict_0)
        base_h_t_t_p_response_0 = module_0.BaseHTTPResponse()
        list_0 = [h_t_t_p_response_1, h_t_t_p_response_3, h_t_t_p_response_2, base_h_t_t_p_response_0]
        h_t_m_l_protocol_0 = module_3.HTMLProtocol(*list_0)
    except BaseException:
        pass

def test_case_6():
    try:
        header_0 = module_1.Header()
        int_0 = -2250
        str_0 = '~~,\r> M\rL'
        h_t_t_p_response_0 = module_0.HTTPResponse(int_0, str_0)
        str_1 = '2T:'
        var_0 = header_0.get_all(str_1)
        int_1 = 416
        bool_0 = True
        streaming_h_t_t_p_response_0 = module_0.StreamingHTTPResponse(header_0, int_1, bool_0)
    except BaseException:
        pass

def test_case_7():
    try:
        h_t_m_l_protocol_0 = None
        int_0 = -346
        str_0 = 'tKo)g|nU1%5xO3^O3d'
        str_1 = '?'
        str_2 = None
        str_3 = 'U-@2K8J*YSZ>L`W@\n7h\n'
        str_4 = '-js5_QDl$n<BAwf'
        dict_0 = {str_0: str_0, str_1: str_2, str_3: str_4, str_2: str_0}
        h_t_t_p_response_0 = module_0.html(h_t_m_l_protocol_0, int_0, dict_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = None
        str_1 = 'deprecated'
        str_2 = None
        str_3 = None
        str_4 = 'l~dRG=_\t#'
        dict_0 = {str_0: str_1, str_2: str_1, str_3: str_3, str_0: str_4}
        h_t_t_p_response_0 = module_0.text(str_0, dict_0, str_3)
    except BaseException:
        pass

def test_case_9():
    try:
        bytes_0 = b'\xc8'
        int_0 = 2909
        str_0 = 'L<dfslK2Ik8v>[VB'
        str_1 = 'vRUf?{\x0cuS+=Q'
        str_2 = '`YS^lm'
        str_3 = '{\x0bl\\$Ry};'
        dict_0 = {str_0: str_1, str_0: str_2, str_3: str_2}
        str_4 = '37u<!]m:qIx&Zih'
        dict_1 = {str_4: bytes_0}
        h_t_t_p_response_0 = module_0.json(bytes_0, int_0, dict_0, str_4, dict_1)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = ':'
        dict_0 = None
        list_0 = [dict_0]
        streaming_h_t_t_p_response_0 = module_0.file_stream(str_0)
        var_0 = streaming_h_t_t_p_response_0.send(*list_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = '\n        Sanitize the Blueprint Entity to override the Version and strict slash\n        behaviors as required.\n\n        :param bp: Sanic Blueprint entity Object\n        :return: Modified Blueprint\n        '
        str_1 = None
        h_t_t_p_response_0 = module_0.html(str_1)
        bytes_0 = b"\xae\xee\x8ca$YB\x1bg7'R%"
        dict_0 = None
        list_0 = [dict_0]
        list_1 = [str_0]
        list_2 = [bytes_0, list_1]
        int_0 = -1857
        streaming_h_t_t_p_response_0 = module_0.file_stream(str_0, str_1, list_2, str_1, int_0)
        var_0 = streaming_h_t_t_p_response_0.send(*list_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = None
        str_1 = '1\':8."7"yg#zr&#v[&r@'
        dict_0 = {str_1: str_0}
        h_t_t_p_response_0 = module_0.html(str_0, dict_0)
        h_t_t_p_response_1 = module_0.text(str_1, str_0)
        dict_1 = None
        list_0 = [dict_1]
        str_2 = '~$\x0bQSM9`b6Hkr'
        int_0 = 423
        str_3 = 'deprected'
        str_4 = 'pT^=>s5&/5+G;{&DK\t'
        dict_2 = {str_3: str_4, str_1: str_3}
        streaming_h_t_t_p_response_0 = module_0.file_stream(str_2, int_0, str_0, dict_2)
        var_0 = streaming_h_t_t_p_response_0.send(*list_0)
    except BaseException:
        pass