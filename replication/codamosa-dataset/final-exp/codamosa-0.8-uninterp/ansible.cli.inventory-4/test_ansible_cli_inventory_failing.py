# Automatically generated by Pynguin.
import ansible.cli.inventory as module_0

def test_case_0():
    try:
        float_0 = 2854.476048
        inventory_c_l_i_0 = module_0.InventoryCLI(float_0)
        var_0 = inventory_c_l_i_0.run()
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'\xc7\x11\xc4\xe6\x86'
        tuple_0 = (bytes_0,)
        inventory_c_l_i_0 = module_0.InventoryCLI(tuple_0)
        var_0 = inventory_c_l_i_0.run()
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = None
        bytes_0 = b'\xa3\x8f-\x15\xde\x9b\xd9\x7f%'
        inventory_c_l_i_0 = module_0.InventoryCLI(bytes_0)
        var_0 = inventory_c_l_i_0.dump(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = b'\xc7\x8aM\xc4\xca\x9bF\xc7\xd4:\xfb"1U'
        inventory_c_l_i_0 = module_0.InventoryCLI(bytes_0)
        var_0 = inventory_c_l_i_0.inventory_graph()
    except BaseException:
        pass

def test_case_4():
    try:
        bool_0 = False
        int_0 = 2500
        inventory_c_l_i_0 = module_0.InventoryCLI(int_0)
        var_0 = inventory_c_l_i_0.json_inventory(bool_0)
    except BaseException:
        pass

def test_case_5():
    try:
        float_0 = -563.22
        bool_0 = True
        inventory_c_l_i_0 = module_0.InventoryCLI(bool_0)
        var_0 = inventory_c_l_i_0.yaml_inventory(float_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'Invalid regex type (%s)'
        float_0 = -1029.0
        tuple_0 = (str_0, float_0)
        list_0 = [tuple_0]
        bytes_0 = b'd{\xecrA\xf6Cs\x1d\x86\x9e[\x0f\x9dK\x16\x9e\x014\xad'
        inventory_c_l_i_0 = module_0.InventoryCLI(bytes_0)
        var_0 = inventory_c_l_i_0.toml_inventory(list_0)
    except BaseException:
        pass