# Automatically generated by Pynguin.
import ansible.inventory.data as module_0
import ansible.inventory.host as module_1
import ansible.inventory.group as module_2

def test_case_0():
    try:
        str_0 = 'qKs"7B'
        inventory_data_0 = module_0.InventoryData()
        inventory_data_1 = module_0.InventoryData()
        var_0 = inventory_data_1.serialize()
        var_1 = inventory_data_0.deserialize(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        inventory_data_0 = module_0.InventoryData()
        var_0 = inventory_data_0.get_groups_dict()
        inventory_data_1 = module_0.InventoryData()
        bool_0 = True
        dict_0 = {inventory_data_1: inventory_data_1, inventory_data_1: bool_0}
        inventory_data_2 = module_0.InventoryData()
        var_1 = inventory_data_2.add_group(dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        inventory_data_0 = module_0.InventoryData()
        bool_0 = False
        var_0 = inventory_data_0.add_group(bool_0)
    except BaseException:
        pass

def test_case_3():
    try:
        inventory_data_0 = module_0.InventoryData()
        var_0 = inventory_data_0.reconcile_inventory()
        list_0 = [var_0, var_0]
        bool_0 = False
        bool_1 = False
        set_0 = {bool_1, var_0, inventory_data_0, var_0}
        var_1 = inventory_data_0.add_host(list_0, bool_0, set_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'Z{$'
        set_0 = {str_0, str_0, str_0}
        int_0 = -1170
        inventory_data_0 = module_0.InventoryData()
        var_0 = inventory_data_0.set_variable(str_0, set_0, int_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bool_0 = False
        list_0 = []
        inventory_data_0 = module_0.InventoryData()
        var_0 = inventory_data_0.add_child(bool_0, list_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'signing_key_fingerprint'
        inventory_data_0 = module_0.InventoryData()
        var_0 = inventory_data_0.get_host(str_0)
        inventory_data_1 = None
        bool_0 = True
        inventory_data_2 = module_0.InventoryData()
        var_1 = inventory_data_2.add_host(inventory_data_1, bool_0)
    except BaseException:
        pass

def test_case_7():
    try:
        float_0 = -2290.330194
        int_0 = 9
        int_1 = 32603
        str_0 = "c=B'Dm\\k18sl\x0b{a\\"
        inventory_data_0 = module_0.InventoryData()
        dict_0 = {int_0: str_0, str_0: inventory_data_0, float_0: int_1, int_0: float_0}
        var_0 = inventory_data_0.deserialize(dict_0)
        var_1 = inventory_data_0.set_variable(float_0, int_1, str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        inventory_data_0 = module_0.InventoryData()
        str_0 = 'localhost'
        var_0 = inventory_data_0.get_host(str_0)
        int_0 = 22
        var_1 = inventory_data_0.add_host(str_0, inventory_data_0, int_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = '&U'
        str_1 = 'all'
        inventory_data_0 = module_0.InventoryData()
        var_0 = inventory_data_0.remove_group(str_1)
        var_1 = inventory_data_0.get_host(str_0)
        inventory_data_1 = module_0.InventoryData()
        inventory_data_2 = module_0.InventoryData()
        var_2 = inventory_data_2.add_host(str_0)
        var_3 = inventory_data_2.reconcile_inventory()
        var_4 = inventory_data_2.deserialize(var_0)
    except BaseException:
        pass

def test_case_10():
    try:
        inventory_data_0 = module_0.InventoryData()
        str_0 = 'localhost'
        var_0 = inventory_data_0.add_host(str_0)
        var_1 = inventory_data_0.name
    except BaseException:
        pass

def test_case_11():
    try:
        inventory_data_0 = module_0.InventoryData()
        str_0 = 'host1'
        host_0 = module_1.Host(str_0)
        str_1 = 'host2'
        host_1 = module_1.Host(str_1)
        str_2 = 'all'
        str_3 = 'group1'
        str_4 = 'group2'
        group_0 = module_2.Group(str_2)
        group_1 = module_2.Group(str_3)
        group_2 = module_2.Group(str_4)
        var_0 = inventory_data_0.add_child(str_2, str_0)
    except BaseException:
        pass

def test_case_12():
    try:
        inventory_data_0 = module_0.InventoryData()
        str_0 = 'test_host'
        var_0 = inventory_data_0.add_host(str_0)
        str_1 = 'test_group'
        var_1 = inventory_data_0.add_group(str_1)
        var_2 = inventory_data_0.add_child(str_1, str_0)
        var_3 = inventory_data_0.groups[str_1]
        var_4 = var_3.hosts
        var_5 = len(var_4)
        var_6 = inventory_data_0.hosts[str_0]
        var_7 = var_6.groups
        var_8 = len(var_7)
        var_9 = inventory_data_0.hosts[str_0]
        var_10 = inventory_data_0.remove_host(var_9)
        var_11 = inventory_data_0.groups[str_1]
        var_12 = var_11.hosts
        var_13 = len(var_12)
        var_14 = inventory_data_0.hosts[str_0]
    except BaseException:
        pass