# Automatically generated by Pynguin.
import ansible.inventory.data as module_0

def test_case_0():
    pass

def test_case_1():
    inventory_data_0 = module_0.InventoryData()

def test_case_2():
    inventory_data_0 = module_0.InventoryData()
    var_0 = inventory_data_0.serialize()

def test_case_3():
    inventory_data_0 = module_0.InventoryData()
    var_0 = inventory_data_0.reconcile_inventory()

def test_case_4():
    bool_0 = False
    inventory_data_0 = module_0.InventoryData()
    var_0 = inventory_data_0.get_host(bool_0)

def test_case_5():
    inventory_data_0 = module_0.InventoryData()
    var_0 = inventory_data_0.remove_group(inventory_data_0)
    str_0 = '127.0.0.1'
    var_1 = inventory_data_0.reconcile_inventory()
    var_2 = inventory_data_0.get_host(str_0)

def test_case_6():
    inventory_data_0 = module_0.InventoryData()
    str_0 = '&#yL`9ov@-\rbS'
    var_0 = inventory_data_0.add_host(str_0)

def test_case_7():
    inventory_data_0 = module_0.InventoryData()
    var_0 = inventory_data_0.get_groups_dict()
    inventory_data_1 = module_0.InventoryData()
    var_1 = inventory_data_1.reconcile_inventory()

def test_case_8():
    inventory_data_0 = module_0.InventoryData()
    var_0 = inventory_data_0.get_groups_dict()
    var_1 = inventory_data_0.get_groups_dict()
    inventory_data_1 = module_0.InventoryData()
    var_2 = inventory_data_1.get_groups_dict()

def test_case_9():
    inventory_data_0 = module_0.InventoryData()
    var_0 = inventory_data_0.get_groups_dict()
    inventory_data_1 = module_0.InventoryData()
    str_0 = 'all'
    var_1 = inventory_data_1.add_group(str_0)
    inventory_data_2 = module_0.InventoryData()

def test_case_10():
    inventory_data_0 = module_0.InventoryData()
    str_0 = 'UM'
    var_0 = inventory_data_0.add_group(str_0)
    str_1 = '#I'
    var_1 = inventory_data_0.add_host(str_1, str_0)
    var_2 = inventory_data_0.add_host(str_1, str_0)
    var_3 = inventory_data_0.reconcile_inventory()
    var_4 = inventory_data_0.get_host(str_0)

def test_case_11():
    inventory_data_0 = module_0.InventoryData()
    var_0 = inventory_data_0.reconcile_inventory()
    str_0 = 'all'
    var_1 = inventory_data_0.groups[str_0]
    var_2 = inventory_data_0.groups[str_0]
    str_1 = 'test_host'
    var_3 = inventory_data_0.add_host(str_1)
    var_4 = inventory_data_0.reconcile_inventory()

def test_case_12():
    inventory_data_0 = module_0.InventoryData()
    str_0 = 'baz'
    var_0 = inventory_data_0.add_group(str_0)
    var_1 = inventory_data_0.add_host(str_0, str_0)
    str_1 = 'bar'
    var_2 = inventory_data_0.add_host(str_1, str_0)
    str_2 = '127.0.0.1'
    var_3 = inventory_data_0.add_host(str_2)
    var_4 = inventory_data_0.reconcile_inventory()
    var_5 = inventory_data_0.get_host(str_2)

def test_case_13():
    inventory_data_0 = module_0.InventoryData()
    str_0 = 'baz'
    var_0 = inventory_data_0.add_group(str_0)
    str_1 = 'fZo'
    var_1 = inventory_data_0.add_host(str_1, str_0)
    var_2 = inventory_data_0.add_host(str_0, var_0)
    str_2 = '127.0.0.1'
    var_3 = inventory_data_0.get_host(str_2)

def test_case_14():
    inventory_data_0 = module_0.InventoryData()
    str_0 = 'baz'
    var_0 = inventory_data_0.add_group(str_0)
    str_1 = 'bar'
    var_1 = inventory_data_0.add_host(str_1, str_0)
    str_2 = '127.0.0.1'
    var_2 = inventory_data_0.add_host(str_2)
    var_3 = inventory_data_0.reconcile_inventory()
    var_4 = inventory_data_0.reconcile_inventory()
    var_5 = inventory_data_0.get_host(str_2)

def test_case_15():
    inventory_data_0 = module_0.InventoryData()
    str_0 = 'baz'
    var_0 = inventory_data_0.add_group(str_0)
    str_1 = 'foo'
    var_1 = inventory_data_0.add_host(str_1, str_0)
    var_2 = inventory_data_0.get_groups_dict()
    var_3 = inventory_data_0.reconcile_inventory()

def test_case_16():
    inventory_data_0 = module_0.InventoryData()
    str_0 = 'test_host'
    var_0 = inventory_data_0.add_host(str_0)
    str_1 = 'all'
    var_1 = inventory_data_0.groups[str_1]
    str_2 = 'ungrouped'
    var_2 = inventory_data_0.groups[str_2]
    var_3 = inventory_data_0.hosts[str_0]
    var_4 = inventory_data_0.remove_host(var_3)
    var_5 = inventory_data_0.groups[str_1]
    var_6 = inventory_data_0.groups[str_2]

def test_case_17():
    inventory_data_0 = module_0.InventoryData()
    str_0 = '127.0.0.1'
    var_0 = inventory_data_0.get_host(str_0)

def test_case_18():
    inventory_data_0 = module_0.InventoryData()
    str_0 = 'localhost'
    var_0 = inventory_data_0.add_host(str_0)
    var_1 = print(str_0)
    str_1 = 'test fail'
    var_2 = print(str_1)

def test_case_19():
    inventory_data_0 = module_0.InventoryData()
    var_0 = inventory_data_0.get_groups_dict()
    str_0 = '\r'
    var_1 = inventory_data_0.add_group(str_0)
    str_1 = 'o=wo'
    var_2 = inventory_data_0.add_group(str_1)
    var_3 = inventory_data_0.add_host(str_1, str_0)
    str_2 = '127.0.0.1'
    var_4 = inventory_data_0.get_groups_dict()
    var_5 = inventory_data_0.reconcile_inventory()
    var_6 = inventory_data_0.get_host(str_2)
    inventory_data_1 = module_0.InventoryData()
    inventory_data_2 = module_0.InventoryData()
    var_7 = inventory_data_0.add_host(str_2)