# Automatically generated by Pynguin.
import ansible.plugins.inventory.toml as module_0

def test_case_0():
    try:
        bool_0 = True
        var_0 = module_0.toml_dumps(bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        inventory_module_0 = module_0.InventoryModule()
        dict_0 = {inventory_module_0: inventory_module_0, inventory_module_0: inventory_module_0, inventory_module_0: inventory_module_0, inventory_module_0: inventory_module_0}
        var_0 = module_0.convert_yaml_objects_to_native(dict_0)
        int_0 = 882
        var_1 = inventory_module_0.verify_file(int_0)
        bytes_0 = b'\x92\xcf\xc4`~N\x9b\xecT\xc9#\x946=M'
        list_0 = [dict_0, dict_0, dict_0]
        var_2 = inventory_module_0.parse(bytes_0, list_0, list_0, inventory_module_0)
    except BaseException:
        pass

def test_case_2():
    try:
        inventory_module_0 = module_0.InventoryModule()
        float_0 = 0.001
        var_0 = inventory_module_0.parse(float_0, inventory_module_0, float_0)
    except BaseException:
        pass

def test_case_3():
    try:
        float_0 = 100.0
        inventory_module_0 = module_0.InventoryModule()
        set_0 = {float_0, inventory_module_0}
        int_0 = 970
        list_0 = [float_0, int_0, float_0, set_0]
        var_0 = module_0.convert_yaml_objects_to_native(list_0)
        str_0 = "6L'{~\t*WEAS-u"
        var_1 = module_0.convert_yaml_objects_to_native(str_0)
        inventory_module_1 = module_0.InventoryModule()
        var_2 = inventory_module_1.parse(inventory_module_0, inventory_module_0, set_0)
    except BaseException:
        pass