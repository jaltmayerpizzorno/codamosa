# Automatically generated by Pynguin.
import ansible.plugins.inventory.host_list as module_0

def test_case_0():
    try:
        complex_0 = None
        inventory_module_0 = module_0.InventoryModule()
        var_0 = inventory_module_0.verify_file(complex_0)
    except BaseException:
        pass

def test_case_1():
    try:
        inventory_module_0 = module_0.InventoryModule()
        list_0 = []
        tuple_0 = None
        str_0 = '<w'
        var_0 = inventory_module_0.parse(list_0, tuple_0, str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        dict_0 = None
        inventory_module_0 = module_0.InventoryModule()
        var_0 = inventory_module_0.parse(inventory_module_0, dict_0, dict_0)
    except BaseException:
        pass

def test_case_3():
    try:
        float_0 = 6782.353
        bool_0 = False
        dict_0 = {float_0: bool_0, float_0: float_0}
        str_0 = ',xU)R:X9u"Xp#j^W'
        inventory_module_0 = module_0.InventoryModule()
        var_0 = inventory_module_0.parse(dict_0, bool_0, str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = 3529
        bool_0 = False
        inventory_module_0 = module_0.InventoryModule()
        str_0 = ''
        var_0 = inventory_module_0.parse(int_0, bool_0, str_0)
        bool_1 = True
        inventory_module_1 = module_0.InventoryModule()
        bytes_0 = b'`\xd9CXc'
        var_1 = inventory_module_0.parse(bool_1, int_0, bytes_0)
    except BaseException:
        pass