# Automatically generated by Pynguin.
import ansible.galaxy.api as module_0

def test_case_0():
    float_0 = -2228.41
    var_0 = module_0.is_rate_limit_exception(float_0)

def test_case_1():
    str_0 = '\n74FQX`'
    var_0 = module_0.get_cache_id(str_0)

def test_case_2():
    bool_0 = False
    str_0 = '\tUuW^;'
    list_0 = None
    var_0 = module_0.get_cache_id(list_0)
    int_0 = -1081
    list_1 = [str_0, bool_0, str_0, bool_0]
    collection_metadata_0 = module_0.CollectionMetadata(*list_1)
    bool_1 = True
    bytes_0 = None
    var_1 = module_0.is_rate_limit_exception(str_0)
    galaxy_a_p_i_0 = module_0.GalaxyAPI(int_0, str_0, collection_metadata_0, list_0, bool_1, bytes_0, str_0)
    collection_metadata_1 = module_0.CollectionMetadata(*list_1)
    var_2 = galaxy_a_p_i_0.__lt__(list_1)
    bool_2 = None
    int_1 = 308
    collection_version_metadata_0 = module_0.CollectionVersionMetadata(bool_2, int_1, bytes_0, galaxy_a_p_i_0, str_0, galaxy_a_p_i_0)

def test_case_3():
    str_0 = 'K$bbzq\x0c]NuPm]}x'
    list_0 = [str_0, str_0]
    galaxy_a_p_i_0 = module_0.GalaxyAPI(str_0, str_0, list_0, str_0)

def test_case_4():
    str_0 = '\tUuW^;'
    dict_0 = {}
    list_0 = [str_0]
    bytes_0 = b'\xf6H\xc4y\xf2V\xa6\xdb\x11\x94\xe8\xc3\xce]'
    galaxy_a_p_i_0 = module_0.GalaxyAPI(dict_0, list_0, bytes_0)
    var_0 = galaxy_a_p_i_0.__repr__()

def test_case_5():
    str_0 = '3CBr/J\\G|-yzaa,v)'
    str_1 = 'mJkvl'
    str_2 = ',p|>uw6dp'
    list_0 = [str_1, str_0]
    galaxy_a_p_i_0 = module_0.GalaxyAPI(str_1, str_2, list_0, str_2)
    var_0 = galaxy_a_p_i_0.__unicode__()
    collection_version_metadata_0 = None
    var_1 = module_0.get_cache_id(collection_version_metadata_0)

def test_case_6():
    bool_0 = False
    str_0 = 'Lv]vj'
    list_0 = [str_0, str_0]
    galaxy_a_p_i_0 = module_0.GalaxyAPI(str_0, str_0, list_0, str_0)
    var_0 = galaxy_a_p_i_0.__lt__(bool_0)

def test_case_7():
    int_0 = 1856
    bytes_0 = b'y\xfe\x02x\x13\xba\xda\xb4\xd1\xe3O\xe48\x7f'
    bool_0 = True
    galaxy_a_p_i_0 = module_0.GalaxyAPI(int_0, bytes_0, bool_0, int_0)
    var_0 = galaxy_a_p_i_0.__repr__()
    str_0 = 'mJkvl'
    str_1 = 'Lv]vj'
    bool_1 = None
    list_0 = None
    str_2 = '{V3yUNbt9\rN'
    dict_0 = None
    collection_metadata_0 = None
    collection_version_metadata_0 = module_0.CollectionVersionMetadata(list_0, str_2, galaxy_a_p_i_0, galaxy_a_p_i_0, dict_0, collection_metadata_0)
    set_0 = {galaxy_a_p_i_0, list_0, var_0}
    str_3 = 'Cache updated'
    dict_1 = {str_1: str_3}
    collection_version_metadata_1 = module_0.CollectionVersionMetadata(bool_1, collection_version_metadata_0, set_0, str_3, collection_version_metadata_0, dict_1)
    var_1 = module_0.cache_lock(collection_version_metadata_1)
    str_4 = 'K$bbzq\x0c]NuP]}x'
    list_1 = [str_4, str_1]
    galaxy_a_p_i_1 = module_0.GalaxyAPI(str_4, str_0, list_1, str_0)
    var_2 = galaxy_a_p_i_1.__unicode__()
    collection_version_metadata_2 = None
    collection_version_metadata_3 = None
    str_5 = '^EaZ\\i*p^iUp=w/Q*9Y'
    var_3 = module_0.get_cache_id(str_5)
    var_4 = module_0.get_cache_id(collection_version_metadata_3)
    bool_2 = True
    var_5 = module_0.is_rate_limit_exception(bool_2)
    float_0 = -1743.85
    str_6 = 'unicode_wrap'
    galaxy_a_p_i_2 = module_0.GalaxyAPI(dict_1, float_0, dict_1, str_6, galaxy_a_p_i_1, dict_1, bool_1, int_0, collection_version_metadata_2)
    str_7 = '&2p+>Y4S^3 }'
    var_6 = galaxy_a_p_i_2.__lt__(str_7)

def test_case_8():
    str_0 = 'https://example.com:8080/path'
    var_0 = module_0.get_cache_id(str_0)

def test_case_9():
    str_0 = 'https://example.com:8080\npath'
    var_0 = module_0.get_cache_id(str_0)