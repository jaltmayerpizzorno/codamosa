# Automatically generated by Pynguin.
import ansible.plugins.lookup.fileglob as module_0

def test_case_0():
    try:
        lookup_module_0 = module_0.LookupModule()
        str_0 = 'test.txt'
        str_1 = [str_0]
        str_2 = {str_0: str_0}
        var_0 = lookup_module_0.run(str_1, str_2)
    except BaseException:
        pass

def test_case_1():
    try:
        lookup_module_0 = module_0.LookupModule()
        str_0 = 'We were unable to decode all characters in the module return data. Replaced some in an effort to return as much as possible'
        var_0 = lookup_module_0.run(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        lookup_module_0 = module_0.LookupModule()
        str_0 = 'myfile'
        str_1 = 'ansible_search_path'
        str_2 = {str_1: str_0}
        var_0 = lookup_module_0.run(str_1, str_2)
        var_1 = lookup_module_0.run(str_2, str_2)
        str_3 = './reative/path/to/file'
        str_4 = [str_3]
        var_2 = {}
        var_3 = lookup_module_0.run(str_4, var_2)
    except BaseException:
        pass

def test_case_3():
    try:
        lookup_module_0 = module_0.LookupModule()
        str_0 = 'myfile'
        str_1 = [str_0]
        str_2 = 'ansible_search_path'
        str_3 = ''
        str_4 = [str_3]
        str_5 = {str_2: str_4}
        var_0 = lookup_module_0.run(str_1, str_5)
        str_6 = '/absolute/path/to/file'
        str_7 = [str_2, str_6, str_4]
        var_1 = {}
        var_2 = lookup_module_0.run(str_7, var_1)
    except BaseException:
        pass