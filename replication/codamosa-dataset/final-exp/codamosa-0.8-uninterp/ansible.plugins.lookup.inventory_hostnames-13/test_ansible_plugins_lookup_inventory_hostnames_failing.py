# Automatically generated by Pynguin.
import ansible.plugins.lookup.inventory_hostnames as module_0

def test_case_0():
    try:
        bytes_0 = b'\x94\xe5\x9b\x8e@p\x806=`!l\xadJS\xcbU'
        int_0 = 232
        set_0 = set()
        list_0 = [set_0, set_0]
        lookup_module_0 = module_0.LookupModule(list_0)
        var_0 = lookup_module_0.run(bytes_0, int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        lookup_module_0 = module_0.LookupModule()
        str_0 = 'groups'
        str_1 = {str_0: str_0, str_0: str_0}
        str_2 = {str_0: str_1}
        var_0 = lookup_module_0.run(str_1, str_2)
    except BaseException:
        pass