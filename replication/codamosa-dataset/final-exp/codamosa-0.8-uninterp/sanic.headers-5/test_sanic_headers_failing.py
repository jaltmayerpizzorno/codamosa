# Automatically generated by Pynguin.
import sanic.headers as module_0

def test_case_0():
    try:
        str_0 = '\n    The router implementation responsible for routing a :class:`Request` object\n    to the appropriate handler.\n    '
        set_0 = {str_0, str_0}
        optional_0 = module_0.parse_forwarded(str_0, set_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = ']'
        set_0 = None
        optional_0 = module_0.parse_xforwarded(str_0, set_0)
    except BaseException:
        pass

def test_case_2():
    try:
        float_0 = 3418.640823
        dict_0 = module_0.fwd_normalize(float_0)
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
        str_0 = 'form-data; name=upload; filename="file.txt"'
        tuple_0 = module_0.parse_content_header(str_0)
        int_0 = 244
        bytes_0 = module_0.format_http1_response(int_0, tuple_0)
    except BaseException:
        pass

def test_case_5():
    try:
        dict_0 = None
        dict_1 = {dict_0: dict_0, dict_0: dict_0, dict_0: dict_0}
        dict_2 = module_0.fwd_normalize(dict_1)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'I\x0c~+;^/-V'
        str_1 = module_0.fwd_normalize_address(str_0)
        tuple_0 = module_0.parse_content_header(str_0)
        str_2 = 'nH'
        str_3 = '_[|O'
        str_4 = module_0.fwd_normalize_address(str_3)
        dict_0 = {str_2: str_1, str_3: tuple_0}
        dict_1 = module_0.fwd_normalize(dict_0)
    except BaseException:
        pass

def test_case_7():
    try:
        set_0 = set()
        str_0 = 'huCGDcF'
        tuple_0 = module_0.parse_host(str_0)
        dict_0 = module_0.fwd_normalize(set_0)
        tuple_1 = module_0.parse_content_header(str_0)
        str_1 = 'request_class'
        str_2 = module_0.fwd_normalize_address(str_1)
        dict_1 = module_0.fwd_normalize(str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'I\x0c~+;^/-V'
        str_1 = module_0.fwd_normalize_address(str_0)
        set_0 = set()
        str_2 = 'huCGDcF'
        int_0 = 10
        dict_0 = {}
        bytes_0 = module_0.format_http1_response(int_0, dict_0)
        tuple_0 = module_0.parse_host(str_2)
        tuple_1 = module_0.parse_host(str_1)
        str_3 = module_0.fwd_normalize_address(str_0)
        dict_1 = module_0.fwd_normalize(set_0)
        tuple_2 = module_0.parse_content_header(str_0)
        str_4 = 'n'
        tuple_3 = module_0.parse_content_header(str_4)
        str_5 = '_[|O'
        str_6 = module_0.fwd_normalize_address(str_5)
        str_7 = 'E\tRO~.1{-5M@1SB'
        tuple_4 = module_0.parse_host(str_7)
        dict_2 = {str_4: str_3, str_5: tuple_3}
        dict_3 = module_0.fwd_normalize(dict_2)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = '1:1:1:1::1:1'
        str_1 = module_0.fwd_normalize_address(str_0)
        str_2 = '1:F:1C1:1::1'
        str_3 = '0'
        var_0 = str_3 * str_2
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = 'by'
        str_1 = 'unknown'
        str_2 = (str_0, str_1)
        str_3 = [str_2]
        dict_0 = module_0.fwd_normalize(str_3)
        str_4 = '[::1]'
        str_5 = (str_0, str_4)
        str_6 = [str_5]
        var_0 = fwd_normalize(str_6)[str_0]
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = 'for'
        str_1 = 'statCic'
        str_2 = (str_0, str_1)
        str_3 = 'port'
        str_4 = '2('
        str_5 = (str_3, str_4)
        str_6 = 'host'
        str_7 = 'hostname'
        str_8 = (str_6, str_7)
        str_9 = 'proto'
        str_10 = (str_9, str_9)
        str_11 = 'path'
        str_12 = (str_11, str_4)
        str_13 = (str_2, str_5, str_8, str_10, str_12)
        dict_0 = module_0.fwd_normalize(str_13)
        str_14 = 'unknown'
        str_15 = (str_0, str_14)
        str_16 = 'invalid'
        str_17 = (str_3, str_16)
        str_18 = (str_6, str_7)
        str_19 = (str_9, str_9)
        str_20 = (str_11, str_2)
        str_21 = (str_15, str_17, str_18, str_19, str_20)
        dict_1 = module_0.fwd_normalize(str_21)
    except BaseException:
        pass