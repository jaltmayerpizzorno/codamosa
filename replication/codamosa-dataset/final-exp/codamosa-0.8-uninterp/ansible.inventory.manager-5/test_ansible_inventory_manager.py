# Automatically generated by Pynguin.
import ansible.inventory.manager as module_0

def test_case_0():
    pass

def test_case_1():
    int_0 = 1214
    inventory_manager_0 = module_0.InventoryManager(int_0)
    var_0 = inventory_manager_0.list_hosts(inventory_manager_0)

def test_case_2():
    dict_0 = {}
    str_0 = 's0,b5-uw"*"?'
    tuple_0 = (str_0,)
    inventory_manager_0 = module_0.InventoryManager(dict_0, str_0, tuple_0)
    str_1 = '&+E54nb_+'
    var_0 = inventory_manager_0.list_hosts(str_1)

def test_case_3():
    int_0 = -365
    dict_0 = {int_0: int_0, int_0: int_0}
    str_0 = 's0,b5-uw"*"?'
    tuple_0 = (str_0,)
    inventory_manager_0 = module_0.InventoryManager(dict_0, str_0, tuple_0)
    str_1 = 'JKzM:(W\t!F ga{~>+VTe'
    var_0 = inventory_manager_0.subset(str_1)
    var_1 = inventory_manager_0.list_hosts()

def test_case_4():
    str_0 = "~m![C'-8)D&$K_yi>4r"
    var_0 = module_0.split_host_pattern(str_0)

def test_case_5():
    bool_0 = True
    inventory_manager_0 = module_0.InventoryManager(bool_0)
    var_0 = inventory_manager_0.subset(bool_0)

def test_case_6():
    int_0 = -344
    dict_0 = {int_0: int_0, int_0: int_0}
    str_0 = 's0,b5-uw"*"?'
    tuple_0 = (str_0,)
    inventory_manager_0 = module_0.InventoryManager(dict_0, str_0, tuple_0)
    var_0 = inventory_manager_0.subset(tuple_0)

def test_case_7():
    str_0 = 't'
    inventory_manager_0 = module_0.InventoryManager(str_0, str_0)

def test_case_8():
    inventory_manager_0 = None
    set_0 = {inventory_manager_0, inventory_manager_0}
    inventory_manager_1 = module_0.InventoryManager(set_0, set_0)
    var_0 = inventory_manager_1.clear_caches()

def test_case_9():
    str_0 = '\n    Return a list of hostnames for a pattern\n    \n    \n    '
    inventory_manager_0 = module_0.InventoryManager(str_0)

def test_case_10():
    str_0 = 'error processing module_util {0} loading redirected collection {1}: {2}'
    str_1 = 'fx9E+bBv'
    inventory_manager_0 = module_0.InventoryManager(str_1)
    var_0 = inventory_manager_0.get_host(str_0)
    str_2 = 'x9MvlF{\rC M:&wMv'
    str_3 = '\\R^gR5'
    inventory_manager_1 = module_0.InventoryManager(str_3)
    var_1 = inventory_manager_1.add_host(str_2)
    var_2 = inventory_manager_1.remove_restriction()

def test_case_11():
    dict_0 = {}
    inventory_manager_0 = module_0.InventoryManager(dict_0)
    var_0 = inventory_manager_0.get_groups_dict()

def test_case_12():
    str_0 = 'refs/tags/'
    list_0 = [str_0, str_0, str_0, str_0]
    str_1 = 'C#$<\\kE6'
    inventory_manager_0 = module_0.InventoryManager(str_1)
    inventory_manager_1 = module_0.InventoryManager(inventory_manager_0)
    var_0 = inventory_manager_1.parse_source(str_0, list_0)
    bytes_0 = b'".\x9c\x1f\x8c\xb9'
    inventory_manager_2 = module_0.InventoryManager(bytes_0)
    var_1 = inventory_manager_2.reconcile_inventory()
    float_0 = 0.5
    inventory_manager_3 = module_0.InventoryManager(float_0)
    var_2 = inventory_manager_3.get_groups_dict()

def test_case_13():
    bool_0 = False
    str_0 = 'hYetfP5m/, I^'
    inventory_manager_0 = module_0.InventoryManager(bool_0, str_0)

