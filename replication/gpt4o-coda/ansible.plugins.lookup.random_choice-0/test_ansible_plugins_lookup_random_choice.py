# Automatically generated by Pynguin.
import ansible.plugins.lookup.random_choice as module_0

def test_case_0():
    lookup_module_0 = module_0.LookupModule()

def test_case_1():
    str_0 = '|Hri!Z6x'
    list_0 = [str_0, str_0, str_0]
    list_1 = [str_0, str_0, str_0, list_0]
    bytes_0 = b'"O{\x0cQR\x89'
    lookup_module_0 = module_0.LookupModule(bytes_0)
    var_0 = lookup_module_0.run(list_1)

def test_case_2():
    str_0 = None
    list_0 = []
    str_1 = '|6lvfaRRW!<'
    str_2 = "kF*'-O'P"
    dict_0 = {str_1: str_1, str_1: str_1, str_2: str_2}
    tuple_0 = (dict_0,)
    lookup_module_0 = module_0.LookupModule(tuple_0)
    var_0 = lookup_module_0.run(str_0, list_0)