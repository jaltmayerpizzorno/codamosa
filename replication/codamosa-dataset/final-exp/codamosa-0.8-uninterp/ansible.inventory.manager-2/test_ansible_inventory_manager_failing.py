# Automatically generated by Pynguin.
import ansible.inventory.manager as module_0
import ansible.utils.display as module_1

def test_case_0():
    try:
        bytes_0 = b'\x9a\xec`b\xee%x\xc1\xe7\x17\xbe\xb95\nw'
        inventory_manager_0 = module_0.InventoryManager(bytes_0)
        var_0 = inventory_manager_0.clear_pattern_cache()
        str_0 = '*|zm !]QhdF'
        var_1 = module_0.split_host_pattern(inventory_manager_0)
        complex_0 = None
        set_0 = set()
        var_2 = inventory_manager_0.get_hosts(str_0, complex_0, set_0)
    except BaseException:
        pass

def test_case_1():
    try:
        float_0 = 2715.0376
        float_1 = None
        set_0 = {float_0, float_1, float_0, float_0}
        inventory_manager_0 = module_0.InventoryManager(float_0, set_0)
    except BaseException:
        pass

def test_case_2():
    try:
        tuple_0 = ()
        str_0 = 'UH]'
        list_0 = [tuple_0, str_0, tuple_0, str_0]
        str_1 = 'Z\tME ue3\n5,Jb^b}]\rR>'
        inventory_manager_0 = module_0.InventoryManager(tuple_0, str_1)
        float_0 = -836.757
        set_0 = set()
        inventory_manager_1 = module_0.InventoryManager(inventory_manager_0, float_0, set_0)
        var_0 = inventory_manager_1.reconcile_inventory()
        var_1 = inventory_manager_1.clear_caches()
        inventory_manager_2 = module_0.InventoryManager(list_0)
        var_2 = inventory_manager_2.refresh_inventory()
        var_3 = inventory_manager_0.add_host(tuple_0)
    except BaseException:
        pass

