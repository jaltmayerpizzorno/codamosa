# Automatically generated by Pynguin.
import ansible.modules.apt_repository as module_0

def test_case_0():
    pass

def test_case_1():
    int_0 = -5017
    var_0 = module_0.main()
    sources_list_0 = module_0.SourcesList(int_0)
    var_1 = sources_list_0.dump()
    int_1 = 307
    dict_0 = None
    str_0 = '-m1*sUW\x0c6f/\n+/c\x0b\\'
    str_1 = 'J.tN2'
    dict_1 = {str_0: int_1, str_0: var_0, str_1: var_1}
    var_2 = module_0.revert_sources_list(str_0, dict_1, int_0)
    ubuntu_sources_list_0 = module_0.UbuntuSourcesList(dict_0)
    var_3 = sources_list_0.save()
    var_4 = ubuntu_sources_list_0.__deepcopy__()
    sources_list_1 = module_0.SourcesList(ubuntu_sources_list_0)
    sources_list_2 = module_0.SourcesList(int_1)
    var_5 = sources_list_2.dump()