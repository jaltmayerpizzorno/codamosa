# Automatically generated by Pynguin.
import ansible.inventory.data as module_0
import ansible.inventory.group as module_1
import ansible.inventory.host as module_2

def test_case_0():
    pass

def test_case_1():
    inventory_data_0 = module_0.InventoryData()

def test_case_2():
    inventory_data_0 = module_0.InventoryData()
    var_0 = inventory_data_0.reconcile_inventory()
    var_1 = inventory_data_0.get_groups_dict()
    inventory_data_1 = module_0.InventoryData()
    var_2 = inventory_data_0.serialize()

def test_case_3():
    inventory_data_0 = module_0.InventoryData()
    var_0 = inventory_data_0.reconcile_inventory()

def test_case_4():
    float_0 = -374.0
    inventory_data_0 = module_0.InventoryData()
    var_0 = inventory_data_0.get_host(float_0)

def test_case_5():
    float_0 = 643.1
    inventory_data_0 = module_0.InventoryData()
    var_0 = inventory_data_0.remove_group(float_0)
    inventory_data_1 = module_0.InventoryData()

def test_case_6():
    str_0 = 'L@R'
    inventory_data_0 = module_0.InventoryData()
    var_0 = inventory_data_0.add_host(str_0)

def test_case_7():
    group_0 = module_1.Group()
    inventory_data_0 = module_0.InventoryData()
    var_0 = inventory_data_0.remove_host(group_0)

def test_case_8():
    inventory_data_0 = module_0.InventoryData()
    var_0 = inventory_data_0.get_groups_dict()

def test_case_9():
    inventory_data_0 = module_0.InventoryData()
    str_0 = "1GN7q2\n2'<"
    var_0 = inventory_data_0.add_host(str_0)
    var_1 = inventory_data_0.reconcile_inventory()
    str_1 = 'all'
    var_2 = inventory_data_0.groups[str_1]

def test_case_10():
    inventory_data_0 = module_0.InventoryData()
    str_0 = 'group1'
    var_0 = inventory_data_0.add_group(str_0)
    var_1 = inventory_data_0.groups[str_0]
    var_2 = inventory_data_0.add_group(str_0)
    str_1 = 'group3'
    var_3 = inventory_data_0.add_group(str_1)

def test_case_11():
    inventory_data_0 = module_0.InventoryData()
    str_0 = '127.0.0.1'
    var_0 = inventory_data_0.add_host(str_0)
    var_1 = inventory_data_0.get_host(str_0)

def test_case_12():
    str_0 = 'aKl'
    inventory_data_0 = module_0.InventoryData()
    inventory_data_1 = module_0.InventoryData()
    var_0 = inventory_data_1.add_host(str_0)
    var_1 = inventory_data_0.get_groups_dict()
    var_2 = inventory_data_1.get_groups_dict()
    var_3 = inventory_data_1.reconcile_inventory()
    var_4 = inventory_data_1.get_host(str_0)
    var_5 = inventory_data_1.reconcile_inventory()
    inventory_data_2 = module_0.InventoryData()

def test_case_13():
    str_0 = 'aKl'
    inventory_data_0 = module_0.InventoryData()
    inventory_data_1 = module_0.InventoryData()
    var_0 = inventory_data_1.add_host(str_0)
    var_1 = inventory_data_0.get_groups_dict()
    var_2 = inventory_data_1.get_groups_dict()
    var_3 = inventory_data_1.reconcile_inventory()
    inventory_data_2 = module_0.InventoryData()
    bool_0 = False
    var_4 = inventory_data_0.get_host(bool_0)
    var_5 = inventory_data_1.get_groups_dict()
    var_6 = inventory_data_2.get_host(str_0)
    var_7 = inventory_data_1.reconcile_inventory()
    inventory_data_3 = module_0.InventoryData()
    inventory_data_4 = module_0.InventoryData()

def test_case_14():
    inventory_data_0 = module_0.InventoryData()
    str_0 = 'localhost'
    var_0 = inventory_data_0.add_host(str_0)
    str_1 = 'testgroup'
    var_1 = inventory_data_0.add_group(str_1)
    var_2 = inventory_data_0.reconcile_inventory()
    str_2 = 'ungrouped'
    var_3 = inventory_data_0.groups[str_2]
    str_3 = 'all'
    var_4 = inventory_data_0.groups[str_3]

def test_case_15():
    inventory_data_0 = module_0.InventoryData()
    str_0 = '127.0.0.1'
    var_0 = inventory_data_0.get_host(str_0)

def test_case_16():
    inventory_data_0 = module_0.InventoryData()
    str_0 = 'localhost'
    var_0 = inventory_data_0.get_host(str_0)
    str_1 = 'localhost'
    var_1 = inventory_data_0.get_host(str_1)

def test_case_17():
    inventory_data_0 = module_0.InventoryData()
    str_0 = 'localhost'
    var_0 = inventory_data_0.get_host(str_0)
    var_1 = inventory_data_0.add_host(str_0)

def test_case_18():
    inventory_data_0 = module_0.InventoryData()
    str_0 = 'test_InventoryData_remove_host'
    host_0 = module_2.Host(str_0)
    var_0 = host_0.name
    var_1 = inventory_data_0.add_host(var_0)
    var_2 = inventory_data_0.remove_host(host_0)

def test_case_19():
    str_0 = 'local'
    var_0 = dict(ansible_python_interpreter=str_0, ansible_connection=str_0)
    var_1 = dict(localhost=var_0)
    inventory_data_0 = module_0.InventoryData()
    str_1 = 'ansible_connection'
    str_2 = 'localhost'
    var_2 = var_1[str_2][str_1]
    str_3 = 'all'
    var_3 = inventory_data_0.add_host(var_2, str_3)
    var_4 = var_1[str_2][str_1]
    var_5 = inventory_data_0.set_variable(var_4, str_2, var_4)
    var_6 = inventory_data_0.reconcile_inventory()

def test_case_20():
    inventory_data_0 = module_0.InventoryData()
    str_0 = 'group_1'
    var_0 = inventory_data_0.add_group(str_0)
    str_1 = 'group_2'
    var_1 = inventory_data_0.add_group(str_1)
    str_2 = 'group_3'
    var_2 = inventory_data_0.add_group(str_2)
    str_3 = 'group_4'
    var_3 = inventory_data_0.add_group(str_3)
    str_4 = 'host_1'
    var_4 = inventory_data_0.add_host(str_4)
    var_5 = inventory_data_0.add_child(str_0, str_4)
    var_6 = inventory_data_0.add_child(str_1, str_4)
    var_7 = inventory_data_0.add_child(str_1, str_2)
    var_8 = inventory_data_0.add_child(str_1, str_3)
    var_9 = inventory_data_0.reconcile_inventory()