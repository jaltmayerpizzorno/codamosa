# Automatically generated by Pynguin.
import ansible.inventory.host as module_0
import ansible.inventory.group as module_1

def test_case_0():
    pass

def test_case_1():
    host_0 = module_0.Host()
    var_0 = host_0.__getstate__()
    var_1 = host_0.__hash__()
    int_0 = 404
    var_2 = host_0.remove_group(int_0)
    var_3 = host_0.__hash__()
    host_1 = module_0.Host(host_0)
    var_4 = host_0.__ne__(host_1)

def test_case_2():
    host_0 = module_0.Host()
    var_0 = host_0.__hash__()
    int_0 = 404
    var_1 = host_0.remove_group(int_0)
    var_2 = host_0.__hash__()
    var_3 = host_0.__ne__(host_0)

def test_case_3():
    str_0 = 'l3Xi:Ee<IQ)4z'
    host_0 = module_0.Host(str_0)
    var_0 = host_0.get_vars()
    group_0 = module_1.Group()
    var_1 = host_0.__ne__(group_0)

def test_case_4():
    host_0 = module_0.Host()
    host_1 = module_0.Host(host_0)
    str_0 = '(`)!L\r?\x0c_0JP2\x0c/bE'
    str_1 = 'eKskXN!+2Q-$v0'
    host_2 = module_0.Host(str_1)
    var_0 = host_2.set_variable(host_1, str_0)

def test_case_5():
    bytes_0 = b'`\xdc\xe3Xb\x88?6\x19'
    dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0}
    host_0 = module_0.Host(dict_0)
    var_0 = host_0.serialize()

def test_case_6():
    host_0 = module_0.Host()

def test_case_7():
    float_0 = 1446.5518
    host_0 = module_0.Host()
    var_0 = host_0.__str__()
    bytes_0 = b'\x89\xca\x03;\x03"\x13u\x19:\xe1i\x9f\x19\xe8\xf14'
    var_1 = host_0.remove_group(bytes_0)
    host_1 = module_0.Host(float_0)
    var_2 = host_1.populate_ancestors()
    host_2 = module_0.Host(host_1)
    var_3 = host_2.__repr__()
    var_4 = host_2.__hash__()

def test_case_8():
    str_0 = 'gw9'
    host_0 = module_0.Host()
    var_0 = host_0.remove_group(str_0)

def test_case_9():
    bytes_0 = b'\x8f\xdfl\x9b(s\xae\xfd,\x19\xfc\xce5'
    host_0 = module_0.Host(bytes_0)
    var_0 = host_0.get_groups()

def test_case_10():
    str_0 = 'l3Xi:Ee<IQ)04Cz'
    host_0 = module_0.Host(str_0)
    var_0 = host_0.get_vars()

def test_case_11():
    str_0 = 'test'
    host_0 = module_0.Host(str_0)
    group_0 = module_1.Group(str_0)
    var_0 = host_0.add_group(group_0)
    var_1 = host_0.add_group(group_0)

def test_case_12():
    str_0 = 'a'
    group_0 = module_1.Group(str_0)
    host_0 = module_0.Host(str_0)
    group_1 = module_1.Group(str_0)
    var_0 = group_0.add_child_group(group_1)
    var_1 = host_0.add_group(group_1)
    var_2 = host_0.remove_group(group_1)

def test_case_13():
    host_0 = module_0.Host()
    str_0 = 'a'
    int_0 = 1
    var_0 = host_0.set_variable(str_0, int_0)
    str_1 = 'b'
    int_1 = 2
    var_1 = host_0.set_variable(str_1, int_1)
    str_2 = 'c'
    str_3 = 'd'
    int_2 = {str_3: int_0}
    var_2 = host_0.set_variable(str_2, int_2)
    int_3 = 3
    var_3 = host_0.set_variable(str_2, int_3)
    int_4 = {str_3: int_1}
    var_4 = host_0.set_variable(str_2, int_4)

def test_case_14():
    str_0 = 'localhost'
    host_0 = module_0.Host(str_0)
    str_1 = 'a'
    str_2 = 'c'
    str_3 = 'd'
    str_4 = {str_2: str_3}
    var_0 = host_0.set_variable(str_1, str_4)
    str_5 = 'e'
    str_6 = 'f'
    str_7 = {str_5: str_6}
    var_1 = host_0.set_variable(str_1, str_7)

def test_case_15():
    str_0 = 'testhost'
    host_0 = module_0.Host(str_0)
    str_1 = 'Q4bpCJMW<'
    str_2 = 'bar'
    var_0 = host_0.set_variable(str_1, str_2)
    str_3 = 'fo1'
    str_4 = 'foo2'
    str_5 = 'bar2'
    str_6 = {str_3: str_4, str_4: str_5}
    var_1 = host_0.set_variable(str_1, str_6)

def test_case_16():
    str_0 = 'a'
    group_0 = module_1.Group(str_0)
    host_0 = module_0.Host(str_0)
    group_1 = module_1.Group(str_0)
    var_0 = host_0.__hash__()
    var_1 = group_0.get_hosts()
    var_2 = group_0.add_child_group(group_1)
    var_3 = host_0.get_magic_vars()
    var_4 = host_0.add_group(group_0)
    var_5 = host_0.add_group(group_1)
    var_6 = host_0.remove_group(group_1)

def test_case_17():
    str_0 = 'a'
    group_0 = module_1.Group(str_0)
    str_1 = 'b'
    group_1 = module_1.Group(str_1)
    group_2 = module_1.Group(str_1)
    var_0 = group_2.add_child_group(group_1)
    var_1 = group_2.add_child_group(group_0)
    str_2 = 'h1'
    host_0 = module_0.Host(str_2)
    var_2 = host_0.add_group(group_0)
    var_3 = host_0.add_group(group_2)
    var_4 = host_0.get_magic_vars()
    var_5 = host_0.remove_group(group_0)

def test_case_18():
    bool_0 = False
    host_0 = module_0.Host(bool_0)
    str_0 = 'localhost'
    str_1 = 'bar'
    str_2 = '127.0.0.1'
    str_3 = 'my_uuid'
    str_4 = 'all'
    var_0 = dict(foo=str_1)
    str_5 = 'all_uuid'
    var_1 = {}
    var_2 = dict(name=str_4, vars=var_0, uuid=str_5, implicit=bool_0, children=var_1)
    var_3 = [var_2]
    var_4 = dict(name=str_0, vars=var_0, address=str_2, uuid=str_3, groups=var_3, implicit=bool_0)
    var_5 = host_0.deserialize(var_4)

def test_case_19():
    str_0 = 'a'
    group_0 = module_1.Group(str_0)
    host_0 = module_0.Host(str_0)
    var_0 = host_0.get_groups()
    group_1 = module_1.Group(str_0)
    group_2 = module_1.Group(str_0)
    var_1 = host_0.__getstate__()
    var_2 = host_0.__hash__()
    var_3 = group_0.get_hosts()
    var_4 = group_0.add_child_group(group_1)
    var_5 = group_0.add_child_group(group_2)
    var_6 = host_0.add_group(group_2)
    var_7 = group_0.__repr__()
    var_8 = host_0.get_magic_vars()
    var_9 = host_0.add_group(group_0)
    var_10 = host_0.add_group(group_1)
    var_11 = host_0.__hash__()
    var_12 = host_0.remove_group(group_1)