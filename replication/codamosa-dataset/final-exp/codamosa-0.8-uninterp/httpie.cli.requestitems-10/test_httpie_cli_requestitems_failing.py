# Automatically generated by Pynguin.
import httpie.cli.argtypes as module_0
import httpie.cli.requestitems as module_1

def test_case_0():
    try:
        str_0 = None
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_0, str_0)
        optional_0 = module_1.process_header_arg(key_value_arg_0)
        str_1 = module_1.load_text_file(key_value_arg_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = "G',(wj(G:"
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_0, str_0)
        str_1 = module_1.process_empty_header_arg(key_value_arg_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'z?muiA;*P4'
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_0, str_0)
        str_1 = module_1.process_query_param_arg(key_value_arg_0)
        tuple_0 = module_1.process_file_upload_arg(key_value_arg_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '&x'
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_0, str_0)
        tuple_0 = module_1.process_file_upload_arg(key_value_arg_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = "!C'7jDvLw+H"
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_0, str_0)
        str_1 = module_1.process_data_item_arg(key_value_arg_0)
        tuple_0 = module_1.process_file_upload_arg(key_value_arg_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'D-I3uz=\\XK3J3GazLi>-'
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_0, str_0)
        str_1 = module_1.process_data_embed_file_contents_arg(key_value_arg_0)
    except BaseException:
        pass

def test_case_6():
    try:
        var_0 = None
        key_value_arg_0 = module_0.KeyValueArg(var_0, var_0, var_0, var_0)
        var_1 = module_1.process_data_embed_raw_json_file_arg(key_value_arg_0)
    except BaseException:
        pass

def test_case_7():
    try:
        request_items_0 = module_1.RequestItems()
        str_0 = None
        str_1 = '$.'
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_0, str_1)
        var_0 = module_1.process_data_raw_json_embed_arg(key_value_arg_0)
    except BaseException:
        pass

def test_case_8():
    try:
        var_0 = None
        key_value_arg_0 = module_0.KeyValueArg(var_0, var_0, var_0, var_0)
        str_0 = module_1.load_text_file(key_value_arg_0)
    except BaseException:
        pass

def test_case_9():
    try:
        request_items_0 = module_1.RequestItems()
        str_0 = ''
        str_1 = None
        str_2 = 'HTTPIE_CONFIG_DIR'
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_1, str_2)
        var_0 = module_1.load_json(key_value_arg_0, str_1)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = '\n    Data items from the command line are serialized as form fields.\n\n    The Content-Type is set to application/x-www-form-urlencoded (if not\n    specified). The presence of any file fields results in a\n    multipart/form-data request.\n\n    '
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_0, str_0)
        var_0 = module_1.load_json(key_value_arg_0, str_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = '{N~eyx:9u|`l'
        request_items_0 = module_1.RequestItems(str_0)
        str_1 = None
        str_2 = '1fBT#SObzm9s'
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_1, str_1, str_2)
        var_0 = key_value_arg_0.__repr__()
        str_3 = module_1.load_text_file(key_value_arg_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = "!C'7jDvLw+H"
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_0, str_0)
        str_1 = module_1.process_data_item_arg(key_value_arg_0)
        optional_0 = module_1.process_header_arg(key_value_arg_0)
        tuple_0 = module_1.process_file_upload_arg(key_value_arg_0)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = '0.9'
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_0, str_0)
        var_0 = module_1.process_data_raw_json_embed_arg(key_value_arg_0)
        request_items_0 = module_1.RequestItems()
        str_1 = None
        key_value_arg_1 = module_0.KeyValueArg(str_1, str_1, str_1, str_1)
        request_items_1 = module_1.RequestItems()
        var_1 = module_1.process_data_embed_raw_json_file_arg(key_value_arg_1)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = ';type='
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_0, str_0)
        tuple_0 = module_1.process_file_upload_arg(key_value_arg_0)
    except BaseException:
        pass