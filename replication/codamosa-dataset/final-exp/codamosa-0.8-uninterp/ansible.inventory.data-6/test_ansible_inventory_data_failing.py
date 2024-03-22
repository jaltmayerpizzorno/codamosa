# Automatically generated by Pynguin.
import ansible.inventory.data as module_0
import ansible.inventory.host as module_1

def test_case_0():
    try:
        inventory_data_0 = module_0.InventoryData()
        var_0 = inventory_data_0.serialize()
        var_1 = inventory_data_0.get_groups_dict()
    except BaseException:
        pass

def test_case_1():
    try:
        inventory_data_0 = module_0.InventoryData()
        var_0 = inventory_data_0.reconcile_inventory()
        var_1 = inventory_data_0.get_groups_dict()
        inventory_data_1 = module_0.InventoryData()
        float_0 = 2305.867279
        var_2 = inventory_data_0.remove_group(float_0)
        int_0 = 133
        inventory_data_2 = module_0.InventoryData()
        var_3 = inventory_data_2.deserialize(int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '\n'
        dict_0 = {str_0: str_0}
        inventory_data_0 = module_0.InventoryData()
        var_0 = inventory_data_0.deserialize(dict_0)
        var_1 = inventory_data_0.reconcile_inventory()
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'Qs..r?g9L8n$OW'
        inventory_data_0 = module_0.InventoryData()
        var_0 = inventory_data_0.get_host(str_0)
        int_0 = -1394
        inventory_data_1 = module_0.InventoryData()
        var_1 = inventory_data_1.reconcile_inventory()
        inventory_data_2 = module_0.InventoryData()
        var_2 = inventory_data_1.serialize()
        var_3 = inventory_data_2.reconcile_inventory()
        str_1 = 'j`'
        var_4 = inventory_data_2.serialize()
        var_5 = inventory_data_2.add_host(str_1)
        var_6 = inventory_data_1.get_host(int_0)
        str_2 = '::@z}\x0cXO'
        var_7 = inventory_data_2.add_group(str_2)
        inventory_data_3 = module_0.InventoryData()
        var_8 = inventory_data_3.get_groups_dict()
        str_3 = ',$Z}lgaV'
        var_9 = inventory_data_3.reconcile_inventory()
        var_10 = inventory_data_1.remove_group(str_3)
        var_11 = inventory_data_2.reconcile_inventory()
        var_12 = inventory_data_2.get_groups_dict()
        str_4 = 'j`'
        var_13 = inventory_data_3.get_host(str_4)
        inventory_data_4 = module_0.InventoryData()
        inventory_data_5 = module_0.InventoryData()
        complex_0 = None
        var_14 = inventory_data_2.add_group(complex_0)
    except BaseException:
        pass

def test_case_4():
    try:
        inventory_data_0 = module_0.InventoryData()
        str_0 = 'localhost'
        var_0 = inventory_data_0.add_host(str_0)
        str_1 = '\npUv|U4U\naPNa'
        var_1 = inventory_data_0.groups[str_1]
    except BaseException:
        pass

def test_case_5():
    try:
        inventory_data_0 = module_0.InventoryData()
        set_0 = set()
        var_0 = inventory_data_0.reconcile_inventory()
        var_1 = inventory_data_0.get_groups_dict()
        inventory_data_1 = module_0.InventoryData()
        float_0 = 2305.867279
        var_2 = inventory_data_0.remove_group(float_0)
        var_3 = inventory_data_1.add_host(inventory_data_0, set_0)
    except BaseException:
        pass

def test_case_6():
    try:
        bool_0 = False
        inventory_data_0 = module_0.InventoryData()
        bytes_0 = b'H\x8b\x04A\x841'
        tuple_0 = ()
        set_0 = {inventory_data_0, inventory_data_0, bool_0}
        var_0 = inventory_data_0.set_variable(bytes_0, tuple_0, set_0)
    except BaseException:
        pass

def test_case_7():
    try:
        inventory_data_0 = module_0.InventoryData()
        var_0 = inventory_data_0.get_groups_dict()
        str_0 = ',stest_host'
        var_1 = inventory_data_0.add_host(str_0)
        var_2 = inventory_data_0.reconcile_inventory()
        var_3 = inventory_data_0.add_child(str_0, str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        inventory_data_0 = module_0.InventoryData()
        str_0 = 'localhost'
        var_0 = None
        var_1 = inventory_data_0.add_host(str_0, var_0, var_0)
        str_1 = 'localhost.localdomain'
        var_2 = inventory_data_0.add_host(str_1, var_0, var_0)
        str_2 = 'll'
        var_3 = inventory_data_0.add_group(str_2)
        list_0 = [var_2, inventory_data_0]
        var_4 = inventory_data_0.add_group(list_0)
    except BaseException:
        pass

def test_case_9():
    try:
        inventory_data_0 = module_0.InventoryData()
        str_0 = '\x0bqlocalhost'
        var_0 = inventory_data_0.add_host(str_0)
        str_1 = '\npUv|U4U\naPNa'
        var_1 = inventory_data_0.groups[str_1]
    except BaseException:
        pass

def test_case_10():
    try:
        inventory_data_0 = module_0.InventoryData()
        str_0 = 'localhost'
        var_0 = inventory_data_0.add_host(str_0)
        var_1 = inventory_data_0.get_host(str_0)
        str_1 = 'all'
        var_2 = inventory_data_0.groups[str_1]
        dict_0 = None
        host_0 = module_1.Host()
        var_3 = inventory_data_0.add_host(dict_0, host_0, dict_0)
    except BaseException:
        pass

def test_case_11():
    try:
        inventory_data_0 = module_0.InventoryData()
        str_0 = 'Group1'
        str_1 = 'Group2'
        var_0 = inventory_data_0.add_group(str_1)
        str_2 = 'Group3'
        var_1 = inventory_data_0.add_group(str_2)
        str_3 = 'host1'
        var_2 = inventory_data_0.add_host(str_3, str_0)
    except BaseException:
        pass

def test_case_12():
    try:
        inventory_data_0 = module_0.InventoryData()
        var_0 = inventory_data_0.reconcile_inventory()
        var_1 = inventory_data_0.get_groups_dict()
        var_2 = inventory_data_0.get_groups_dict()
        inventory_data_1 = module_0.InventoryData()
        bool_0 = False
        var_3 = inventory_data_0.remove_group(bool_0)
        str_0 = ''
        var_4 = inventory_data_0.add_host(str_0)
    except BaseException:
        pass

def test_case_13():
    try:
        inventory_data_0 = module_0.InventoryData()
        str_0 = ',stest_host'
        var_0 = inventory_data_0.add_host(str_0)
        var_1 = inventory_data_0.reconcile_inventory()
        var_2 = inventory_data_0.get_host(str_0)
        var_3 = str_0.name
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = 'Qs..r?g9L8n$OW'
        inventory_data_0 = module_0.InventoryData()
        var_0 = inventory_data_0.get_host(str_0)
        int_0 = -1394
        inventory_data_1 = module_0.InventoryData()
        var_1 = inventory_data_1.reconcile_inventory()
        inventory_data_2 = module_0.InventoryData()
        var_2 = inventory_data_1.serialize()
        var_3 = inventory_data_2.reconcile_inventory()
        str_1 = 'j`'
        var_4 = inventory_data_2.serialize()
        var_5 = inventory_data_2.add_host(str_1)
        var_6 = inventory_data_1.get_host(int_0)
        str_2 = '::@z}\x0cXO'
        var_7 = inventory_data_2.add_group(str_2)
        inventory_data_3 = module_0.InventoryData()
        int_1 = 1244
        tuple_0 = (int_1,)
        var_8 = inventory_data_2.add_child(str_2, tuple_0)
    except BaseException:
        pass