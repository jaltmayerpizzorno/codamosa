# Automatically generated by Pynguin.
import ansible.plugins.lookup.template as module_0

def test_case_0():
    try:
        list_0 = None
        lookup_module_0 = module_0.LookupModule()
        lookup_module_1 = module_0.LookupModule(list_0)
        str_0 = 'V#/\x0bUW\tZc`q'
        lookup_module_2 = module_0.LookupModule(str_0)
        bytes_0 = b'\n\x8f\x06\xf7\xc4\xb4\x05\xdd\xc7\x0e\xc6\x0c'
        var_0 = lookup_module_2.run(bytes_0, bytes_0)
    except BaseException:
        pass