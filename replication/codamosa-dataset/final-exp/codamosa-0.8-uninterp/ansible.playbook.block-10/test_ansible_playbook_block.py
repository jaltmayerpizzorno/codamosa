# Automatically generated by Pynguin.
import ansible.playbook.block as module_0

def test_case_0():
    pass

def test_case_1():
    block_0 = module_0.Block()

def test_case_2():
    str_0 = 'YZ5bq/'
    int_0 = -21
    block_0 = module_0.Block(int_0)
    var_0 = block_0.set_loader(str_0)
    var_1 = block_0.__repr__()

def test_case_3():
    block_0 = module_0.Block()
    var_0 = block_0.get_vars()
    var_1 = block_0.has_tasks()

def test_case_4():
    bytes_0 = b'\xca\xdcX\xde\x11\xf3\x85\xe5'
    block_0 = module_0.Block()
    var_0 = block_0.is_block(bytes_0)

def test_case_5():
    block_0 = module_0.Block()
    bytes_0 = b'\xb4\x15\xd7L)Y\xacS\xbe\x17l'
    var_0 = block_0.preprocess_data(bytes_0)
    var_1 = block_0.get_dep_chain()

def test_case_6():
    block_0 = module_0.Block()
    var_0 = block_0.copy()

def test_case_7():
    tuple_0 = ()
    block_0 = module_0.Block()
    block_1 = module_0.Block(tuple_0, block_0)
    var_0 = block_1.serialize()

def test_case_8():
    block_0 = module_0.Block()
    var_0 = block_0.get_dep_chain()

def test_case_9():
    block_0 = module_0.Block()
    var_0 = block_0.serialize()

def test_case_10():
    block_0 = module_0.Block()
    dict_0 = {}
    var_0 = block_0.deserialize(dict_0)

def test_case_11():
    bytes_0 = b''
    block_0 = module_0.Block(bytes_0)
    var_0 = block_0.set_loader(block_0)

def test_case_12():
    bytes_0 = b'\t02\x13\x8c\xc5\xf9P\x0e\xd2\x1a\x1d\x89'
    block_0 = module_0.Block(bytes_0)
    var_0 = block_0.serialize()

def test_case_13():
    dict_0 = {}
    str_0 = "D|A'1n"
    block_0 = module_0.Block(dict_0, str_0)
    var_0 = block_0.filter_tagged_tasks(str_0)

def test_case_14():
    block_0 = module_0.Block()
    var_0 = block_0.has_tasks()

def test_case_15():
    block_0 = module_0.Block()
    var_0 = block_0.get_dep_chain()
    var_1 = block_0.get_include_params()
    var_2 = block_0.__repr__()

def test_case_16():
    block_0 = module_0.Block()
    var_0 = block_0.get_first_parent_include()

def test_case_17():
    str_0 = '}wt$b[o8'
    tuple_0 = ()
    block_0 = module_0.Block(str_0, tuple_0)
    str_1 = 'U;k'
    var_0 = block_0.set_loader(tuple_0)
    dict_0 = {str_1: str_1, str_1: str_1, str_1: str_1}
    bool_0 = True
    block_1 = module_0.Block(bool_0, block_0, dict_0)
    var_1 = block_1.all_parents_static()
    var_2 = block_1.copy()

def test_case_18():
    block_0 = module_0.Block()
    str_0 = 'P\tWn'
    block_1 = module_0.Block(block_0)
    var_0 = block_1.filter_tagged_tasks(str_0)
    var_1 = block_0.has_tasks()

def test_case_19():
    str_0 = 'foo'
    block_0 = module_0.Block()
    var_0 = block_0.serialize()
    var_1 = block_0.deserialize(var_0)

def test_case_20():
    block_0 = module_0.Block()
    var_0 = []
    var_1 = block_0.preprocess_data(var_0)
    var_2 = {}
    var_3 = block_0.preprocess_data(var_2)
    str_0 = 'block'
    str_1 = 'rescue'
    var_4 = []
    var_5 = []
    var_6 = {str_0: var_4, str_1: var_5}
    var_7 = block_0.preprocess_data(var_6)
    str_2 = 'ls'
    var_8 = block_0.preprocess_data(str_2)