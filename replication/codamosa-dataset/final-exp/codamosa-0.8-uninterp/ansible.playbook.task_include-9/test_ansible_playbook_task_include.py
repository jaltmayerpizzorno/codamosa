# Automatically generated by Pynguin.
import ansible.playbook.task_include as module_0

def test_case_0():
    pass

def test_case_1():
    task_include_0 = module_0.TaskInclude()

def test_case_2():
    bytes_0 = b'\x85\xd1\xc6~\x8fm\x1a\xab\xc4z\x88\xc6mP\x06\xf6p2'
    list_0 = [bytes_0, bytes_0, bytes_0]
    bytes_1 = b'\xdb}X\x9a\rW\xb6\x1b\xa7'
    bool_0 = False
    task_include_0 = module_0.TaskInclude(bool_0)
    var_0 = task_include_0.build_parent_block()
    dict_0 = {}
    task_include_1 = module_0.TaskInclude(bytes_1, dict_0)
    var_1 = task_include_1.copy(list_0)

def test_case_3():
    task_include_0 = module_0.TaskInclude()
    var_0 = task_include_0.get_vars()

def test_case_4():
    task_include_0 = module_0.TaskInclude()
    var_0 = task_include_0.build_parent_block()

def test_case_5():
    str_0 = 'localhost'
    str_1 = '1'
    str_2 = '2'
    var_0 = dict(action=str_0, one=str_1, two=str_2)
    var_1 = None
    task_include_0 = module_0.TaskInclude(var_1, var_1, var_1)
    var_2 = task_include_0.preprocess_data(var_0)