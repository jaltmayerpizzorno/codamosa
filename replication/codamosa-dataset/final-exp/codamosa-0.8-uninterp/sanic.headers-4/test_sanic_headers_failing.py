# Automatically generated by Pynguin.
import sanic.headers as module_0

def test_case_0():
    try:
        bytes_0 = b'\xd6/\xa2\xdaGuG\xf6\x0b\x9b%\x99\x9b\xc3'
        list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
        str_0 = 'tyqv.SzF%'
        str_1 = '7\x0b5X0_B6smeD'
        str_2 = module_0.fwd_normalize_address(str_1)
        optional_0 = module_0.parse_forwarded(list_0, str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        set_0 = set()
        list_0 = None
        optional_0 = module_0.parse_xforwarded(set_0, list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        iterable_0 = None
        dict_0 = module_0.fwd_normalize(iterable_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = None
        str_1 = module_0.fwd_normalize_address(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = -923
        iterable_0 = None
        str_0 = 'ag&s'
        tuple_0 = module_0.parse_host(str_0)
        bytes_0 = module_0.format_http1_response(int_0, iterable_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bytes_0 = b'~\xd23\xeen\xf0\xf0'
        dict_0 = module_0.fwd_normalize(bytes_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'xSSG'
        str_1 = '$LV~B{ qcOqs"Z'
        tuple_0 = module_0.parse_content_header(str_1)
        tuple_1 = module_0.parse_content_header(str_0)
        dict_0 = {str_0: str_0, str_0: str_0}
        int_0 = -2
        bytes_0 = module_0.format_http1_response(int_0, dict_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'unknown'
        str_1 = module_0.fwd_normalize_address(str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = '$SMi7KKFLA}x'
        dict_0 = {str_0: str_0}
        tuple_0 = module_0.parse_host(str_0)
        str_1 = 'Y'
        str_2 = "12'5l|S"
        str_3 = module_0.fwd_normalize_address(str_2)
        tuple_1 = module_0.parse_host(str_1)
        int_0 = 191
        str_4 = '_future_middleware'
        list_0 = [tuple_1, str_4, int_0, dict_0]
        dict_1 = module_0.fwd_normalize(list_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'by'
        str_1 = 'http://localhost:8080/test/?test=123'
        str_2 = (str_0, str_1)
        str_3 = '_exception'
        str_4 = '192.168.0.1'
        str_5 = (str_3, str_4)
        str_6 = 'host'
        str_7 = 's'
        str_8 = (str_6, str_7)
        str_9 = 'proto'
        str_10 = 'http'
        str_11 = (str_9, str_10)
        str_12 = 'port'
        str_13 = (str_12, str_0)
        str_14 = 'path'
        str_15 = (str_14, str_2)
        str_16 = [str_2, str_5, str_8, str_11, str_13, str_15]
        dict_0 = module_0.fwd_normalize(str_16)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = 'for'
        str_1 = '192.0.2.1'
        str_2 = (str_0, str_1)
        str_3 = [str_2]
        dict_0 = module_0.fwd_normalize(str_3)
        str_4 = (str_0, str_1)
        str_5 = 'by'
        str_6 = '2001:db8::1'
        str_7 = (str_5, str_6)
        str_8 = [str_4, str_7]
        dict_1 = module_0.fwd_normalize(str_8)
        str_9 = 'host'
        str_10 = 'example.com'
        str_11 = (str_9, str_10)
        str_12 = [str_11]
        dict_2 = module_0.fwd_normalize(str_12)
        str_13 = 'proto'
        str_14 = (str_13, str_8)
        str_15 = [str_14]
        dict_3 = module_0.fwd_normalize(str_15)
    except BaseException:
        pass