# Automatically generated by Pynguin.
import ansible.plugins.lookup.fileglob as module_0

def test_case_0():
    try:
        int_0 = -890
        str_0 = 'an3ir|'
        lookup_module_0 = module_0.LookupModule(str_0)
        dict_0 = {str_0: lookup_module_0, str_0: str_0, str_0: str_0, str_0: lookup_module_0, str_0: str_0}
        dict_1 = {str_0: str_0, str_0: int_0, str_0: lookup_module_0, int_0: int_0}
        var_0 = lookup_module_0.run(dict_1, dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = False
        lookup_module_0 = module_0.LookupModule()
        var_0 = lookup_module_0.run(bool_0)
    except BaseException:
        pass

def test_case_2():
    try:
        lookup_module_0 = module_0.LookupModule()
        tuple_0 = ()
        var_0 = lookup_module_0.run(tuple_0)
        bytes_0 = b'\xa5\n\xef\xf2\x8a\x1d\xfe\xa9\x14_Y\x8av\x03M\x89r\xe5'
        var_1 = lookup_module_0.run(bytes_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = ":m\n\x0b@6'Hm)|Dh+_"
        lookup_module_0 = module_0.LookupModule()
        var_0 = lookup_module_0.run(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '+?97?Q{G"lh?(&*\\bQzY'
        str_1 = "Gq>'$Q\\&v<u!T-:?1/"
        str_2 = 'D'
        dict_0 = {str_0: str_0, str_1: str_1, str_2: str_1}
        list_0 = [str_1, dict_0]
        bool_0 = True
        set_0 = set()
        str_3 = 'lS\tT.9'
        dict_1 = {str_3: str_2, str_0: list_0}
        list_1 = [str_1, dict_1, bool_0]
        lookup_module_0 = module_0.LookupModule(set_0)
        var_0 = lookup_module_0.run(list_1, **dict_0)
    except BaseException:
        pass