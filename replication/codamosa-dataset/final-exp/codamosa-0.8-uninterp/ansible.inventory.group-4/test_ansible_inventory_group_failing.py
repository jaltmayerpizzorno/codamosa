# Automatically generated by Pynguin.
import ansible.inventory.group as module_0

def test_case_0():
    try:
        str_0 = 'F>^Z&7u$= q;'
        group_0 = module_0.Group(str_0)
        var_0 = group_0.__repr__()
        var_1 = group_0.add_host(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'group@example.com'
        group_0 = module_0.Group()
        var_0 = group_0.__str__()
        str_1 = '_'
        var_1 = module_0.to_safe_group_name(str_0, str_1)
        bool_0 = True
        var_2 = module_0.to_safe_group_name(str_0, str_1, bool_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'F>^Z&7u$= q;'
        group_0 = module_0.Group(str_0)
        dict_0 = {str_0: str_0, group_0: str_0, group_0: str_0}
        var_0 = group_0.__setstate__(dict_0)
        var_1 = group_0.add_host(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        float_0 = -746.9
        group_0 = module_0.Group()
        var_0 = group_0.remove_host(group_0)
        var_1 = group_0.remove_host(float_0)
    except BaseException:
        pass

def test_case_4():
    try:
        dict_0 = {}
        list_0 = [dict_0, dict_0, dict_0]
        group_0 = module_0.Group()
        var_0 = group_0.add_child_group(list_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'g2'
        group_0 = module_0.Group(str_0)
        var_0 = group_0.add_host(group_0)
    except BaseException:
        pass

def test_case_6():
    try:
        group_0 = module_0.Group()
        var_0 = group_0.get_descendants()
        str_0 = 'included: %s for %s'
        var_1 = group_0.add_host(str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'g1'
        group_0 = module_0.Group(str_0)
        bytes_0 = None
        var_0 = group_0.set_priority(bytes_0)
        str_1 = 'g2'
        group_1 = module_0.Group(str_1)
        str_2 = 'g3'
        group_2 = module_0.Group(str_2)
        var_1 = group_0.add_child_group(group_1)
        var_2 = group_2.add_child_group(group_1)
        var_3 = group_0.add_host(group_1)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = "N#'\x0chA0)G|s"
        group_0 = module_0.Group(str_0)
        var_0 = group_0.get_descendants()
        group_1 = module_0.Group()
        var_1 = group_1.clear_hosts_cache()
        group_2 = module_0.Group()
        var_2 = group_2.__getstate__()
        var_3 = group_2.__repr__()
        var_4 = group_2.__getstate__()
        var_5 = group_2.get_vars()
        var_6 = group_1.get_hosts()
        group_3 = module_0.Group()
        bytes_0 = b'j\x1bq\x8f'
        var_7 = group_2.set_priority(bytes_0)
    except BaseException:
        pass

def test_case_9():
    try:
        group_0 = module_0.Group()
        str_0 = 'cU(k\x0cbF('
        group_1 = module_0.Group(str_0)
        var_0 = group_1.clear_hosts_cache()
        var_1 = group_0.get_name()
        var_2 = group_1.add_child_group(group_1)
    except BaseException:
        pass

def test_case_10():
    try:
        group_0 = module_0.Group()
        var_0 = group_0.get_hosts()
        var_1 = group_0.get_ancestors()
        var_2 = group_0.remove_host(group_0)
        group_1 = module_0.Group()
        var_3 = group_1.__str__()
        var_4 = group_0.add_host(group_1)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = 'g1'
        group_0 = module_0.Group(str_0)
        str_1 = 'g2'
        group_1 = module_0.Group(str_1)
        str_2 = 'g3'
        group_2 = module_0.Group(str_2)
        var_0 = group_0.add_child_group(group_1)
        var_1 = group_2.add_child_group(group_1)
        var_2 = group_0.add_host(group_1)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = 'g1'
        group_0 = module_0.Group(str_0)
        str_1 = 'g2'
        group_1 = module_0.Group(str_1)
        str_2 = 'g3'
        group_2 = module_0.Group(str_2)
        var_0 = group_0.add_child_group(group_1)
        var_1 = group_2.add_child_group(group_1)
        var_2 = group_1.__getstate__()
        var_3 = group_0.add_host(group_1)
    except BaseException:
        pass

def test_case_13():
    try:
        group_0 = module_0.Group()
        var_0 = group_0.get_hosts()
        var_1 = group_0.get_ancestors()
        var_2 = group_0.get_vars()
        var_3 = group_0.__str__()
        str_0 = 'gRl 6'
        str_1 = 'cU(k\x0cbF('
        dict_0 = {}
        var_4 = group_0.deserialize(dict_0)
        var_5 = group_0.__getstate__()
        group_1 = module_0.Group(str_1)
        var_6 = group_0.__repr__()
        var_7 = group_0.get_hosts()
        list_0 = [str_0, group_1]
        var_8 = group_0.set_priority(list_0)
        var_9 = group_1.get_name()
        var_10 = group_1.add_child_group(group_0)
        var_11 = group_0.clear_hosts_cache()
        var_12 = group_0.add_child_group(group_1)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = 'g1'
        group_0 = module_0.Group(str_0)
        str_1 = 'g2'
        group_1 = module_0.Group(str_1)
        group_2 = module_0.Group(str_0)
        var_0 = group_0.add_child_group(group_1)
        var_1 = group_2.add_child_group(group_1)
        var_2 = group_0.add_host(group_1)
    except BaseException:
        pass