# Automatically generated by Pynguin.
import ansible.plugins.inventory.toml as module_0

def test_case_0():
    pass

def test_case_1():
    bool_0 = False
    inventory_module_0 = module_0.InventoryModule()
    var_0 = inventory_module_0.verify_file(bool_0)
    var_1 = module_0.convert_yaml_objects_to_native(bool_0)
    inventory_module_1 = module_0.InventoryModule()

def test_case_2():
    inventory_module_0 = module_0.InventoryModule()
    dict_0 = {inventory_module_0: inventory_module_0, inventory_module_0: inventory_module_0, inventory_module_0: inventory_module_0}
    var_0 = module_0.convert_yaml_objects_to_native(dict_0)
    bool_0 = True
    set_0 = {bool_0, bool_0, bool_0, bool_0}
    inventory_module_1 = module_0.InventoryModule()
    tuple_0 = (set_0,)
    var_1 = module_0.convert_yaml_objects_to_native(tuple_0)

def test_case_3():
    str_0 = 'Xk.N7uV\x0bX?6'
    complex_0 = None
    var_0 = module_0.convert_yaml_objects_to_native(complex_0)
    bool_0 = True
    inventory_module_0 = module_0.InventoryModule()
    var_1 = inventory_module_0.verify_file(bool_0)
    var_2 = module_0.convert_yaml_objects_to_native(str_0)

def test_case_4():
    inventory_module_0 = module_0.InventoryModule()
    bool_0 = None
    var_0 = inventory_module_0.verify_file(bool_0)