# Automatically generated by Pynguin.
import ansible.plugins.inventory.toml as module_0

def test_case_0():
    pass

def test_case_1():
    bool_0 = False
    inventory_module_0 = module_0.InventoryModule()
    var_0 = inventory_module_0.verify_file(bool_0)
    inventory_module_1 = module_0.InventoryModule()
    var_1 = module_0.convert_yaml_objects_to_native(inventory_module_1)

def test_case_2():
    str_0 = 'w/'
    inventory_module_0 = module_0.InventoryModule()
    bytes_0 = b'96\x8b\x9b\x06\xbe'
    var_0 = inventory_module_0.verify_file(bytes_0)
    dict_0 = {str_0: str_0}
    var_1 = module_0.convert_yaml_objects_to_native(dict_0)
    inventory_module_1 = module_0.InventoryModule()

def test_case_3():
    inventory_module_0 = module_0.InventoryModule()
    str_0 = 'ozQk/qmLP*u(<-'
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.convert_yaml_objects_to_native(list_0)
    var_1 = module_0.convert_yaml_objects_to_native(str_0)
    var_2 = module_0.convert_yaml_objects_to_native(list_0)

def test_case_4():
    float_0 = 405.3967
    inventory_module_0 = module_0.InventoryModule()
    var_0 = inventory_module_0.verify_file(float_0)

def test_case_5():
    inventory_module_0 = module_0.InventoryModule()
    var_0 = None
    var_1 = inventory_module_0.verify_file(var_0)
    str_0 = '/tmp'
    var_2 = inventory_module_0.verify_file(str_0)