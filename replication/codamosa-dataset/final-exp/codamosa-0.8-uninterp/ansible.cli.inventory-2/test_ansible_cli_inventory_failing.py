# Automatically generated by Pynguin.
import ansible.cli.inventory as module_0

def test_case_0():
    try:
        bytes_0 = b'[\xd9%M\x15)'
        inventory_c_l_i_0 = module_0.InventoryCLI(bytes_0)
        var_0 = inventory_c_l_i_0.run()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'l'
        inventory_c_l_i_0 = module_0.InventoryCLI(str_0)
        var_0 = inventory_c_l_i_0.run()
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'get_connections'
        int_0 = -2420
        inventory_c_l_i_0 = module_0.InventoryCLI(int_0)
        var_0 = inventory_c_l_i_0.dump(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bool_0 = False
        bytes_0 = b'\xafuq\xc2\xa1.G7(\xdf\x8e\xf9\xf2{\x8aF\xa3\xa0\xed'
        tuple_0 = (bool_0, bytes_0)
        inventory_c_l_i_0 = module_0.InventoryCLI(tuple_0)
        var_0 = inventory_c_l_i_0.inventory_graph()
    except BaseException:
        pass

def test_case_4():
    try:
        float_0 = 241.676
        inventory_c_l_i_0 = module_0.InventoryCLI(float_0)
        dict_0 = {inventory_c_l_i_0: inventory_c_l_i_0, inventory_c_l_i_0: float_0, float_0: inventory_c_l_i_0}
        str_0 = 'a1@Z#k8eoE]Ez:-z$'
        inventory_c_l_i_1 = module_0.InventoryCLI(str_0)
        var_0 = inventory_c_l_i_1.json_inventory(dict_0)
    except BaseException:
        pass

def test_case_5():
    try:
        int_0 = -1388
        bool_0 = False
        float_0 = None
        tuple_0 = (int_0, bool_0, float_0)
        str_0 = 'g$lnZ}Xq5^Fsfo,EDQ\t'
        inventory_c_l_i_0 = module_0.InventoryCLI(str_0)
        var_0 = inventory_c_l_i_0.yaml_inventory(tuple_0)
    except BaseException:
        pass

def test_case_6():
    try:
        int_0 = None
        int_1 = 6510
        str_0 = '.tar.gz'
        dict_0 = {int_0: int_0, int_1: int_0}
        inventory_c_l_i_0 = module_0.InventoryCLI(dict_0)
        var_0 = inventory_c_l_i_0.toml_inventory(str_0)
    except BaseException:
        pass