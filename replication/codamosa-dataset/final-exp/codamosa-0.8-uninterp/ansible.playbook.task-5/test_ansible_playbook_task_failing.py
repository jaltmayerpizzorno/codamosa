# Automatically generated by Pynguin.
import ansible.playbook.task as module_0
import ansible.playbook.block as module_1

def test_case_0():
    try:
        str_0 = 'x'
        task_0 = module_0.Task(str_0)
        var_0 = task_0.__repr__()
        list_0 = [task_0, task_0, str_0]
        set_0 = None
        bytes_0 = b'\x8c\xc8\xc1W\x94\xd1\xc1\xac\xe8\x88\xb6\xa9\xa6\x97\xf8\x87\x90\xf2'
        var_1 = task_0.load(list_0, list_0, set_0, bytes_0)
    except BaseException:
        pass

def test_case_1():
    try:
        tuple_0 = ()
        float_0 = -810.0
        task_0 = module_0.Task(tuple_0, float_0)
        var_0 = task_0.__repr__()
    except BaseException:
        pass

def test_case_2():
    try:
        task_0 = module_0.Task()
        bytes_0 = b'+\xca\xb0BD?fbQ\xcc\x1a\x1d\xfc\xe4G\xea\xa4'
        var_0 = task_0.load(task_0, bytes_0)
    except BaseException:
        pass

def test_case_3():
    try:
        task_0 = module_0.Task()
        var_0 = task_0.preprocess_data(task_0)
    except BaseException:
        pass

def test_case_4():
    try:
        task_0 = module_0.Task()
        set_0 = {task_0, task_0, task_0, task_0}
        var_0 = task_0.post_validate(set_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '%;]Fe7<B,"$7uw N_9'
        task_0 = module_0.Task(str_0)
        var_0 = task_0.get_include_params()
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'SXyJFy4L{1O'
        task_0 = module_0.Task(str_0)
        var_0 = task_0.serialize()
    except BaseException:
        pass

def test_case_7():
    try:
        bytes_0 = b's\x0b\xc4e\x90\xf4\x02B'
        str_0 = 'timed out waiting for %s: %s'
        tuple_0 = (bytes_0, str_0)
        str_1 = '6$a~vkYT+};Y=s3/*4'
        task_0 = module_0.Task(str_1)
        var_0 = task_0.deserialize(tuple_0)
    except BaseException:
        pass

def test_case_8():
    try:
        float_0 = -1561.0
        task_0 = module_0.Task()
        set_0 = {float_0}
        task_1 = module_0.Task(set_0)
        var_0 = task_1.set_loader(task_0)
    except BaseException:
        pass

def test_case_9():
    try:
        tuple_0 = None
        str_0 = 'Current:'
        task_0 = module_0.Task(tuple_0, str_0)
        var_0 = task_0.all_parents_static()
        set_0 = {task_0, task_0}
        var_1 = task_0.get_vars()
        task_1 = module_0.Task()
        var_2 = task_1.deserialize(set_0)
    except BaseException:
        pass

def test_case_10():
    try:
        bool_0 = True
        float_0 = None
        dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_0}
        task_0 = module_0.Task()
        var_0 = task_0.all_parents_static()
        task_1 = module_0.Task(dict_0)
        var_1 = task_1.get_name(float_0)
        task_2 = module_0.Task()
        var_2 = task_2.__repr__()
        task_3 = module_0.Task(bool_0)
        var_3 = task_2.get_name()
        var_4 = task_3.all_parents_static()
    except BaseException:
        pass

