# Automatically generated by Pynguin.
import ansible.plugins.inventory.constructed as module_0

def test_case_0():
    try:
        bytes_0 = b'o\xb5\xcb\xb7|O\xe0\xc4\x0b\x8b_6\x87L'
        list_0 = [bytes_0, bytes_0, bytes_0]
        tuple_0 = ()
        dict_0 = {bytes_0: list_0, bytes_0: tuple_0}
        bytes_1 = b'\x01\x99\xab\x11\x8b\xbb\xd8\x1a\xc6\x12\x1d>\x8a\xba\xeaw\xcb'
        inventory_module_0 = module_0.InventoryModule()
        var_0 = inventory_module_0.get_all_host_vars(list_0, dict_0, bytes_1)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = None
        int_0 = -1477
        bool_0 = True
        inventory_module_0 = module_0.InventoryModule()
        var_0 = inventory_module_0.host_groupvars(str_0, int_0, bool_0)
    except BaseException:
        pass

def test_case_2():
    try:
        inventory_module_0 = module_0.InventoryModule()
        bytes_0 = b'\xa8x\x9b\x87\xc2\x85\xf3o;\x06\xb5\xd4'
        str_0 = '=\x0b B5@Z-q&a8*Tz7V'
        set_0 = {str_0}
        var_0 = inventory_module_0.host_vars(bytes_0, str_0, set_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = "}92=o'yo"
        float_0 = -1074.6
        inventory_module_0 = module_0.InventoryModule()
        inventory_module_1 = module_0.InventoryModule()
        var_0 = inventory_module_1.parse(str_0, float_0, inventory_module_0)
    except BaseException:
        pass

def test_case_4():
    try:
        float_0 = 0.5
        tuple_0 = None
        str_0 = 'H5ZsI[8/!T.x'
        inventory_module_0 = module_0.InventoryModule()
        var_0 = inventory_module_0.parse(float_0, tuple_0, str_0)
    except BaseException:
        pass