# Automatically generated by Pynguin.
import ansible.playbook.block as module_0
import ansible.playbook.role as module_1

def test_case_0():
    pass

def test_case_1():
    block_0 = module_0.Block()

def test_case_2():
    float_0 = -74.631252
    bytes_0 = b'm\xb4\x90$\xb0\xa4\xda\xf2\xbb\x0f\x07\xe9x\xb0\x8eY\x0c\xd7\x8c'
    set_0 = {float_0}
    block_0 = module_0.Block(float_0, bytes_0, bytes_0, set_0)
    var_0 = block_0.copy(float_0)

def test_case_3():
    block_0 = module_0.Block()
    var_0 = block_0.__repr__()

def test_case_4():
    int_0 = 2536
    block_0 = module_0.Block(int_0)
    bool_0 = False
    block_1 = module_0.Block(block_0, bool_0)
    var_0 = block_0.__ne__(block_0)
    var_1 = block_1.serialize()
    var_2 = block_1.get_include_params()
    var_3 = block_0.all_parents_static()

def test_case_5():
    float_0 = 1242.8729
    block_0 = module_0.Block()
    block_1 = module_0.Block(float_0, block_0, block_0)
    var_0 = block_1.get_vars()
    str_0 = 'M|S!t\niW6}'
    var_1 = block_1.filter_tagged_tasks(str_0)
    dict_0 = {float_0: float_0, float_0: float_0, float_0: float_0}
    var_2 = block_1.__repr__()
    var_3 = block_1.has_tasks()
    var_4 = block_0.serialize()
    var_5 = block_0.get_first_parent_include()
    var_6 = block_0.filter_tagged_tasks(dict_0)
    var_7 = block_1.serialize()

def test_case_6():
    block_0 = module_0.Block()
    var_0 = block_0.copy()

def test_case_7():
    block_0 = module_0.Block()
    var_0 = block_0.serialize()

def test_case_8():
    float_0 = 1242.8729
    block_0 = module_0.Block()
    block_1 = module_0.Block(float_0, block_0, block_0)
    list_0 = None
    var_0 = block_1.copy(list_0, float_0)

def test_case_9():
    block_0 = module_0.Block()
    var_0 = {}
    var_1 = block_0.deserialize(var_0)

def test_case_10():
    block_0 = module_0.Block()
    int_0 = 10
    var_0 = block_0.set_loader(int_0)

def test_case_11():
    float_0 = 1242.8729
    block_0 = module_0.Block()
    block_1 = module_0.Block(float_0, block_0, block_0)
    str_0 = "mA|VK'(y^"
    var_0 = block_1.filter_tagged_tasks(str_0)
    var_1 = block_1.all_parents_static()
    var_2 = block_1.get_first_parent_include()
    var_3 = block_1.__repr__()
    var_4 = block_1.has_tasks()
    bool_0 = False
    var_5 = block_1.is_block(bool_0)
    var_6 = block_1.serialize()
    bytes_0 = b'h\xc7\x19;\xa3'
    dict_0 = {bytes_0: var_0, float_0: block_0}
    var_7 = block_0.set_loader(dict_0)
    role_0 = module_1.Role()
    block_2 = module_0.Block(role_0)
    var_8 = block_2.copy()
    var_9 = block_1.set_loader(block_2)

def test_case_12():
    bytes_0 = b'\x92S\xa8\x99\xc5\x83B\xdb\x07\xd9'
    block_0 = module_0.Block(bytes_0)
    var_0 = block_0.serialize()

def test_case_13():
    block_0 = module_0.Block()
    float_0 = None
    var_0 = block_0.filter_tagged_tasks(float_0)

def test_case_14():
    block_0 = module_0.Block()
    var_0 = block_0.has_tasks()

def test_case_15():
    int_0 = 2536
    block_0 = module_0.Block(int_0)
    bool_0 = False
    block_1 = module_0.Block(block_0, bool_0)
    var_0 = block_1.get_include_params()

