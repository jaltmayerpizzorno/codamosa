# Automatically generated by Pynguin.
import ansible.playbook.helpers as module_0

def test_case_0():
    pass

def test_case_1():
    display_0 = None
    str_0 = 'rs\t|7T^K!DaW`(dZ0D:'
    var_0 = module_0.load_list_of_blocks(display_0, str_0)

def test_case_2():
    list_0 = []
    float_0 = 362.848
    set_0 = set()
    tuple_0 = (set_0, list_0)
    var_0 = module_0.load_list_of_tasks(list_0, float_0, tuple_0, set_0)

def test_case_3():
    str_0 = None
    list_0 = [str_0, str_0]
    int_0 = -401
    float_0 = None
    var_0 = module_0.load_list_of_blocks(list_0, int_0, float_0)

def test_case_4():
    str_0 = 'action'
    str_1 = 'ping'
    str_2 = {str_0: str_1}
    str_3 = [str_2]
    var_0 = None
    bool_0 = False
    var_1 = module_0.load_list_of_tasks(str_3, var_0, var_0, var_0, var_0, bool_0, var_0, var_0)
    var_2 = var_1[bool_0]
    var_3 = len(var_1)