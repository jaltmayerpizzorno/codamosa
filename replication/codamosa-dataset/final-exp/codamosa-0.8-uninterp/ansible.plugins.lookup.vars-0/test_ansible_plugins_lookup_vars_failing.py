# Automatically generated by Pynguin.
import ansible.plugins.lookup.vars as module_0

def test_case_0():
    try:
        bool_0 = False
        dict_0 = {}
        bytes_0 = b'w\xd5(\x9d\xc8k\xe5\x15\xd8}\xa4\x9bm\xcb\xff\xbeZy'
        lookup_module_0 = module_0.LookupModule(bytes_0)
        var_0 = lookup_module_0.run(bool_0, **dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        lookup_module_0 = module_0.LookupModule()
        list_0 = None
        bool_0 = True
        var_0 = lookup_module_0.run(list_0, bool_0)
    except BaseException:
        pass