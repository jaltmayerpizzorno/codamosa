# Automatically generated by Pynguin.
import ansible.plugins.lookup.file as module_0

def test_case_0():
    try:
        bool_0 = True
        str_0 = 'Y)\\a!'
        dict_0 = {str_0: bool_0}
        float_0 = 2207.32567
        dict_1 = {float_0: float_0}
        lookup_module_0 = module_0.LookupModule(dict_1)
        var_0 = lookup_module_0.run(bool_0, **dict_0)
    except BaseException:
        pass