# Automatically generated by Pynguin.
import httpie.cli.argtypes as module_0
import httpie.cli.requestitems as module_1

def test_case_0():
    try:
        str_0 = None
        str_1 = '(,\r(\\/0!_#{'
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_0, str_1)
        str_2 = module_1.process_empty_header_arg(key_value_arg_0)
        var_0 = module_1.process_data_embed_raw_json_file_arg(key_value_arg_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '\r\n7U\t'
        str_1 = '`y2F'
        str_2 = '7^\\2*vG3:?KMQDs'
        str_3 = 'Encoded HTTP message stream.\n\n    The message bytes are converted to an encoding suitable for\n    `self.env.stdout`. Unicode errors are replaced and binary data\n    is suppressed. The body is always streamed by line.\n\n    '
        str_4 = 'QE;pL6r\x0bY7FZ\n%1'
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_2, str_3, str_4)
        optional_0 = module_1.process_header_arg(key_value_arg_0)
        str_5 = None
        str_6 = 'w)'
        key_value_arg_1 = module_0.KeyValueArg(str_1, str_0, str_5, str_6)
        str_7 = module_1.process_data_item_arg(key_value_arg_1)
        str_8 = module_1.process_query_param_arg(key_value_arg_1)
        var_0 = key_value_arg_1.__repr__()
        str_9 = "&'|RGXdernXY5Sux"
        key_value_arg_2 = module_0.KeyValueArg(str_9, str_2, str_2, str_2)
        str_10 = module_1.process_empty_header_arg(key_value_arg_2)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'kH;^d@'
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_0, str_0)
        tuple_0 = module_1.process_file_upload_arg(key_value_arg_0)
    except BaseException:
        pass

def test_case_3():
    try:
        key_value_arg_0 = None
        str_0 = module_1.process_data_item_arg(key_value_arg_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = None
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_0, str_0)
        str_1 = module_1.process_data_embed_file_contents_arg(key_value_arg_0)
    except BaseException:
        pass

def test_case_5():
    try:
        key_value_arg_0 = None
        var_0 = module_1.process_data_embed_raw_json_file_arg(key_value_arg_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'test.txt'
        str_1 = ''
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_1, str_0)
        str_2 = module_1.load_text_file(key_value_arg_0)
        var_0 = module_1.process_data_raw_json_embed_arg(key_value_arg_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = None
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_0, str_0)
        var_0 = module_1.process_data_embed_raw_json_file_arg(key_value_arg_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'XQr9#nNQF%o-ZK<'
        str_1 = 'a\x0b2>z'
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_1, str_0)
        var_0 = module_1.process_data_embed_raw_json_file_arg(key_value_arg_0)
    except BaseException:
        pass

def test_case_9():
    try:
        int_0 = -1525
        request_items_0 = module_1.RequestItems(int_0)
        str_0 = None
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_0, str_0)
        str_1 = module_1.load_text_file(key_value_arg_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = None
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_0, str_0)
        optional_0 = module_1.process_header_arg(key_value_arg_0)
        var_0 = module_1.process_data_embed_raw_json_file_arg(key_value_arg_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = 'Y1)'
        str_1 = 'https://'
        str_2 = None
        key_value_arg_0 = module_0.KeyValueArg(str_1, str_0, str_2, str_2)
        var_0 = module_1.load_json(key_value_arg_0, str_2)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = '7'
        str_1 = None
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_1, str_1)
        var_0 = module_1.process_data_raw_json_embed_arg(key_value_arg_0)
        var_1 = key_value_arg_0.__repr__()
        key_value_arg_1 = None
        var_2 = module_1.process_data_embed_raw_json_file_arg(key_value_arg_1)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = 'test.txt'
        str_1 = None
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_1, str_1)
        var_0 = module_1.process_data_embed_raw_json_file_arg(key_value_arg_0)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = ';type='
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_0, str_0)
        tuple_0 = module_1.process_file_upload_arg(key_value_arg_0)
    except BaseException:
        pass