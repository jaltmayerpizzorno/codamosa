# Automatically generated by Pynguin.
import ansible.inventory.group as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = '1\n(@O\ny|v#)\x0bV$dZ'
    group_0 = module_0.Group(str_0)

def test_case_2():
    group_0 = module_0.Group()

def test_case_3():
    group_0 = module_0.Group()
    var_0 = group_0.__repr__()
    str_0 = '|[-~'
    dict_0 = {str_0: str_0}
    var_1 = group_0.__getstate__()
    var_2 = group_0.get_vars()
    var_3 = group_0.deserialize(dict_0)

def test_case_4():
    group_0 = module_0.Group()
    var_0 = group_0.__getstate__()

def test_case_5():
    group_0 = module_0.Group()
    var_0 = group_0.get_hosts()

def test_case_6():
    group_0 = module_0.Group()
    var_0 = group_0.get_descendants()

def test_case_7():
    group_0 = module_0.Group()
    var_0 = group_0.clear_hosts_cache()

def test_case_8():
    group_0 = module_0.Group()
    var_0 = group_0.get_name()

def test_case_9():
    str_0 = "'tst"
    group_0 = module_0.Group(str_0)
    group_1 = module_0.Group(str_0)
    var_0 = group_0.add_child_group(group_1)

def test_case_10():
    group_0 = module_0.Group()
    var_0 = group_0.remove_host(group_0)

def test_case_11():
    group_0 = module_0.Group()
    float_0 = -1074.0
    group_1 = module_0.Group()
    var_0 = group_1.set_variable(group_0, float_0)

def test_case_12():
    str_0 = "'tst"
    group_0 = module_0.Group(str_0)
    group_1 = module_0.Group(str_0)
    var_0 = group_0.add_child_group(group_1)
    var_1 = group_0.get_vars()

def test_case_13():
    str_0 = 'g'
    group_0 = module_0.Group(str_0)
    bytes_0 = b'h\xe9\xc6\xc3\xb5\xff\xe4\xdf\xf8\x84\x9ds\xb8\x1a\xbe\xfc'
    float_0 = 266.0
    var_0 = group_0.set_variable(bytes_0, float_0)

def test_case_14():
    group_0 = module_0.Group()
    var_0 = group_0.get_descendants()
    group_1 = module_0.Group()
    var_1 = group_0.__getstate__()
    group_2 = module_0.Group()
    group_3 = module_0.Group()
    var_2 = group_3.get_name()
    var_3 = group_3.get_hosts()
    var_4 = group_1.get_ancestors()
    var_5 = group_2.__str__()
    var_6 = group_1.add_child_group(group_3)

def test_case_15():
    str_0 = 'hostgroup-with-dashes'
    var_0 = module_0.to_safe_group_name(str_0)
    str_1 = 'host group with spaces'
    var_1 = module_0.to_safe_group_name(str_1)
    str_2 = '-'
    var_2 = module_0.to_safe_group_name(str_1, str_2)
    bool_0 = True
    var_3 = module_0.to_safe_group_name(str_1, str_2, bool_0)
    var_4 = module_0.to_safe_group_name(str_1, str_2, bool_0)

def test_case_16():
    group_0 = module_0.Group()
    var_0 = group_0.get_descendants()
    group_1 = module_0.Group()
    var_1 = group_0.__getstate__()
    group_2 = module_0.Group()
    group_3 = module_0.Group()
    var_2 = group_3.get_name()
    var_3 = group_3.get_hosts()
    var_4 = group_1.get_ancestors()
    var_5 = group_2.__str__()
    var_6 = group_1.add_child_group(group_3)
    var_7 = group_3.clear_hosts_cache()

def test_case_17():
    float_0 = None
    str_0 = 'zPYK#\tm^,H<g'
    float_1 = 1024.882728
    str_1 = '`s[gtbH=P+Lk6r3'
    dict_0 = {str_0: float_0, str_0: float_1, str_1: float_0}
    group_0 = module_0.Group()
    var_0 = group_0.set_priority(dict_0)
    int_0 = -964
    var_1 = group_0.set_variable(str_1, int_0)
    group_1 = module_0.Group()
    var_2 = group_1.add_child_group(group_0)
    var_3 = group_1.get_descendants()
    group_2 = module_0.Group()
    var_4 = group_2.remove_host(group_0)
    int_1 = -1202
    str_2 = 'REPL co5sole for executijg Ansible tasks.'
    var_5 = group_2.set_variable(int_1, str_2)
    var_6 = group_2.get_name()
    var_7 = group_0.get_ancestors()
    var_8 = group_0.get_ancestors()
    var_9 = group_2.get_descendants()
    var_10 = group_1.get_hosts()
    var_11 = group_0.get_vars()
    var_12 = group_2.get_name()
    group_3 = module_0.Group()
    var_13 = group_3.get_ancestors()
    var_14 = group_2.deserialize(dict_0)
    var_15 = group_2.__str__()
    var_16 = group_2.add_child_group(group_0)

def test_case_18():
    group_0 = module_0.Group()
    str_0 = '`s[gtH=P+Lk6r3'
    str_1 = '1'
    var_0 = group_0.set_variable(str_0, str_1)
    str_2 = 'a'
    var_1 = group_0.set_variable(str_0, str_2)
    str_3 = 'test'
    str_4 = 'test2'
    str_5 = {str_4: str_4}
    var_2 = group_0.set_variable(str_3, str_5)

def test_case_19():
    group_0 = module_0.Group()
    str_0 = 'a'
    str_1 = 'a1'
    str_2 = 'a2'
    str_3 = 'v1'
    str_4 = 'v2'
    str_5 = {str_1: str_3, str_2: str_4}
    var_0 = group_0.set_variable(str_0, str_5)
    str_6 = 'a3'
    str_7 = 'v2_new'
    str_8 = 'v3'
    str_9 = {str_2: str_7, str_6: str_8}
    var_1 = group_0.set_variable(str_0, str_9)
    var_2 = group_0.get_hosts()

def test_case_20():
    group_0 = module_0.Group()
    str_0 = 'a'
    str_1 = 'a1'
    str_2 = 'a2'
    str_3 = {str_1: str_1, str_2: str_2}
    var_0 = group_0.set_variable(str_0, str_3)
    var_1 = group_0.set_variable(str_0, str_1)
    str_4 = 'whatever'
    var_2 = group_0.set_variable(str_0, str_4)