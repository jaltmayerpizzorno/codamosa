# Automatically generated by Pynguin.
import ansible.inventory.group as module_0

def test_case_0():
    try:
        str_0 = 'some-file@some_host'
        var_0 = module_0.to_safe_group_name(str_0)
        str_1 = '[_.:]some-file@some_host'
        var_1 = module_0.to_safe_group_name(str_1)
        bool_0 = True
        var_2 = module_0.to_safe_group_name(str_1, bool_0)
        bool_1 = False
        var_3 = module_0.to_safe_group_name(str_1, bool_1)
        var_4 = module_0.to_safe_group_name(str_1, bool_1, bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        group_0 = module_0.Group()
        bool_0 = False
        var_0 = group_0.add_host(bool_0)
    except BaseException:
        pass

def test_case_2():
    try:
        group_0 = module_0.Group()
        bytes_0 = b'6E\xa7\xfd'
        var_0 = group_0.get_name()
        var_1 = group_0.set_priority(bytes_0)
    except BaseException:
        pass

def test_case_3():
    try:
        group_0 = module_0.Group()
        var_0 = group_0.set_priority(group_0)
        var_1 = group_0.get_name()
        var_2 = group_0.add_child_group(group_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'test2'
        group_0 = module_0.Group(str_0)
        var_0 = group_0.add_host(group_0)
    except BaseException:
        pass

def test_case_5():
    try:
        group_0 = module_0.Group()
        var_0 = group_0.__repr__()
        var_1 = group_0.set_priority(group_0)
        var_2 = group_0.get_name()
        group_1 = module_0.Group()
        var_3 = group_1.add_child_group(group_0)
        var_4 = group_0.serialize()
        var_5 = group_0.serialize()
        var_6 = group_1.get_vars()
        var_7 = group_1.get_hosts()
        float_0 = -2587.583754429654
        group_2 = module_0.Group(float_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '|yhR_p;bE\x0b}.'
        int_0 = -1891
        bool_0 = False
        group_0 = module_0.Group(bool_0)
        var_0 = group_0.set_variable(str_0, int_0)
        group_1 = module_0.Group()
        var_1 = group_1.serialize()
        var_2 = group_1.__repr__()
        var_3 = group_1.set_priority(group_1)
        var_4 = group_1.get_name()
        group_2 = module_0.Group()
        var_5 = group_2.add_child_group(group_1)
        var_6 = group_1.serialize()
        var_7 = group_1.serialize()
        complex_0 = None
        var_8 = group_1.set_variable(group_2, complex_0)
        str_1 = '\\*'
        dict_0 = {str_0: var_7, str_0: str_1}
        var_9 = group_0.set_variable(str_0, dict_0)
        var_10 = group_2.deserialize(var_6)
        var_11 = group_2.serialize()
        var_12 = group_2.__str__()
        var_13 = group_2.get_hosts()
        group_3 = module_0.Group(str_1)
        group_4 = module_0.Group()
        var_14 = group_0.serialize()
        tuple_0 = None
        var_15 = group_1.deserialize(tuple_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'G1'
        group_0 = module_0.Group(str_0)
        str_1 = 'G4'
        group_1 = module_0.Group(str_1)
        str_2 = 'G6'
        group_2 = module_0.Group(str_2)
        str_3 = 'G7'
        group_3 = module_0.Group(str_3)
        str_4 = 'G9'
        var_0 = group_3.__repr__()
        group_4 = module_0.Group(str_4)
        var_1 = group_0.add_child_group(group_4)
        var_2 = group_2.add_child_group(group_0)
        var_3 = group_1.add_child_group(group_0)
        var_4 = group_1.add_child_group(group_2)
        var_5 = group_1.serialize()
        var_6 = group_0.deserialize(group_4)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'G1'
        group_0 = module_0.Group(str_0)
        str_1 = ''
        group_1 = module_0.Group(str_1)
        str_2 = 'G4'
        group_2 = module_0.Group(str_2)
        group_3 = module_0.Group(str_0)
        str_3 = 'G7'
        group_4 = module_0.Group(str_3)
        str_4 = 'G8'
        group_5 = module_0.Group(str_4)
        str_5 = 'G9'
        group_6 = module_0.Group(str_5)
        var_0 = group_0.add_child_group(group_5)
        var_1 = group_3.add_child_group(group_1)
        var_2 = group_1.add_child_group(group_2)
        var_3 = group_2.add_child_group(group_0)
        var_4 = group_2.add_child_group(group_3)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'G1'
        group_0 = module_0.Group(str_0)
        str_1 = 'G4'
        group_1 = module_0.Group(str_1)
        str_2 = 'G7'
        group_2 = module_0.Group(str_2)
        str_3 = 'G9'
        var_0 = group_2.__repr__()
        group_3 = module_0.Group(str_3)
        var_1 = group_0.add_child_group(group_3)
        var_2 = group_2.add_child_group(group_0)
        var_3 = group_2.add_child_group(group_1)
        var_4 = group_1.add_child_group(group_0)
        var_5 = group_1.add_child_group(group_0)
        var_6 = group_1.serialize()
        var_7 = group_0.deserialize(group_3)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = '|yhR_p;bE\x0b}.'
        int_0 = -1891
        bool_0 = False
        group_0 = module_0.Group(bool_0)
        var_0 = group_0.set_variable(str_0, int_0)
        group_1 = module_0.Group()
        var_1 = group_1.serialize()
        var_2 = group_1.__repr__()
        var_3 = group_1.set_priority(group_1)
        var_4 = group_1.get_name()
        var_5 = group_0.clear_hosts_cache()
        group_2 = module_0.Group()
        var_6 = group_2.add_child_group(group_1)
        var_7 = group_1.serialize()
        var_8 = group_1.serialize()
        complex_0 = None
        var_9 = group_1.set_variable(group_2, complex_0)
        str_1 = ''
        bytes_0 = b'\xe1\x15\xe8\xa4J\xa1\x9c\x99\x93)\xce\x19?-r('
        dict_0 = {str_0: var_8, str_0: str_1}
        var_10 = group_0.set_variable(str_0, dict_0)
        dict_1 = {str_1: bytes_0, str_1: group_2, str_1: str_1}
        var_11 = group_1.deserialize(dict_1)
        var_12 = group_2.serialize()
        var_13 = group_2.__str__()
        var_14 = group_1.add_child_group(group_2)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = 'G4'
        group_0 = module_0.Group(str_0)
        var_0 = group_0.remove_host(group_0)
        group_1 = module_0.Group(str_0)
        str_1 = 'G6'
        group_2 = module_0.Group(str_1)
        str_2 = 'G8'
        group_3 = module_0.Group(str_2)
        var_1 = group_3.add_child_group(group_0)
        var_2 = group_2.add_child_group(group_0)
        var_3 = group_1.get_vars()
        var_4 = group_0.add_host(group_2)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = ',\x0cy[ n7i`>12vR\x0b`fZ;c'
        group_0 = module_0.Group(str_0)
        var_0 = group_0.remove_host(group_0)
        str_1 = 'G6'
        var_1 = group_0.get_name()
        group_1 = module_0.Group(str_1)
        group_2 = module_0.Group(str_1)
        var_2 = group_2.add_child_group(group_0)
        var_3 = group_1.add_child_group(group_0)
        var_4 = group_1.get_vars()
        var_5 = group_1.add_host(group_1)
    except BaseException:
        pass