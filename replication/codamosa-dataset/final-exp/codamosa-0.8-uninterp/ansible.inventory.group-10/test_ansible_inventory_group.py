# Automatically generated by Pynguin.
import ansible.inventory.group as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'gr#up1'
    group_0 = module_0.Group(str_0)

def test_case_2():
    group_0 = module_0.Group()

def test_case_3():
    group_0 = module_0.Group()
    var_0 = group_0.__str__()

def test_case_4():
    group_0 = module_0.Group()
    var_0 = group_0.__getstate__()

def test_case_5():
    dict_0 = {}
    group_0 = module_0.Group()
    var_0 = group_0.deserialize(dict_0)

def test_case_6():
    group_0 = module_0.Group()
    var_0 = group_0.get_hosts()

def test_case_7():
    group_0 = module_0.Group()
    var_0 = group_0.get_ancestors()
    var_1 = group_0.get_vars()

def test_case_8():
    int_0 = 300
    group_0 = module_0.Group()
    var_0 = group_0.get_name()
    var_1 = group_0.clear_hosts_cache()
    var_2 = group_0.set_variable(int_0, int_0)
    var_3 = group_0.set_priority(group_0)

def test_case_9():
    str_0 = 'test'
    group_0 = module_0.Group(str_0)
    str_1 = 'test_child'
    group_1 = module_0.Group(str_1)
    var_0 = group_0.add_child_group(group_1)

def test_case_10():
    group_0 = module_0.Group()
    var_0 = group_0.get_hosts()
    group_1 = module_0.Group()
    var_1 = group_0.get_ancestors()
    var_2 = group_0.add_child_group(group_1)
    var_3 = group_1.__getstate__()

def test_case_11():
    group_0 = module_0.Group()
    str_0 = 'key'
    str_1 = 'value'
    var_0 = group_0.set_variable(str_0, str_1)
    var_1 = group_0.set_variable(str_0, str_1)
    var_2 = group_0.vars[str_0]
    str_2 = 'ansible_group_priority'
    str_3 = '1'
    var_3 = group_0.set_variable(str_2, str_3)
    bool_0 = True
    var_4 = group_0.set_variable(str_2, bool_0)
    float_0 = 0.5
    var_5 = group_0.set_variable(str_2, float_0)

def test_case_12():
    str_0 = ''
    group_0 = module_0.Group(str_0)
    group_1 = module_0.Group(str_0)
    group_2 = module_0.Group(str_0)
    var_0 = group_0.add_child_group(group_2)
    var_1 = group_1.add_child_group(group_0)
    group_3 = module_0.Group()
    var_2 = group_3.set_variable(group_1, str_0)

def test_case_13():
    group_0 = module_0.Group()
    group_1 = module_0.Group()
    group_2 = module_0.Group()
    group_3 = module_0.Group()
    group_4 = module_0.Group()
    group_5 = module_0.Group()
    var_0 = group_0.add_child_group(group_1)
    var_1 = group_0.add_child_group(group_1)
    var_2 = group_1.add_child_group(group_2)
    group_6 = module_0.Group()

def test_case_14():
    str_0 = 'abcd'
    var_0 = module_0.to_safe_group_name(str_0)
    str_1 = '|abcd'
    str_2 = '_'
    var_1 = module_0.to_safe_group_name(str_1, str_2)
    bool_0 = True
    var_2 = module_0.to_safe_group_name(str_1, str_2, bool_0)

def test_case_15():
    str_0 = 'Unit test for method set_variable of class Group'
    str_1 = 'test_group_set_variable'
    group_0 = module_0.Group(str_1)
    str_2 = 'key'
    str_3 = 'value'
    var_0 = group_0.set_variable(str_2, str_3)
    str_4 = 'dict_key'
    var_1 = {}
    var_2 = group_0.set_variable(str_4, var_1)
    str_5 = 'key1'
    str_6 = {str_5: str_0}
    var_3 = group_0.set_variable(str_4, str_6)
    var_4 = group_0.set_variable(str_4, str_4)

def test_case_16():
    str_0 = 'name'
    str_1 = 'vars'
    str_2 = 'depth'
    str_3 = 'hosts'
    str_4 = 'parent_groups'
    str_5 = 'test'
    str_6 = 'var1'
    str_7 = 'v1'
    str_8 = {str_6: str_7}
    int_0 = 3
    str_9 = 'hoJtf'
    str_10 = 'host2'
    str_11 = [str_9, str_10]
    str_12 = 'parent1'
    var_0 = []
    var_1 = {str_0: str_12, str_4: var_0}
    str_13 = 'parent2'
    var_2 = []
    var_3 = {str_0: str_13, str_4: var_2}
    var_4 = [var_1, var_3]
    var_5 = {str_0: str_5, str_1: str_8, str_2: int_0, str_3: str_11, str_4: var_4}
    group_0 = module_0.Group(str_5)
    var_6 = group_0.deserialize(var_5)

