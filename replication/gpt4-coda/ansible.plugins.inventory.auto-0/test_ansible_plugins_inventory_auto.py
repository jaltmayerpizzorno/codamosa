# Automatically generated by Pynguin.
import ansible.plugins.inventory.auto as module_0

def test_case_0():
    pass

def test_case_1():
    inventory_module_0 = module_0.InventoryModule()
    str_0 = 'tDwHx(\x0cQR43K*U\rg_'
    var_0 = inventory_module_0.verify_file(str_0)

def test_case_2():
    inventory_module_0 = module_0.InventoryModule()
    str_0 = 'valid_inventory.yml'
    var_0 = inventory_module_0.verify_file(str_0)
    var_1 = inventory_module_0.verify_file(str_0)
    str_1 = 'inventory'
    var_2 = inventory_module_0.verify_file(str_1)
    str_2 = '.hidden_inventory.yml'
    var_3 = inventory_module_0.verify_file(str_2)

def test_case_3():
    inventory_module_0 = module_0.InventoryModule()
    str_0 = 'valid_inventory.yml'
    var_0 = inventory_module_0.verify_file(str_0)
    str_1 = 'valid_inventory.yaml'
    var_1 = inventory_module_0.verify_file(str_1)
    str_2 = 'invalid_inventory.txt'
    var_2 = inventory_module_0.verify_file(str_2)
    str_3 = 'inventory'
    var_3 = inventory_module_0.verify_file(str_3)
    str_4 = '.hidden_inventory.yml'
    var_4 = inventory_module_0.verify_file(str_4)