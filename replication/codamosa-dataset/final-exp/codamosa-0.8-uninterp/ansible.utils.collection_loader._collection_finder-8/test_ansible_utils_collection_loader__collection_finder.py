# Automatically generated by Pynguin.
import ansible.utils.collection_loader._collection_finder as module_0

def test_case_0():
    pass

def test_case_1():
    ansible_collection_finder_0 = module_0._AnsibleCollectionFinder()

def test_case_2():
    ansible_collection_finder_0 = module_0._AnsibleCollectionFinder()
    str_0 = ''
    var_0 = ansible_collection_finder_0.set_playbook_paths(str_0)

def test_case_3():
    int_0 = -677
    ansible_path_hook_finder_0 = module_0._AnsiblePathHookFinder(int_0, int_0)

def test_case_4():
    ansible_collection_ref_0 = None
    int_0 = -175
    ansible_path_hook_finder_0 = module_0._AnsiblePathHookFinder(int_0, int_0)
    var_0 = ansible_path_hook_finder_0.iter_modules(ansible_collection_ref_0)

def test_case_5():
    ansible_collection_ref_0 = None
    set_0 = {ansible_collection_ref_0, ansible_collection_ref_0}
    ansible_collection_finder_0 = module_0._AnsibleCollectionFinder(set_0)
    var_0 = ansible_collection_finder_0.set_playbook_paths(set_0)

def test_case_6():
    str_0 = 'tess/fixtures/collections'
    ansible_collection_finder_0 = module_0._AnsibleCollectionFinder(str_0)

def test_case_7():
    str_0 = 'tess/fixtures/collections'
    ansible_collection_finder_0 = module_0._AnsibleCollectionFinder(str_0)
    var_0 = ansible_collection_finder_0.find_module(str_0)

def test_case_8():
    ansible_collection_finder_0 = module_0._AnsibleCollectionFinder()
    str_0 = 'Z/J'
    bool_0 = False
    float_0 = 314.2
    ansible_path_hook_finder_0 = module_0._AnsiblePathHookFinder(bool_0, float_0)
    var_0 = ansible_path_hook_finder_0.find_module(str_0)

def test_case_9():
    str_0 = '/tmp/ansible_collections/ansible_collections/my_namespace/my_collection'
    str_1 = [str_0]
    str_2 = 'ansible_collections.my_namespace.my_collection'
    ansible_collection_pkg_loader_base_0 = module_0._AnsibleCollectionPkgLoaderBase(str_2, str_1)

def test_case_10():
    str_0 = '/tmp/ansible_collections/ansible_collections/my_namespace/my_collection'
    str_1 = [str_0]
    str_2 = 'ansible_collections.my_namespace.my_collection'
    ansible_collection_pkg_loader_base_0 = module_0._AnsibleCollectionPkgLoaderBase(str_2, str_1)
    var_0 = ansible_collection_pkg_loader_base_0.is_package(str_2)

def test_case_11():
    str_0 = 'ansible_collections.col_name'
    ansible_collection_pkg_loader_base_0 = module_0._AnsibleCollectionPkgLoaderBase(str_0, str_0)
    str_1 = '/fie_paths'
    var_0 = ansible_collection_pkg_loader_base_0.get_data(str_1)

def test_case_12():
    str_0 = 'ansible_collections.l_name'
    str_1 = '/path'
    str_2 = [str_1]
    ansible_collection_pkg_loader_base_0 = module_0._AnsibleCollectionPkgLoaderBase(str_0, str_2)
    bytes_0 = b'w'
    str_3 = 'p]u.'
    tuple_0 = (ansible_collection_pkg_loader_base_0, bytes_0, str_0, str_3)
    ansible_collection_finder_0 = module_0._AnsibleCollectionFinder(tuple_0)

def test_case_13():
    str_0 = 'rDsKC'
    set_0 = {str_0, str_0, str_0, str_0}
    ansible_path_hook_finder_0 = module_0._AnsiblePathHookFinder(str_0, set_0)
    var_0 = ansible_path_hook_finder_0.iter_modules(set_0)
    ansible_internal_redirect_loader_0 = None
    ansible_collection_finder_0 = module_0._AnsibleCollectionFinder()
    dict_0 = {ansible_internal_redirect_loader_0: ansible_path_hook_finder_0}
    var_1 = ansible_collection_finder_0.find_module(str_0, dict_0)
    var_2 = ansible_path_hook_finder_0.iter_modules(set_0)
    var_3 = ansible_collection_finder_0.set_playbook_paths(var_0)

def test_case_14():
    str_0 = '/tmp/ansible_collections/ansible_collections/my_namespace/my_collection'
    str_1 = [str_0]
    str_2 = 'ansible_collections.my_namespace.my_collection'
    ansible_collection_pkg_loader_base_0 = module_0._AnsibleCollectionPkgLoaderBase(str_2, str_1)
    var_0 = ansible_collection_pkg_loader_base_0.get_code(str_2)
    var_1 = ansible_collection_pkg_loader_base_0.is_package(str_2)