# Automatically generated by Pynguin.
import ansible.plugins.inventory.advanced_host_list as module_0

def test_case_0():
    pass

def test_case_1():
    inventory_module_0 = module_0.InventoryModule()
    dict_0 = {}
    var_0 = inventory_module_0.verify_file(dict_0)

def test_case_2():
    inventory_module_0 = module_0.InventoryModule()
    tuple_0 = ()
    var_0 = inventory_module_0.verify_file(tuple_0)
    tuple_1 = ()
    var_1 = inventory_module_0.verify_file(tuple_1)
    str_0 = '^([^\\s]+)\\s+([\\d\\.]+)'
    inventory_module_1 = module_0.InventoryModule()
    tuple_2 = (inventory_module_0, inventory_module_1, str_0)
    list_0 = []
    str_1 = ''
    var_2 = inventory_module_0.parse(tuple_2, list_0, str_1)