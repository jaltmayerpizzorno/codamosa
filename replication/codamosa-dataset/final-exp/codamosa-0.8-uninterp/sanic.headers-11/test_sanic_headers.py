# Automatically generated by Pynguin.
import sanic.headers as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'HUvpl5I(3U'
    tuple_0 = module_0.parse_content_header(str_0)

def test_case_2():
    str_0 = 'b\r!$(xbZ11bw8{AaU'
    str_1 = module_0.fwd_normalize_address(str_0)

def test_case_3():
    str_0 = 'Az'
    tuple_0 = module_0.parse_host(str_0)
    str_1 = 'b\r!$(xbZ11bw8{AaU'
    str_2 = module_0.fwd_normalize_address(str_1)

def test_case_4():
    str_0 = '\n    Returns response object with body in html format.\n\n    :param body: str or bytes-ish, or an object with __html__ or _repr_html_.\n    :param status: Response code.\n    :param hepders: Custom Headers.\n    '
    tuple_0 = module_0.parse_host(str_0)

def test_case_5():
    str_0 = '`EMu`LwV.pr'
    str_1 = '>{2%wY<M]#('
    tuple_0 = module_0.parse_host(str_1)
    int_0 = 372
    tuple_1 = module_0.parse_content_header(str_0)
    tuple_2 = ()
    bytes_0 = module_0.format_http1_response(int_0, tuple_2)
    str_2 = 'l'
    tuple_3 = module_0.parse_host(str_2)
    str_3 = '/m%D-o'
    str_4 = module_0.fwd_normalize_address(str_3)

def test_case_6():
    str_0 = 'q~st'
    str_1 = 'for'
    str_2 = 'proto'
    str_3 = ' HTTP '
    str_4 = (str_1, str_0)
    str_5 = (str_0, str_0)
    str_6 = '80'
    str_7 = (str_3, str_6)
    str_8 = 'http'
    str_9 = (str_2, str_8)
    str_10 = [str_4, str_5, str_7, str_9]
    dict_0 = module_0.fwd_normalize(str_10)

def test_case_7():
    str_0 = 'example.com'
    tuple_0 = module_0.parse_host(str_0)
    str_1 = 'example.com:80'
    tuple_1 = module_0.parse_host(str_1)

def test_case_8():
    str_0 = 'q~st'
    str_1 = '  HoKt4  '
    str_2 = (str_0, str_1)
    str_3 = 'Uoqfr'
    str_4 = (str_3, str_2)
    str_5 = 'port'
    tuple_0 = module_0.parse_host(str_3)
    str_6 = ')8B@0~'
    str_7 = (str_5, str_6)
    str_8 = 'pCt_'
    str_9 = [str_2, str_4, str_7, str_4]
    dict_0 = module_0.fwd_normalize(str_9)
    str_10 = (str_3, str_3)
    str_11 = (str_0, str_0)
    str_12 = '80'
    str_13 = (str_5, str_12)
    str_14 = 'http'
    str_15 = (str_8, str_14)
    str_16 = [str_10, str_11, str_13, str_15]
    dict_1 = module_0.fwd_normalize(str_16)