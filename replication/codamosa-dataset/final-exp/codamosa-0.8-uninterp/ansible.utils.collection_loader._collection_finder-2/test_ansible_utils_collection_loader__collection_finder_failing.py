# Automatically generated by Pynguin.
import ansible.utils.collection_loader._collection_finder as module_0

def test_case_0():
    try:
        ansible_collection_finder_0 = module_0._AnsibleCollectionFinder()
        str_0 = ',4wC#92T"lL)A\\q'
        ansible_collection_pkg_loader_base_0 = module_0._AnsibleCollectionPkgLoaderBase(str_0, str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'ansible_collections.ansible'
        ansible_collection_finder_0 = module_0._AnsibleCollectionFinder()
        ansible_collection_root_pkg_loader_0 = module_0._AnsibleCollectionRootPkgLoader(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'ansible_collections.ansible'
        str_1 = '/tmp/collction'
        ansible_collection_pkg_loader_base_0 = module_0._AnsibleCollectionPkgLoaderBase(str_0, str_1)
        str_2 = '/tmp/collection/ansible/plugins/collection'
        var_0 = ansible_collection_pkg_loader_base_0.get_data(str_2)
        str_3 = 'The vault-ids %s are available to encrypt. Specify the vault-id to encrypt with --encrypt-vault-id'
        var_1 = ansible_collection_pkg_loader_base_0.iter_modules(str_3)
        ansible_collection_n_s_pkg_loader_0 = module_0._AnsibleCollectionNSPkgLoader(str_3)
    except BaseException:
        pass

def test_case_3():
    try:
        ansible_collection_finder_0 = module_0._AnsibleCollectionFinder()
        str_0 = 'Rl\\_5\x0c\x0b@cY'
        ansible_collection_loader_0 = module_0._AnsibleCollectionLoader(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'ansible.module4utils.si;'
        ansible_internal_redirect_loader_0 = module_0._AnsibleInternalRedirectLoader(str_0, str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 's.cl'
        ansible_collection_ref_0 = module_0.AnsibleCollectionRef(str_0, str_0, str_0, str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        ansible_collection_finder_0 = None
        tuple_0 = None
        ansible_collection_ref_0 = module_0.AnsibleCollectionRef(ansible_collection_finder_0, ansible_collection_finder_0, tuple_0, tuple_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'ansible_collections.ansible'
        ansible_collection_pkg_loader_base_0 = module_0._AnsibleCollectionPkgLoaderBase(str_0, str_0)
        var_0 = ansible_collection_pkg_loader_base_0.load_module(str_0)
        var_1 = ansible_collection_pkg_loader_base_0.__repr__()
        ansible_collection_finder_0 = module_0._AnsibleCollectionFinder(ansible_collection_pkg_loader_base_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'ansible_collections.ansible'
        ansible_collection_pkg_loader_base_0 = module_0._AnsibleCollectionPkgLoaderBase(str_0, str_0)
        str_1 = '/tmp/collection/ansible/plugins/collection'
        bool_0 = False
        float_0 = -1689.0
        bytes_0 = b'\x88\x9a\n\xf4\xe9\xa4\t\x83d\xfc\xf1-\r\xa7'
        tuple_0 = (bool_0, float_0, bytes_0)
        ansible_path_hook_finder_0 = module_0._AnsiblePathHookFinder(str_1, str_1)
        var_0 = ansible_path_hook_finder_0.find_module(tuple_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'ansible_collections.ansible'
        bool_0 = False
        ansible_collection_pkg_loader_0 = module_0._AnsibleCollectionPkgLoader(str_0, bool_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = 'ansib\re.modu\ne4utils.si;'
        ansible_internal_redirect_loader_0 = module_0._AnsibleInternalRedirectLoader(str_0, str_0)
    except BaseException:
        pass

def test_case_11():
    try:
        dict_0 = None
        ansible_collection_finder_0 = module_0._AnsibleCollectionFinder(dict_0)
        str_0 = 't'
        var_0 = ansible_collection_finder_0.find_module(str_0)
        bool_0 = False
        ansible_path_hook_finder_0 = module_0._AnsiblePathHookFinder(bool_0, dict_0)
        var_1 = ansible_path_hook_finder_0.iter_modules(bool_0)
        ansible_collection_pkg_loader_base_0 = module_0._AnsibleCollectionPkgLoaderBase(bool_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = 'T\\aBR2q'
        ansible_collection_finder_0 = module_0._AnsibleCollectionFinder()
        var_0 = ansible_collection_finder_0.set_playbook_paths(str_0)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = 'ansible_collections.ansible'
        str_1 = '/tmp/crllection'
        ansible_collection_pkg_loader_base_0 = module_0._AnsibleCollectionPkgLoaderBase(str_0, str_1)
        var_0 = ansible_collection_pkg_loader_base_0.get_data(str_0)
    except BaseException:
        pass

def test_case_14():
    try:
        dict_0 = None
        dict_1 = None
        ansible_collection_finder_0 = module_0._AnsibleCollectionFinder(dict_1, dict_0)
        str_0 = '[i'
        var_0 = ansible_collection_finder_0.find_module(str_0)
        str_1 = '1'
        str_2 = 'romisc'
        str_3 = 'Unknown or undocumentable plugin type: %s'
        var_1 = ansible_collection_finder_0.set_playbook_paths(str_2)
        set_0 = set()
        bytes_0 = b'\xfa\r\x1c\x98\x16'
        var_2 = ansible_collection_finder_0.set_playbook_paths(set_0)
        ansible_path_hook_finder_0 = module_0._AnsiblePathHookFinder(set_0, bytes_0)
        ansible_path_hook_finder_1 = module_0._AnsiblePathHookFinder(str_3, ansible_path_hook_finder_0)
        ansible_collection_ref_0 = module_0.AnsibleCollectionRef(str_1, str_2, ansible_path_hook_finder_1, dict_0)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = ')@$f+`#{uLZk;QQrewP-'
        int_0 = 3600
        tuple_0 = (int_0,)
        list_0 = [int_0, int_0, tuple_0, tuple_0]
        ansible_path_hook_finder_0 = module_0._AnsiblePathHookFinder(tuple_0, list_0)
        var_0 = ansible_path_hook_finder_0.find_module(str_0)
        str_1 = 'E_K_)]WM&WuhdC}joK'
        ansible_collection_finder_0 = module_0._AnsibleCollectionFinder()
        list_1 = [ansible_collection_finder_0, str_1]
        ansible_collection_loader_0 = module_0._AnsibleCollectionLoader(list_1)
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = 'ansible_collections.ansible'
        str_1 = 'I)i/K'
        ansible_collection_pkg_loader_base_0 = module_0._AnsibleCollectionPkgLoaderBase(str_0, str_1)
        str_2 = "'`yy).8+ir3"
        var_0 = ansible_collection_pkg_loader_base_0.iter_modules(str_2)
        var_1 = ansible_collection_pkg_loader_base_0.load_module(str_2)
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = 'ansible_collections.ansible'
        ansible_collection_pkg_loader_base_0 = module_0._AnsibleCollectionPkgLoaderBase(str_0, str_0)
        list_0 = []
        int_0 = 2392
        ansible_path_hook_finder_0 = module_0._AnsiblePathHookFinder(list_0, int_0)
        var_0 = ansible_collection_pkg_loader_base_0.get_source(ansible_path_hook_finder_0)
    except BaseException:
        pass

def test_case_18():
    try:
        str_0 = 'ansible_collections.ansible'
        str_1 = '/tmp/collection'
        ansible_collection_pkg_loader_base_0 = module_0._AnsibleCollectionPkgLoaderBase(str_0, str_1)
        str_2 = '130'
        var_0 = ansible_collection_pkg_loader_base_0.is_package(str_2)
    except BaseException:
        pass

def test_case_19():
    try:
        str_0 = 'ansible_collections.ansible'
        str_1 = '9\\sfs6'
        ansible_collection_pkg_loader_base_0 = module_0._AnsibleCollectionPkgLoaderBase(str_0, str_1)
        var_0 = ansible_collection_pkg_loader_base_0.load_module(str_1)
    except BaseException:
        pass

def test_case_20():
    try:
        str_0 = 'ansible_collections.ansible'
        ansible_collection_n_s_pkg_loader_0 = module_0._AnsibleCollectionNSPkgLoader(str_0)
    except BaseException:
        pass

def test_case_21():
    try:
        ansible_collection_finder_0 = module_0._AnsibleCollectionFinder()
        list_0 = [ansible_collection_finder_0, ansible_collection_finder_0, ansible_collection_finder_0]
        var_0 = ansible_collection_finder_0.set_playbook_paths(list_0)
    except BaseException:
        pass

def test_case_22():
    try:
        str_0 = 'ansible_collections.ansible'
        str_1 = '/mp/collection'
        ansible_collection_pkg_loader_base_0 = module_0._AnsibleCollectionPkgLoaderBase(str_0, str_1)
        ansible_collection_finder_0 = module_0._AnsibleCollectionFinder()
        list_0 = []
        var_0 = ansible_collection_pkg_loader_base_0.get_data(list_0)
    except BaseException:
        pass

def test_case_23():
    try:
        str_0 = 'namespace.collection'
        str_1 = 'subdir'
        str_2 = 'resource'
        str_3 = 'modules'
        ansible_collection_ref_0 = module_0.AnsibleCollectionRef(str_0, str_1, str_2, str_3)
        str_4 = 'namespace.collection'
        str_5 = 'subdir'
        str_6 = 'resource'
        str_7 = 'foo'
        ansible_collection_ref_1 = module_0.AnsibleCollectionRef(str_4, str_5, str_6, str_7)
    except BaseException:
        pass