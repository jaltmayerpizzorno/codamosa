# Automatically generated by Pynguin.
import ansible.plugins.lookup.nested as module_0

def test_case_0():
    try:
        dict_0 = {}
        lookup_module_0 = module_0.LookupModule()
        var_0 = lookup_module_0.run(dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        lookup_module_0 = module_0.LookupModule()
        bytes_0 = b'i\xd5y'
        var_0 = lookup_module_0.run(bytes_0)
    except BaseException:
        pass