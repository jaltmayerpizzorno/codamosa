# Automatically generated by Pynguin.
import ansible.playbook.task_include as module_0

def test_case_0():
    pass

def test_case_1():
    task_include_0 = module_0.TaskInclude()
    var_0 = task_include_0.build_parent_block()

def test_case_2():
    task_include_0 = module_0.TaskInclude()
    var_0 = task_include_0.get_vars()

def test_case_3():
    task_include_0 = module_0.TaskInclude()
    str_0 = 'action'
    str_1 = 'args'
    str_2 = 'include'
    str_3 = 'var1'
    str_4 = 'var2'
    str_5 = 'var3'
    str_6 = 'foo'
    str_7 = 'baz'
    str_8 = {str_3: str_6, str_4: str_3, str_5: str_7}
    str_9 = {str_0: str_2, str_1: str_8}
    var_0 = task_include_0.load_data(str_9)
    var_1 = task_include_0.get_vars()