def test_case_11():
    try:
        task_0 = module_0.Task()
        set_0 = {task_0, task_0, task_0, task_0}
        var_0 = task_0.get_first_parent_include()
        var_1 = task_0.post_validate(set_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = 'm*L'
        task_0 = module_0.Task(str_0)
        var_0 = task_0.get_first_parent_include()
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = 'x'
        float_0 = 0.0
        tuple_0 = ()
        list_0 = [str_0, str_0, tuple_0]
        task_0 = module_0.Task(tuple_0, list_0)
        var_0 = task_0.set_loader(float_0)
        task_1 = module_0.Task(str_0)
        var_1 = task_1.__repr__()
        list_1 = [task_1, task_1, str_0]
        set_0 = None
        bytes_0 = b'\x8c\xc8\xc1W\x94\xd1\xc1\xac\xe8\x88\xb6\xa9\xa6\x97\xf8\x87\x90\xf2'
        var_2 = task_1.load(list_1, list_1, set_0, bytes_0)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = '{d`e'
        bool_0 = False
        block_0 = module_1.Block(str_0, bool_0)
        task_0 = module_0.Task(block_0)
        var_0 = task_0.serialize()
        str_1 = 'oX'
        var_1 = dict(action=str_1)
        var_2 = task_0.preprocess_data(var_1)
        var_3 = dict(nope=var_1)
        var_4 = task_0.all_parents_static()
        var_5 = task_0.get_first_parent_include()
        var_6 = dict(action=var_3)
        var_7 = task_0.serialize()
        complex_0 = None
        set_0 = {str_1, task_0}
        block_1 = module_1.Block(complex_0, set_0)
        var_8 = task_0.__repr__()
        dict_0 = None
        var_9 = task_0.post_validate(dict_0)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = 'x'
        task_0 = module_0.Task(str_0)
        var_0 = task_0.copy()
    except BaseException:
        pass

def test_case_16():
    try:
        var_0 = {}
        task_0 = module_0.Task()
        var_1 = task_0.preprocess_data(var_0)
    except BaseException:
        pass

def test_case_17():
    try:
        task_0 = module_0.Task()
        task_1 = module_0.Task(task_0)
        str_0 = 'no_log'
        var_0 = task_1.get_name(str_0)
        bytes_0 = b'\xf7\xcc^p\xa6E\xa8'
        var_1 = task_1.load(task_0, bytes_0)
    except BaseException:
        pass

def test_case_18():
    try:
        int_0 = 1278
        dict_0 = {int_0: int_0, int_0: int_0, int_0: int_0}
        int_1 = -1496
        int_2 = -1333
        set_0 = {int_1, int_2, int_2}
        str_0 = 'Kk=ys\r_y N#|'
        task_0 = module_0.Task(set_0, str_0)
        var_0 = task_0.preprocess_data(dict_0)
    except BaseException:
        pass

def test_case_19():
    try:
        list_0 = []
        str_0 = 'Gy[MEaue6|lb\t\x0cU1C'
        task_0 = module_0.Task(list_0, str_0)
        var_0 = task_0.serialize()
    except BaseException:
        pass

def test_case_20():
    try:
        int_0 = None
        bool_0 = True
        bytes_0 = b'F\xb0\t\xdb\x02\x805\xac\xa5\xccm'
        task_0 = module_0.Task()
        var_0 = task_0.get_include_params()
        dict_0 = {int_0: int_0, int_0: bool_0, bool_0: int_0, bytes_0: int_0}
        task_1 = module_0.Task(dict_0)
        task_2 = module_0.Task(bool_0)
        var_1 = task_2.deserialize(dict_0)
        var_2 = task_1.__repr__()
        var_3 = task_2.__repr__()
        var_4 = task_0.get_vars()
        var_5 = task_2.serialize()
    except BaseException:
        pass

def test_case_21():
    try:
        str_0 = 'nope'
        var_0 = dict(nope=str_0)
        var_1 = dict(action=str_0)
        task_0 = module_0.Task()
        var_2 = task_0.preprocess_data(var_1)
        var_3 = dict(nope=str_0)
        var_4 = dict(action=var_2)
        task_1 = module_0.Task()
        var_5 = task_1.preprocess_data(var_4)
    except BaseException:
        pass

def test_case_22():
    try:
        str_0 = '{]$e'
        bool_0 = False
        block_0 = module_1.Block(str_0, bool_0)
        var_0 = dict(action=str_0)
        task_0 = module_0.Task()
        var_1 = dict(nope=var_0)
        var_2 = task_0.all_parents_static()
        var_3 = task_0.get_first_parent_include()
        var_4 = task_0.get_vars()
        var_5 = dict(action=var_1)
        var_6 = task_0.serialize()
        var_7 = task_0.preprocess_data(var_6)
    except BaseException:
        pass