# Automatically generated by Pynguin.
import ansible.playbook.task_include as module_0

def test_case_0():
    pass

def test_case_1():
    task_include_0 = module_0.TaskInclude()

def test_case_2():
    str_0 = 'include'
    str_1 = {str_0: str_0, str_0: str_0, str_0: str_0}
    task_include_0 = module_0.TaskInclude(str_0, str_0, str_0)
    var_0 = task_include_0.load(str_1)

def test_case_3():
    bytes_0 = None
    task_include_0 = module_0.TaskInclude()
    var_0 = task_include_0.copy(bytes_0)

def test_case_4():
    task_include_0 = module_0.TaskInclude()
    var_0 = task_include_0.get_vars()

def test_case_5():
    task_include_0 = module_0.TaskInclude()
    var_0 = task_include_0.build_parent_block()