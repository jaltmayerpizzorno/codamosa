# Automatically generated by Pynguin.
import ansible.plugins.inventory.host_list as module_0

def test_case_0():
    try:
        str_0 = '\n10.6.2.6\n10.6.2.7\n'
        inventory_module_0 = module_0.InventoryModule()
        var_0 = None
        var_1 = inventory_module_0.parse(var_0, var_0, str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        inventory_module_0 = module_0.InventoryModule()
        int_0 = None
        var_0 = inventory_module_0.parse(inventory_module_0, int_0, inventory_module_0)
    except BaseException:
        pass

def test_case_2():
    try:
        inventory_module_0 = module_0.InventoryModule()
        str_0 = ''
        str_1 = ',\npXb#)+pZm*s.+'
        var_0 = inventory_module_0.parse(str_0, str_0, str_1)
    except BaseException:
        pass

def test_case_3():
    try:
        inventory_module_0 = module_0.InventoryModule()
        str_0 = ''
        var_0 = inventory_module_0.parse(str_0, str_0, str_0)
        str_1 = "g-'AksLUI#"
        var_1 = inventory_module_0.parse(str_0, str_0, str_1)
    except BaseException:
        pass