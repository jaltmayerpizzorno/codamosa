# Automatically generated by Pynguin.
import ansible.collections.list as module_0

def test_case_0():
    try:
        var_0 = module_0.list_collection_dirs()
        var_1 = list(var_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '\n    Helper class for Galaxy, which is used to parse both dependencies\n    specified in meta/main.yml and requirements.yml files.\n    '
        var_0 = module_0.list_collection_dirs(str_0, str_0)
        var_1 = list(var_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '.'
        str_1 = [str_0]
        var_0 = module_0.list_valid_collection_paths(str_1)
        var_1 = list(var_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '\x0c`'
        str_1 = [str_0, str_0]
        var_0 = module_0.list_collection_dirs(str_1, str_0)
        var_1 = list(var_0)
    except BaseException:
        pass