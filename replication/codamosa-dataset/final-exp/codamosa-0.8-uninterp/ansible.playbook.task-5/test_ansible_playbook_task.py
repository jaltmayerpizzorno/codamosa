# Automatically generated by Pynguin.
import ansible.playbook.task as module_0

def test_case_0():
    pass

def test_case_1():
    task_0 = module_0.Task()

def test_case_2():
    task_0 = module_0.Task()
    var_0 = task_0.__repr__()

def test_case_3():
    task_0 = module_0.Task()
    var_0 = task_0.get_vars()

def test_case_4():
    task_0 = module_0.Task()
    task_1 = module_0.Task(task_0)
    str_0 = 'no_log'
    var_0 = task_1.get_name(str_0)
    var_1 = task_1.get_vars()
    var_2 = task_1.serialize()
    var_3 = task_0.get_first_parent_include()
    var_4 = task_1.get_first_parent_include()
    var_5 = task_0.get_first_parent_include()
    tuple_0 = None
    var_6 = task_1.copy(tuple_0)

def test_case_5():
    task_0 = module_0.Task()
    var_0 = task_0.get_include_params()

def test_case_6():
    str_0 = "3X'\tK+zzc5P%U$I]k{"
    int_0 = 733
    int_1 = 70
    task_0 = module_0.Task(int_1)
    task_1 = module_0.Task(task_0, task_0)
    list_0 = [str_0, int_0, str_0, task_0]
    var_0 = task_1.get_name(list_0)
    var_1 = task_1.copy(str_0, int_0)

def test_case_7():
    task_0 = module_0.Task()
    var_0 = task_0.serialize()

def test_case_8():
    tuple_0 = ()
    int_0 = 233
    bool_0 = True
    dict_0 = {int_0: tuple_0, int_0: tuple_0, bool_0: tuple_0, tuple_0: int_0}
    task_0 = module_0.Task(dict_0)
    var_0 = task_0.get_name()
    str_0 = '{o(s16KV|H`z'
    tuple_1 = (tuple_0, int_0, str_0)
    bytes_0 = b'Xi#\xc4%'
    str_1 = '95HNZ\t]`'
    task_1 = module_0.Task(str_1)
    var_1 = task_1.copy(tuple_1, bytes_0)

def test_case_9():
    task_0 = module_0.Task()
    str_0 = 'ebug'
    str_1 = '2.10'
    var_0 = dict(action=str_0, _ansible_version=str_1, args=task_0)
    var_1 = task_0.deserialize(var_0)
    var_2 = dict()

def test_case_10():
    str_0 = 'oe'
    var_0 = dict(nope=str_0)
    var_1 = dict(action=str_0)
    task_0 = module_0.Task()
    var_2 = task_0.preprocess_data(var_1)
    var_3 = dict(nope=var_1)
    var_4 = dict(action=var_3)
    task_1 = module_0.Task()

def test_case_11():
    str_0 = 'oX'
    var_0 = dict(nope=str_0)
    var_1 = dict(action=str_0)
    task_0 = module_0.Task()
    var_2 = task_0.preprocess_data(var_1)
    var_3 = dict(nope=var_1)
    var_4 = dict(action=var_3)
    task_1 = module_0.Task()
    var_5 = task_0.preprocess_data(var_2)