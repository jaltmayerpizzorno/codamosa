# Automatically generated by Pynguin.
import ansible.modules.apt_repository as module_0

def test_case_0():
    try:
        bytes_0 = b'\x8f\x0b\x0b\xa5\xb52\xf0\xb2,9Kl\x95(\x1d\xef\xab\x1c'
        int_0 = -2461
        var_0 = module_0.install_python_apt(bytes_0, int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        tuple_0 = None
        sources_list_0 = module_0.SourcesList(tuple_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = 250
        ubuntu_sources_list_0 = module_0.UbuntuSourcesList(int_0)
    except BaseException:
        pass

def test_case_3():
    try:
        invalid_source_0 = module_0.InvalidSource()
        var_0 = module_0.get_add_ppa_signing_key_callback(invalid_source_0)
    except BaseException:
        pass

def test_case_4():
    try:
        dict_0 = {}
        list_0 = [dict_0, dict_0]
        str_0 = 'Y]z8:Z2Z`@`oc'
        var_0 = module_0.revert_sources_list(dict_0, list_0, str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '46'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
        dict_1 = {str_0: str_0, str_0: str_0}
        list_0 = []
        var_0 = module_0.revert_sources_list(dict_0, dict_1, list_0)
    except BaseException:
        pass