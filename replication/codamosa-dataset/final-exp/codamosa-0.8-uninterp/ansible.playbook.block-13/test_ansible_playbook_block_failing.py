# Automatically generated by Pynguin.
import ansible.playbook.block as module_0
import ansible.playbook.role as module_1

def test_case_0():
    try:
        set_0 = set()
        str_0 = '7c]0lM7&~yHiK6NO0'
        block_0 = module_0.Block(set_0, str_0)
        var_0 = block_0.get_first_parent_include()
    except BaseException:
        pass

def test_case_1():
    try:
        block_0 = module_0.Block()
        str_0 = '60Z'
        var_0 = block_0.__eq__(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        list_0 = []
        block_0 = module_0.Block(list_0)
        float_0 = 1242.8729
        block_1 = module_0.Block(float_0, block_0, block_0)
        str_0 = 'M|S!t\niW6}'
        var_0 = block_1.filter_tagged_tasks(str_0)
        var_1 = block_0.get_vars()
        bytes_0 = b'h\xc7\x19\xc1\xa3'
        var_2 = block_1.deserialize(bytes_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = b'\xce]k\xb1\x13'
        dict_0 = None
        str_0 = "seq\r*38'ftUR2|1~?"
        block_0 = module_0.Block(str_0)
        var_0 = block_0.load(bytes_0, dict_0, bytes_0)
    except BaseException:
        pass

def test_case_4():
    try:
        float_0 = -74.631252
        str_0 = 'running TaskExecutor() for %s/%s'
        block_0 = module_0.Block(float_0, str_0)
        var_0 = block_0.serialize()
    except BaseException:
        pass

def test_case_5():
    try:
        bool_0 = True
        role_0 = module_1.Role()
        list_0 = [role_0]
        block_0 = module_0.Block(bool_0, role_0, list_0)
        var_0 = block_0.serialize()
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'failed'
        bytes_0 = b'\xefT\t\xecG\x9at\x05GNDm\x17'
        block_0 = module_0.Block(str_0, bytes_0)
        var_0 = block_0.all_parents_static()
    except BaseException:
        pass

def test_case_7():
    try:
        set_0 = set()
        bytes_0 = b'\xac\xd4\x11/\xc28u\xb44\t'
        block_0 = module_0.Block(set_0, bytes_0)
        var_0 = block_0.get_include_params()
    except BaseException:
        pass

def test_case_8():
    try:
        bool_0 = True
        set_0 = None
        tuple_0 = ()
        int_0 = 2607
        block_0 = module_0.Block(tuple_0, int_0)
        list_0 = [bool_0, bool_0, bool_0]
        block_1 = module_0.Block(list_0)
        str_0 = '])hgu`n|%1U}$#|g?'
        block_2 = module_0.Block(str_0)
        var_0 = block_2.filter_tagged_tasks(set_0)
        bytes_0 = b'\xdb\xc8\x05\xe0'
        var_1 = block_2.preprocess_data(bytes_0)
        var_2 = block_2.get_include_params()
        var_3 = block_2.preprocess_data(var_1)
        block_3 = module_0.Block()
        var_4 = block_0.serialize()
    except BaseException:
        pass

def test_case_9():
    try:
        dict_0 = {}
        str_0 = 'S@uhwx2^k\x0cR?,'
        block_0 = module_0.Block(dict_0, dict_0, str_0)
        var_0 = block_0.get_dep_chain()
        var_1 = block_0.set_loader(dict_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = '~cr'
        block_0 = module_0.Block()
        bool_0 = False
        float_0 = 3087.7877
        var_0 = block_0.filter_tagged_tasks(float_0)
        set_0 = {str_0, bool_0}
        var_1 = block_0.get_vars()
        int_0 = None
        var_2 = block_0.get_vars()
        var_3 = block_0.set_loader(float_0)
        tuple_0 = (bool_0, set_0, bool_0, int_0)
        var_4 = block_0.is_block(tuple_0)
        var_5 = block_0.set_loader(str_0)
        block_1 = module_0.Block()
        var_6 = block_1.serialize()
        bytes_0 = b'.\xb0\xdc\xa9\x06\xa9\xc85"\xe9\xc0\x9ek\x11w\xa2\x11\xe7 '
        var_7 = block_1.is_block(bytes_0)
        list_0 = [var_6, var_7]
        var_8 = block_0.get_first_parent_include()
        bool_1 = True
        var_9 = block_1.filter_tagged_tasks(bool_1)
        var_10 = block_1.has_tasks()
        block_2 = module_0.Block(set_0)
        float_1 = None
        var_11 = block_1.copy(float_1)
        float_2 = 1152.0
        str_1 = '5\t@,1/K\x0cw^GN'
        var_12 = block_1.all_parents_static()
        str_2 = 'QhcW?IT|RE.8{:W4\t{\x0c'
        tuple_1 = (str_1, str_2)
        var_13 = block_1.load(list_0, float_2, block_2, tuple_1)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = 'shell'
        str_1 = 'ls'
        var_0 = dict(module=str_0, args=str_1)
        str_2 = 'always'
        list_0 = [str_2, str_0]
        bytes_0 = b"\xbeD\xe8\x1a[\xf2(\xf2;E\xeaG\xba.W\x11]f'\x05"
        int_0 = -2237
        block_0 = module_0.Block(bytes_0, int_0)
        var_1 = block_0.deserialize(list_0)
    except BaseException:
        pass