# Automatically generated by Pynguin.
import ansible.utils.collection_loader._collection_finder as module_0

def test_case_0():
    pass

def test_case_1():
    ansible_collection_finder_0 = module_0._AnsibleCollectionFinder()

def test_case_2():
    ansible_collection_finder_0 = module_0._AnsibleCollectionFinder()
    set_0 = {ansible_collection_finder_0, ansible_collection_finder_0}
    var_0 = ansible_collection_finder_0.set_playbook_paths(set_0)

def test_case_3():
    str_0 = 'MakC'
    ansible_path_hook_finder_0 = module_0._AnsiblePathHookFinder(str_0, str_0)
    var_0 = ansible_path_hook_finder_0.find_module(str_0)

def test_case_4():
    str_0 = 'ansible_collections.foo.init'
    ansible_collection_pkg_loader_base_0 = module_0._AnsibleCollectionPkgLoaderBase(str_0, str_0)
    var_0 = ansible_collection_pkg_loader_base_0.get_code(str_0)

def test_case_5():
    str_0 = 'namespLoe.collecio'
    str_1 = 'subdir1.subdir2'
    bool_0 = False
    list_0 = [str_0, bool_0, str_1]
    ansible_collection_finder_0 = module_0._AnsibleCollectionFinder(list_0)

def test_case_6():
    ansible_collection_finder_0 = module_0._AnsibleCollectionFinder()
    str_0 = 'MnMs4\\+A'
    var_0 = ansible_collection_finder_0.find_module(str_0, ansible_collection_finder_0)

def test_case_7():
    ansible_collection_finder_0 = module_0._AnsibleCollectionFinder()
    set_0 = {ansible_collection_finder_0, ansible_collection_finder_0}
    var_0 = ansible_collection_finder_0.set_playbook_paths(set_0)
    int_0 = 71
    str_0 = 'MnMs4\\+ A'
    var_1 = ansible_collection_finder_0.find_module(str_0, ansible_collection_finder_0)
    ansible_path_hook_finder_0 = module_0._AnsiblePathHookFinder(set_0, str_0)
    var_2 = ansible_path_hook_finder_0.iter_modules(int_0)

def test_case_8():
    ansible_collection_finder_0 = module_0._AnsibleCollectionFinder()
    set_0 = {ansible_collection_finder_0, ansible_collection_finder_0}
    str_0 = ''
    ansible_path_hook_finder_0 = module_0._AnsiblePathHookFinder(set_0, str_0)
    str_1 = '^+u'
    var_0 = ansible_path_hook_finder_0.find_module(str_1)

def test_case_9():
    str_0 = 'ansible_collections.test_collection.subcollection.subsubcollection'
    str_1 = '/a/b/c/d'
    str_2 = '/e/f/g/h'
    str_3 = [str_1, str_2]
    ansible_collection_pkg_loader_base_0 = module_0._AnsibleCollectionPkgLoaderBase(str_0, str_3)
    var_0 = ansible_collection_pkg_loader_base_0._fullname
    var_1 = ansible_collection_pkg_loader_base_0.load_module(var_0)
    var_2 = ansible_collection_pkg_loader_base_0._fullname

def test_case_10():
    str_0 = 'ansible_collections.test_collection.subcollection.subsubcollection'
    ansible_collection_pkg_loader_base_0 = module_0._AnsibleCollectionPkgLoaderBase(str_0, str_0)
    var_0 = ansible_collection_pkg_loader_base_0.load_module(str_0)

def test_case_11():
    str_0 = 'namespace.collection'
    str_1 = 'action'
    ansible_collection_ref_0 = module_0.AnsibleCollectionRef(str_0, str_1, str_1, str_1)

def test_case_12():
    str_0 = 'namespace.collection'
    str_1 = 'subdir1.subdir2'
    str_2 = 'action'
    ansible_collection_ref_0 = module_0.AnsibleCollectionRef(str_0, str_1, str_1, str_2)
    var_0 = ansible_collection_ref_0.__repr__()

def test_case_13():
    ansible_collection_finder_0 = module_0._AnsibleCollectionFinder()
    str_0 = 'ansible_coll!ctions.somens'
    var_0 = ansible_collection_finder_0.find_module(str_0, ansible_collection_finder_0)
    var_1 = print(var_0)
    str_1 = 'ansible_collections.somens.somecoll'
    var_2 = ansible_collection_finder_0.find_module(str_1, str_0)
    var_3 = print(var_2)