# Automatically generated by Pynguin.
import ansible.galaxy.api as module_0
import urllib.error as module_1

def test_case_0():
    pass

def test_case_1():
    str_0 = 'http://[2001:db8::1]:8080'
    var_0 = module_0.get_cache_id(str_0)
    str_1 = 'http://example.com:invalid'
    var_1 = module_0.get_cache_id(str_1)

def test_case_2():
    str_0 = 'http://example.com/api'
    str_1 = 'http://example.com/api/v2'
    int_0 = 400
    h_t_t_p_error_0 = module_1.HTTPError(str_1, int_0, str_0, str_0, str_0)
    galaxy_error_0 = module_0.GalaxyError(h_t_t_p_error_0, str_0)

def test_case_3():
    str_0 = 'https://galaxy.ansible.com'
    galaxy_a_p_i_0 = module_0.GalaxyAPI(str_0, str_0, str_0)

def test_case_4():
    str_0 = "7K9MTr:8eGJs'Bn[>"
    bytes_0 = b'O\x03C\x8b%'
    tuple_0 = (bytes_0,)
    dict_0 = {bytes_0: str_0}
    list_0 = [str_0, dict_0, bytes_0]
    bytes_1 = b'\x972\x875J\xdaG\x9b\x87\xffb9Rh\xf7\xd3'
    galaxy_a_p_i_0 = module_0.GalaxyAPI(str_0, tuple_0, dict_0, bytes_0, list_0, bytes_1, dict_0)
    var_0 = galaxy_a_p_i_0.__repr__()

def test_case_5():
    bytes_0 = b'lF\xabOU\xa6\xc4M\xbe2w&'
    var_0 = module_0.is_rate_limit_exception(bytes_0)

def test_case_6():
    str_0 = "7K9MTr:8eGJs'Bn[>"
    bytes_0 = b'O\x03C\x8b%'
    tuple_0 = (bytes_0,)
    dict_0 = {bytes_0: str_0}
    list_0 = [str_0, dict_0, bytes_0]
    bytes_1 = b'\x972\x875J\xdaG\x9b\x87\xffb9Rh\xf7\xd3'
    galaxy_a_p_i_0 = module_0.GalaxyAPI(str_0, tuple_0, dict_0, bytes_0, list_0, bytes_1, dict_0)
    var_0 = galaxy_a_p_i_0.__lt__(str_0)

def test_case_7():
    str_0 = '8JHW?|paB(1'
    dict_0 = {str_0: str_0}
    list_0 = [dict_0, str_0, dict_0]
    list_1 = [str_0]
    float_0 = -1515.02921
    galaxy_a_p_i_0 = module_0.GalaxyAPI(str_0, dict_0, list_0, list_1, float_0)
    var_0 = galaxy_a_p_i_0.__unicode__()

def test_case_8():
    str_0 = 'http://example.com/api'
    int_0 = 404
    str_1 = 'Not Found'
    h_t_t_p_error_0 = module_1.HTTPError(str_0, int_0, str_1, str_0, str_0)
    str_2 = 'Resource not found'
    galaxy_error_0 = module_0.GalaxyError(h_t_t_p_error_0, str_2)
    int_1 = 400
    h_t_t_p_error_1 = module_1.HTTPError(str_1, int_1, str_2, str_2, str_2)