# Automatically generated by Pynguin.
import ansible.utils.collection_loader._collection_finder as module_0

def test_case_0():
    pass

def test_case_1():
    ansible_collection_finder_0 = module_0._AnsibleCollectionFinder()

def test_case_2():
    str_0 = "H4m4]:V,*)|{lNRV##' "
    ansible_collection_finder_0 = module_0._AnsibleCollectionFinder(str_0)

def test_case_3():
    tuple_0 = ()
    str_0 = 'x-@"54F`)-pnv\n0'
    ansible_path_hook_finder_0 = module_0._AnsiblePathHookFinder(tuple_0, str_0)

def test_case_4():
    tuple_0 = ()
    str_0 = 'x-@"54F`)-pnv\n0'
    ansible_path_hook_finder_0 = module_0._AnsiblePathHookFinder(tuple_0, str_0)
    str_1 = 'Z5'
    bytes_0 = b''
    ansible_path_hook_finder_1 = module_0._AnsiblePathHookFinder(tuple_0, bytes_0)
    ansible_path_hook_finder_2 = module_0._AnsiblePathHookFinder(str_1, ansible_path_hook_finder_1)

def test_case_5():
    tuple_0 = ()
    ansible_collection_finder_0 = module_0._AnsibleCollectionFinder(tuple_0)

def test_case_6():
    ansible_collection_finder_0 = module_0._AnsibleCollectionFinder()
    list_0 = []
    var_0 = ansible_collection_finder_0.set_playbook_paths(list_0)

def test_case_7():
    ansible_collection_finder_0 = module_0._AnsibleCollectionFinder()
    str_0 = '=o\x0bee\ta\r:'
    tuple_0 = (str_0, ansible_collection_finder_0, str_0)
    var_0 = ansible_collection_finder_0.set_playbook_paths(tuple_0)

def test_case_8():
    ansible_collection_finder_0 = module_0._AnsibleCollectionFinder()
    str_0 = 'R""_;MT^B'
    var_0 = ansible_collection_finder_0.set_playbook_paths(str_0)

def test_case_9():
    str_0 = 'ansible_collections.test.test.test'
    ansible_collection_pkg_loader_base_0 = module_0._AnsibleCollectionPkgLoaderBase(str_0, str_0)

def test_case_10():
    str_0 = 'ansible_collections.test.test.test'
    str_1 = '/test/test/test'
    str_2 = [str_1]
    ansible_collection_pkg_loader_base_0 = module_0._AnsibleCollectionPkgLoaderBase(str_0, str_2)
    var_0 = ansible_collection_pkg_loader_base_0.load_module(str_0)

def test_case_11():
    str_0 = 'ansible_collections.test.test.test'
    ansible_collection_pkg_loader_base_0 = module_0._AnsibleCollectionPkgLoaderBase(str_0, str_0)
    var_0 = ansible_collection_pkg_loader_base_0.load_module(str_0)

def test_case_12():
    str_0 = 'ansible_collections.test.test.test'
    ansible_collection_pkg_loader_base_0 = module_0._AnsibleCollectionPkgLoaderBase(str_0, str_0)
    var_0 = ansible_collection_pkg_loader_base_0.load_module(str_0)
    bool_0 = False
    var_1 = ansible_collection_pkg_loader_base_0.iter_modules(bool_0)