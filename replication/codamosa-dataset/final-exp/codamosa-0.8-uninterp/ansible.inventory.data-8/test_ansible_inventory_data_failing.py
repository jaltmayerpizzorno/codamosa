# Automatically generated by Pynguin.
import ansible.inventory.data as module_0

def test_case_0():
    try:
        inventory_data_0 = module_0.InventoryData()
        inventory_data_1 = module_0.InventoryData()
        var_0 = inventory_data_1.deserialize(inventory_data_0)
    except BaseException:
        pass

def test_case_1():
    try:
        inventory_data_0 = module_0.InventoryData()
        var_0 = inventory_data_0.get_groups_dict()
        list_0 = [inventory_data_0, inventory_data_0]
        var_1 = inventory_data_0.add_group(list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        inventory_data_0 = module_0.InventoryData()
        var_0 = inventory_data_0.get_groups_dict()
        inventory_data_1 = module_0.InventoryData()
        dict_0 = None
        inventory_data_2 = module_0.InventoryData()
        var_1 = inventory_data_2.add_group(dict_0)
    except BaseException:
        pass

def test_case_3():
    try:
        inventory_data_0 = module_0.InventoryData()
        str_0 = 'localhost'
        str_1 = 'allL'
        var_0 = inventory_data_0.get_host(str_0)
        var_1 = inventory_data_0.add_host(str_0, str_1)
    except BaseException:
        pass

def test_case_4():
    try:
        inventory_data_0 = module_0.InventoryData()
        int_0 = -39
        var_0 = inventory_data_0.add_host(inventory_data_0, int_0)
    except BaseException:
        pass

def test_case_5():
    try:
        inventory_data_0 = module_0.InventoryData()
        str_0 = 'all'
        var_0 = inventory_data_0.add_host(str_0, str_0)
        var_1 = inventory_data_0.reconcile_inventory()
    except BaseException:
        pass

def test_case_6():
    try:
        float_0 = None
        inventory_data_0 = module_0.InventoryData()
        var_0 = inventory_data_0.remove_host(float_0)
    except BaseException:
        pass

def test_case_7():
    try:
        int_0 = -579
        dict_0 = {int_0: int_0, int_0: int_0}
        list_0 = [dict_0]
        inventory_data_0 = module_0.InventoryData()
        var_0 = inventory_data_0.set_variable(int_0, int_0, list_0)
    except BaseException:
        pass

def test_case_8():
    try:
        inventory_data_0 = module_0.InventoryData()
        str_0 = 'a'
        var_0 = inventory_data_0.add_group(str_0)
        bytes_0 = b'\x7f\xfc\x0f\xf5\xddW\xe71\x97<.\xa7'
        var_1 = inventory_data_0.add_child(bytes_0, bytes_0)
    except BaseException:
        pass

def test_case_9():
    try:
        inventory_data_0 = module_0.InventoryData()
        str_0 = 'a'
        var_0 = inventory_data_0.add_host(str_0)
        str_1 = 'b'
        var_1 = inventory_data_0.add_group(str_1)
        str_2 = 'Um:'
        var_2 = inventory_data_0.add_host(str_2)
        list_0 = []
        var_3 = inventory_data_0.add_host(list_0)
    except BaseException:
        pass

def test_case_10():
    try:
        float_0 = 0.001
        tuple_0 = (float_0,)
        dict_0 = {tuple_0: tuple_0}
        inventory_data_0 = module_0.InventoryData()
        var_0 = inventory_data_0.deserialize(dict_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = 'all'
        str_1 = 'F'
        inventory_data_0 = module_0.InventoryData()
        var_0 = inventory_data_0.add_child(str_0, str_1)
    except BaseException:
        pass

def test_case_12():
    try:
        inventory_data_0 = module_0.InventoryData()
        str_0 = 'localhost'
        str_1 = 'all'
        var_0 = inventory_data_0.add_host(str_0, str_1)
        var_1 = inventory_data_0.get_host(str_0)
        var_2 = inventory_data_0.get_groups_dict()
        var_3 = inventory_data_0.reconcile_inventory()
        var_4 = inventory_data_0.reconcile_inventory()
        list_0 = [var_0, str_1]
        tuple_0 = (list_0,)
        var_5 = inventory_data_0.get_host(tuple_0)
    except BaseException:
        pass

def test_case_13():
    try:
        inventory_data_0 = module_0.InventoryData()
        str_0 = 'localhost'
        str_1 = 'all'
        var_0 = inventory_data_0.get_host(str_0)
        var_1 = inventory_data_0.get_host(str_0)
        var_2 = inventory_data_0.add_host(str_1, str_1)
        var_3 = inventory_data_0.remove_group(inventory_data_0)
        str_2 = 'localhost2'
        var_4 = inventory_data_0.add_host(str_2, str_1)
        str_3 = 'localhost4'
        var_5 = inventory_data_0.add_host(str_3, str_1)
        var_6 = inventory_data_0.reconcile_inventory()
    except BaseException:
        pass