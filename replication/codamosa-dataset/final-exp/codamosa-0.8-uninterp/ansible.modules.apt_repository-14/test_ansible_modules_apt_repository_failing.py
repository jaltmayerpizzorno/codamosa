# Automatically generated by Pynguin.
import ansible.modules.apt_repository as module_0

def test_case_0():
    try:
        ubuntu_sources_list_0 = None
        set_0 = {ubuntu_sources_list_0, ubuntu_sources_list_0, ubuntu_sources_list_0}
        var_0 = module_0.install_python_apt(ubuntu_sources_list_0, set_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = None
        sources_list_0 = module_0.SourcesList(int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = False
        int_0 = -241
        ubuntu_sources_list_0 = module_0.UbuntuSourcesList(bool_0, int_0)
    except BaseException:
        pass

def test_case_3():
    try:
        invalid_source_0 = module_0.InvalidSource()
        set_0 = {invalid_source_0, invalid_source_0, invalid_source_0}
        var_0 = module_0.get_add_ppa_signing_key_callback(set_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bytes_0 = b'{\x12'
        str_0 = None
        str_1 = '(.U}'
        dict_0 = {str_0: bytes_0, str_1: bytes_0}
        str_2 = '__main__'
        var_0 = module_0.revert_sources_list(bytes_0, dict_0, str_2)
    except BaseException:
        pass