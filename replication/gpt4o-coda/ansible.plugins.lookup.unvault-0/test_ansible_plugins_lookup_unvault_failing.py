# Automatically generated by Pynguin.
import ansible.plugins.lookup.unvault as module_0

def test_case_0():
    try:
        str_0 = 'U'
        str_1 = 'failed to look up user with uid %s. Create user up to this point in real play'
        dict_0 = {str_0: str_0, str_1: str_1, str_1: str_1}
        lookup_module_0 = module_0.LookupModule()
        var_0 = lookup_module_0.run(dict_0)
    except BaseException:
        pass