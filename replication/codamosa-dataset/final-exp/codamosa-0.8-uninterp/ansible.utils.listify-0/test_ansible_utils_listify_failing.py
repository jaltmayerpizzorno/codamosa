# Automatically generated by Pynguin.
import ansible.utils.listify as module_0

def test_case_0():
    try:
        bool_0 = None
        str_0 = 'with_nested requires at least one element in the nested list'
        var_0 = module_0.listify_lookup_plugin_terms(bool_0, str_0, str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '+;r!Vecv=0@'
        bool_0 = False
        tuple_0 = (str_0,)
        var_0 = module_0.listify_lookup_plugin_terms(str_0, bool_0, tuple_0, tuple_0)
    except BaseException:
        pass