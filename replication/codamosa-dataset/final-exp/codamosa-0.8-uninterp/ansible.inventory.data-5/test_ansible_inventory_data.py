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
    inventory_data_1 = module_0.InventoryData()
    var_1 = inventory_data_1.get_groups_dict()

def test_case_3():
    inventory_data_0 = module_0.InventoryData()
    var_0 = inventory_data_0.reconcile_inventory()

def test_case_4():
    tuple_0 = None
    inventory_data_0 = module_0.InventoryData()
    var_0 = inventory_data_0.get_host(tuple_0)

def test_case_5():
    bool_0 = None
    inventory_data_0 = module_0.InventoryData()
    var_0 = inventory_data_0.remove_group(bool_0)

def test_case_6():
    inventory_data_0 = module_0.InventoryData()
    str_0 = 'localhost1'
    var_0 = inventory_data_0.add_host(str_0)

def test_case_7():
    inventory_data_0 = module_0.InventoryData()
    str_0 = 'host1'
    host_0 = module_1.Host(str_0)
    var_0 = inventory_data_0.remove_host(host_0)
    str_1 = 'ungrouped'
    var_1 = inventory_data_0.groups[str_1]

def test_case_8():
    str_0 = 'Unit test for method reconcile_inventory of class InventoryData'
    inventory_data_0 = module_0.InventoryData()
    str_1 = 'all'
    var_0 = inventory_data_0.add_group(str_0)
    str_2 = 'group1'
    var_1 = inventory_data_0.add_group(str_2)
    str_3 = 'group%level_var'
    var_2 = inventory_data_0.set_variable(str_2, str_3, str_0)
    var_3 = inventory_data_0.add_host(str_3, str_1)
    var_4 = inventory_data_0.reconcile_inventory()

def test_case_9():
    inventory_data_0 = module_0.InventoryData()
    str_0 = 'localhost'
    var_0 = inventory_data_0.reconcile_inventory()
    var_1 = inventory_data_0.add_host(str_0)
    var_2 = inventory_data_0.reconcile_inventory()
    var_3 = inventory_data_0.reconcile_inventory()
    var_4 = inventory_data_0.reconcile_inventory()
    var_5 = inventory_data_0.reconcile_inventory()

def test_case_10():
    inventory_data_0 = module_0.InventoryData()
    str_0 = 'localhost'
    var_0 = inventory_data_0.reconcile_inventory()
    var_1 = inventory_data_0.add_host(str_0)
    var_2 = inventory_data_0.reconcile_inventory()
    var_3 = inventory_data_0.reconcile_inventory()
    var_4 = inventory_data_0.reconcile_inventory()
    var_5 = inventory_data_0.get_groups_dict()

def test_case_11():
    inventory_data_0 = module_0.InventoryData()
    str_0 = 'a'
    var_0 = inventory_data_0.add_host(str_0)
    str_1 = 'b'
    var_1 = inventory_data_0.add_host(str_1)
    str_2 = 'c'
    var_2 = inventory_data_0.add_host(str_2)
    str_3 = 'group1'
    var_3 = inventory_data_0.add_group(str_3)
    var_4 = inventory_data_0.add_child(str_3, str_0)
    var_5 = inventory_data_0.add_child(str_3, str_1)
    var_6 = inventory_data_0.add_child(str_3, str_2)
    var_7 = inventory_data_0.remove_group(str_3)
    var_8 = len(str_0)
    int_0 = 0
    var_9 = var_8 == int_0
    var_10 = len(var_2)
    int_1 = 2
    var_11 = var_10 == int_1
    var_12 = str_2 and var_11

def test_case_12():
    inventory_data_0 = module_0.InventoryData()
    str_0 = 'all'
    var_0 = inventory_data_0.add_group(str_0)
    var_1 = inventory_data_0.add_group(str_0)
    str_1 = 'test'
    var_2 = inventory_data_0.add_group(str_1)
    var_3 = inventory_data_0.add_group(str_1)

def test_case_13():
    inventory_data_0 = module_0.InventoryData()
    str_0 = 'localhost1'
    var_0 = inventory_data_0.add_host(str_0)
    var_1 = inventory_data_0.add_host(str_0)

def test_case_14():
    inventory_data_0 = module_0.InventoryData()
    str_0 = 'localhost'
    var_0 = inventory_data_0.add_host(str_0)
    var_1 = inventory_data_0.get_groups_dict()

def test_case_15():
    inventory_data_0 = module_0.InventoryData()
    str_0 = 'test_host'
    var_0 = inventory_data_0.add_host(str_0)
    str_1 = 'ungrouped'
    var_1 = inventory_data_0.groups[str_1]
    var_2 = inventory_data_0.hosts[str_0]
    var_3 = inventory_data_0.remove_host(var_2)
    str_2 = 'jgqveeL2C<Q0@'
    var_4 = inventory_data_0.add_host(str_2)

def test_case_16():
    inventory_data_0 = module_0.InventoryData()
    str_0 = 'localhost'
    var_0 = inventory_data_0.add_host(str_0)
    var_1 = inventory_data_0.get_host(str_0)
    var_2 = inventory_data_0.get_groups_dict()

def test_case_17():
    inventory_data_0 = module_0.InventoryData()
    str_0 = '127.0.0.1'
    var_0 = inventory_data_0.get_host(str_0)

def test_case_18():
    str_0 = 'Unit test for method reconcile_inventory of class InventoryData'
    inventory_data_0 = module_0.InventoryData()
    var_0 = inventory_data_0.add_group(str_0)
    str_1 = 'ungrouped'
    var_1 = inventory_data_0.add_group(str_1)
    str_2 = 'group1'
    var_2 = inventory_data_0.add_group(str_2)
    str_3 = 'group_level_var'
    str_4 = 'group1_val'
    var_3 = inventory_data_0.set_variable(str_2, str_3, str_4)
    var_4 = inventory_data_0.add_host(str_0, str_0)
    var_5 = inventory_data_0.reconcile_inventory()
    var_6 = inventory_data_0.reconcile_inventory()

def test_case_19():
    inventory_data_0 = module_0.InventoryData()
    str_0 = 'localhost'
    var_0 = inventory_data_0.add_host(str_0)
    str_1 = '127.0.0.1'
    var_1 = inventory_data_0.add_host(str_1)
    str_2 = 'node1.example.com'
    var_2 = inventory_data_0.add_host(str_2)
    str_3 = 'node2.example.com'
    var_3 = inventory_data_0.add_host(str_3)
    str_4 = 'group1'
    var_4 = inventory_data_0.add_group(str_4)
    str_5 = 'group2'
    var_5 = inventory_data_0.add_group(str_5)
    var_6 = inventory_data_0.add_child(str_4, str_2)
    var_7 = inventory_data_0.add_child(str_5, str_2)
    var_8 = inventory_data_0.add_child(str_5, str_3)
    str_6 = 'all'
    var_9 = inventory_data_0.add_child(str_6, str_2)
    var_10 = inventory_data_0.add_child(str_6, str_3)
    var_11 = inventory_data_0.add_child(str_6, str_4)