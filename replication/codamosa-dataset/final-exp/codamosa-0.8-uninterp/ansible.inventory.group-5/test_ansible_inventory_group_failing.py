# Automatically generated by Pynguin.
import ansible.inventory.group as module_0

def test_case_0():
    try:
        bool_0 = True
        group_0 = module_0.Group()
        var_0 = group_0.deserialize(bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = True
        group_0 = module_0.Group()
        var_0 = group_0.add_child_group(bool_0)
    except BaseException:
        pass

def test_case_2():
    try:
        group_0 = module_0.Group()
        var_0 = group_0.get_hosts()
        var_1 = group_0.add_host(group_0)
    except BaseException:
        pass

def test_case_3():
    try:
        group_0 = module_0.Group()
        set_0 = {group_0, group_0, group_0}
        var_0 = group_0.set_priority(set_0)
        var_1 = group_0.get_hosts()
        var_2 = group_0.serialize()
        var_3 = group_0.remove_host(group_0)
        var_4 = group_0.add_host(group_0)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = None
        set_0 = set()
        group_0 = module_0.Group()
        var_0 = group_0.set_variable(int_0, set_0)
        str_0 = 'Fri'
        group_1 = module_0.Group(str_0)
        var_1 = group_1.get_hosts()
        str_1 = '~ L(M4D'
        var_2 = group_0.set_priority(str_1)
    except BaseException:
        pass

def test_case_5():
    try:
        group_0 = module_0.Group()
        var_0 = group_0.get_hosts()
        var_1 = group_0.get_hosts()
        var_2 = group_0.serialize()
        var_3 = group_0.remove_host(group_0)
        var_4 = group_0.add_host(group_0)
    except BaseException:
        pass

def test_case_6():
    try:
        int_0 = None
        set_0 = set()
        group_0 = module_0.Group()
        var_0 = group_0.set_variable(int_0, set_0)
        str_0 = 'CLJ\rI"`7xBb'
        group_1 = module_0.Group(str_0)
        var_1 = group_0.get_hosts()
        float_0 = None
        var_2 = group_1.set_priority(float_0)
        var_3 = group_1.get_name()
        group_2 = module_0.Group()
        var_4 = group_0.__repr__()
        var_5 = group_0.add_child_group(group_0)
    except BaseException:
        pass

def test_case_7():
    try:
        group_0 = module_0.Group()
        var_0 = group_0.remove_host(group_0)
        var_1 = group_0.add_host(group_0)
    except BaseException:
        pass

def test_case_8():
    try:
        int_0 = None
        group_0 = module_0.Group()
        group_1 = module_0.Group()
        var_0 = group_1.add_child_group(group_0)
        var_1 = group_0.set_variable(int_0, int_0)
        str_0 = 'CLJ\rI"`7xBb'
        var_2 = group_1.__repr__()
        var_3 = group_1.get_hosts()
        var_4 = group_0.__getstate__()
        var_5 = group_0.__getstate__()
        dict_0 = {str_0: var_4, str_0: var_1}
        var_6 = group_0.deserialize(dict_0)
        var_7 = group_0.remove_host(group_0)
        var_8 = group_1.get_name()
        var_9 = group_1.__repr__()
        var_10 = group_0.add_child_group(group_1)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'all'
        group_0 = module_0.Group(str_0)
        str_1 = 'group'
        group_1 = module_0.Group(str_1)
        var_0 = group_1.add_child_group(group_0)
        var_1 = group_0.add_child_group(group_1)
    except BaseException:
        pass