def test_case_16():
    str_0 = ''
    block_0 = module_0.Block(str_0)
    var_0 = block_0.all_parents_static()
    var_1 = block_0.has_tasks()

def test_case_17():
    float_0 = -452.497
    tuple_0 = (float_0,)
    int_0 = 480
    block_0 = module_0.Block(tuple_0, int_0)
    block_1 = module_0.Block(block_0)
    var_0 = block_1.get_first_parent_include()

def test_case_18():
    float_0 = 1242.8729
    block_0 = module_0.Block()
    var_0 = block_0.get_dep_chain()
    var_1 = block_0.all_parents_static()
    block_1 = module_0.Block(float_0, block_0, block_0)
    dict_0 = {}
    var_2 = block_0.preprocess_data(dict_0)
    set_0 = {float_0}
    var_3 = block_1.set_loader(set_0)
    str_0 = 'M|S!t\niW6}'
    var_4 = block_1.filter_tagged_tasks(str_0)
    var_5 = block_1.all_parents_static()
    dict_1 = {float_0: float_0, float_0: float_0, float_0: float_0}
    var_6 = block_1.has_tasks()
    var_7 = block_0.serialize()
    var_8 = block_0.get_first_parent_include()
    var_9 = block_0.filter_tagged_tasks(dict_1)
    int_0 = -1803
    str_1 = 'n)'
    block_2 = module_0.Block(float_0, str_1)
    list_0 = []
    var_10 = block_1.copy()
    str_2 = "SmNE`\x0bmX{'`+/vL~>"
    block_3 = module_0.Block(int_0, list_0, str_2, float_0)
    var_11 = block_3.deserialize(dict_1)

def test_case_19():
    float_0 = 1242.8729
    block_0 = module_0.Block()
    block_1 = module_0.Block(float_0, block_0, block_0)
    str_0 = "mA|VK'(y^"
    var_0 = block_1.filter_tagged_tasks(str_0)
    var_1 = block_1.all_parents_static()
    var_2 = block_1.get_first_parent_include()
    var_3 = block_1.__repr__()
    var_4 = block_1.has_tasks()
    bool_0 = False
    var_5 = block_1.is_block(bool_0)
    list_0 = [bool_0, bool_0, var_0, var_3]
    var_6 = block_1.preprocess_data(list_0)
    var_7 = block_1.serialize()
    bytes_0 = b'\xaf\xcfo7\x844I\xa0'
    dict_0 = {bytes_0: var_0, float_0: block_0}
    var_8 = block_0.set_loader(dict_0)
    role_0 = module_1.Role()
    block_2 = module_0.Block(role_0)
    var_9 = block_2.copy()

def test_case_20():
    block_0 = module_0.Block()
    block_1 = module_0.Block(block_0)
    var_0 = block_1.serialize()

def test_case_21():
    str_0 = 'name'
    str_1 = 'metadata'
    str_2 = 'test_block'
    var_0 = {}
    var_1 = {str_0: str_2, str_1: var_0}
    block_0 = module_0.Block()
    var_2 = block_0.deserialize(var_1)
    str_3 = 'tasks'
    var_3 = {}
    str_4 = {str_0: str_1}
    str_5 = 'task2'
    str_6 = {str_0: str_5}
    str_7 = [str_4, str_6]
    var_4 = {str_0: str_2, str_1: var_3, str_3: str_7}
    block_1 = module_0.Block()
    var_5 = block_1.deserialize(var_4)

def test_case_22():
    float_0 = 1242.8729
    block_0 = module_0.Block()
    block_1 = module_0.Block(float_0, block_0, block_0)
    str_0 = 'M|S!t\niW6}'
    var_0 = block_1.filter_tagged_tasks(str_0)
    dict_0 = {float_0: float_0, float_0: float_0, float_0: float_0}
    var_1 = block_1.has_tasks()
    var_2 = block_0.serialize()
    var_3 = block_0.get_first_parent_include()
    var_4 = block_0.filter_tagged_tasks(dict_0)
    var_5 = block_1.serialize()