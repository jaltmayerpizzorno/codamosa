# Automatically generated by Pynguin.
import ansible.plugins.filter.encryption as module_0

def test_case_0():
    try:
        bytes_0 = b'\x05\xd1\x97\xbevG\x18j}\xe9\xa3\xfa\x88\x8a_\x98\x86\xbe\x1d'
        var_0 = module_0.do_vault(bytes_0, bytes_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'M'
        filter_module_0 = module_0.FilterModule()
        tuple_0 = (str_0,)
        int_0 = None
        list_0 = [str_0, tuple_0]
        str_1 = '\n    Return the containing collection name for a given path, or None if the path is not below a configured collection, or\n    the collection cannot be loaded (eg, the collection is masked by another of the same name higher in the configured\n    collection roots).\n    :param path: path to evaluate for collection containment\n    :return: collection name or None\n    '
        var_0 = filter_module_0.filters()
        var_1 = module_0.do_unvault(str_0, str_1)
        var_2 = module_0.do_vault(tuple_0, int_0, list_0, int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'o}D)yN'
        bool_0 = False
        var_0 = module_0.do_vault(bool_0, str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = b'\x9c2\xcc\xd3\x08\x89\xb6\xe2\xf5\xc1\xa1\x9d\xf0p\xdc\x901\x8e9'
        list_0 = None
        var_0 = module_0.do_unvault(bytes_0, list_0)
    except BaseException:
        pass

def test_case_4():
    try:
        list_0 = []
        filter_module_0 = module_0.FilterModule(*list_0)
        var_0 = filter_module_0.filters()
        filter_module_1 = module_0.FilterModule()
        var_1 = filter_module_0.filters()
        set_0 = set()
        str_0 = '[\x0b'
        var_2 = module_0.do_unvault(set_0, str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '$ANSIBLE_VAULT;1.1;AES256;ansible\r\n35393662383262643133313239656232303237613566363464333839633363383961626537\r\n39376661306466393933353465336336626537623661303439653361306639336138623265\r\n32653532616335623062616662393961623233313\r\n'
        var_0 = module_0.do_unvault(str_0, str_0)
    except BaseException:
        pass