# Automatically generated by Pynguin.
import httpie.cli.requestitems as module_0
import httpie.cli.argtypes as module_1

def test_case_0():
    pass

def test_case_1():
    request_items_0 = module_0.RequestItems()

def test_case_2():
    str_0 = 'auto'
    key_value_arg_0 = module_1.KeyValueArg(str_0, str_0, str_0, str_0)
    optional_0 = module_0.process_header_arg(key_value_arg_0)

def test_case_3():
    str_0 = ''
    str_1 = 'KN\x0b'
    str_2 = '`kCx+Vf!$tWR!g?n01'
    key_value_arg_0 = module_1.KeyValueArg(str_0, str_0, str_1, str_2)
    str_3 = module_0.process_query_param_arg(key_value_arg_0)

def test_case_4():
    str_0 = '[0,1,2]'
    str_1 = 'l!1<!)2iZ'
    str_2 = 'SQfOiJ'
    key_value_arg_0 = module_1.KeyValueArg(str_0, str_0, str_1, str_2)
    var_0 = module_0.process_data_raw_json_embed_arg(key_value_arg_0)

def test_case_5():
    str_0 = 'test.txt'
    key_value_arg_0 = module_1.KeyValueArg(str_0, str_0, str_0, str_0)
    tuple_0 = module_0.process_file_upload_arg(key_value_arg_0)