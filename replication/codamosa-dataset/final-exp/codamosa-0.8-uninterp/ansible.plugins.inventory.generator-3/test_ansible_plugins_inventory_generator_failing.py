# Automatically generated by Pynguin.
import ansible.plugins.inventory.generator as module_0

def test_case_0():
    try:
        inventory_module_0 = module_0.InventoryModule()
        inventory_module_1 = module_0.InventoryModule()
        str_0 = 'AsQQ>Fh#x%EO'
        bool_0 = True
        inventory_module_2 = module_0.InventoryModule()
        var_0 = inventory_module_2.template(str_0, bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        float_0 = 5564.0275
        list_0 = [float_0, float_0, float_0]
        str_0 = 'cost'
        inventory_module_0 = module_0.InventoryModule()
        var_0 = inventory_module_0.add_parents(float_0, list_0, str_0, str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'\xb8\x97k\xfd{7\x01i\x0b'
        inventory_module_0 = module_0.InventoryModule()
        var_0 = inventory_module_0.verify_file(bytes_0)
        inventory_module_1 = module_0.InventoryModule()
        bool_0 = False
        inventory_module_2 = module_0.InventoryModule()
        inventory_module_3 = module_0.InventoryModule()
        var_1 = inventory_module_2.parse(inventory_module_1, bool_0, inventory_module_1)
    except BaseException:
        pass

def test_case_3():
    try:
        inventory_module_0 = module_0.InventoryModule()
        var_0 = inventory_module_0.inventory
        str_0 = 'child'
        str_1 = 'name'
        str_2 = 'vars'
        str_3 = 'parent1'
        str_4 = 'var1'
        str_5 = 'value1'
        str_6 = {str_4: str_5}
        str_7 = {str_1: str_3, str_2: str_6}
        str_8 = 'parent2'
        str_9 = {str_1: str_8}
        str_10 = [str_7, str_9]
        var_1 = {}
        var_2 = inventory_module_0.add_parents(var_0, str_0, str_10, var_1)
    except BaseException:
        pass