# Automatically generated by Pynguin.
import ansible.playbook.task_include as module_0
import ansible.utils.display as module_1

def test_case_0():
    pass

def test_case_1():
    task_include_0 = module_0.TaskInclude()

def test_case_2():
    task_include_0 = module_0.TaskInclude()
    var_0 = task_include_0.get_vars()

def test_case_3():
    task_include_0 = module_0.TaskInclude()
    var_0 = task_include_0.build_parent_block()

def test_case_4():
    display_0 = module_1.Display()
    str_0 = 'import_tasks'
    var_0 = dict(file=str_0)
    bool_0 = False
    var_1 = dict(action=str_0, args=var_0, rc=bool_0, changed=bool_0)
    task_include_0 = module_0.TaskInclude()
    var_2 = task_include_0.preprocess_data(var_1)