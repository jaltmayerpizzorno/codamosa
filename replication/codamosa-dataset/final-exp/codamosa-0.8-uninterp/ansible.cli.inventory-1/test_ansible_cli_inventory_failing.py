# Automatically generated by Pynguin.
import ansible.cli.inventory as module_0

def test_case_0():
    try:
        str_0 = '-_'
        inventory_c_l_i_0 = module_0.InventoryCLI(str_0)
        var_0 = inventory_c_l_i_0.run()
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = 8192
        inventory_c_l_i_0 = module_0.InventoryCLI(int_0)
        var_0 = inventory_c_l_i_0.dump(int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = -1374
        dict_0 = {int_0: int_0, int_0: int_0, int_0: int_0}
        bytes_0 = b'\x92'
        tuple_0 = (dict_0, bytes_0)
        list_0 = [tuple_0, bytes_0]
        tuple_1 = (list_0,)
        inventory_c_l_i_0 = module_0.InventoryCLI(tuple_1)
        inventory_c_l_i_1 = module_0.InventoryCLI(inventory_c_l_i_0)
        var_0 = inventory_c_l_i_1.inventory_graph()
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = b''
        int_0 = 5986
        inventory_c_l_i_0 = module_0.InventoryCLI(int_0)
        var_0 = inventory_c_l_i_0.json_inventory(bytes_0)
    except BaseException:
        pass

def test_case_4():
    try:
        float_0 = -1891.14
        float_1 = -522.0
        float_2 = 321.155
        set_0 = {float_2, float_1, float_0, float_2}
        list_0 = [float_0, float_0, float_1, set_0]
        str_0 = ';\x0b}z^^TP\tRL+yu>e'
        inventory_c_l_i_0 = module_0.InventoryCLI(str_0)
        var_0 = inventory_c_l_i_0.yaml_inventory(list_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bytes_0 = b'\xe3t\x81$g\x0f\xff'
        int_0 = 2351
        dict_0 = {int_0: int_0, int_0: int_0}
        inventory_c_l_i_0 = module_0.InventoryCLI(dict_0)
        var_0 = inventory_c_l_i_0.toml_inventory(bytes_0)
    except BaseException:
        pass