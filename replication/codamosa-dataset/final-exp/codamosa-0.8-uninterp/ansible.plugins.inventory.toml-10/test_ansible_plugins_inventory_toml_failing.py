# Automatically generated by Pynguin.
import ansible.plugins.inventory.toml as module_0

def test_case_0():
    try:
        inventory_module_0 = module_0.InventoryModule()
        var_0 = module_0.toml_dumps(inventory_module_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'yl@-J\xf0J\xbf\xe3\x85\x9b\x17z'
        list_0 = [bytes_0, bytes_0]
        str_0 = '`\n^W{'
        inventory_module_0 = module_0.InventoryModule()
        var_0 = inventory_module_0.verify_file(str_0)
        var_1 = module_0.convert_yaml_objects_to_native(inventory_module_0)
        str_1 = '\x0c=:{m[1a?j'
        var_2 = module_0.convert_yaml_objects_to_native(str_1)
        var_3 = module_0.convert_yaml_objects_to_native(list_0)
        inventory_module_1 = module_0.InventoryModule()
        str_2 = 'O^Lx/qw4PsCE|]6[(l$'
        str_3 = ' Dwpbk'
        var_4 = inventory_module_1.parse(inventory_module_0, list_0, str_2, str_3)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'CP\xee\xb4|F\xccd\xdf\\\x9b'
        int_0 = 1656
        inventory_module_0 = module_0.InventoryModule()
        var_0 = inventory_module_0.parse(bytes_0, int_0, int_0)
    except BaseException:
        pass