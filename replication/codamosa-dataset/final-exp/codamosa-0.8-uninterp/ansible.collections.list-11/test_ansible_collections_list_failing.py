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
        str_0 = 'test_namU:space'
        var_0 = module_0.list_collection_dirs(str_0, str_0)
        var_1 = list(var_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '.,aKqJr'
        var_0 = module_0.list_collection_dirs(str_0, str_0)
        var_1 = list(var_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '\n    This is a generic TCP Connection Info strategy class that relies\n    on the psutil module, which is not ideal for targets, but necessary\n    for cross platform support.\n\n    A subclass may wish to override some or all of these methods.\n      - _get_exclude_ips()\n      - get_active_connections()\n\n    All subclasses MUST define platform and distribution (which may be None).\n    '
        var_0 = module_0.list_collection_dirs(str_0, str_0)
        var_1 = list(var_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'test_namespace.test_collection'
        var_0 = list(str_0)
        var_1 = module_0.list_collection_dirs(var_0, var_0)
        var_2 = list(var_1)
    except BaseException:
        pass