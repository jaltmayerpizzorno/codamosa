# Automatically generated by Pynguin.
import ansible.inventory.data as module_0
import ansible.inventory.host as module_1

def test_case_0():
    try:
        bytes_0 = b'\xe1\x86\xa1\xd1\xc3'
        set_0 = {bytes_0, bytes_0}
        inventory_data_0 = module_0.InventoryData()
        var_0 = inventory_data_0.deserialize(set_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'|\xb1 \x9dY\xc3\x84\xed%\xb0\xbcU\x15\x13\xeb\xfa\r+:'
        dict_0 = {bytes_0: bytes_0}
        inventory_data_0 = module_0.InventoryData()
        var_0 = inventory_data_0.deserialize(dict_0)
        inventory_data_1 = module_0.InventoryData()
        var_1 = inventory_data_1.serialize()
        var_2 = inventory_data_1.serialize()
        inventory_data_2 = module_0.InventoryData()
        var_3 = inventory_data_2.add_host(bytes_0)
    except BaseException:
        pass

def test_case_2():
    try:
        inventory_data_0 = module_0.InventoryData()
        list_0 = [inventory_data_0]
        inventory_data_1 = module_0.InventoryData()
        var_0 = inventory_data_1.add_group(list_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'PkjI`OT?\x0c3'
        inventory_data_0 = module_0.InventoryData()
        var_0 = inventory_data_0.remove_group(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = -295
        int_1 = -2185
        set_0 = {int_0, int_1, int_0}
        inventory_data_0 = module_0.InventoryData()
        var_0 = inventory_data_0.remove_group(set_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bytes_0 = b'|\xb1 \x9dY\xc3\x84\xed%\xb0\xbcU\x15\x13\xeb\xfa\r+:'
        inventory_data_0 = module_0.InventoryData()
        inventory_data_1 = module_0.InventoryData()
        var_0 = inventory_data_1.serialize()
        var_1 = inventory_data_1.serialize()
        inventory_data_2 = module_0.InventoryData()
        var_2 = inventory_data_2.add_host(bytes_0)
    except BaseException:
        pass

def test_case_6():
    try:
        set_0 = None
        tuple_0 = (set_0,)
        inventory_data_0 = module_0.InventoryData()
        var_0 = inventory_data_0.remove_group(tuple_0)
        dict_0 = {}
        str_0 = "![qRlD'lte0|otl=t"
        var_1 = inventory_data_0.add_host(dict_0, str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        inventory_data_0 = module_0.InventoryData()
        var_0 = inventory_data_0.serialize()
        bytes_0 = b'\x18\x90\xfbR\xdb\xc6\xe7{J7t\xd0'
        str_0 = '(1o~dm/(3\th,*P\twO'
        tuple_0 = (str_0,)
        float_0 = 100.0
        var_1 = inventory_data_0.set_variable(bytes_0, tuple_0, float_0)
    except BaseException:
        pass

def test_case_8():
    try:
        inventory_data_0 = module_0.InventoryData()
        bytes_0 = b'a\xe8\x17y+\xd2\xb4\t;\xfa\xa8\xce\x8a\xb0-,A'
        inventory_data_1 = module_0.InventoryData()
        var_0 = inventory_data_1.add_child(inventory_data_0, bytes_0)
    except BaseException:
        pass

def test_case_9():
    try:
        inventory_data_0 = module_0.InventoryData()
        var_0 = inventory_data_0.reconcile_inventory()
        var_1 = inventory_data_0.serialize()
        var_2 = inventory_data_0.get_groups_dict()
    except BaseException:
        pass

def test_case_10():
    try:
        inventory_data_0 = module_0.InventoryData()
        str_0 = '^O'
        var_0 = inventory_data_0.get_host(str_0)
        var_1 = inventory_data_0.get_groups_dict()
        list_0 = [inventory_data_0]
        host_0 = module_1.Host(list_0)
        var_2 = inventory_data_0.get_host(host_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = '\\^O'
        inventory_data_0 = module_0.InventoryData()
        var_0 = inventory_data_0.add_host(str_0)
        var_1 = inventory_data_0.remove_group(str_0)
        var_2 = inventory_data_0.get_groups_dict()
        var_3 = inventory_data_0.get_groups_dict()
        var_4 = inventory_data_0.get_host(inventory_data_0)
        var_5 = inventory_data_0.reconcile_inventory()
        list_0 = None
        bool_0 = True
        bytes_0 = b'\x80\x83\x81)\xef\x15\xcc\xb5\x973\xe18\x98\xb0\x90\xb5\x8a\xdd'
        var_6 = inventory_data_0.add_host(bool_0, bytes_0, list_0)
    except BaseException:
        pass

def test_case_12():
    try:
        inventory_data_0 = module_0.InventoryData()
        bytes_0 = b'| \x9dY\x84\xed%\xb0\xbcU\x15\x13\xeb}\r+:'
        dict_0 = {bytes_0: bytes_0}
        inventory_data_1 = module_0.InventoryData()
        var_0 = inventory_data_1.deserialize(dict_0)
        inventory_data_2 = module_0.InventoryData()
        inventory_data_3 = module_0.InventoryData()
        var_1 = inventory_data_0.reconcile_inventory()
        str_0 = '9#a'
        var_2 = inventory_data_2.add_host(str_0, inventory_data_0)
    except BaseException:
        pass

def test_case_13():
    try:
        inventory_data_0 = module_0.InventoryData()
        var_0 = inventory_data_0.reconcile_inventory()
        inventory_data_1 = module_0.InventoryData()
        tuple_0 = ()
        var_1 = inventory_data_0.add_group(tuple_0)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = 'all'
        inventory_data_0 = module_0.InventoryData()
        str_1 = 'test'
        var_0 = inventory_data_0.add_host(str_1, str_0)
        var_1 = inventory_data_0.reconcile_inventory()
        var_2 = inventory_data_0.add_host(str_0, str_0)
        var_3 = inventory_data_0.add_host(str_1, str_0)
        var_4 = inventory_data_0.add_child(str_0, str_1)
        var_5 = inventory_data_0.reconcile_inventory()
    except BaseException:
        pass

def test_case_15():
    try:
        inventory_data_0 = module_0.InventoryData()
        str_0 = 'LA'
        var_0 = inventory_data_0.add_group(str_0)
        str_1 = 'LA_1'
        var_1 = inventory_data_0.add_group(str_1)
        str_2 = 'localhost'
        var_2 = inventory_data_0.add_host(str_2, str_0)
        str_3 = 'host_A'
        var_3 = inventory_data_0.add_host(str_3, str_0)
        str_4 = 'host_B'
        var_4 = inventory_data_0.add_host(str_4, str_0)
        var_5 = inventory_data_0.get_host(str_3)
        var_6 = inventory_data_0.reconcile_inventory()
        var_7 = inventory_data_0.get_host(str_3)
        list_0 = [var_4]
        var_8 = inventory_data_0.add_host(list_0)
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = '\\^O'
        inventory_data_0 = module_0.InventoryData()
        var_0 = inventory_data_0.add_host(str_0)
        var_1 = inventory_data_0.add_group(str_0)
        var_2 = inventory_data_0.reconcile_inventory()
        var_3 = inventory_data_0.remove_group(str_0)
        var_4 = inventory_data_0.get_groups_dict()
        var_5 = inventory_data_0.reconcile_inventory()
        inventory_data_1 = module_0.InventoryData()
        var_6 = inventory_data_1.get_host(inventory_data_1)
        var_7 = inventory_data_0.reconcile_inventory()
        var_8 = inventory_data_1.serialize()
        inventory_data_2 = module_0.InventoryData()
        var_9 = inventory_data_2.serialize()
        bool_0 = False
        inventory_data_3 = module_0.InventoryData()
        var_10 = inventory_data_3.add_host(bool_0)
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = '\n*** STARTING unit test ***\n'
        var_0 = print(str_0)
        inventory_data_0 = module_0.InventoryData()
        str_1 = 'all'
        str_2 = 'apaches'
        var_1 = inventory_data_0.add_child(str_1, str_2)
    except BaseException:
        pass