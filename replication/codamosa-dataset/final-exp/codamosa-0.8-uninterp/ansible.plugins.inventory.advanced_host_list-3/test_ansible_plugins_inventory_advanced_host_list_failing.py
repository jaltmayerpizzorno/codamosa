# Automatically generated by Pynguin.
import ansible.plugins.inventory.advanced_host_list as module_0

def test_case_0():
    try:
        inventory_module_0 = module_0.InventoryModule()
        var_0 = inventory_module_0.verify_file(inventory_module_0)
    except BaseException:
        pass

def test_case_1():
    try:
        dict_0 = {}
        inventory_module_0 = module_0.InventoryModule()
        var_0 = inventory_module_0.parse(dict_0, dict_0, inventory_module_0)
    except BaseException:
        pass

def test_case_2():
    try:
        inventory_module_0 = module_0.InventoryModule()
        var_0 = None
        str_0 = 'server-1[01:05],server-2[01:05]'
        var_1 = inventory_module_0.parse(var_0, var_0, str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        inventory_module_0 = module_0.InventoryModule()
        var_0 = None
        str_0 = 'server-1[01:05server-2[01:05]'
        var_1 = inventory_module_0.parse(var_0, var_0, str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        inventory_module_0 = module_0.InventoryModule()
        var_0 = None
        str_0 = 'server-1[01:0u],server-2[01D05]'
        var_1 = inventory_module_0.parse(var_0, var_0, str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        inventory_module_0 = module_0.InventoryModule()
        var_0 = None
        str_0 = 's\rrver-1[01:00],server-2[0?:05]'
        var_1 = inventory_module_0.parse(var_0, var_0, str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        inventory_module_0 = module_0.InventoryModule()
        var_0 = None
        str_0 = ',61'
        var_1 = inventory_module_0.parse(var_0, var_0, str_0)
    except BaseException:
        pass