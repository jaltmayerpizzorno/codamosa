# Automatically generated by Pynguin.
import httpie.cli.argtypes as module_0
import httpie.cli.requestitems as module_1

def test_case_0():
    try:
        str_0 = '\x0b\\2]VVBC5}).7*Kk'
        none_type_0 = None
        key_value_arg_0 = module_0.KeyValueArg(str_0, none_type_0, str_0, str_0)
        optional_0 = module_1.process_header_arg(key_value_arg_0)
        var_0 = module_1.process_data_embed_raw_json_file_arg(key_value_arg_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '\n    By default, only the final request/response is shown. Use this flag to show\n    any intermediary requests/responses as well. Intermediary requests include\n    followed redirects (with --follow), the first unauthorized request when\n    Digest auth is used (--auth=digest), etc.\n\n    '
        str_1 = 'set-cookie'
        request_items_0 = module_1.RequestItems()
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_1, str_1, str_0)
        str_2 = module_1.process_empty_header_arg(key_value_arg_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = None
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_0, str_0)
        str_1 = module_1.process_empty_header_arg(key_value_arg_0)
        str_2 = module_1.process_data_embed_file_contents_arg(key_value_arg_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'Fh;T\rAb5('
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_0, str_0)
        str_1 = module_1.process_query_param_arg(key_value_arg_0)
        tuple_0 = module_1.process_file_upload_arg(key_value_arg_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = "=v'\nu5v:%W"
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_0, str_0)
        tuple_0 = module_1.process_file_upload_arg(key_value_arg_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = "=v'\nu5v:%W"
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_0, str_0)
        str_1 = module_1.process_data_item_arg(key_value_arg_0)
        tuple_0 = module_1.process_file_upload_arg(key_value_arg_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = None
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_0, str_0)
        str_1 = module_1.process_data_embed_file_contents_arg(key_value_arg_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'arg.value'
        var_0 = module_1.process_data_embed_raw_json_file_arg(str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'PBxqU\rkoQfm),'
        str_1 = '72?N'
        str_2 = ')\x0bJT3!u16\n!34$b\\Npk'
        str_3 = 'rF|zIuy|KLcBY'
        key_value_arg_0 = module_0.KeyValueArg(str_1, str_1, str_2, str_3)
        var_0 = key_value_arg_0.__repr__()
        str_4 = module_1.process_data_item_arg(key_value_arg_0)
        key_value_arg_1 = module_0.KeyValueArg(str_0, str_0, str_0, str_0)
        var_1 = module_1.process_data_raw_json_embed_arg(key_value_arg_1)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = ":Q-Q)Je\ntkH\x0c'%|B-"
        str_1 = 'X10y.b\r\t Hy=B9\nGtYiY'
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_1, str_0)
        var_0 = module_1.process_data_embed_raw_json_file_arg(key_value_arg_0)
    except BaseException:
        pass

def test_case_10():
    try:
        key_value_arg_0 = None
        str_0 = 'K{=]8tv\x0bbb^ra'
        var_0 = module_1.load_json(key_value_arg_0, str_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = '8$kG=KY ['
        str_1 = '"kckG6gD"00:2oF*}\'RW'
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_1, str_0)
        optional_0 = module_1.process_header_arg(key_value_arg_0)
        str_2 = '^u6\r4o84j}YA2Z8+D'
        key_value_arg_1 = module_0.KeyValueArg(str_2, str_2, str_2, str_2)
        tuple_0 = module_1.process_file_upload_arg(key_value_arg_1)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = None
        str_1 = 'p\nwyg5,mI3I2"DX'
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_1, str_1)
        var_0 = module_1.process_data_raw_json_embed_arg(key_value_arg_0)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = '\rZ3yzVw~H) L<%ey/p'
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_0, str_0)
        str_1 = module_1.process_data_item_arg(key_value_arg_0)
        bool_0 = True
        request_items_0 = module_1.RequestItems(bool_0)
        tuple_0 = module_1.process_file_upload_arg(key_value_arg_0)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = 'test.txt'
        str_1 = 'KJj1}2d+m'
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_0, str_1)
        tuple_0 = module_1.process_file_upload_arg(key_value_arg_0)
        var_0 = module_1.process_data_embed_raw_json_file_arg(key_value_arg_0)
    except BaseException:
        pass