# Automatically generated by Pynguin.
import ansible.plugins.lookup.fileglob as module_0

def test_case_0():
    try:
        lookup_module_0 = module_0.LookupModule()
        str_0 = None
        list_0 = [str_0, str_0, str_0, str_0]
        str_1 = '(?P<subsection>.*)%s'
        int_0 = -1113
        dict_0 = {int_0: int_0, int_0: int_0, int_0: int_0}
        bool_0 = False
        dict_1 = {str_1: bool_0, str_1: dict_0}
        var_0 = lookup_module_0.run(str_1, list_0, **dict_1)
    except BaseException:
        pass

def test_case_1():
    try:
        float_0 = 599.0
        lookup_module_0 = module_0.LookupModule()
        var_0 = lookup_module_0.run(float_0)
    except BaseException:
        pass

def test_case_2():
    try:
        lookup_module_0 = module_0.LookupModule()
        str_0 = None
        dict_0 = {str_0: lookup_module_0, str_0: str_0}
        var_0 = lookup_module_0.run(dict_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'H['
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
        lookup_module_0 = module_0.LookupModule()
        var_0 = lookup_module_0.run(str_0, **dict_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '/playbooks/files/fooapp/hosts'
        str_1 = '/playbooks/files/fooapp/main.yml'
        str_2 = '/fooapp/main.yml'
        str_3 = [str_2]
        str_4 = 'ansible_search_path'
        list_0 = []
        str_5 = 'abK|}qq'
        str_6 = 'qDo'
        str_7 = 'L8r4'
        str_8 = "D}WL72`msbm'3<<!*"
        dict_0 = {str_8: str_1, str_4: str_2}
        dict_1 = {str_5: str_4, str_6: str_5, str_7: dict_0, str_0: dict_0}
        lookup_module_0 = module_0.LookupModule(**dict_1)
        int_0 = -405
        lookup_module_1 = module_0.LookupModule(lookup_module_0, int_0, **dict_1)
        var_0 = lookup_module_1.run(list_0, list_0)
        str_9 = '/playbooks'
        str_10 = [str_9]
        str_11 = {str_4: str_10}
        lookup_module_2 = module_0.LookupModule()
        var_1 = lookup_module_2.run(str_3, str_11)
    except BaseException:
        pass