def test_case_3():
    try:
        tuple_0 = ()
        str_0 = 'VJ'
        inventory_manager_0 = module_0.InventoryManager(tuple_0, str_0)
        list_0 = [tuple_0, inventory_manager_0, tuple_0, str_0]
        var_0 = inventory_manager_0.get_host(list_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bool_0 = False
        inventory_manager_0 = module_0.InventoryManager(bool_0)
        bytes_0 = b'X'
        var_0 = inventory_manager_0.restrict_to_hosts(bytes_0)
    except BaseException:
        pass

def test_case_5():
    try:
        float_0 = 567.52
        inventory_manager_0 = module_0.InventoryManager(float_0)
        var_0 = inventory_manager_0.list_groups()
        int_0 = None
        inventory_manager_1 = module_0.InventoryManager(float_0)
        var_1 = inventory_manager_1.list_hosts()
        var_2 = inventory_manager_0.restrict_to_hosts(int_0)
        float_1 = -5140.28
        var_3 = module_0.order_patterns(float_1)
    except BaseException:
        pass

def test_case_6():
    try:
        dict_0 = {}
        list_0 = [dict_0, dict_0, dict_0]
        inventory_manager_0 = module_0.InventoryManager(dict_0, list_0)
    except BaseException:
        pass

def test_case_7():
    try:
        float_0 = 567.52
        inventory_manager_0 = module_0.InventoryManager(float_0)
        var_0 = inventory_manager_0.list_groups()
        int_0 = None
        inventory_manager_1 = module_0.InventoryManager(float_0)
        var_1 = inventory_manager_1.list_hosts()
        var_2 = inventory_manager_0.restrict_to_hosts(int_0)
        float_1 = -5140.28
        var_3 = inventory_manager_1.get_hosts()
        var_4 = module_0.order_patterns(float_1)
    except BaseException:
        pass

def test_case_8():
    try:
        bool_0 = True
        inventory_manager_0 = module_0.InventoryManager(bool_0)
        inventory_manager_1 = None
        dict_0 = {bool_0: inventory_manager_1}
        inventory_manager_2 = module_0.InventoryManager(dict_0)
        var_0 = inventory_manager_0.clear_pattern_cache()
        list_0 = None
        set_0 = {bool_0, bool_0, inventory_manager_0, inventory_manager_0}
        float_0 = -392.5894
        int_0 = -251
        tuple_0 = (float_0, int_0)
        float_1 = None
        tuple_1 = (set_0, tuple_0, int_0, float_1)
        inventory_manager_3 = module_0.InventoryManager(list_0, tuple_1)
    except BaseException:
        pass

def test_case_9():
    try:
        float_0 = 1324.75
        inventory_manager_0 = module_0.InventoryManager(float_0)
        str_0 = '3(zFg'
        inventory_manager_1 = module_0.InventoryManager(str_0)
        var_0 = inventory_manager_0.parse_sources()
        str_1 = '{$g4N@ \\'
        str_2 = 'M-3x+\x0b|YBD\t,+913rI'
        str_3 = '&'
        dict_0 = {str_3: str_2, str_1: inventory_manager_1}
        float_1 = 619.7898
        str_4 = 'Failed to perform archive operation'
        var_1 = inventory_manager_0.get_hosts(dict_0, float_1, str_4)
    except BaseException:
        pass

def test_case_10():
    try:
        bool_0 = True
        float_0 = 567.52
        inventory_manager_0 = module_0.InventoryManager(float_0)
        var_0 = inventory_manager_0.list_groups()
        inventory_manager_1 = module_0.InventoryManager(float_0)
        var_1 = inventory_manager_0.list_hosts()
        bool_1 = False
        list_0 = [bool_1, bool_0, inventory_manager_1]
        var_2 = inventory_manager_0.restrict_to_hosts(list_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = 'In test_InventoryManager_list_hosts'
        var_0 = print(str_0)
        str_1 = '6lWO\x0cwIU"*\x0bf:Cp#Mc*k'
        str_2 = 'localhost,'
        inventory_manager_0 = module_0.InventoryManager(str_1, str_2)
        float_0 = 2988.043
        display_0 = module_1.Display()
        bool_0 = False
        dict_0 = {str_2: bool_0, str_2: str_0, str_1: float_0}
        tuple_0 = (display_0, dict_0)
        tuple_1 = (float_0, tuple_0)
        inventory_manager_1 = module_0.InventoryManager(tuple_1)
        int_0 = None
        var_1 = inventory_manager_1.subset(int_0)
        list_0 = [str_2]
        var_2 = inventory_manager_1.list_hosts(list_0)
        var_3 = inventory_manager_1.list_hosts()
        set_0 = {int_0}
        display_1 = module_1.Display(set_0)
        inventory_manager_2 = module_0.InventoryManager(set_0, tuple_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = 'localhost,'
        inventory_manager_0 = module_0.InventoryManager(str_0, str_0)
        str_1 = 'localhost'
        var_0 = inventory_manager_0.subset(str_1)
        var_1 = inventory_manager_0.subset(str_0)
        str_2 = '@somefile'
        var_2 = inventory_manager_0.subset(str_2)
    except BaseException:
        pass

def test_case_13():
    try:
        complex_0 = None
        inventory_manager_0 = module_0.InventoryManager(complex_0)
        list_0 = []
        bytes_0 = b'\xe1\xdfh\xfc6n:40m:\x11B\xe7\x91}'
        var_0 = module_0.split_host_pattern(bytes_0)
        var_1 = inventory_manager_0.restrict_to_hosts(list_0)
        var_2 = inventory_manager_0.reconcile_inventory()
        int_0 = -466
        inventory_manager_1 = module_0.InventoryManager(int_0)
        var_3 = inventory_manager_1.list_hosts()
        inventory_manager_2 = module_0.InventoryManager(bytes_0)
        var_4 = inventory_manager_2.remove_restriction()
        var_5 = inventory_manager_1.list_groups()
        inventory_manager_3 = module_0.InventoryManager(complex_0, bytes_0)
    except BaseException:
        pass

def test_case_14():
    try:
        bool_0 = False
        inventory_manager_0 = module_0.InventoryManager(bool_0)
        var_0 = inventory_manager_0.clear_pattern_cache()
        str_0 = ';EcF!,:\ny.N'
        float_0 = -3982.92
        var_1 = inventory_manager_0.parse_source(float_0)
        dict_0 = {var_1: str_0}
        var_2 = module_0.order_patterns(dict_0)
        list_0 = []
        inventory_manager_1 = module_0.InventoryManager(str_0, list_0)
        var_3 = inventory_manager_0.list_hosts()
        var_4 = inventory_manager_1.list_groups()
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = "Oh](\n'\x0cqf!sGG1;"
        set_0 = {str_0}
        inventory_manager_0 = module_0.InventoryManager(set_0)
        str_1 = '+9&:j>T\rgdU_4]*|\x0ctUn'
        var_0 = module_0.order_patterns(str_1)
        bytes_0 = b''
        var_1 = inventory_manager_0.add_group(bytes_0)
    except BaseException:
        pass

def test_case_16():
    try:
        bytes_0 = b"T\xbd\x84\x18\x8c\xb8\xe5\xb6\xb7\xf5\xca>'\x89@]\x1e"
        float_0 = 2.0
        bool_0 = False
        display_0 = module_1.Display()
        display_1 = module_1.Display(display_0)
        dict_0 = {float_0: bool_0, bool_0: bool_0, float_0: bytes_0, display_0: bytes_0}
        bool_1 = False
        list_0 = [bytes_0, display_0, bool_1]
        str_0 = '=(AD\tz'
        inventory_manager_0 = module_0.InventoryManager(str_0)
        var_0 = inventory_manager_0.refresh_inventory()
        inventory_manager_1 = module_0.InventoryManager(list_0)
        var_1 = inventory_manager_0.reconcile_inventory()
        var_2 = inventory_manager_1.clear_pattern_cache()
        var_3 = inventory_manager_1.clear_caches()
        var_4 = inventory_manager_0.clear_pattern_cache()
        bytes_1 = b''
        inventory_manager_2 = module_0.InventoryManager(bool_1, bytes_1)
        var_5 = display_1.banner(list_0)
        var_6 = inventory_manager_2.get_hosts(bool_0, display_1, dict_0)
        dict_1 = {bytes_0: bytes_0, float_0: float_0, bytes_0: float_0, float_0: bytes_0}
        inventory_manager_3 = module_0.InventoryManager(dict_1)
        var_7 = display_0.display(bool_0, dict_0)
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = 'localhost,'
        inventory_manager_0 = module_0.InventoryManager(str_0, str_0)
        str_1 = 'localhost,foobar'
        var_0 = inventory_manager_0.subset(str_1)
        str_2 = '@o5mefile'
        var_1 = inventory_manager_0.subset(str_2)
    except BaseException:
        pass