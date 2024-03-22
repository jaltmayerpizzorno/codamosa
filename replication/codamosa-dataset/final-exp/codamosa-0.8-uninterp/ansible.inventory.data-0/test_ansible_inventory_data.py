# Automatically generated by Pynguin.
import ansible.inventory.data as module_0
import ansible.inventory.host as module_1

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
    inventory_data_0 = module_0.InventoryData()
    str_0 = '127.0.0.1'
    var_0 = inventory_data_0.get_host(str_0)

def test_case_5():
    inventory_data_0 = module_0.InventoryData()
    inventory_data_1 = module_0.InventoryData()
    var_0 = inventory_data_1.remove_group(inventory_data_0)

def test_case_6():
    inventory_data_0 = module_0.InventoryData()
    str_0 = 'all'
    var_0 = inventory_data_0.add_host(str_0, str_0)

def test_case_7():
    inventory_data_0 = module_0.InventoryData()
    str_0 = 'test_host'
    host_0 = module_1.Host(str_0)
    var_0 = inventory_data_0.remove_host(host_0)

def test_case_8():
    inventory_data_0 = module_0.InventoryData()
    str_0 = 'localhost'
    str_1 = 'all'
    var_0 = inventory_data_0.add_host(str_0, str_1)

def test_case_9():
    inventory_data_0 = module_0.InventoryData()
    var_0 = inventory_data_0.get_groups_dict()

def test_case_10():
    int_0 = 1146
    int_1 = 1453
    inventory_data_0 = module_0.InventoryData()
    var_0 = inventory_data_0.get_host(int_1)
    inventory_data_1 = module_0.InventoryData()
    inventory_data_2 = module_0.InventoryData()
    var_1 = inventory_data_2.remove_group(int_0)

def test_case_11():
    inventory_data_0 = module_0.InventoryData()
    str_0 = 'localhost'
    var_0 = inventory_data_0.add_host(str_0)
    var_1 = inventory_data_0.add_host(str_0)

def test_case_12():
    inventory_data_0 = module_0.InventoryData()
    str_0 = 'localhost'
    var_0 = inventory_data_0.serialize()
    str_1 = 'A'
    var_1 = inventory_data_0.add_host(str_1)
    var_2 = inventory_data_0.reconcile_inventory()
    var_3 = inventory_data_0.get_host(str_0)
    var_4 = inventory_data_0.get_groups_dict()
    inventory_data_1 = module_0.InventoryData()
    inventory_data_2 = module_0.InventoryData()
    var_5 = inventory_data_0.get_groups_dict()

def test_case_13():
    inventory_data_0 = module_0.InventoryData()
    str_0 = 'test_group'
    var_0 = inventory_data_0.add_host(str_0)
    var_1 = inventory_data_0.reconcile_inventory()
    inventory_data_1 = module_0.InventoryData()
    var_2 = inventory_data_0.get_groups_dict()

def test_case_14():
    inventory_data_0 = module_0.InventoryData()
    var_0 = inventory_data_0.serialize()
    str_0 = 'A'
    var_1 = inventory_data_0.add_host(str_0)
    var_2 = inventory_data_0.reconcile_inventory()
    var_3 = inventory_data_0.reconcile_inventory()
    inventory_data_1 = module_0.InventoryData()
    var_4 = inventory_data_0.get_groups_dict()

def test_case_15():
    inventory_data_0 = module_0.InventoryData()
    str_0 = 'host1'
    var_0 = inventory_data_0.add_host(str_0)
    str_1 = 'host2'
    var_1 = inventory_data_0.add_host(str_1)
    var_2 = inventory_data_0.hosts[str_1]
    var_3 = inventory_data_0.remove_host(var_2)
    str_2 = 'group1'
    var_4 = inventory_data_0.add_group(str_2)
    var_5 = inventory_data_0.add_child(str_2, str_0)
    var_6 = inventory_data_0.reconcile_inventory()
    var_7 = inventory_data_0.hosts[str_0]

def test_case_16():
    inventory_data_0 = module_0.InventoryData()
    str_0 = 'localhost'
    var_0 = inventory_data_0.reconcile_inventory()
    var_1 = inventory_data_0.add_host(str_0)
    var_2 = inventory_data_0.get_host(str_0)
    var_3 = inventory_data_0.get_groups_dict()
    var_4 = inventory_data_0.get_host(str_0)

def test_case_17():
    inventory_data_0 = module_0.InventoryData()
    str_0 = 'localhost'
    var_0 = inventory_data_0.add_host(str_0)
    str_1 = '127.0.0.1'
    var_1 = inventory_data_0.get_host(str_1)

def test_case_18():
    inventory_data_0 = module_0.InventoryData()
    str_0 = 'host1'
    var_0 = inventory_data_0.add_host(str_0)
    str_1 = 'host2'
    var_1 = inventory_data_0.add_host(str_1)
    var_2 = inventory_data_0.hosts[str_1]
    str_2 = 'group1'
    var_3 = inventory_data_0.add_group(str_2)
    var_4 = inventory_data_0.add_child(str_2, str_0)
    var_5 = inventory_data_0.reconcile_inventory()