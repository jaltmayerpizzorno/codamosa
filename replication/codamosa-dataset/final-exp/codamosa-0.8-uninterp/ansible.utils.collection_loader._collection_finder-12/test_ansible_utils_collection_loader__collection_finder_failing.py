# Automatically generated by Pynguin.
import ansible.utils.collection_loader._collection_finder as module_0
import ansible.utils.collection_loader._collection_config as module_1

def test_case_0():
    try:
        str_0 = 'Calling %s to load vars for %s'
        ansible_collection_finder_0 = module_0._AnsibleCollectionFinder(str_0)
        ansible_collection_n_s_pkg_loader_0 = module_0._AnsibleCollectionNSPkgLoader(ansible_collection_finder_0)
    except BaseException:
        pass

def test_case_1():
    try:
        ansible_collection_finder_0 = module_0._AnsibleCollectionFinder()
        str_0 = 'ansible.test'
        var_0 = ansible_collection_finder_0.find_module(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'SSq'
        ansible_collection_pkg_loader_0 = module_0._AnsibleCollectionPkgLoader(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'ansible_collections'
        ansible_collection_loader_0 = module_0._AnsibleCollectionLoader(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'ansib!le'
        ansible_internal_redirect_loader_0 = module_0._AnsibleInternalRedirectLoader(str_0, str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'ansible'
        ansible_internal_redirect_loader_0 = module_0._AnsibleInternalRedirectLoader(str_0, str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        float_0 = 1599.6604495242698
        ansible_collection_finder_0 = module_0._AnsibleCollectionFinder()
        str_0 = '_v\tINS/'
        ansible_collection_ref_0 = module_0.AnsibleCollectionRef(float_0, str_0, ansible_collection_finder_0, ansible_collection_finder_0)
    except BaseException:
        pass

def test_case_7():
    try:
        int_0 = -4030
        bool_0 = True
        dict_0 = None
        bool_1 = False
        ansible_collection_ref_0 = module_0.AnsibleCollectionRef(int_0, bool_0, dict_0, bool_1)
    except BaseException:
        pass

def test_case_8():
    try:
        ansible_collection_finder_0 = module_0._AnsibleCollectionFinder()
        str_0 = 'ansible_collections'
        list_0 = [ansible_collection_finder_0, ansible_collection_finder_0, str_0, ansible_collection_finder_0]
        var_0 = ansible_collection_finder_0.set_playbook_paths(list_0)
        float_0 = None
        set_0 = {ansible_collection_finder_0, ansible_collection_finder_0}
        tuple_0 = ()
        ansible_collection_finder_1 = module_0._AnsibleCollectionFinder(set_0, tuple_0)
        var_1 = ansible_collection_finder_1.set_playbook_paths(float_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'ansible_collections.ns'
        ansible_collection_pkg_loader_base_0 = module_0._AnsibleCollectionPkgLoaderBase(str_0, str_0)
        float_0 = 4050.96
        ansible_internal_redirect_loader_0 = None
        ansible_collection_ref_0 = module_0.AnsibleCollectionRef(ansible_collection_pkg_loader_base_0, ansible_internal_redirect_loader_0, float_0, ansible_internal_redirect_loader_0)
    except BaseException:
        pass

def test_case_10():
    try:
        ansible_collection_finder_0 = module_0._AnsibleCollectionFinder()
        str_0 = 'ansible_collections'
        ansible_collection_n_s_pkg_loader_0 = module_0._AnsibleCollectionNSPkgLoader(str_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = 'ansible_collections.ns'
        ansible_collection_pkg_loader_base_0 = module_0._AnsibleCollectionPkgLoaderBase(str_0, str_0)
        float_0 = -950.4246
        set_0 = {float_0, ansible_collection_pkg_loader_base_0, ansible_collection_pkg_loader_base_0, ansible_collection_pkg_loader_base_0}
        var_0 = ansible_collection_pkg_loader_base_0.get_source(set_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = 'ansible_collections.ns'
        str_1 = [str_0]
        ansible_collection_pkg_loader_base_0 = module_0._AnsibleCollectionPkgLoaderBase(str_0, str_1)
        var_0 = ansible_collection_pkg_loader_base_0.get_source(str_0)
        str_2 = 'Insible_collections.ns'
        str_3 = '/home/user/ansible_collections/ns/test_collection'
        str_4 = [str_3]
        ansible_collection_pkg_loader_base_1 = module_0._AnsibleCollectionPkgLoaderBase(str_2, str_4)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = 'foo.bar'
        str_1 = 'I\x0cg!Ck'
        str_2 = 'role'
        ansible_collection_ref_0 = module_0.AnsibleCollectionRef(str_0, str_1, str_0, str_2)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = 'foo.bar'
        ansible_collection_ref_0 = module_0.AnsibleCollectionRef(str_0, str_0, str_0, str_0)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = 'ansible_collections.ns'
        ansible_collection_pkg_loader_base_0 = module_0._AnsibleCollectionPkgLoaderBase(str_0, str_0)
        int_0 = 3
        var_0 = ansible_collection_pkg_loader_base_0.is_package(int_0)
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = 'foo.bar'
        str_1 = 'role'
        ansible_collection_ref_0 = module_0.AnsibleCollectionRef(str_0, str_1, str_0, str_1)
        list_0 = None
        var_0 = ansible_collection_ref_0.legacy_plugin_dir_to_plugin_type(list_0)
    except BaseException:
        pass

def test_case_17():
    try:
        ansible_collection_finder_0 = module_0._AnsibleCollectionFinder()
        str_0 = 'B`\r7vw[E0)'
        str_1 = 'Jyf\rZy:W~\x0c*tM"ms",'
        var_0 = ansible_collection_finder_0.set_playbook_paths(str_1)
        str_2 = 'XsJ;AYAfSR9:'
        dict_0 = {str_0: ansible_collection_finder_0, str_0: str_0, str_2: ansible_collection_finder_0, str_2: str_0}
        dict_1 = {}
        ansible_path_hook_finder_0 = module_0._AnsiblePathHookFinder(dict_0, dict_1)
        str_3 = 'ansible_collections'
        var_1 = ansible_collection_finder_0.find_module(str_3)
        var_2 = ansible_collection_finder_0.find_module(str_3)
        ansible_collection_finder_1 = module_0._AnsibleCollectionFinder()
        ansible_collection_finder_2 = module_0._AnsibleCollectionFinder(ansible_collection_finder_1)
    except BaseException:
        pass

def test_case_18():
    try:
        str_0 = 'ansible_collections'
        ansible_collection_config_0 = module_1.AnsibleCollectionConfig()
        ansible_collection_pkg_loader_0 = module_0._AnsibleCollectionPkgLoader(str_0)
    except BaseException:
        pass

def test_case_19():
    try:
        ansible_collection_finder_0 = module_0._AnsibleCollectionFinder()
        str_0 = 'ansible_collections'
        str_1 = 'dD|%u-=D0m"C\x0bX9\x0cOP}'
        var_0 = ansible_collection_finder_0.find_module(str_0, str_1)
    except BaseException:
        pass

def test_case_20():
    try:
        ansible_collection_finder_0 = module_0._AnsibleCollectionFinder()
        str_0 = 'ansible_collections'
        list_0 = [str_0, str_0, ansible_collection_finder_0]
        var_0 = ansible_collection_finder_0.set_playbook_paths(list_0)
        var_1 = ansible_collection_finder_0.find_module(str_0)
        ansible_collection_finder_1 = module_0._AnsibleCollectionFinder(list_0)
        str_1 = 'u7C `9q}'
        dict_0 = {str_1: list_0, str_0: str_1}
        ansible_collection_config_0 = module_1.AnsibleCollectionConfig(**dict_0)
    except BaseException:
        pass

def test_case_21():
    try:
        str_0 = 'ansible_collections.ns'
        ansible_collection_pkg_loader_base_0 = module_0._AnsibleCollectionPkgLoaderBase(str_0, str_0)
        list_0 = []
        dict_0 = {str_0: ansible_collection_pkg_loader_base_0}
        bytes_0 = None
        tuple_0 = (list_0, dict_0, bytes_0)
        var_0 = ansible_collection_pkg_loader_base_0.get_data(tuple_0)
    except BaseException:
        pass

def test_case_22():
    try:
        str_0 = 'ansible_collections.ns'
        ansible_collection_pkg_loader_base_0 = module_0._AnsibleCollectionPkgLoaderBase(str_0, str_0)
        dict_0 = None
        var_0 = ansible_collection_pkg_loader_base_0.iter_modules(dict_0)
        str_1 = 'ansible_collections.ns'
        var_1 = ansible_collection_pkg_loader_base_0.get_source(str_1)
        str_2 = 'ansible_collections.ns.test_collection'
        str_3 = [str_0]
        set_0 = {str_2, ansible_collection_pkg_loader_base_0}
        float_0 = 4047.29724
        ansible_collection_finder_0 = module_0._AnsibleCollectionFinder()
        ansible_internal_redirect_loader_0 = None
        ansible_collection_ref_0 = module_0.AnsibleCollectionRef(str_3, set_0, float_0, ansible_internal_redirect_loader_0)
    except BaseException:
        pass

def test_case_23():
    try:
        str_0 = 'ansible_collections.ns'
        ansible_collection_pkg_loader_base_0 = module_0._AnsibleCollectionPkgLoaderBase(str_0, str_0)
        dict_0 = {}
        ansible_path_hook_finder_0 = module_0._AnsiblePathHookFinder(dict_0, str_0)
        var_0 = ansible_collection_pkg_loader_base_0.load_module(ansible_path_hook_finder_0)
    except BaseException:
        pass

def test_case_24():
    try:
        str_0 = 'foo.bar'
        str_1 = 'role'
        ansible_collection_ref_0 = module_0.AnsibleCollectionRef(str_0, str_1, str_0, str_1)
        bool_0 = None
        var_0 = ansible_collection_ref_0.try_parse_fqcr(bool_0, ansible_collection_ref_0)
        var_1 = ansible_collection_ref_0.is_valid_collection_name(ansible_collection_ref_0)
        dict_0 = {}
        ansible_collection_config_0 = module_1.AnsibleCollectionConfig(**dict_0)
        float_0 = -1428.4858
        set_0 = {float_0, ansible_collection_ref_0, str_1}
        var_2 = ansible_collection_ref_0.is_valid_fqcr(dict_0, set_0)
        var_3 = ansible_collection_ref_0.is_valid_collection_name(ansible_collection_config_0)
        dict_1 = {str_0: bool_0}
        bytes_0 = b'*\x93fL\x8c\xcdz'
        ansible_collection_loader_0 = module_0._AnsibleCollectionLoader(dict_1, bytes_0)
    except BaseException:
        pass

def test_case_25():
    try:
        str_0 = 'ansible_collections.ns'
        ansible_collection_pkg_loader_base_0 = module_0._AnsibleCollectionPkgLoaderBase(str_0, str_0)
        int_0 = -2633
        var_0 = ansible_collection_pkg_loader_base_0.get_code(int_0)
    except BaseException:
        pass

def test_case_26():
    try:
        str_0 = 'ansible_collections.ns'
        ansible_collection_pkg_loader_base_0 = module_0._AnsibleCollectionPkgLoaderBase(str_0, str_0)
        float_0 = None
        var_0 = ansible_collection_pkg_loader_base_0.get_data(float_0)
    except BaseException:
        pass

def test_case_27():
    try:
        ansible_collection_finder_0 = module_0._AnsibleCollectionFinder()
        str_0 = 'ansible.test'
        int_0 = 4
        var_0 = ansible_collection_finder_0.find_module(str_0, int_0)
    except BaseException:
        pass

def test_case_28():
    try:
        str_0 = 'ansible_collections.ns'
        ansible_collection_pkg_loader_base_0 = module_0._AnsibleCollectionPkgLoaderBase(str_0, str_0)
        var_0 = ansible_collection_pkg_loader_base_0.__repr__()
        var_1 = ansible_collection_pkg_loader_base_0.get_code(str_0)
        ansible_collection_n_s_pkg_loader_0 = module_0._AnsibleCollectionNSPkgLoader(str_0)
    except BaseException:
        pass