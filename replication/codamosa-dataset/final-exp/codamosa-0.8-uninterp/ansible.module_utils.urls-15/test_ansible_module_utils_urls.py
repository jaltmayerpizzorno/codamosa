# Automatically generated by Pynguin.
import ansible.module_utils.urls as module_0

def test_case_0():
    pass

def test_case_1():
    request_0 = None
    missing_module_error_0 = module_0.MissingModuleError(request_0, request_0)

def test_case_2():
    h_t_t_p_s_client_auth_handler_0 = module_0.HTTPSClientAuthHandler()

def test_case_3():
    str_0 = 'C 4<\x0c Dq'
    var_0 = module_0.get_channel_binding_cert_hash(str_0)

def test_case_4():
    request_0 = module_0.Request()

def test_case_5():
    str_0 = 'H'
    custom_h_t_t_p_s_connection_0 = None
    s_s_l_validation_handler_0 = module_0.SSLValidationHandler(str_0, custom_h_t_t_p_s_connection_0)
    var_0 = s_s_l_validation_handler_0.detect_no_proxy(custom_h_t_t_p_s_connection_0)
    var_1 = s_s_l_validation_handler_0.get_ca_certs()

def test_case_6():
    dict_0 = {}
    var_0 = module_0.prepare_multipart(dict_0)
    h_t_t_p_s_client_auth_handler_0 = module_0.HTTPSClientAuthHandler()
    connection_error_0 = module_0.ConnectionError()

def test_case_7():
    str_0 = 'fetch_url_tZt.txt'
    var_0 = module_0.atexit_remove_file(str_0)

def test_case_8():
    request_0 = module_0.Request()
    str_0 = 'GET'
    str_1 = 'https://ww.google.com'
    var_0 = request_0.open(str_0, str_1)