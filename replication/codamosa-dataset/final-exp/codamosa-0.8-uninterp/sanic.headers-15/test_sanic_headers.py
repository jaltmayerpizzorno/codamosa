# Automatically generated by Pynguin.
import sanic.headers as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = ']wBC <\x0b4\n is'
    tuple_0 = module_0.parse_content_header(str_0)

def test_case_2():
    str_0 = 'https'
    str_1 = (str_0, str_0)
    str_2 = 'host'
    str_3 = 'm.sanic.vn'
    str_4 = (str_2, str_3)
    str_5 = [str_1, str_4]
    dict_0 = module_0.fwd_normalize(str_5)

def test_case_3():
    str_0 = '_T]&{{f '
    str_1 = module_0.fwd_normalize_address(str_0)

def test_case_4():
    str_0 = 'request_middleware'
    str_1 = module_0.fwd_normalize_address(str_0)

def test_case_5():
    str_0 = 'Sd'
    tuple_0 = module_0.parse_host(str_0)

def test_case_6():
    str_0 = 'RO{~i#g'
    tuple_0 = module_0.parse_host(str_0)

def test_case_7():
    str_0 = 'form-data; name=upload; filename="file.txt"'
    str_1 = 'Checking the data:'
    var_0 = print(str_1, str_0)
    tuple_0 = module_0.parse_content_header(str_0)
    str_2 = 'Please check the result: '
    var_1 = print(str_2, tuple_0)

def test_case_8():
    str_0 = 'secret'
    str_1 = 'obfuscated'
    str_2 = (str_0, str_1)
    str_3 = 'by'
    str_4 = (str_3, str_1)
    str_5 = [str_2, str_4]
    dict_0 = module_0.fwd_normalize(str_5)
    str_6 = (str_0, str_1)
    str_7 = 'for'
    str_8 = (str_7, str_1)
    str_9 = [str_6, str_8]
    dict_1 = module_0.fwd_normalize(str_9)
    str_10 = (str_7, str_1)
    str_11 = (str_0, str_1)
    str_12 = [str_10, str_11]
    dict_2 = module_0.fwd_normalize(str_12)
    str_13 = (str_3, str_1)
    str_14 = (str_0, str_1)
    str_15 = [str_13, str_14]
    dict_3 = module_0.fwd_normalize(str_15)