# Automatically generated by Pynguin.
import sanic.response as module_0
import pathlib as module_1
import sanic.compat as module_2

def test_case_0():
    pass

def test_case_1():
    str_0 = '\n        Async iterate over request body.\n        '
    h_t_t_p_response_0 = module_0.redirect(str_0)

def test_case_2():
    str_0 = 'Could not generate a name for handler'
    h_t_t_p_response_0 = module_0.text(str_0)

def test_case_3():
    str_0 = 'request_class'
    streaming_h_t_t_p_response_0 = module_0.StreamingHTTPResponse(str_0)

def test_case_4():
    str_0 = '8f'
    h_t_t_p_response_0 = module_0.text(str_0)
    h_t_t_p_response_1 = module_0.empty(h_t_t_p_response_0)
    h_t_m_l_protocol_0 = None
    str_1 = 'Tk^9ZZlxN8'
    str_2 = '|\rT*'
    dict_0 = {str_1: str_1, str_1: str_2}
    h_t_t_p_response_2 = module_0.html(h_t_m_l_protocol_0, dict_0)

def test_case_5():
    h_t_m_l_protocol_0 = None
    h_t_t_p_response_0 = module_0.json(h_t_m_l_protocol_0)

def test_case_6():
    base_h_t_t_p_response_0 = module_0.BaseHTTPResponse()
    int_0 = 987
    h_t_m_l_protocol_0 = None
    streaming_h_t_t_p_response_0 = module_0.StreamingHTTPResponse(base_h_t_t_p_response_0, int_0, h_t_m_l_protocol_0)
    str_0 = ';{fssh=?]\nE#)Wok}'
    h_t_t_p_response_0 = module_0.raw(streaming_h_t_t_p_response_0, str_0)
    h_t_m_l_protocol_1 = None
    h_t_t_p_response_1 = module_0.html(h_t_m_l_protocol_1)

def test_case_7():
    h_t_m_l_protocol_0 = None
    h_t_t_p_response_0 = module_0.html(h_t_m_l_protocol_0)

def test_case_8():
    str_0 = '\x0bd~R0ab\x0b\x0bq:e '
    h_t_t_p_response_0 = module_0.html(str_0)

def test_case_9():
    callable_0 = None
    str_0 = 'rccea8 9k}z|'
    var_0 = module_0.stream(callable_0, str_0)

def test_case_10():
    bytes_0 = b'\x04J\xe0\x95a'
    h_t_t_p_response_0 = module_0.html(bytes_0)
    pure_path_0 = module_1.PurePath()
    h_t_t_p_response_1 = module_0.html(bytes_0)

def test_case_11():
    str_0 = '\r!0kI#~>."Cy|S8$LKg4'
    var_0 = module_0.stream(str_0)
    optional_0 = None
    h_t_t_p_response_0 = module_0.raw(optional_0)
    str_1 = '_name'
    h_t_t_p_response_1 = module_0.redirect(str_1)
    bytes_0 = b'\x19c5\x90|\xea\xdc\x08'
    str_2 = 'd'
    str_3 = None
    str_4 = ''
    list_0 = []
    bool_0 = False
    int_0 = 2944
    dict_0 = {}
    header_0 = module_2.Header(**dict_0)
    streaming_h_t_t_p_response_0 = module_0.StreamingHTTPResponse(bool_0, int_0, header_0, str_0, bytes_0)
    var_1 = streaming_h_t_t_p_response_0.write(list_0)
    str_5 = '\n        Update app.config. Full implementation can be found in the user guide.\n\n        `See user guide re: configuration\n        <https://sanicframework.org/guide/deployment/configuration.html#basics>`__\n        '
    dict_1 = {str_2: str_3, str_4: str_3, str_5: str_4, str_4: str_4}
    h_t_t_p_response_2 = module_0.empty()
    h_t_t_p_response_3 = module_0.empty(str_2, dict_1)
    str_6 = 'a'
    str_7 = None
    h_t_t_p_response_4 = module_0.html(str_3, dict_1)
    str_8 = '\n        Method to parse `query_string` using `urllib.parse.parse_qsl`.\n        This methods is used by `query_args` property.\n        Can be used directly if you need to change default parameters.\n\n        :param keep_blank_values:\n            flag indicating whether blank values in\n            percent-encoded queries should be treated as blank strings.\n            A true value indicates that blanks should be retained as blank\n            strings.  The default false value indicates that blank values\n            are to be ignored and treated as if they were  not included.\n        :type keep_blank_values: bool\n        :param strict_parsing:\n            flag indicating what to do with parsing errors.\n            If false (the default), errors are silently ignored. If true,\n            errors raise a ValueError exception.\n        :type strict_parsing: bool\n        :param encoding:\n            specify how to decode percent-encoded sequences\n            into Unicode characters, as accepted by the bytes.decode() method.\n        :type encoding: str\n        :param errors:\n            specify how to decode percent-encoded sequences\n            into Unicode characters, as accepted by the bytes.decode() method.\n        :type errors: str\n        :return: list\n        '
    h_t_t_p_response_5 = module_0.json(str_7)
    h_t_t_p_response_6 = module_0.empty(dict_1)
    h_t_t_p_response_7 = module_0.text(str_8, str_6)
    str_9 = "'Q$_w:"
    h_t_t_p_response_8 = module_0.redirect(str_9, dict_1)