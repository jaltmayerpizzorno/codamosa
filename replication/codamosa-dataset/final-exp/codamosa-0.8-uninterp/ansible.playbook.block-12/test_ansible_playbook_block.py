# Automatically generated by Pynguin.
import ansible.playbook.block as module_0
import ansible.playbook.role as module_1

def test_case_0():
    pass

def test_case_1():
    block_0 = module_0.Block()
    var_0 = block_0.get_dep_chain()

def test_case_2():
    bool_0 = True
    int_0 = -1046
    block_0 = module_0.Block(bool_0, bool_0, bool_0, int_0)
    var_0 = block_0.filter_tagged_tasks(bool_0)

def test_case_3():
    dict_0 = None
    set_0 = set()
    block_0 = module_0.Block(dict_0, set_0)
    dict_1 = {}
    var_0 = block_0.is_block(dict_1)
    var_1 = block_0.copy()
    tuple_0 = ()
    str_0 = 'D8(='
    var_2 = block_0.has_tasks()
    tuple_1 = (tuple_0, str_0, set_0, set_0)
    block_1 = module_0.Block(tuple_1)
    block_2 = module_0.Block(block_1)
    var_3 = block_2.__ne__(block_1)
    var_4 = block_1.get_vars()
    var_5 = block_2.serialize()

def test_case_4():
    str_0 = '>MAtt[rc"<Kw\x0c=Z\n'
    block_0 = module_0.Block(str_0)
    var_0 = block_0.preprocess_data(str_0)

def test_case_5():
    bytes_0 = b'\xb1\xb4\x02\x10$0)\x9aF\xde\x08\xb6\xe5\x85\xdd'
    str_0 = '9MMXv\n=^nGcWu7$\x0b'
    block_0 = module_0.Block(str_0)
    var_0 = block_0.filter_tagged_tasks(bytes_0)
    list_0 = []
    block_1 = module_0.Block()
    var_1 = block_0.all_parents_static()
    var_2 = block_0.get_dep_chain()
    var_3 = block_1.preprocess_data(list_0)
    int_0 = 0
    var_4 = block_1.filter_tagged_tasks(int_0)

def test_case_6():
    block_0 = module_0.Block()
    var_0 = block_0.copy()

def test_case_7():
    block_0 = module_0.Block()
    var_0 = block_0.serialize()

def test_case_8():
    var_0 = dict()
    block_0 = module_0.Block()
    var_1 = block_0.deserialize(var_0)

def test_case_9():
    bytes_0 = b'\x04\x95\x8e\x07\x17|\xa4k\xb0'
    str_0 = '6d3be'
    block_0 = module_0.Block(str_0)
    var_0 = block_0.set_loader(bytes_0)

def test_case_10():
    str_0 = 'g*(|5'
    block_0 = module_0.Block(str_0)
    var_0 = block_0.serialize()

def test_case_11():
    role_0 = module_1.Role()
    block_0 = module_0.Block(role_0)
    var_0 = block_0.serialize()

def test_case_12():
    block_0 = module_0.Block()
    float_0 = 1000.0
    var_0 = block_0.filter_tagged_tasks(float_0)

def test_case_13():
    block_0 = module_0.Block()
    var_0 = block_0.has_tasks()

def test_case_14():
    float_0 = -386.063173
    bool_0 = True
    dict_0 = {bool_0: bool_0}
    list_0 = [dict_0, bool_0]
    str_0 = '0242ac11-000f-9401-5ab7-00000000006c'
    block_0 = module_0.Block(list_0, str_0)
    block_1 = module_0.Block(bool_0, dict_0, block_0)
    var_0 = block_1.filter_tagged_tasks(float_0)
    str_1 = ',lM+Rwhq+\r[cQ"!}6'
    str_2 = '}PA#]v  %kH3KhTZ:'
    block_2 = module_0.Block(str_2)
    var_1 = block_2.all_parents_static()
    var_2 = block_2.filter_tagged_tasks(str_1)

def test_case_15():
    block_0 = module_0.Block()
    var_0 = block_0.get_first_parent_include()

def test_case_16():
    str_0 = 'block'
    str_1 = 'action'
    str_2 = '/bin/echo'
    str_3 = {str_1: str_2, str_1: str_2}
    str_4 = [str_3]
    str_5 = {str_0: str_4}
    block_0 = module_0.Block()
    var_0 = block_0.preprocess_data(str_5)