# Automatically generated by Pynguin.
import ansible.inventory.group as module_0

def test_case_0():
    try:
        group_0 = module_0.Group()
        var_0 = group_0.__str__()
        var_1 = group_0.clear_hosts_cache()
        var_2 = group_0.get_name()
        str_0 = 'o7+i'
        float_0 = -1198.2
        set_0 = {float_0, float_0, float_0, str_0}
        var_3 = group_0.deserialize(set_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'u;3'
        group_0 = module_0.Group(str_0)
        group_1 = module_0.Group()
        var_0 = group_1.__setstate__(group_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'T'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
        group_0 = module_0.Group()
        var_0 = group_0.deserialize(dict_0)
        group_1 = module_0.Group()
        group_2 = module_0.Group(group_1)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '4'
        group_0 = module_0.Group(str_0)
        group_1 = module_0.Group()
        set_0 = None
        var_0 = group_1.deserialize(set_0)
    except BaseException:
        pass

def test_case_4():
    try:
        group_0 = module_0.Group()
        group_1 = module_0.Group()
        var_0 = group_1.add_host(group_0)
    except BaseException:
        pass

def test_case_5():
    try:
        group_0 = module_0.Group()
        str_0 = 'BHn@yoe'
        var_0 = group_0.set_priority(str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        group_0 = module_0.Group()
        var_0 = group_0.get_hosts()
        var_1 = group_0.get_hosts()
        var_2 = group_0.get_name()
        group_1 = module_0.Group()
        list_0 = None
        tuple_0 = ()
        set_0 = {group_1, list_0}
        var_3 = group_0.set_variable(tuple_0, set_0)
        var_4 = group_1.add_child_group(set_0)
    except BaseException:
        pass

def test_case_7():
    try:
        group_0 = module_0.Group()
        var_0 = group_0.get_hosts()
        group_1 = module_0.Group()
        str_0 = ''
        int_0 = 86
        var_1 = group_0.set_variable(str_0, int_0)
        var_2 = group_1.add_child_group(group_1)
    except BaseException:
        pass

def test_case_8():
    try:
        group_0 = module_0.Group()
        var_0 = group_0.serialize()
        str_0 = '1xm'
        list_0 = [var_0, var_0]
        var_1 = group_0.set_priority(list_0)
        var_2 = group_0.get_hosts()
        var_3 = group_0.remove_host(group_0)
        dict_0 = None
        var_4 = group_0.get_vars()
        var_5 = group_0.remove_host(group_0)
        list_1 = [var_0, var_1, dict_0, str_0]
        var_6 = group_0.add_child_group(list_1)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'g1'
        group_0 = module_0.Group(str_0)
        str_1 = 'g2'
        group_1 = module_0.Group(str_1)
        str_2 = 'g4'
        group_2 = module_0.Group(str_2)
        var_0 = group_0.add_child_group(group_1)
        var_1 = group_1.add_child_group(group_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = 'ansible_group_priority'
        str_1 = 'test_group'
        group_0 = module_0.Group(str_1)
        int_0 = 1
        var_0 = group_0.set_variable(str_0, int_0)
        var_1 = test_group.get_vars()[str_0]
    except BaseException:
        pass