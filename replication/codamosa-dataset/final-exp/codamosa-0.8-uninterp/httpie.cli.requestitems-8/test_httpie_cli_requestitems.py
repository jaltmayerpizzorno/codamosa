# Automatically generated by Pynguin.
import httpie.cli.requestitems as module_0
import httpie.cli.argtypes as module_1

def test_case_0():
    pass

def test_case_1():
    request_items_0 = module_0.RequestItems()

def test_case_2():
    str_0 = '\x0bvv$\\TkL(0#P41200Sq'
    str_1 = 'FUKoT)x'
    key_value_arg_0 = module_1.KeyValueArg(str_0, str_0, str_1, str_0)
    optional_0 = module_0.process_header_arg(key_value_arg_0)

def test_case_3():
    var_0 = None
    str_0 = '{"abc": 123}'
    str_1 = '--data "{"abc": 123}"'
    str_2 = '='
    key_value_arg_0 = module_1.KeyValueArg(var_0, str_0, str_2, str_1)
    var_1 = module_0.process_data_raw_json_embed_arg(key_value_arg_0)