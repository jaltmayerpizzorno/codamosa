# Automatically generated by Pynguin.
import ansible.module_utils.urls as module_0

def test_case_0():
    pass

def test_case_1():
    h_t_t_p_s_client_auth_handler_0 = module_0.HTTPSClientAuthHandler()

def test_case_2():
    int_0 = -776
    unix_h_t_t_p_connection_0 = module_0.UnixHTTPConnection(int_0)

def test_case_3():
    str_0 = 'L8,ykOY}P\r;u'
    dict_0 = {str_0: str_0}
    request_0 = module_0.Request(dict_0, str_0)
    request_with_method_0 = None
    unix_h_t_t_p_handler_0 = module_0.UnixHTTPHandler(request_with_method_0)
    s_s_l_validation_handler_0 = module_0.SSLValidationHandler(request_0, unix_h_t_t_p_handler_0)
    var_0 = s_s_l_validation_handler_0.get_ca_certs()

def test_case_4():
    parse_result_dotted_dict_0 = module_0.ParseResultDottedDict()

def test_case_5():
    parse_result_dotted_dict_0 = module_0.ParseResultDottedDict()
    var_0 = parse_result_dotted_dict_0.as_list()

def test_case_6():
    str_0 = '\x0ceixHDx'
    var_0 = module_0.generic_urlparse(str_0)

def test_case_7():
    list_0 = []
    proxy_error_0 = module_0.ProxyError(*list_0)
    s_s_l_validation_handler_0 = module_0.SSLValidationHandler(proxy_error_0, proxy_error_0)
    var_0 = s_s_l_validation_handler_0.get_ca_certs()

def test_case_8():
    parse_result_dotted_dict_0 = module_0.ParseResultDottedDict()
    var_0 = module_0.get_channel_binding_cert_hash(parse_result_dotted_dict_0)

def test_case_9():
    dict_0 = {}
    str_0 = 'Currnt:'
    request_0 = module_0.Request(dict_0, str_0)

def test_case_10():
    parse_result_dotted_dict_0 = module_0.ParseResultDottedDict()
    bool_0 = False
    var_0 = module_0.atexit_remove_file(bool_0)
    var_1 = module_0.RedirectHandlerFactory(parse_result_dotted_dict_0)
    var_2 = module_0.url_argument_spec()

def test_case_11():
    str_0 = 'R6b?;oeK'
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    request_0 = module_0.Request(dict_0, str_0)

def test_case_12():
    str_0 = 'L8,ykOY}P\r;'
    dict_0 = {}
    request_0 = module_0.Request(dict_0, str_0)
    s_s_l_validation_handler_0 = module_0.SSLValidationHandler(request_0, dict_0)
    bool_0 = None
    var_0 = s_s_l_validation_handler_0.detect_no_proxy(bool_0)

def test_case_13():
    str_0 = 'b={wlWT?gb3p,iZ'
    parse_result_dotted_dict_0 = module_0.ParseResultDottedDict()
    var_0 = parse_result_dotted_dict_0.as_list()
    list_0 = [str_0]
    bytes_0 = b'\xf8<\xadO%0\x06a\x0c\xc8\xd4\xcd\x96G\xd6W\x96\xe7'
    var_1 = module_0.generic_urlparse(bytes_0)
    custom_h_t_t_p_s_connection_0 = module_0.CustomHTTPSConnection(*list_0)

def test_case_14():
    parse_result_dotted_dict_0 = module_0.ParseResultDottedDict()
    var_0 = module_0.prepare_multipart(parse_result_dotted_dict_0)

def test_case_15():
    str_0 = 'v\n&%o'
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
    var_0 = module_0.prepare_multipart(dict_0)

def test_case_16():
    str_0 = 'b*JoQ'
    var_0 = module_0.atexit_remove_file(str_0)

def test_case_17():
    str_0 = '\n        Initializes this object with a valid Templar() object, as\n        well as several dictionaries of variables representing\n        different scopes (in jinja2 terminology).\n        '
    var_0 = module_0.generic_urlparse(str_0)

def test_case_18():
    str_0 = '\n    This test should test that the method __call__\n    of class UnixHTTPSConnection is actually returning self\n    '
    str_1 = '/tmp/unk'
    str_2 = 'example.org'
    int_0 = 443
    list_0 = [str_1, str_1, str_1]
    set_0 = {int_0, str_0, str_0, str_2}
    unix_h_t_t_p_connection_0 = module_0.UnixHTTPConnection(set_0)
    no_s_s_l_error_0 = module_0.NoSSLError()
    var_0 = unix_h_t_t_p_connection_0.__call__(*list_0)

def test_case_19():
    str_0 = 'file1'
    str_1 = 'file2'
    str_2 = 'text_form_field'
    str_3 = 'filename'
    str_4 = 'mime_type'
    str_5 = '/bin/true'
    str_6 = 'application/octet-stream'
    str_7 = {str_3: str_5, str_4: str_6}
    str_8 = 'content'
    str_9 = 'text based file content'
    str_10 = 'fake.txt'
    str_11 = 'text/plain'
    str_12 = {str_8: str_9, str_3: str_10, str_4: str_11}
    str_13 = 'value'
    str_14 = {str_0: str_7, str_1: str_12, str_2: str_13}
    var_0 = module_0.prepare_multipart(str_14)

def test_case_20():
    str_0 = 'file1'
    str_1 = 'file2'
    str_2 = 'text_form_field'
    str_3 = 'filename'
    str_4 = 'mime_type'
    str_5 = 'content'
    str_6 = 'text based file content'
    str_7 = 'fake.txt'
    str_8 = 'text/plain'
    str_9 = {str_5: str_6, str_3: str_7, str_4: str_8}
    str_10 = 'value'
    str_11 = {str_0: str_0, str_1: str_9, str_2: str_10}
    var_0 = module_0.prepare_multipart(str_11)