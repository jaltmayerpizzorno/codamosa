# Automatically generated by Pynguin.
import ansible.utils.collection_loader._collection_finder as module_0

def test_case_0():
    try:
        ansible_collection_finder_0 = module_0._AnsibleCollectionFinder()
        bytes_0 = b'4t\xde'
        ansible_path_hook_finder_0 = module_0._AnsiblePathHookFinder(bytes_0, bytes_0)
        ansible_collection_pkg_loader_0 = module_0._AnsibleCollectionPkgLoader(ansible_path_hook_finder_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '/dumm\t-collections-base-path'
        ansible_collection_finder_0 = module_0._AnsibleCollectionFinder(str_0)
        str_1 = ')-'
        ansible_path_hook_finder_0 = module_0._AnsiblePathHookFinder(ansible_collection_finder_0, str_1)
        var_0 = ansible_collection_finder_0.set_playbook_paths(str_1)
        ansible_collection_root_pkg_loader_0 = module_0._AnsibleCollectionRootPkgLoader(str_1, str_1)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'SdZYNB5~UvsX\\Fa'
        ansible_collection_pkg_loader_0 = module_0._AnsibleCollectionPkgLoader(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'ABC.XYZ'
        str_1 = ''
        str_2 = 'role'
        ansible_collection_ref_0 = module_0.AnsibleCollectionRef(str_0, str_1, str_1, str_2)
        float_0 = 3065.223056
        ansible_internal_redirect_loader_0 = module_0._AnsibleInternalRedirectLoader(str_0, float_0)
    except BaseException:
        pass

def test_case_4():
    try:
        tuple_0 = ()
        float_0 = 0.2
        ansible_internal_redirect_loader_0 = module_0._AnsibleInternalRedirectLoader(tuple_0, float_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'ansible.module_utils.basic'
        ansible_internal_redirect_loader_0 = module_0._AnsibleInternalRedirectLoader(str_0, str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '/dummy-collections-base-path'
        str_1 = [str_0]
        ansible_collection_finder_0 = module_0._AnsibleCollectionFinder(str_1)
        ansible_path_hook_finder_0 = module_0._AnsiblePathHookFinder(ansible_collection_finder_0, str_1)
        str_2 = 'ansible_collections'
        var_0 = ansible_path_hook_finder_0.find_module(str_2)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'w\rmRbE\x0b|}'
        ansible_collection_n_s_pkg_loader_0 = module_0._AnsibleCollectionNSPkgLoader(str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        ansible_collection_finder_0 = module_0._AnsibleCollectionFinder()
        str_0 = 'ansible'
        var_0 = ansible_collection_finder_0.find_module(str_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'ABC.XYZ'
        str_1 = ''
        ansible_collection_ref_0 = module_0.AnsibleCollectionRef(str_0, str_1, str_1, str_1)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = 'role'
        ansible_collection_ref_0 = module_0.AnsibleCollectionRef(str_0, str_0, str_0, str_0)
    except BaseException:
        pass

def test_case_11():
    try:
        bytes_0 = b'\xe9\xd0'
        str_0 = '>#u{Q'
        list_0 = [bytes_0, bytes_0, str_0]
        ansible_collection_finder_0 = module_0._AnsibleCollectionFinder(list_0)
        var_0 = ansible_collection_finder_0.set_playbook_paths(list_0)
        ansible_collection_n_s_pkg_loader_0 = module_0._AnsibleCollectionNSPkgLoader(ansible_collection_finder_0)
    except BaseException:
        pass

def test_case_12():
    try:
        ansible_collection_finder_0 = module_0._AnsibleCollectionFinder()
        bool_0 = True
        str_0 = '\\]NQZI6M84I8{'
        int_0 = -386
        ansible_path_hook_finder_0 = module_0._AnsiblePathHookFinder(str_0, int_0)
        var_0 = ansible_path_hook_finder_0.iter_modules(bool_0)
        str_1 = 'ansible'
        var_1 = ansible_collection_finder_0.find_module(str_1)
    except BaseException:
        pass

def test_case_13():
    try:
        float_0 = -1799.012176
        ansible_collection_finder_0 = module_0._AnsibleCollectionFinder()
        ansible_path_hook_finder_0 = module_0._AnsiblePathHookFinder(ansible_collection_finder_0, float_0)
        var_0 = ansible_path_hook_finder_0.__repr__()
        str_0 = "DLY'(_Zr,QezA2jero"
        ansible_collection_loader_0 = module_0._AnsibleCollectionLoader(str_0)
    except BaseException:
        pass

def test_case_14():
    try:
        ansible_collection_finder_0 = module_0._AnsibleCollectionFinder()
        str_0 = 'a>mM!/+a'
        var_0 = ansible_collection_finder_0.find_module(str_0)
        str_1 = 'ansible'
        var_1 = ansible_collection_finder_0.find_module(str_1)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = 'module'
        str_1 = 'namespace.collection'
        var_0 = None
        str_2 = 'resource'
        ansible_collection_ref_0 = module_0.AnsibleCollectionRef(str_1, var_0, str_2, str_0)
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = '/dummy-collections-base-path'
        ansible_collection_finder_0 = module_0._AnsibleCollectionFinder(str_0)
        ansible_path_hook_finder_0 = module_0._AnsiblePathHookFinder(ansible_collection_finder_0, str_0)
        str_1 = 'ansible_collections'
        var_0 = ansible_path_hook_finder_0.find_module(str_1)
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = '{#Q&;\tJj\r:-r$JWF\\O,e'
        ansible_internal_redirect_loader_0 = None
        ansible_collection_finder_0 = module_0._AnsibleCollectionFinder(str_0, ansible_internal_redirect_loader_0)
        ansible_collection_pkg_loader_base_0 = module_0._AnsibleCollectionPkgLoaderBase(ansible_collection_finder_0)
    except BaseException:
        pass

def test_case_18():
    try:
        str_0 = 'ABC.XYZ'
        str_1 = '/]_i'
        str_2 = 'role'
        ansible_collection_ref_0 = module_0.AnsibleCollectionRef(str_0, str_1, str_1, str_2)
    except BaseException:
        pass

def test_case_19():
    try:
        str_0 = '/dumm\t-collections-base-path'
        ansible_collection_finder_0 = module_0._AnsibleCollectionFinder(str_0)
        str_1 = '/dummy-collections-base-path/ansible_collections'
        ansible_path_hook_finder_0 = module_0._AnsiblePathHookFinder(ansible_collection_finder_0, str_1)
        var_0 = ansible_collection_finder_0.set_playbook_paths(str_0)
        var_1 = ansible_path_hook_finder_0.__repr__()
        str_2 = 'ansible_collections'
        ansible_collection_root_pkg_loader_0 = module_0._AnsibleCollectionRootPkgLoader(str_2, str_1)
        str_3 = 'A+U8v,#='
        set_0 = {str_1, str_3, ansible_path_hook_finder_0}
        ansible_collection_finder_1 = module_0._AnsibleCollectionFinder(set_0)
        ansible_internal_redirect_loader_0 = None
        var_2 = ansible_collection_finder_1.set_playbook_paths(ansible_internal_redirect_loader_0)
    except BaseException:
        pass

def test_case_20():
    try:
        str_0 = '/dumm\t-collections-base-path'
        ansible_collection_finder_0 = module_0._AnsibleCollectionFinder(str_0)
        ansible_path_hook_finder_0 = module_0._AnsiblePathHookFinder(ansible_collection_finder_0, str_0)
        var_0 = ansible_path_hook_finder_0.__repr__()
        str_1 = 'ansible_collections'
        ansible_collection_root_pkg_loader_0 = module_0._AnsibleCollectionRootPkgLoader(str_1, str_0)
        ansible_internal_redirect_loader_0 = None
        ansible_collection_ref_0 = module_0.AnsibleCollectionRef(ansible_path_hook_finder_0, ansible_collection_finder_0, ansible_collection_root_pkg_loader_0, ansible_internal_redirect_loader_0)
    except BaseException:
        pass

def test_case_21():
    try:
        ansible_collection_finder_0 = module_0._AnsibleCollectionFinder()
        str_0 = 'ansible_collections.default.test_plugin'
        var_0 = ansible_collection_finder_0.find_module(str_0)
    except BaseException:
        pass

def test_case_22():
    try:
        str_0 = 'ansible_collections.somens'
        str_1 = '/path/somewhere'
        str_2 = '/path/elsewhere'
        str_3 = [str_1, str_2]
        ansible_collection_pkg_loader_base_0 = module_0._AnsibleCollectionPkgLoaderBase(str_0, str_3)
        var_0 = ansible_collection_pkg_loader_base_0.is_package(str_0)
        str_4 = 'ansible_collections.somens.other'
        var_1 = ansible_collection_pkg_loader_base_0.is_package(str_4)
    except BaseException:
        pass

def test_case_23():
    try:
        str_0 = '/dumm\t-collect=ons-base-pah'
        ansible_collection_finder_0 = module_0._AnsibleCollectionFinder(str_0)
        str_1 = ''
        ansible_path_hook_finder_0 = module_0._AnsiblePathHookFinder(ansible_collection_finder_0, str_1)
        var_0 = ansible_collection_finder_0.set_playbook_paths(str_0)
        str_2 = 'ansible_collections'
        ansible_collection_root_pkg_loader_0 = module_0._AnsibleCollectionRootPkgLoader(str_2, str_1)
        str_3 = '/p\\|H~%uj`~1k|'
        var_1 = ansible_path_hook_finder_0.find_module(str_3)
        var_2 = ansible_path_hook_finder_0.find_module(str_2)
    except BaseException:
        pass

def test_case_24():
    try:
        ansible_collection_finder_0 = module_0._AnsibleCollectionFinder()
        str_0 = 'ansible_collections.default.test_plugin'
        float_0 = -474.40091
        ansible_collection_root_pkg_loader_0 = module_0._AnsibleCollectionRootPkgLoader(str_0, float_0)
    except BaseException:
        pass

def test_case_25():
    try:
        str_0 = ''
        ansible_collection_finder_0 = module_0._AnsibleCollectionFinder(str_0)
        ansible_path_hook_finder_0 = module_0._AnsiblePathHookFinder(ansible_collection_finder_0, str_0)
        ansible_collection_root_pkg_loader_0 = None
        var_0 = ansible_collection_finder_0.set_playbook_paths(str_0)
        str_1 = 'pU\\|H~%uj`~1|'
        var_1 = ansible_path_hook_finder_0.find_module(str_1)
        var_2 = ansible_path_hook_finder_0.find_module(str_1)
        var_3 = ansible_path_hook_finder_0.__repr__()
        set_0 = {var_2, str_1}
        str_2 = "5^'OJN"
        list_0 = [str_0, str_2, var_0]
        list_1 = [list_0, var_1, str_0]
        ansible_collection_ref_0 = module_0.AnsibleCollectionRef(ansible_collection_root_pkg_loader_0, str_0, set_0, list_1)
    except BaseException:
        pass