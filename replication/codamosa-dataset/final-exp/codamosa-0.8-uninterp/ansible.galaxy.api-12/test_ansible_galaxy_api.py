# Automatically generated by Pynguin.
import ansible.galaxy.api as module_0
import urllib.error as module_1

def test_case_0():
    pass

def test_case_1():
    bytes_0 = b'*T\x97\xff\xaa\xa8] \x16*6\x9e\x91\xd4>\xb1\xf5'
    var_0 = module_0.is_rate_limit_exception(bytes_0)

def test_case_2():
    str_0 = 'http://example.com/galaxy/api.json'
    var_0 = module_0.get_cache_id(str_0)
    var_1 = module_0.get_cache_id(str_0)
    str_1 = 'http://example.com/galaxy/api.json#anchor'
    var_2 = module_0.get_cache_id(str_1)
    str_2 = 'http://example.com/galaxy/api.json?q=foo%20bar#anchor'
    var_3 = module_0.get_cache_id(str_2)
    str_3 = 'http://example.com:8080/galaxy/api.json'
    var_4 = module_0.get_cache_id(str_3)

def test_case_3():
    int_0 = 404
    str_0 = ''
    h_t_t_p_error_0 = module_1.HTTPError(str_0, int_0, str_0, str_0, str_0)
    galaxy_error_0 = module_0.GalaxyError(h_t_t_p_error_0, str_0)

def test_case_4():
    dict_0 = {}
    str_0 = 'e%/~Aud3XnO/M(^?r7.\\'
    list_0 = [str_0, str_0, str_0, dict_0]
    str_1 = 'a\\YjxI1X!U-'
    collection_version_metadata_0 = module_0.CollectionVersionMetadata(dict_0, str_0, dict_0, list_0, str_1, list_0)

def test_case_5():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    str_0 = '6Ovk4p0#fp'
    galaxy_a_p_i_0 = module_0.GalaxyAPI(bool_0, list_0, str_0)

def test_case_6():
    bool_0 = True
    int_0 = 1000
    list_0 = []
    str_0 = 'r VN#~\t-r '
    dict_0 = {str_0: int_0, str_0: int_0, str_0: str_0}
    galaxy_a_p_i_0 = module_0.GalaxyAPI(bool_0, int_0, list_0, dict_0)
    var_0 = galaxy_a_p_i_0.__unicode__()

def test_case_7():
    dict_0 = {}
    str_0 = '1U^o) \x0bmfRDEbBfiQk'
    str_1 = '\\~!%fc;Nn3kV1<Z.'
    dict_1 = {str_0: str_0, str_1: dict_0, str_0: str_0, str_0: dict_0}
    list_0 = [str_1, dict_0]
    str_2 = 'm17f_+JrT'
    bool_0 = True
    float_0 = 2.0
    galaxy_a_p_i_0 = module_0.GalaxyAPI(list_0, str_2, list_0, bool_0, float_0)
    var_0 = galaxy_a_p_i_0.__lt__(dict_1)
    list_1 = [str_1, str_1, str_1, dict_0]
    str_3 = 'a\\YjxI1X!U-'
    collection_version_metadata_0 = module_0.CollectionVersionMetadata(dict_0, str_3, dict_0, list_1, str_3, list_1)

def test_case_8():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    str_0 = '6Ovk4p0#fp'
    galaxy_a_p_i_0 = module_0.GalaxyAPI(bool_0, list_0, str_0)
    var_0 = galaxy_a_p_i_0.__repr__()

def test_case_9():
    galaxy_error_0 = None
    float_0 = 2.0
    var_0 = module_0.cache_lock(float_0)
    dict_0 = {float_0: var_0, galaxy_error_0: galaxy_error_0}
    list_0 = [float_0, float_0, galaxy_error_0, var_0]
    var_1 = module_0.g_connect(list_0)
    tuple_0 = ()
    list_1 = [dict_0, float_0, list_0]
    str_0 = ']C\nDk]'
    bool_0 = False
    str_1 = 'qh'
    dict_1 = {str_1: dict_0, str_1: list_1, str_1: float_0}
    bytes_0 = b'\xd2\xd0\xf3\xce\xe4\x9eB\x8e\xd1\xc0\xd2a\xf3'
    collection_version_metadata_0 = module_0.CollectionVersionMetadata(float_0, dict_1, bytes_0, dict_1, str_1, list_1)
    galaxy_a_p_i_0 = module_0.GalaxyAPI(tuple_0, list_1, dict_0, float_0, str_0, list_0, bool_0, str_0, list_0, collection_version_metadata_0)