def test_case_14():
    float_0 = 592.65
    inventory_manager_0 = module_0.InventoryManager(float_0)
    var_0 = inventory_manager_0.parse_source(float_0)

def test_case_15():
    dict_0 = {}
    inventory_manager_0 = module_0.InventoryManager(dict_0)
    var_0 = inventory_manager_0.list_hosts()

def test_case_16():
    bytes_0 = b"[\xc6!f\xdd\xcf\x8c\xf6\xf4\xf5d'\xa8"
    inventory_manager_0 = module_0.InventoryManager(bytes_0)
    var_0 = inventory_manager_0.list_groups()

def test_case_17():
    str_0 = ''
    inventory_manager_0 = module_0.InventoryManager(str_0, str_0)
    var_0 = inventory_manager_0.clear_pattern_cache()

def test_case_18():
    int_0 = -365
    dict_0 = {int_0: int_0, int_0: int_0}
    str_0 = 's0,b5-uw"*"?'
    str_1 = 'n[kvUM'
    tuple_0 = (str_0,)
    list_0 = [str_1, dict_0, tuple_0]
    tuple_1 = (tuple_0, list_0)
    inventory_manager_0 = module_0.InventoryManager(dict_0, str_0, tuple_1)
    var_0 = inventory_manager_0.clear_caches()
    var_1 = inventory_manager_0.get_groups_dict()
    var_2 = inventory_manager_0.subset(list_0)
    set_0 = {int_0}
    var_3 = module_0.split_host_pattern(set_0)

def test_case_19():
    str_0 = ''
    inventory_manager_0 = module_0.InventoryManager(str_0, str_0)

def test_case_20():
    bool_0 = True
    str_0 = 'hYetfP5m/, I^'
    inventory_manager_0 = module_0.InventoryManager(bool_0, str_0)
    var_0 = inventory_manager_0.clear_pattern_cache()

def test_case_21():
    str_0 = ':'
    bool_0 = True
    inventory_manager_0 = module_0.InventoryManager(bool_0)
    bytes_0 = None
    set_0 = {str_0, str_0, bytes_0}
    inventory_manager_1 = module_0.InventoryManager(set_0, str_0)
    var_0 = inventory_manager_1.parse_source(inventory_manager_0)
    inventory_manager_2 = module_0.InventoryManager(str_0)
    var_1 = inventory_manager_2.list_hosts()
    inventory_manager_3 = module_0.InventoryManager(str_0, str_0)
    int_0 = 1214
    var_2 = inventory_manager_2.refresh_inventory()
    var_3 = inventory_manager_3.get_groups_dict()
    var_4 = inventory_manager_3.subset(int_0)
    int_1 = -1236
    inventory_manager_4 = module_0.InventoryManager(int_1)
    var_5 = inventory_manager_4.list_hosts(inventory_manager_2)

def test_case_22():
    var_0 = None
    inventory_manager_0 = module_0.InventoryManager(var_0)
    var_1 = inventory_manager_0.list_hosts()
    str_0 = 'all'
    var_2 = inventory_manager_0.list_hosts(str_0)

def test_case_23():
    int_0 = -365
    str_0 = '6Gy'
    dict_0 = {int_0: int_0, int_0: int_0}
    tuple_0 = (str_0,)
    bytes_0 = b'znd\xd7\r\xde\xd9K|b\xe3\x85%'
    inventory_manager_0 = module_0.InventoryManager(bytes_0)
    str_1 = 'M'
    inventory_manager_1 = module_0.InventoryManager(str_1, str_1)
    var_0 = inventory_manager_1.list_hosts(inventory_manager_0)
    inventory_manager_2 = module_0.InventoryManager(dict_0, str_0, tuple_0)
    var_1 = inventory_manager_2.clear_caches()
    inventory_manager_3 = module_0.InventoryManager(bytes_0, tuple_0)
    str_2 = '3iqi?;|&Qy0zHq~$d7-\x0b'
    list_0 = [inventory_manager_0, int_0, str_2, str_2]
    var_2 = inventory_manager_2.get_hosts(list_0)

