# Automatically generated by Pynguin.
import ansible.inventory.group as module_0

def test_case_0():
    try:
        group_0 = module_0.Group()
        var_0 = group_0.__repr__()
        var_1 = group_0.clear_hosts_cache()
        var_2 = group_0.add_host(group_0)
    except BaseException:
        pass

def test_case_1():
    try:
        group_0 = module_0.Group()
        var_0 = group_0.get_hosts()
        var_1 = group_0.get_descendants()
        str_0 = 'E)P~B4U'
        float_0 = 0.001
        var_2 = group_0.__getstate__()
        var_3 = group_0.clear_hosts_cache()
        var_4 = group_0.set_variable(str_0, float_0)
        var_5 = group_0.clear_hosts_cache()
        var_6 = group_0.add_host(group_0)
    except BaseException:
        pass

def test_case_2():
    try:
        group_0 = module_0.Group()
        var_0 = group_0.serialize()
        bytes_0 = b'v\x9eM\x06\xa9\xe5c\xad7'
        var_1 = group_0.__setstate__(bytes_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bool_0 = False
        group_0 = module_0.Group()
        var_0 = group_0.add_child_group(bool_0)
    except BaseException:
        pass

def test_case_4():
    try:
        group_0 = module_0.Group()
        var_0 = group_0.add_host(group_0)
    except BaseException:
        pass

def test_case_5():
    try:
        group_0 = module_0.Group()
        var_0 = group_0.get_descendants()
        str_0 = '^B\x0cQQL=a.ZEU['
        float_0 = 0.001
        var_1 = group_0.clear_hosts_cache()
        list_0 = [float_0]
        var_2 = group_0.set_priority(list_0)
        var_3 = group_0.set_variable(str_0, float_0)
        var_4 = group_0.add_host(group_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '.swp'
        group_0 = module_0.Group()
        var_0 = group_0.get_vars()
        dict_0 = {str_0: str_0}
        group_1 = module_0.Group()
        var_1 = group_1.deserialize(dict_0)
        group_2 = module_0.Group()
        str_1 = 'download_only'
        var_2 = group_2.set_priority(str_1)
    except BaseException:
        pass

def test_case_7():
    try:
        group_0 = module_0.Group()
        var_0 = group_0.get_hosts()
        var_1 = group_0.get_hosts()
        str_0 = 'E)P~B4U'
        float_0 = 0.001
        list_0 = [float_0]
        var_2 = group_0.set_priority(list_0)
        var_3 = group_0.set_variable(str_0, float_0)
        var_4 = group_0.clear_hosts_cache()
        var_5 = group_0.add_host(group_0)
    except BaseException:
        pass

def test_case_8():
    try:
        group_0 = module_0.Group()
        var_0 = group_0.get_hosts()
        group_1 = module_0.Group()
        var_1 = group_0.get_vars()
        var_2 = group_0.add_child_group(group_1)
        var_3 = group_0.get_name()
        var_4 = group_1.clear_hosts_cache()
        var_5 = group_1.remove_host(group_1)
        var_6 = group_1.add_host(group_1)
    except BaseException:
        pass

def test_case_9():
    try:
        group_0 = module_0.Group()
        var_0 = group_0.get_name()
        var_1 = group_0.get_name()
        var_2 = group_0.add_child_group(group_0)
    except BaseException:
        pass

def test_case_10():
    try:
        group_0 = module_0.Group()
        var_0 = group_0.serialize()
        group_1 = module_0.Group()
        var_1 = group_1.get_hosts()
        group_2 = module_0.Group()
        var_2 = group_2.get_vars()
        var_3 = group_1.add_child_group(group_2)
        var_4 = group_1.get_name()
        var_5 = group_2.clear_hosts_cache()
        var_6 = group_2.remove_host(group_2)
        var_7 = group_2.add_child_group(group_1)
    except BaseException:
        pass

def test_case_11():
    try:
        group_0 = module_0.Group()
        var_0 = group_0.get_hosts()
        group_1 = module_0.Group()
        var_1 = group_0.get_vars()
        var_2 = group_0.add_child_group(group_1)
        var_3 = group_0.get_name()
        var_4 = group_1.remove_host(group_1)
        var_5 = group_1.add_host(group_1)
    except BaseException:
        pass

def test_case_12():
    try:
        group_0 = module_0.Group()
        var_0 = group_0.serialize()
        group_1 = module_0.Group()
        var_1 = group_1.get_vars()
        var_2 = group_0.add_child_group(group_1)
        var_3 = group_0.get_name()
        str_0 = '$)ZE}\t]'
        var_4 = group_1.remove_host(group_1)
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: var_1, str_0: str_0}
        var_5 = group_0.add_child_group(group_1)
        var_6 = group_1.get_ancestors()
        group_2 = module_0.Group()
        var_7 = group_2.__str__()
        group_3 = module_0.Group()
        var_8 = group_1.__getstate__()
        bytes_0 = b'\xf5\x8c\xb7\x1d@\x06\xc1\xe8\xec\xedX\xbb3\xa3\xeb'
        set_0 = {group_1, bytes_0}
        list_0 = [var_1]
        tuple_0 = (set_0, str_0, dict_0, list_0)
        var_9 = group_1.set_variable(bytes_0, tuple_0)
        var_10 = group_1.get_hosts()
        var_11 = group_2.__setstate__(tuple_0)
    except BaseException:
        pass

def test_case_13():
    try:
        group_0 = module_0.Group()
        group_1 = module_0.Group()
        var_0 = group_1.set_priority(group_0)
        str_0 = 'BU7C<`'
        group_2 = module_0.Group()
        var_1 = group_2.get_hosts()
        var_2 = group_2.get_hosts()
        group_3 = module_0.Group()
        var_3 = group_3.get_vars()
        set_0 = None
        var_4 = group_2.set_variable(str_0, set_0)
        var_5 = group_2.add_child_group(group_3)
        str_1 = 'plugin redirect loop resolving {0} (path: {1})'
        list_0 = [var_5]
        var_6 = module_0.to_safe_group_name(str_1, str_0, list_0)
        var_7 = group_3.clear_hosts_cache()
        var_8 = group_3.remove_host(group_3)
        int_0 = 65001
        var_9 = group_2.set_variable(str_0, int_0)
        var_10 = group_0.__str__()
        group_4 = module_0.Group()
        var_11 = group_3.__getstate__()
        var_12 = group_3.clear_hosts_cache()
        var_13 = group_3.serialize()
        var_14 = group_2.get_hosts()
        var_15 = group_4.get_vars()
        var_16 = group_4.add_host(group_4)
    except BaseException:
        pass