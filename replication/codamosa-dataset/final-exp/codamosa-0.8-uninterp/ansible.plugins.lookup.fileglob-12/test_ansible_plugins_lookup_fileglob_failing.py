# Automatically generated by Pynguin.
import ansible.plugins.lookup.fileglob as module_0

def test_case_0():
    try:
        str_0 = '.`ep9~?5c@~UE0i[!T'
        str_1 = '=zW1h\x0cZ!K_fioSm'
        str_2 = '9`~,?a0Dn\x0cJ~Y\r\r0b()'
        dict_0 = {str_1: str_0, str_0: str_1, str_2: str_2}
        lookup_module_0 = module_0.LookupModule(str_0, **dict_0)
        lookup_module_1 = module_0.LookupModule()
        list_0 = [str_2, str_1, dict_0, str_1]
        var_0 = lookup_module_0.run(list_0, dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'st_creator'
        lookup_module_0 = module_0.LookupModule()
        var_0 = lookup_module_0.run(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        lookup_module_0 = module_0.LookupModule()
        str_0 = 'ansible_search_path'
        str_1 = '/tmp'
        str_2 = [str_1]
        str_3 = {str_0: str_2}
        var_0 = lookup_module_0.run(str_0, str_3)
        var_1 = lookup_module_0.run(str_1, str_3)
    except BaseException:
        pass

def test_case_3():
    try:
        lookup_module_0 = module_0.LookupModule()
        str_0 = '*.json'
        str_1 = [str_0]
        str_2 = 'ansible_search_path'
        str_3 = '/tmp'
        str_4 = [str_3]
        str_5 = {str_2: str_4}
        var_0 = lookup_module_0.run(str_1, str_5)
        var_1 = lookup_module_0.run(str_0, str_5)
        str_6 = [str_0]
        var_2 = {}
        var_3 = lookup_module_0.run(str_6, var_2)
    except BaseException:
        pass

def test_case_4():
    try:
        lookup_module_0 = module_0.LookupModule()
        str_0 = ''
        str_1 = [str_0]
        str_2 = 'ansible_search_path'
        str_3 = [str_0]
        str_4 = {str_2: str_3}
        var_0 = lookup_module_0.run(str_1, str_4)
        str_5 = [str_4]
        str_6 = {str_2: str_5}
        var_1 = lookup_module_0.run(str_0, str_6)
        str_7 = [str_0]
        var_2 = {}
        var_3 = lookup_module_0.run(str_7, var_2)
    except BaseException:
        pass