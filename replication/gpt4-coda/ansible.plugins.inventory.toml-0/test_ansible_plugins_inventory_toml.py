# Automatically generated by Pynguin.
import ansible.plugins.inventory.toml as module_0

def test_case_0():
    pass

def test_case_1():
    bool_0 = False
    var_0 = module_0.convert_yaml_objects_to_native(bool_0)

def test_case_2():
    str_0 = 'ansible.executor.discovery'
    dict_0 = {str_0: str_0, str_0: str_0}
    ansible_toml_encoder_0 = module_0.AnsibleTomlEncoder()
    bytes_0 = b'\xc5\xbc\xddW\xc8nt.\xdb\x8b\x10'
    var_0 = module_0.convert_yaml_objects_to_native(bytes_0)
    list_0 = [dict_0, str_0, dict_0]
    inventory_module_0 = module_0.InventoryModule()
    inventory_module_1 = module_0.InventoryModule()
    var_1 = inventory_module_0.verify_file(list_0)
    var_2 = module_0.convert_yaml_objects_to_native(dict_0)
    ansible_toml_encoder_1 = module_0.AnsibleTomlEncoder()

def test_case_3():
    str_0 = 'iO0t-'
    var_0 = module_0.convert_yaml_objects_to_native(str_0)
    list_0 = []
    inventory_module_0 = module_0.InventoryModule()
    var_1 = inventory_module_0.verify_file(list_0)

def test_case_4():
    inventory_module_0 = module_0.InventoryModule()
    var_0 = inventory_module_0.verify_file(inventory_module_0)