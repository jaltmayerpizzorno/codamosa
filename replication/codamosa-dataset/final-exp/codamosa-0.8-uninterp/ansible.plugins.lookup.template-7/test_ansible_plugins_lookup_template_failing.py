# Automatically generated by Pynguin.
import ansible.plugins.lookup.template as module_0

def test_case_0():
    try:
        float_0 = None
        list_0 = [float_0, float_0, float_0]
        dict_0 = None
        list_1 = [dict_0, dict_0, dict_0]
        lookup_module_0 = module_0.LookupModule(list_1)
        lookup_module_1 = module_0.LookupModule(lookup_module_0)
        var_0 = lookup_module_1.run(float_0, list_0)
    except BaseException:
        pass