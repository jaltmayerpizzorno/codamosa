# Automatically generated by Pynguin.
import ansible.plugins.lookup.fileglob as module_0

def test_case_0():
    try:
        dict_0 = {}
        str_0 = 'L){y&wkTcN\x0b$[,T1Gv1'
        lookup_module_0 = module_0.LookupModule(**dict_0)
        var_0 = lookup_module_0.run(str_0, str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = "aSa(?TJ*0\\'y"
        lookup_module_0 = module_0.LookupModule()
        var_0 = lookup_module_0.run(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'ansible_search_path'
        str_1 = './.test_lookup_plugins'
        str_2 = {str_0: str_1}
        lookup_module_0 = module_0.LookupModule()
        var_0 = lookup_module_0.run(str_1, str_2)
    except BaseException:
        pass