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
        inventory_module_0 = module_0.InventoryModule()
        int_0 = None
        dict_0 = {int_0: int_0, int_0: int_0, int_0: int_0}
        var_0 = module_0.convert_yaml_objects_to_native(dict_0)
        inventory_module_1 = module_0.InventoryModule()
    except BaseException:
        pass

def test_case_2():
    try:
        inventory_module_0 = module_0.InventoryModule()
        list_0 = [inventory_module_0, inventory_module_0]
        float_0 = -995.0
        bytes_0 = b"v>wm\xe0\xe5\xbb\x02\xb2\xbc\xae\x04\xb9g\x9f\xe7\xe9\x1b'\xbe"
        tuple_0 = (bytes_0,)
        var_0 = module_0.convert_yaml_objects_to_native(list_0)
        set_0 = None
        var_1 = inventory_module_0.verify_file(set_0)
        tuple_1 = (list_0, float_0, tuple_0, inventory_module_0)
        bytes_1 = b'\x1a\xe9'
        set_1 = {bytes_1}
        int_0 = -906
        bool_0 = True
        var_2 = inventory_module_0.parse(set_1, int_0, bool_0, tuple_1)
    except BaseException:
        pass

def test_case_3():
    try:
        inventory_module_0 = module_0.InventoryModule()
        var_0 = inventory_module_0.parse(inventory_module_0, inventory_module_0, inventory_module_0)
    except BaseException:
        pass