def test_case_24():
    str_0 = '}:'
    inventory_manager_0 = module_0.InventoryManager(str_0)
    var_0 = inventory_manager_0.list_hosts()
    bool_0 = True
    inventory_manager_1 = module_0.InventoryManager(bool_0)
    int_0 = 1214
    var_1 = inventory_manager_1.get_groups_dict()
    var_2 = module_0.split_host_pattern(int_0)
    float_0 = -691.491
    str_1 = '4\x0b(K8'
    set_0 = {str_1, float_0, int_0}
    var_3 = inventory_manager_1.get_hosts(str_1, set_0)

def test_case_25():
    dict_0 = {}
    str_0 = 's0,b5-uw"*"?'
    tuple_0 = (str_0,)
    inventory_manager_0 = module_0.InventoryManager(dict_0, str_0, tuple_0)
    str_1 = '&+E4n*_+'
    var_0 = inventory_manager_0.list_hosts(str_1)
    var_1 = inventory_manager_0.list_hosts()

def test_case_26():
    int_0 = -365
    dict_0 = {int_0: int_0, int_0: int_0}
    str_0 = 's0,b5-uw"*"?'
    tuple_0 = (str_0,)
    inventory_manager_0 = module_0.InventoryManager(dict_0, str_0, tuple_0)
    bytes_0 = None
    var_0 = inventory_manager_0.subset(bytes_0)
    var_1 = inventory_manager_0.list_hosts(int_0)

def test_case_27():
    dict_0 = {}
    str_0 = 's0,b5-uw"*"?'
    tuple_0 = (str_0,)
    inventory_manager_0 = module_0.InventoryManager(dict_0, str_0, tuple_0)
    str_1 = 'JKzM:(W\t!F ga{~>+VTe'
    var_0 = inventory_manager_0.subset(str_1)
    var_1 = inventory_manager_0.list_hosts()

def test_case_28():
    str_0 = "'O\nNgMdS0*ZL@,"
    list_0 = [str_0]
    tuple_0 = (list_0,)
    str_1 = 'uhD<qzJ~['
    tuple_1 = (tuple_0, str_1)
    inventory_manager_0 = module_0.InventoryManager(tuple_1, str_0)
    dict_0 = {}
    str_2 = 's0,b5-uw"*"?'
    tuple_2 = (str_2,)
    inventory_manager_1 = module_0.InventoryManager(dict_0, str_2, tuple_2)
    var_0 = inventory_manager_1.subset(str_2)
    str_3 = '*YWRVC&'
    var_1 = inventory_manager_1.get_host(str_3)
    var_2 = inventory_manager_1.list_hosts()

def test_case_29():
    var_0 = None
    str_0 = '?t'
    str_1 = 'localhost'
    var_1 = sorted(str_1)
    inventory_manager_0 = module_0.InventoryManager(var_0, str_0)
    bool_0 = True
    var_2 = inventory_manager_0.list_hosts(str_1)
    var_3 = inventory_manager_0.list_hosts()

def test_case_30():
    str_0 = "'O\nNgMdS0*ZL@,"
    list_0 = []
    bool_0 = True
    set_0 = {bool_0}
    str_1 = 'p'
    inventory_manager_0 = module_0.InventoryManager(set_0, str_1)
    var_0 = inventory_manager_0.refresh_inventory()
    tuple_0 = (list_0,)
    str_2 = '|hDLzz~6['
    tuple_1 = (tuple_0, str_2)
    inventory_manager_1 = module_0.InventoryManager(tuple_1, str_0)
    str_3 = '/pynguin/bK3j\\<=sN'
    var_1 = inventory_manager_1.get_hosts(inventory_manager_1, str_3)
    var_2 = inventory_manager_1.get_groups_dict()
    dict_0 = {}
    str_4 = 's0,b5-uw"*"?'
    int_0 = 248
    var_3 = inventory_manager_0.parse_source(int_0)
    var_4 = module_0.order_patterns(dict_0)
    var_5 = inventory_manager_1.list_hosts()
    tuple_2 = (str_4,)
    inventory_manager_2 = module_0.InventoryManager(dict_0, str_4, tuple_2)
    var_6 = inventory_manager_2.get_hosts()
    float_0 = -754.0
    inventory_manager_3 = module_0.InventoryManager(float_0, dict_0)
    var_7 = inventory_manager_3.list_hosts()
    var_8 = inventory_manager_3.restrict_to_hosts(list_0)
    var_9 = inventory_manager_3.get_hosts()