def test_case_17():
    str_0 = 'g1'
    group_0 = module_0.Group(str_0)
    str_1 = 'g2'
    group_1 = module_0.Group(str_1)
    str_2 = 'g3'
    group_2 = module_0.Group(str_2)
    str_3 = 'g4'
    group_3 = module_0.Group(str_3)
    str_4 = 'g5'
    group_4 = module_0.Group(str_4)
    var_0 = group_0.add_child_group(group_1)
    var_1 = group_1.add_child_group(group_2)
    var_2 = group_0.add_child_group(group_3)
    var_3 = group_3.add_child_group(group_4)
    bool_0 = True
    var_4 = group_0.get_descendants()

def test_case_18():
    str_0 = 'A'
    group_0 = module_0.Group(str_0)
    str_1 = 'B'
    group_1 = module_0.Group(str_1)
    str_2 = 'C'
    group_2 = module_0.Group(str_2)
    str_3 = 'D'
    group_3 = module_0.Group(str_3)
    str_4 = 'E'
    group_4 = module_0.Group(str_4)
    str_5 = 'F'
    group_5 = module_0.Group(str_5)
    var_0 = group_0.add_child_group(group_1)
    var_1 = group_1.add_child_group(group_3)
    var_2 = group_1.add_child_group(group_4)
    var_3 = group_2.add_child_group(group_4)
    var_4 = group_3.add_child_group(group_5)
    var_5 = group_1.get_hosts()
    var_6 = group_5.get_ancestors()
    var_7 = group_0.get_descendants()
    var_8 = group_2.get_descendants()
    bool_0 = True
    var_9 = group_2.get_descendants()
    var_10 = group_1.__repr__()

def test_case_19():
    str_0 = 'A'
    group_0 = module_0.Group(str_0)
    group_1 = module_0.Group(str_0)
    str_1 = ''
    group_2 = module_0.Group(str_1)
    str_2 = 'D'
    group_3 = module_0.Group(str_2)
    str_3 = 'E'
    group_4 = module_0.Group(str_3)
    str_4 = 'F'
    group_5 = module_0.Group(str_4)
    var_0 = group_0.add_child_group(group_1)
    var_1 = group_1.add_child_group(group_3)
    var_2 = group_1.add_child_group(group_4)
    var_3 = group_2.add_child_group(group_4)
    var_4 = group_3.add_child_group(group_5)
    var_5 = group_5.get_ancestors()
    group_6 = module_0.Group()

def test_case_20():
    str_0 = 'A'
    group_0 = module_0.Group(str_0)
    group_1 = module_0.Group(str_0)
    group_2 = module_0.Group(str_0)
    str_1 = 'D'
    var_0 = group_0.get_descendants()
    group_3 = module_0.Group(str_1)
    str_2 = 'E'
    group_4 = module_0.Group(str_2)
    var_1 = group_1.add_child_group(group_3)
    var_2 = group_1.add_child_group(group_4)
    var_3 = group_2.add_child_group(group_4)
    var_4 = group_3.add_child_group(group_2)
    var_5 = group_3.get_ancestors()
    group_5 = module_0.Group()
    var_6 = group_5.set_variable(group_4, str_1)

def test_case_21():
    str_0 = "R\nlA{{='=UA}$crlp);"
    group_0 = module_0.Group(str_0)
    group_1 = module_0.Group(str_0)
    var_0 = group_0.add_child_group(group_1)
    str_1 = ''
    group_2 = module_0.Group(str_1)
    str_2 = '`b7p'
    var_1 = group_0.get_descendants()
    group_3 = module_0.Group(str_2)
    str_3 = 'gHv[wA&NQ"'
    group_4 = module_0.Group(str_3)
    str_4 = 'F'
    var_2 = group_1.add_child_group(group_4)
    var_3 = group_2.add_child_group(group_4)
    var_4 = group_3.add_child_group(group_2)
    var_5 = group_3.get_ancestors()
    bool_0 = True
    set_0 = {str_0, group_4, bool_0, str_4}
    group_5 = module_0.Group()
    var_6 = group_5.set_variable(bool_0, set_0)

def test_case_22():
    str_0 = "R\nlA{{='=UA}$crlp);"
    group_0 = module_0.Group(str_0)
    group_1 = module_0.Group(str_0)
    str_1 = ''
    var_0 = group_0.get_descendants()
    group_2 = module_0.Group(str_1)
    str_2 = 'D'
    var_1 = group_0.get_descendants()
    group_3 = module_0.Group(str_2)
    str_3 = 'gHv[wA&NQ"'
    var_2 = group_2.add_child_group(group_1)
    group_4 = module_0.Group(str_3)
    var_3 = group_1.add_child_group(group_4)
    var_4 = group_2.add_child_group(group_4)
    var_5 = group_3.add_child_group(group_2)
    var_6 = group_3.get_ancestors()
    group_5 = module_0.Group()
    str_4 = 'F\r<B.o4'
    var_7 = group_2.set_variable(str_4, str_1)