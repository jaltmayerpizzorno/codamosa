# Automatically generated by Pynguin.
import ansible.galaxy.api as module_0
import urllib.error as module_1
import threading as module_2

def test_case_0():
    try:
        str_0 = '*'
        bool_0 = False
        list_0 = [bool_0, str_0]
        set_0 = {str_0}
        int_0 = -948
        int_1 = 496
        bool_1 = True
        bytes_0 = b'\x1a\xe0\xd0<\x97\x92\xc9o'
        galaxy_a_p_i_0 = module_0.GalaxyAPI(bool_0, list_0, set_0, int_0, int_1, str_0, str_0, bool_1, bytes_0)
        var_0 = module_0.is_rate_limit_exception(str_0)
        dict_0 = {var_0: var_0}
        float_0 = -86.433
        list_1 = [str_0]
        bool_2 = True
        str_1 = ' --no-block'
        h_t_t_p_error_0 = module_1.HTTPError(dict_0, float_0, list_1, bool_2, str_1)
        thread_0 = module_2.Thread()
        collection_metadata_0 = module_0.CollectionMetadata(*list_1)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'\xd6j\x84\xd9"\x0e\x93x\xb6\xcbHc\t\xf8'
        set_0 = {bytes_0, bytes_0, bytes_0, bytes_0}
        list_0 = []
        str_0 = 'Ug=ye'
        galaxy_a_p_i_0 = module_0.GalaxyAPI(str_0, list_0, bytes_0, set_0, str_0, bytes_0)
        float_0 = 15.954946413437845
        var_0 = module_0.is_rate_limit_exception(float_0)
        str_1 = '\x0c+EW'
        var_1 = module_0.get_cache_id(str_1)
        var_2 = galaxy_a_p_i_0.__lt__(galaxy_a_p_i_0)
    except BaseException:
        pass