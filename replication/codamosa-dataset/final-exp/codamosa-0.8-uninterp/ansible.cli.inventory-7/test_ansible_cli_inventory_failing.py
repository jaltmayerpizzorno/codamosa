# Automatically generated by Pynguin.
import ansible.cli.inventory as module_0

def test_case_0():
    try:
        bytes_0 = b'+\x9c;\x01c\x0c)'
        dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0}
        inventory_c_l_i_0 = module_0.InventoryCLI(dict_0)
        var_0 = inventory_c_l_i_0.init_parser()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'S'
        inventory_c_l_i_0 = module_0.InventoryCLI(str_0)
        var_0 = inventory_c_l_i_0.run()
    except BaseException:
        pass

def test_case_2():
    try:
        dict_0 = {}
        str_0 = ';((^c\x0bqo=MXFZ'
        inventory_c_l_i_0 = module_0.InventoryCLI(str_0)
        var_0 = inventory_c_l_i_0.post_process_args(dict_0)
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = -3003
        inventory_c_l_i_0 = module_0.InventoryCLI(int_0)
        bool_0 = True
        inventory_c_l_i_1 = module_0.InventoryCLI(bool_0)
        var_0 = inventory_c_l_i_1.dump(inventory_c_l_i_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bool_0 = True
        inventory_c_l_i_0 = module_0.InventoryCLI(bool_0)
        var_0 = inventory_c_l_i_0.inventory_graph()
    except BaseException:
        pass

def test_case_5():
    try:
        set_0 = set()
        float_0 = -798.9
        float_1 = None
        list_0 = [float_0, set_0, set_0]
        inventory_c_l_i_0 = module_0.InventoryCLI(list_0)
        var_0 = inventory_c_l_i_0.json_inventory(float_1)
    except BaseException:
        pass

def test_case_6():
    try:
        bool_0 = True
        float_0 = -4582.6
        inventory_c_l_i_0 = module_0.InventoryCLI(float_0)
        var_0 = inventory_c_l_i_0.yaml_inventory(bool_0)
    except BaseException:
        pass

def test_case_7():
    try:
        tuple_0 = ()
        str_0 = 'N43T'
        inventory_c_l_i_0 = module_0.InventoryCLI(str_0)
        var_0 = inventory_c_l_i_0.toml_inventory(tuple_0)
    except BaseException:
        pass