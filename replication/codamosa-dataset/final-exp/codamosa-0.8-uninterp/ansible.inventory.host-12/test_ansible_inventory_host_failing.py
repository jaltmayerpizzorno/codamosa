# Automatically generated by Pynguin.
import ansible.inventory.host as module_0

def test_case_0():
    try:
        float_0 = -2460.17
        host_0 = module_0.Host()
        bool_0 = True
        tuple_0 = (bool_0,)
        host_1 = module_0.Host(tuple_0)
        dict_0 = {float_0: float_0}
        var_0 = host_1.__setstate__(dict_0)
        var_1 = host_1.deserialize(tuple_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b"\x84\xd0q\x8e\xec;}\x87\xe7\xa3`\x14'`\xec"
        str_0 = ")czwJ'+ L_z%/8hhR"
        host_0 = module_0.Host()
        var_0 = host_0.populate_ancestors(str_0)
        host_1 = module_0.Host(bytes_0)
        var_1 = host_1.__repr__()
        var_2 = host_1.get_name()
        var_3 = host_1.__str__()
        var_4 = host_1.__str__()
        var_5 = host_1.get_vars()
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'\xad\xc0b\xa1z\xb5\xech\\2&\x91'
        host_0 = module_0.Host(bytes_0)
        var_0 = host_0.populate_ancestors()
        var_1 = host_0.populate_ancestors()
        var_2 = host_0.get_name()
        tuple_0 = (host_0,)
        var_3 = host_0.__eq__(tuple_0)
        var_4 = host_0.__repr__()
        var_5 = host_0.get_magic_vars()
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = "nJK'ld0q(\tZB` ]F90Kr"
        host_0 = module_0.Host(str_0)
        var_0 = host_0.get_magic_vars()
        bool_0 = True
        list_0 = [bool_0, bool_0]
        host_1 = module_0.Host(bool_0, list_0)
    except BaseException:
        pass