# Automatically generated by Pynguin.
import ansible.playbook.block as module_0
import ansible.playbook.role as module_1

def test_case_0():
    pass

def test_case_1():
    int_0 = None
    block_0 = module_0.Block(int_0)

def test_case_2():
    bytes_0 = b'\xa7\x95\x9a\xfc'
    float_0 = 562.503551
    block_0 = module_0.Block(bytes_0, float_0)
    var_0 = block_0.__repr__()
    tuple_0 = ()
    list_0 = [tuple_0, tuple_0]
    block_1 = module_0.Block(tuple_0, list_0)
    var_1 = block_1.has_tasks()

def test_case_3():
    set_0 = None
    tuple_0 = ()
    float_0 = 5328.03575
    block_0 = module_0.Block(tuple_0, float_0, set_0)
    float_1 = 3099.76
    block_1 = module_0.Block(float_1)
    var_0 = block_1.set_loader(set_0)
    var_1 = block_1.get_vars()

def test_case_4():
    str_0 = '^^;wzV'
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    bytes_0 = b'\xa8\x88k\x08\xa0\xe1\xa9\xee\xd3\x07oK'
    bool_0 = False
    block_0 = module_0.Block(bytes_0, bool_0)
    var_0 = block_0.preprocess_data(dict_0)

def test_case_5():
    role_0 = None
    block_0 = module_0.Block()
    var_0 = block_0.preprocess_data(role_0)

def test_case_6():
    block_0 = module_0.Block()
    var_0 = block_0.copy()

def test_case_7():
    block_0 = module_0.Block()
    var_0 = block_0.serialize()

def test_case_8():
    float_0 = None
    set_0 = {float_0, float_0, float_0, float_0}
    str_0 = 'E# 1P6%'
    block_0 = module_0.Block(float_0, set_0, str_0)
    var_0 = block_0.filter_tagged_tasks(float_0)

def test_case_9():
    block_0 = module_0.Block()
    var_0 = dict()
    var_1 = block_0.deserialize(var_0)

def test_case_10():
    str_0 = '\t4'
    block_0 = module_0.Block()
    var_0 = block_0.set_loader(str_0)

def test_case_11():
    str_0 = '$[h\r\tV/~q"40}h'
    block_0 = module_0.Block(str_0)
    var_0 = block_0.serialize()

def test_case_12():
    block_0 = module_0.Block()
    var_0 = block_0.has_tasks()

def test_case_13():
    float_0 = 3614.295
    set_0 = {float_0, float_0, float_0, float_0}
    block_0 = module_0.Block(set_0)
    var_0 = block_0.get_include_params()
    var_1 = block_0.preprocess_data(float_0)
    var_2 = block_0.is_block(block_0)

def test_case_14():
    block_0 = module_0.Block()
    var_0 = block_0.all_parents_static()
    var_1 = block_0.serialize()
    var_2 = block_0.all_parents_static()

def test_case_15():
    block_0 = module_0.Block()
    var_0 = block_0.get_dep_chain()
    block_1 = module_0.Block()
    str_0 = '5$Pb\tK3S$]}F^'
    var_1 = block_0.copy()
    var_2 = block_1.set_loader(str_0)
    var_3 = block_1.has_tasks()
    var_4 = block_1.get_first_parent_include()

def test_case_16():
    bool_0 = True
    block_0 = module_0.Block()
    var_0 = block_0.copy(bool_0, bool_0)

def test_case_17():
    list_0 = []
    int_0 = 1797
    tuple_0 = ()
    bytes_0 = b'fR'
    block_0 = module_0.Block(tuple_0, bytes_0)
    bytes_1 = b'\x19\x18\x9e\xd2\x8b\xb1p\xa2'
    float_0 = -1945.302179
    role_0 = module_1.Role(bytes_1, float_0)
    bool_0 = False
    block_1 = module_0.Block(bool_0)
    var_0 = block_0.load(list_0, int_0, block_0, role_0)
    float_1 = 790.3
    str_0 = 'dc\x0bC'
    block_2 = module_0.Block(str_0)
    str_1 = '0242ac11-0005-78e8-56ac-000000002521'
    tuple_1 = (float_1, block_2, str_1, str_0)
    block_3 = module_0.Block()
    var_1 = block_3.set_loader(tuple_1)
    block_4 = module_0.Block(float_1)

def test_case_18():
    bool_0 = False
    int_0 = -2607
    block_0 = module_0.Block(int_0)
    block_1 = module_0.Block(bool_0, block_0, int_0)
    var_0 = block_1.copy()
    block_2 = module_0.Block(bool_0)
    var_1 = block_1.all_parents_static()
    block_3 = module_0.Block()
    var_2 = block_3.get_first_parent_include()

def test_case_19():
    str_0 = 'role_name'
    str_1 = 'role_path'
    str_2 = 'test'
    str_3 = '/foo/bar/baz'
    str_4 = {str_0: str_2, str_1: str_3}
    role_0 = module_1.Role()
    var_0 = role_0.deserialize(str_4)
    str_5 = 'role'
    str_6 = 'use_handlers'
    str_7 = 'vars'
    str_8 = 'always'
    bool_0 = False
    var_1 = {}
    var_2 = []
    var_3 = {str_5: str_4, str_6: bool_0, str_7: var_1, str_8: var_2}
    block_0 = module_0.Block()
    var_4 = block_0.deserialize(var_3)
    block_1 = module_0.Block()