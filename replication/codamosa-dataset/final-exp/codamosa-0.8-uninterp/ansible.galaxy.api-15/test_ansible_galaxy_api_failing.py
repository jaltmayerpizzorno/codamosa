# Automatically generated by Pynguin.
import ansible.galaxy.api as module_0

def test_case_0():
    try:
        galaxy_error_0 = None
        set_0 = {galaxy_error_0, galaxy_error_0, galaxy_error_0, galaxy_error_0}
        list_0 = [set_0, galaxy_error_0, set_0]
        bool_0 = True
        dict_0 = None
        int_0 = 181
        bytes_0 = b'\x9d\x1bR\x9c\xe0H\xd1km'
        tuple_0 = ()
        collection_metadata_0 = None
        galaxy_a_p_i_0 = module_0.GalaxyAPI(list_0, bool_0, dict_0, int_0, bytes_0, tuple_0, collection_metadata_0)
        var_0 = galaxy_a_p_i_0.__lt__(galaxy_a_p_i_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = False
        dict_0 = None
        var_0 = module_0.get_cache_id(dict_0)
        list_0 = [dict_0, bool_0]
        var_1 = module_0.is_rate_limit_exception(list_0)
        collection_metadata_0 = module_0.CollectionMetadata()
    except BaseException:
        pass