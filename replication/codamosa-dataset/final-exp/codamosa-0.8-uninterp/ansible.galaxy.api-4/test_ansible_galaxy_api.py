# Automatically generated by Pynguin.
import ansible.galaxy.api as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'Will not manage /etc/crontab via cron_file, see documentation.'
    var_0 = module_0.is_rate_limit_exception(str_0)

def test_case_2():
    str_0 = 'https://galaxy.ansible.com:80Q0/api'
    var_0 = module_0.get_cache_id(str_0)

def test_case_3():
    collection_version_metadata_0 = None
    var_0 = module_0.is_rate_limit_exception(collection_version_metadata_0)
    list_0 = None
    str_0 = 'wSx/$R'
    bytes_0 = b'\x03E\x7f\xca\x90\xdfeP]\xbfd\x0e{d0;\xbef~'
    str_1 = "'V+=aI;i{(_"
    dict_0 = {str_0: bytes_0, str_1: str_1, str_0: var_0}
    int_0 = 525
    bool_0 = True
    collection_version_metadata_1 = module_0.CollectionVersionMetadata(bytes_0, dict_0, collection_version_metadata_0, int_0, bool_0, bool_0)
    var_1 = module_0.get_cache_id(list_0)

def test_case_4():
    str_0 = 'user]ame'
    bool_0 = False
    galaxy_a_p_i_0 = module_0.GalaxyAPI(str_0, str_0, str_0)

def test_case_5():
    int_0 = 70
    bool_0 = True
    str_0 = 'V7*I0~Jbo<k,$?m6_yO'
    bool_1 = False
    bool_2 = True
    dict_0 = {}
    bool_3 = None
    tuple_0 = (bool_3, str_0)
    galaxy_a_p_i_0 = module_0.GalaxyAPI(bool_2, dict_0, tuple_0)
    galaxy_a_p_i_1 = module_0.GalaxyAPI(int_0, bool_0, str_0, bool_1, galaxy_a_p_i_0, int_0, galaxy_a_p_i_0, dict_0, str_0)
    var_0 = galaxy_a_p_i_1.__str__()

def test_case_6():
    int_0 = 4423
    bytes_0 = b"\xcdmv\x93[\xe3e\x86'R\x1f\xe5\n+\x80q\xbf"
    str_0 = '+{_+/0;'
    dict_0 = {str_0: bytes_0}
    galaxy_a_p_i_0 = module_0.GalaxyAPI(int_0, bytes_0, dict_0)
    var_0 = galaxy_a_p_i_0.__unicode__()

def test_case_7():
    str_0 = 'user]ame'
    bool_0 = True
    galaxy_a_p_i_0 = module_0.GalaxyAPI(str_0, str_0, str_0)
    int_0 = 1417
    var_0 = galaxy_a_p_i_0.__lt__(int_0)

def test_case_8():
    int_0 = 70
    bool_0 = True
    str_0 = 'V7*I0~Jbo<k,$?m6_yO'
    bool_1 = False
    bool_2 = True
    dict_0 = {}
    bool_3 = None
    tuple_0 = (bool_3, str_0)
    galaxy_a_p_i_0 = module_0.GalaxyAPI(bool_2, dict_0, tuple_0)
    dict_1 = {str_0: str_0, str_0: tuple_0}
    str_1 = '9'
    galaxy_a_p_i_1 = module_0.GalaxyAPI(int_0, bool_0, str_0, bool_1, galaxy_a_p_i_0, int_0, galaxy_a_p_i_0, dict_1, str_1)
    var_0 = galaxy_a_p_i_1.__str__()

def test_case_9():
    str_0 = 'https://galaxy.ansible.com/api/'
    var_0 = module_0.get_cache_id(str_0)
    str_1 = 'https://galaxy.ansible.com:8080/api'
    var_1 = module_0.get_cache_id(str_1)