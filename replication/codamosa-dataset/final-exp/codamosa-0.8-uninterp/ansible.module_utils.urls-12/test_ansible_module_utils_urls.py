# Automatically generated by Pynguin.
import ansible.module_utils.urls as module_0
import urllib.request as module_1

def test_case_0():
    pass

def test_case_1():
    str_0 = '3k(p"Poh1@B6QH'
    var_0 = module_0.generic_urlparse(str_0)

def test_case_2():
    bool_0 = True
    var_0 = module_0.atexit_remove_file(bool_0)

def test_case_3():
    str_0 = 'https://ww-.go glL.com'
    bool_0 = True
    var_0 = module_0.maybe_add_ssl_handler(str_0, bool_0)

def test_case_4():
    dict_0 = {}
    request_0 = module_0.Request(dict_0)

def test_case_5():
    dict_0 = {}
    var_0 = module_0.prepare_multipart(dict_0)

def test_case_6():
    str_0 = '+jOwpl'
    dict_0 = {str_0: str_0}
    request_0 = module_0.Request(dict_0)

def test_case_7():
    str_0 = 'https://www.google.com/'
    var_0 = module_1.urlopen(str_0)

def test_case_8():
    str_0 = 'https:/github.com/ansible/nible'
    str_1 = '4t43'
    s_s_l_validation_handler_0 = module_0.SSLValidationHandler(str_0, str_1)
    var_0 = s_s_l_validation_handler_0.detect_no_proxy(str_0)

def test_case_9():
    float_0 = -431.17
    var_0 = module_0.get_channel_binding_cert_hash(float_0)

def test_case_10():
    str_0 = '\n        This is a helper loading function for the dependencies list,\n        which returns a list of RoleInclude objects\n        '
    var_0 = module_0.generic_urlparse(str_0)

def test_case_11():
    str_0 = "8;31:<oIs3\x0bn?C\\M1'd}"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    var_0 = module_0.prepare_multipart(dict_0)

def test_case_12():
    str_0 = 'https://www.google.com/'
    var_0 = module_1.urlopen(str_0)
    var_1 = module_0.getpeercert(var_0)