# Automatically generated by Pynguin.
import ansible.plugins.lookup.vars as module_0

def test_case_0():
    try:
        bool_0 = False
        lookup_module_0 = module_0.LookupModule()
        var_0 = lookup_module_0.run(bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        list_0 = None
        bytes_0 = b'\xba\xa5f`\xa6\xbd'
        lookup_module_0 = module_0.LookupModule()
        var_0 = lookup_module_0.run(list_0, bytes_0)
    except BaseException:
        pass