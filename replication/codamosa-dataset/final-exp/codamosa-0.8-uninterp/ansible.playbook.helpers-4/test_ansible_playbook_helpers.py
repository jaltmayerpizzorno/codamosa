# Automatically generated by Pynguin.
import ansible.playbook.helpers as module_0
import ansible.utils.display as module_1

def test_case_0():
    pass

def test_case_1():
    str_0 = 'testmodule'
    var_0 = dict(module=str_0)
    var_1 = dict(action=var_0)
    var_2 = [var_1]
    var_3 = None
    bool_0 = False
    var_4 = module_0.load_list_of_tasks(var_2, var_3, var_3, var_3, var_3, bool_0, var_3, var_3)
    var_5 = dict(module=str_0)
    var_6 = dict(action=var_2)
    var_7 = dict(module=str_0)
    var_8 = dict(action=var_7)

def test_case_2():
    str_0 = 'testmodule'
    var_0 = dict(module=str_0)
    var_1 = dict(action=var_0)
    var_2 = [var_1]
    var_3 = None
    bool_0 = False
    list_0 = [var_3]
    display_0 = module_1.Display()
    var_4 = module_0.load_list_of_blocks(list_0, display_0, display_0, bool_0)
    var_5 = module_0.load_list_of_tasks(var_2, var_3, var_3, var_3, var_3, bool_0, var_3, var_3)
    var_6 = dict(module=str_0)
    var_7 = dict(action=var_6)
    var_8 = dict(module=str_0)
    var_9 = dict(action=var_8)