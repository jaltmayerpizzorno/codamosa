# Automatically generated by Pynguin.
import ansible.playbook.task as module_0
import ansible.playbook.block as module_1

def test_case_0():
    try:
        bool_0 = True
        bytes_0 = b'\xa4R\xb1;\x83z\x95C\x1b\xcb\x893\x84\xc1\x94W:N'
        dict_0 = {bytes_0: bytes_0}
        task_0 = module_0.Task(bytes_0, bool_0, dict_0)
        var_0 = task_0.get_first_parent_include()
    except BaseException:
        pass

def test_case_1():
    try:
        task_0 = module_0.Task()
        set_0 = {task_0, task_0, task_0}
        str_0 = 'Hp>pS2i(k'
        var_0 = task_0.load(set_0, task_0, str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        var_0 = {}
        task_0 = module_0.Task()
        var_1 = task_0.preprocess_data(var_0)
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
        bytes_0 = b''
        dict_0 = {bytes_0: bytes_0}
        bool_0 = False
        task_0 = module_0.Task()
        task_1 = module_0.Task(task_0, task_0)
        var_0 = task_1.get_name(bool_0)
        task_2 = module_0.Task(bytes_0)
        str_0 = ')KOru\x0b4N,j\tw3?\x0b?(5'
        var_1 = task_2.deserialize(dict_0)
        var_2 = task_2.serialize()
        dict_1 = {str_0: str_0, str_0: str_0, str_0: str_0}
        var_3 = task_1.preprocess_data(dict_1)
    except BaseException:
        pass

def test_case_5():
    try:
        task_0 = module_0.Task()
        float_0 = -785.591
        var_0 = task_0.post_validate(float_0)
    except BaseException:
        pass

def test_case_6():
    try:
        float_0 = 0.0
        dict_0 = {float_0: float_0}
        int_0 = -2362
        int_1 = -1700
        task_0 = module_0.Task(int_0, int_1)
        var_0 = task_0.post_validate(dict_0)
    except BaseException:
        pass

def test_case_7():
    try:
        bytes_0 = b'?\xd7\xce\xa8\x9b\x84\x16`Z\x83\xb4'
        task_0 = module_0.Task(bytes_0)
        var_0 = task_0.__repr__()
        var_1 = task_0.get_vars()
    except BaseException:
        pass

def test_case_8():
    try:
        tuple_0 = ()
        set_0 = {tuple_0, tuple_0, tuple_0}
        dict_0 = {tuple_0: tuple_0}
        task_0 = module_0.Task(set_0, dict_0)
        var_0 = task_0.get_include_params()
    except BaseException:
        pass

def test_case_9():
    try:
        float_0 = 1665.7
        str_0 = 'cEQmakyQ'
        task_0 = module_0.Task(float_0, str_0)
        var_0 = task_0.copy()
    except BaseException:
        pass

def test_case_10():
    try:
        task_0 = module_0.Task()
        var_0 = task_0.copy()
        tuple_0 = ()
        float_0 = 322.9
        dict_0 = {tuple_0: tuple_0, tuple_0: tuple_0, tuple_0: tuple_0, tuple_0: float_0}
        float_1 = -3039.39
        task_1 = module_0.Task(dict_0, float_1)
        var_1 = task_1.all_parents_static()
    except BaseException:
        pass

def test_case_11():
    try:
        task_0 = module_0.Task()
        int_0 = 3756
        var_0 = task_0.get_first_parent_include()
        var_1 = task_0.get_name()
        var_2 = task_0.set_loader(int_0)
        bool_0 = None
        dict_0 = {bool_0: var_2}
        var_3 = task_0.deserialize(dict_0)
        str_0 = 'parameters are mutually exclusive: %s'
        var_4 = task_0.set_loader(str_0)
        var_5 = task_0.__repr__()
        task_1 = module_0.Task(int_0)
        bytes_0 = b'\xd2'
        var_6 = task_1.set_loader(bytes_0)
    except BaseException:
        pass

def test_case_12():
    try:
        task_0 = module_0.Task()
        str_0 = 'J*\\nb7>({KADOb*_r'
        task_1 = module_0.Task(str_0)
        var_0 = task_0.all_parents_static()
        var_1 = task_1.serialize()
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = 'Jft;F/tTNY'
        int_0 = -1371
        list_0 = [int_0, int_0]
        str_1 = '0p'
        float_0 = -2172.700458
        float_1 = -2411.33
        task_0 = module_0.Task(float_1)
        var_0 = task_0.get_name(float_0)
        task_1 = module_0.Task(int_0, list_0, str_1)
        var_1 = task_1.copy(str_0)
    except BaseException:
        pass

def test_case_14():
    try:
        task_0 = module_0.Task()
        task_1 = module_0.Task(task_0, task_0)
        var_0 = task_0.preprocess_data(task_1)
    except BaseException:
        pass

def test_case_15():
    try:
        task_0 = module_0.Task()
        task_1 = module_0.Task(task_0)
        dict_0 = {task_0: task_0, task_0: task_1}
        bool_0 = False
        var_0 = task_0.load(dict_0, bool_0)
    except BaseException:
        pass

def test_case_16():
    try:
        float_0 = 2407.585701
        task_0 = module_0.Task(float_0)
        var_0 = task_0.serialize()
    except BaseException:
        pass

def test_case_17():
    try:
        bytes_0 = b''
        dict_0 = {bytes_0: bytes_0}
        task_0 = module_0.Task()
        task_1 = module_0.Task(task_0, task_0)
        var_0 = task_1.copy()
        var_1 = task_0.get_name()
        str_0 = ')KOru\x0b4N,j\tw3?\x0b?('
        str_1 = 'O<#9Q$X^)(4`PfPV'
        var_2 = task_1.deserialize(dict_0)
        var_3 = task_1.serialize()
        dict_1 = {str_0: str_1, str_1: str_0, str_0: str_1, str_1: str_0}
        task_2 = module_0.Task(dict_1)
        var_4 = task_1.preprocess_data(task_1)
    except BaseException:
        pass

def test_case_18():
    try:
        bytes_0 = b''
        dict_0 = {bytes_0: bytes_0}
        task_0 = module_0.Task(bytes_0)
        var_0 = task_0.copy()
        var_1 = task_0.get_name()
        str_0 = 'collections'
        var_2 = task_0.get_vars()
        str_1 = 'O<#9Q$X^)(4`PfPV'
        task_1 = module_0.Task()
        var_3 = task_0.get_include_params()
        var_4 = task_0.deserialize(dict_0)
        var_5 = task_0.serialize()
        var_6 = task_0.__repr__()
        var_7 = task_0.get_first_parent_include()
        dict_1 = {str_0: str_1, str_1: str_1, str_1: str_0, str_0: dict_0}
        task_2 = module_0.Task(dict_0)
        var_8 = task_2.preprocess_data(dict_1)
    except BaseException:
        pass

def test_case_19():
    try:
        task_0 = module_0.Task()
        str_0 = 'na%e'
        str_1 = 'action'
        var_0 = task_0.copy()
        var_1 = task_0.serialize()
        str_2 = {str_0: str_0, str_1: str_0}
        var_2 = task_0.serialize()
        var_3 = task_0.copy()
        var_4 = task_0.get_first_parent_include()
        var_5 = task_0.preprocess_data(str_2)
        var_6 = task_0.preprocess_data(task_0)
    except BaseException:
        pass

def test_case_20():
    try:
        str_0 = 'vars'
        str_1 = 'action'
        str_2 = 'ignore_errors'
        bool_0 = True
        str_3 = 'foo'
        str_4 = 'bar'
        str_5 = {str_3: str_4}
        str_6 = 'ping'
        var_0 = {str_0: bool_0, str_0: str_5, str_1: str_6, str_2: bool_0}
        task_0 = module_0.Task()
        var_1 = task_0.load_data(var_0)
        var_2 = task_0.post_validate(str_1)
    except BaseException:
        pass

def test_case_21():
    try:
        task_0 = module_0.Task()
        str_0 = 'action'
        str_1 = 'test'
        str_2 = {str_0: str_1}
        var_0 = task_0.deserialize(str_2)
        str_3 = 'args'
        str_4 = '{{test}}'
        str_5 = {str_0: str_1, str_3: str_4}
        var_1 = task_0.deserialize(str_5)
        str_6 = 'notify'
        str_7 = 'something'
        str_8 = {str_0: str_1, str_3: str_4, str_6: str_7}
        var_2 = task_0.deserialize(str_8)
        str_9 = 'role'
        str_10 = {str_0: str_1, str_9: str_1}
        var_3 = task_0.deserialize(str_10)
    except BaseException:
        pass

def test_case_22():
    try:
        str_0 = 'SGML'
        str_1 = 'action'
        str_2 = 'ignore_errors'
        bool_0 = True
        str_3 = 'foo'
        str_4 = 'bar'
        str_5 = {str_3: str_4}
        str_6 = 'ping'
        var_0 = {str_0: bool_0, str_0: str_5, str_1: str_6, str_2: bool_0}
        task_0 = module_0.Task()
        var_1 = task_0.load_data(var_0)
    except BaseException:
        pass

def test_case_23():
    try:
        task_0 = module_0.Task()
        str_0 = 'action'
        str_1 = 'name'
        str_2 = 'args'
        str_3 = 'tags'
        str_4 = 'when'
        str_5 = 'parent'
        str_6 = 'parent_type'
        str_7 = 'set_fact'
        str_8 = 'foo'
        str_9 = 'bar'
        str_10 = 'baz'
        str_11 = {str_9: str_10}
        str_12 = 'condition'
        str_13 = [str_12]
        str_14 = 'include_role'
        var_0 = {str_0: str_14, str_1: str_8, str_5: str_13, str_6: str_13}
        str_15 = 'role_path'
        var_1 = {str_0: str_7, str_1: str_8, str_2: str_11, str_3: str_5, str_4: str_13, str_5: var_0, str_6: str_15, str_5: str_1}
        var_2 = task_0.deserialize(var_1)
    except BaseException:
        pass

def test_case_24():
    try:
        task_0 = module_0.Task()
        var_0 = task_0.all_parents_static()
        task_1 = module_0.Task()
        var_1 = task_1.serialize()
        block_0 = module_1.Block()
        var_2 = task_1.get_include_params()
        var_3 = block_0.get_vars()
        task_2 = module_0.Task(block_0)
        var_4 = task_2.get_name()
        var_5 = task_2.get_name()
        var_6 = task_1.copy()
        float_0 = None
        task_3 = module_0.Task(float_0, task_2)
    except BaseException:
        pass