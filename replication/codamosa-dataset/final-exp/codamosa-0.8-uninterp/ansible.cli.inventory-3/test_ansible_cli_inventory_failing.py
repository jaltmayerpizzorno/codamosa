# Automatically generated by Pynguin.
import ansible.cli.inventory as module_0

def test_case_0():
    try:
        str_0 = '@'
        inventory_c_l_i_0 = module_0.InventoryCLI(str_0)
        var_0 = inventory_c_l_i_0.run()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '_diff'
        str_1 = '!_[wfFwKn3'
        inventory_c_l_i_0 = module_0.InventoryCLI(str_1)
        var_0 = inventory_c_l_i_0.dump(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        float_0 = -2119.91
        inventory_c_l_i_0 = module_0.InventoryCLI(float_0)
        var_0 = inventory_c_l_i_0.inventory_graph()
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'ESTABLISH LOCAL CONNECTION FOR USER: {0}'
        str_1 = '[Ly\r"bE'
        float_0 = -1541.6
        dict_0 = {str_1: str_1, str_1: float_0, str_1: str_1, str_1: float_0}
        inventory_c_l_i_0 = module_0.InventoryCLI(dict_0)
        var_0 = inventory_c_l_i_0.json_inventory(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        dict_0 = None
        str_0 = '=%0[j<x1m_1>#d'
        set_0 = set()
        tuple_0 = (set_0,)
        list_0 = [str_0, str_0, tuple_0]
        inventory_c_l_i_0 = module_0.InventoryCLI(list_0)
        var_0 = inventory_c_l_i_0.yaml_inventory(dict_0)
    except BaseException:
        pass

def test_case_5():
    try:
        tuple_0 = ()
        bytes_0 = b'\xf2\xa6G\xc02e\xc8\xfds\x87\xb9\xa4\xa4\x08\xf3D7\x06mE'
        dict_0 = {bytes_0: tuple_0, bytes_0: bytes_0, tuple_0: bytes_0}
        tuple_1 = (bytes_0, dict_0)
        list_0 = [tuple_0, tuple_0, tuple_1, tuple_0]
        bytes_1 = b'\x88\t\x8fd\x0c7#I\x98a\x18o\x8d\xdf'
        inventory_c_l_i_0 = module_0.InventoryCLI(bytes_1)
        var_0 = inventory_c_l_i_0.toml_inventory(list_0)
    except BaseException:
        pass