# Automatically generated by Pynguin.
import ansible.playbook.task as module_0

def test_case_0():
    try:
        bool_0 = True
        task_0 = module_0.Task(bool_0)
        list_0 = []
        tuple_0 = (task_0, list_0)
        bytes_0 = b"f\x16\xa6\xb5J'"
        var_0 = task_0.load(tuple_0, bool_0, bytes_0, bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = ''
        dict_0 = {str_0: str_0, str_0: str_0}
        task_0 = module_0.Task()
        var_0 = task_0.load(dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        task_0 = module_0.Task()
        var_0 = task_0.preprocess_data(task_0)
    except BaseException:
        pass

def test_case_3():
    try:
        task_0 = module_0.Task()
        set_0 = set()
        var_0 = task_0.post_validate(set_0)
    except BaseException:
        pass

def test_case_4():
    try:
        task_0 = module_0.Task()
        float_0 = -2395.853514219399
        task_1 = module_0.Task(float_0)
        var_0 = task_1.__repr__()
        bool_0 = False
        task_2 = module_0.Task(task_0, task_1, bool_0)
        task_3 = module_0.Task()
        var_1 = task_3.all_parents_static()
        str_0 = ':F&ESeqvVnLm#S'
        var_2 = task_1.get_name(str_0)
        var_3 = task_2.get_vars()
        var_4 = task_2.get_name()
        var_5 = task_0.get_name()
        var_6 = task_2.post_validate(task_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '8\r'
        task_0 = module_0.Task(str_0)
        var_0 = task_0.get_vars()
    except BaseException:
        pass

def test_case_6():
    try:
        task_0 = module_0.Task()
        task_1 = module_0.Task(task_0)
        var_0 = task_1.get_include_params()
        bool_0 = False
        str_0 = 'j!'
        task_2 = module_0.Task(bool_0, str_0)
        var_1 = task_1.get_vars()
        var_2 = task_2.get_name()
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'delegate_facts'
        task_0 = module_0.Task(str_0)
        var_0 = task_0.get_name()
        dict_0 = {}
        var_1 = task_0.copy(dict_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = '\nWP#\\q8}f9z'
        str_1 = '7F!HGK\\A5s&6r'
        float_0 = 285.56
        task_0 = module_0.Task(str_1, float_0)
        list_0 = [float_0, float_0, str_0, str_0]
        var_0 = task_0.copy(list_0)
        var_1 = task_0.serialize()
    except BaseException:
        pass

def test_case_9():
    try:
        var_0 = None
        int_0 = -2486
        tuple_0 = (int_0,)
        task_0 = module_0.Task()
        var_1 = task_0.copy(tuple_0)
        task_1 = module_0.Task()
        var_2 = task_1.post_validate(var_0)
    except BaseException:
        pass

def test_case_10():
    try:
        int_0 = 630
        task_0 = module_0.Task(int_0)
        var_0 = task_0.serialize()
    except BaseException:
        pass

def test_case_11():
    try:
        int_0 = -76
        task_0 = module_0.Task(int_0)
        var_0 = task_0.all_parents_static()
    except BaseException:
        pass

def test_case_12():
    try:
        float_0 = -2762.725
        task_0 = module_0.Task(float_0)
        var_0 = task_0.get_first_parent_include()
    except BaseException:
        pass

def test_case_13():
    try:
        task_0 = module_0.Task()
        dict_0 = {task_0: task_0}
        var_0 = task_0.preprocess_data(dict_0)
    except BaseException:
        pass

def test_case_14():
    try:
        float_0 = -215.354845
        str_0 = 'J%8\\4b+Q'
        task_0 = module_0.Task(float_0, str_0)
        task_1 = module_0.Task()
        var_0 = task_1.set_loader(task_1)
        var_1 = task_1.get_first_parent_include()
        dict_0 = {}
        var_2 = task_0.preprocess_data(dict_0)
    except BaseException:
        pass

def test_case_15():
    try:
        set_0 = set()
        str_0 = '>\x0c&ho8 dxhL8>*'
        task_0 = module_0.Task(set_0, str_0)
        var_0 = task_0.serialize()
    except BaseException:
        pass

def test_case_16():
    try:
        task_0 = module_0.Task()
        var_0 = task_0.get_first_parent_include()
        float_0 = -2395.853514219399
        task_1 = module_0.Task(float_0)
        var_1 = task_1.__repr__()
        bool_0 = False
        var_2 = task_0.copy()
        task_2 = module_0.Task(task_0, task_1, bool_0)
        var_3 = task_0.all_parents_static()
        task_3 = module_0.Task()
        var_4 = task_3.all_parents_static()
        var_5 = task_2.get_vars()
        var_6 = task_2.get_name()
        var_7 = task_3.get_include_params()
        var_8 = task_1.__repr__()
        var_9 = task_0.get_include_params()
        var_10 = task_2.get_first_parent_include()
        var_11 = task_0.get_name()
        var_12 = task_2.serialize()
    except BaseException:
        pass

def test_case_17():
    try:
        tuple_0 = None
        bool_0 = True
        dict_0 = {}
        task_0 = module_0.Task()
        list_0 = [task_0, tuple_0, bool_0, bool_0]
        task_1 = module_0.Task(list_0, list_0)
        var_0 = task_1.deserialize(dict_0)
        list_1 = [tuple_0, tuple_0, tuple_0]
        var_1 = task_0.get_include_params()
        task_2 = module_0.Task(list_1)
        str_0 = '$Fy>nX4ER'
        str_1 = '!;\x0csy'
        task_3 = module_0.Task(str_1, list_1)
        var_2 = task_3.copy(str_0)
        var_3 = task_1.serialize()
    except BaseException:
        pass