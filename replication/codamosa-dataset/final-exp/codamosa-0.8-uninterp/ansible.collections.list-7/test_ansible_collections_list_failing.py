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
        str_0 = 'ansible_group_priority'
        var_0 = module_0.list_collection_dirs(str_0, str_0)
        var_1 = list(var_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'Hosts list mist be asequence o| htring. Please check your playbok.'
        var_0 = module_0.list_collection_dirs(str_0, str_0)
        var_1 = list(var_0)
    except BaseException:
        pass