# Automatically generated by Pynguin.
import sanic.headers as module_0

def test_case_0():
    try:
        bytes_0 = b'+\x87\xd5@\x1f\x14Ao\xe4\xb8$'
        dict_0 = {bytes_0: bytes_0}
        optional_0 = module_0.parse_forwarded(bytes_0, dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        dict_0 = None
        optional_0 = module_0.parse_xforwarded(dict_0, dict_0)
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
        int_0 = 413
        bytes_0 = module_0.format_http1_response(int_0, int_0)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = 0
        float_0 = -164.78712
        set_0 = {float_0, float_0, float_0}
        bytes_0 = module_0.format_http1_response(int_0, set_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'twIm<pl?=uYYd/\\Bfv'
        dict_0 = module_0.fwd_normalize(str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '192.168.2.120'
        str_1 = module_0.fwd_normalize_address(str_0)
        str_2 = '192.168.2.120/32'
        str_3 = module_0.fwd_normalize_address(str_2)
        str_4 = '_1:abc:123:def:456:789:1:2:3:4'
        str_5 = module_0.fwd_normalize_address(str_4)
        str_6 = 'example.com'
        str_7 = module_0.fwd_normalize_address(str_6)
        str_8 = 'example.com/32'
        str_9 = module_0.fwd_normalize_address(str_8)
        str_10 = '_example-com'
        str_11 = module_0.fwd_normalize_address(str_10)
        str_12 = 'unknown'
        str_13 = module_0.fwd_normalize_address(str_12)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'by'
        str_1 = '192.168.1.1'
        str_2 = [str_0]
        str_3 = (str_0, str_1)
        str_4 = (str_2, str_1)
        str_5 = [str_3, str_4]
        dict_0 = module_0.fwd_normalize(str_5)
    except BaseException:
        pass

def test_case_8():
    try:
        int_0 = -479
        dict_0 = {}
        bytes_0 = module_0.format_http1_response(int_0, dict_0)
        tuple_0 = ()
        str_0 = 'S\t-qi&C'
        optional_0 = module_0.parse_xforwarded(tuple_0, str_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = '12.34.56.78'
        str_1 = module_0.fwd_normalize_address(str_0)
        str_2 = '_12.34.56.78'
        str_3 = module_0.fwd_normalize_address(str_2)
        str_4 = '[::1]'
        str_5 = module_0.fwd_normalize_address(str_4)
        str_6 = '_[::1]'
        str_7 = module_0.fwd_normalize_address(str_6)
        str_8 = 'host'
        str_9 = 'example.com'
        str_10 = (str_8, str_9)
        str_11 = [str_10]
        dict_0 = module_0.fwd_normalize(str_11)
        dict_1 = module_0.fwd_normalize(str_10)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = 'Forwarded'
        str_1 = 'b'
        str_2 = module_0.fwd_normalize_address(str_1)
        str_3 = module_0.fwd_normalize_address(str_0)
        str_4 = 's'
        str_5 = module_0.fwd_normalize_address(str_4)
        str_6 = module_0.fwd_normalize_address(str_5)
        str_7 = 'unknown'
        str_8 = module_0.fwd_normalize_address(str_7)
    except BaseException:
        pass