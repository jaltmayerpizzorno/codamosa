# Automatically generated by Pynguin.
import ansible.playbook.block as module_0
import ansible.playbook.base as module_1
import ansible.playbook.role as module_2

def test_case_0():
    try:
        float_0 = 2068.1225
        str_0 = ''
        list_0 = [str_0, str_0, str_0, float_0]
        block_0 = module_0.Block(float_0, str_0, list_0, float_0)
        var_0 = block_0.copy()
    except BaseException:
        pass

def test_case_1():
    try:
        set_0 = set()
        str_0 = "recursively merges dicts. not just simple a['key'] = b['key'], if\n    both a and b have a key whose value is a dict then dict_merge is called\n    on both values and the result stored in the returned dictionary."
        block_0 = module_0.Block(set_0, str_0)
        var_0 = block_0.get_dep_chain()
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '48\n#7UA.. R2b|it:'
        str_1 = "^hN^_38u'tOq\x0cn"
        dict_0 = {str_1: str_0, str_1: str_0, str_0: str_1}
        block_0 = module_0.Block()
        var_0 = block_0.__eq__(dict_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = ' '
        block_0 = module_0.Block()
        block_1 = module_0.Block(str_0, block_0)
        var_0 = block_1.all_parents_static()
        int_0 = -1912
        var_1 = block_1.__ne__(int_0)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = None
        block_0 = module_0.Block()
        list_0 = [block_0]
        bytes_0 = b'\xfbi\nR\xd7\x8b\xf9\xfd\xbb\xb5'
        var_0 = block_0.is_block(int_0)
        str_0 = 'i_ge}qOc+*B#?{=6-D9'
        tuple_0 = ()
        set_0 = set()
        block_1 = module_0.Block(tuple_0, set_0)
        var_1 = block_1.__ne__(block_0)
        dict_0 = {}
        var_2 = block_0.filter_tagged_tasks(dict_0)
        block_2 = module_0.Block(list_0, bytes_0, str_0)
        var_3 = block_2.filter_tagged_tasks(int_0)
        list_1 = [var_2, var_3]
        var_4 = block_2.preprocess_data(list_1)
        var_5 = block_2.get_vars()
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '6<h/AH>`l['
        tuple_0 = ()
        bool_0 = False
        block_0 = module_0.Block()
        var_0 = block_0.load(str_0, tuple_0, bool_0)
    except BaseException:
        pass

def test_case_6():
    try:
        block_0 = module_0.Block()
        str_0 = 'actions'
        var_0 = block_0.deserialize(str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        bytes_0 = b'\x8c\xc7\xdaAM\xa3\x9a\xbe\x1cU-'
        list_0 = [bytes_0]
        str_0 = 'Failed to install service. rc: %s, out: %s, err: %s'
        block_0 = module_0.Block(bytes_0, str_0)
        var_0 = block_0.set_loader(list_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = '~'
        list_0 = []
        int_0 = -1663
        block_0 = module_0.Block(str_0, list_0, int_0)
        var_0 = block_0.serialize()
    except BaseException:
        pass

def test_case_9():
    try:
        int_0 = 2472
        float_0 = 5931.9405
        tuple_0 = ()
        block_0 = module_0.Block(int_0, float_0, tuple_0)
        var_0 = block_0.serialize()
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = '?\x0csC5W9tw9mG7\n3>C50'
        float_0 = -2415.44094
        int_0 = -2473
        tuple_0 = (float_0, int_0)
        list_0 = [tuple_0]
        block_0 = module_0.Block(str_0, list_0)
        var_0 = block_0.get_include_params()
    except BaseException:
        pass

def test_case_11():
    try:
        list_0 = []
        bytes_0 = b's\x873n\xebp\xa2'
        block_0 = module_0.Block(list_0, bytes_0, list_0)
        var_0 = block_0.all_parents_static()
    except BaseException:
        pass

def test_case_12():
    try:
        bytes_0 = b'V\xe4\xc0\x15\x0c[\r\n<\x88'
        dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0}
        list_0 = [dict_0, bytes_0, bytes_0, dict_0]
        block_0 = module_0.Block(bytes_0, list_0)
        var_0 = block_0.get_first_parent_include()
    except BaseException:
        pass

def test_case_13():
    try:
        base_0 = module_1.Base()
        set_0 = {base_0}
        bool_0 = False
        list_0 = [set_0, bool_0, bool_0, set_0]
        role_0 = module_2.Role(bool_0, list_0)
        str_0 = ''
        block_0 = module_0.Block(set_0, role_0, str_0)
        var_0 = block_0.serialize()
    except BaseException:
        pass

def test_case_14():
    try:
        block_0 = module_0.Block()
        var_0 = block_0.get_vars()
        var_1 = block_0.serialize()
        var_2 = block_0.get_include_params()
        str_0 = '\rU\r<'
        dict_0 = {}
        block_1 = module_0.Block(dict_0, block_0)
        list_0 = [var_0, var_0, str_0]
        var_3 = block_1.is_block(list_0)
        var_4 = block_0.copy()
        float_0 = -1069.4243
        var_5 = block_0.filter_tagged_tasks(dict_0)
        float_1 = 1532.9154
        set_0 = {float_1}
        tuple_0 = (float_0, float_1)
        int_0 = -2749
        var_6 = block_1.load(list_0, set_0, tuple_0, int_0)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = 'block'
        str_1 = 'tasks'
        str_2 = {str_1: str_1}
        str_3 = [str_2]
        str_4 = {str_0: str_3}
        var_0 = None
        bool_0 = False
        block_0 = module_0.Block(var_0, var_0, var_0, var_0, bool_0)
        var_1 = block_0.load_data(str_4)
    except BaseException:
        pass

def test_case_16():
    try:
        int_0 = 1772
        set_0 = {int_0}
        tuple_0 = None
        float_0 = 1000.0
        bool_0 = False
        str_0 = 'G\x0c,ON;U(%@=Ye?'
        bool_1 = True
        block_0 = module_0.Block(str_0, bool_1)
        dict_0 = {tuple_0: set_0, float_0: str_0, tuple_0: set_0}
        block_1 = module_0.Block(block_0, tuple_0, dict_0)
        var_0 = block_1.set_loader(bool_0)
    except BaseException:
        pass

def test_case_17():
    try:
        tuple_0 = ()
        dict_0 = {tuple_0: tuple_0}
        int_0 = 13
        str_0 = 'X}T}UfXZ0mh&T]k'
        bytes_0 = b'\xdfA=g\x07v$\xe6K\xb24\xd8\x8f\xc9\xde5\xf8\x82'
        list_0 = None
        int_1 = 1459
        tuple_1 = (bytes_0, list_0, int_1)
        bool_0 = True
        block_0 = module_0.Block(tuple_1, bool_0)
        var_0 = block_0.load(dict_0, int_0, int_0, str_0)
    except BaseException:
        pass