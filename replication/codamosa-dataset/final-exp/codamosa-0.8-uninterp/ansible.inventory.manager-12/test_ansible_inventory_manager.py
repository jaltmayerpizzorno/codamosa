# Automatically generated by Pynguin.
import ansible.inventory.manager as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'fileglob'
    var_0 = module_0.order_patterns(str_0)

def test_case_2():
    str_0 = 'w{`d-.9$'
    var_0 = module_0.split_host_pattern(str_0)

def test_case_3():
    list_0 = []
    float_0 = 2555.297
    inventory_manager_0 = module_0.InventoryManager(list_0)
    var_0 = inventory_manager_0.list_hosts(float_0)

def test_case_4():
    str_0 = '@vMCi,@u0+gV'
    inventory_manager_0 = module_0.InventoryManager(str_0)
    var_0 = inventory_manager_0.list_hosts()
    var_1 = inventory_manager_0.list_hosts(str_0)

def test_case_5():
    bool_0 = False
    inventory_manager_0 = module_0.InventoryManager(bool_0)

def test_case_6():
    int_0 = 2263
    str_0 = '*#2g_'
    inventory_manager_0 = module_0.InventoryManager(int_0, str_0)
    var_0 = inventory_manager_0.clear_pattern_cache()

def test_case_7():
    bytes_0 = b''
    inventory_manager_0 = module_0.InventoryManager(bytes_0)
    var_0 = inventory_manager_0.get_groups_dict()

def test_case_8():
    str_0 = "3vW.\r'd~w"
    int_0 = None
    bytes_0 = b'\x11,E\xc1U\xd7\xa1\xe6\xa9ao\x9d\xdf\x8d\xaa\xfd'
    dict_0 = {}
    str_1 = '/pynguin/#a\ni0< Do]{'
    inventory_manager_0 = module_0.InventoryManager(bytes_0, dict_0, str_1)
    var_0 = inventory_manager_0.subset(int_0)
    inventory_manager_1 = module_0.InventoryManager(str_0)
    var_1 = inventory_manager_1.reconcile_inventory()
    dict_1 = {inventory_manager_1: str_0}
    var_2 = inventory_manager_1.subset(dict_1)

def test_case_9():
    int_0 = -1455
    tuple_0 = (int_0,)
    str_0 = 'vMCi,@u0+gV'
    inventory_manager_0 = module_0.InventoryManager(str_0)
    var_0 = inventory_manager_0.list_hosts()
    complex_0 = None
    var_1 = inventory_manager_0.list_hosts(complex_0)
    var_2 = inventory_manager_0.get_host(str_0)
    inventory_manager_1 = module_0.InventoryManager(str_0, str_0)
    inventory_manager_2 = module_0.InventoryManager(tuple_0)
    var_3 = inventory_manager_0.list_hosts()
    var_4 = inventory_manager_2.get_groups_dict()

def test_case_10():
    list_0 = []
    str_0 = '9im>Y^706,J-]l4f\x0c'
    inventory_manager_0 = module_0.InventoryManager(list_0, str_0)

def test_case_11():
    str_0 = '\rlTz'
    list_0 = [str_0, str_0, str_0]
    list_1 = []
    str_1 = 'status'
    inventory_manager_0 = module_0.InventoryManager(list_1, str_1)
    var_0 = inventory_manager_0.parse_source(list_0)

def test_case_12():
    str_0 = 'a.r~x7mWv'
    inventory_manager_0 = module_0.InventoryManager(str_0)
    var_0 = inventory_manager_0.refresh_inventory()

def test_case_13():
    list_0 = []
    str_0 = '9im>Y^706,J-]l4f\x0c'
    int_0 = 1974
    inventory_manager_0 = module_0.InventoryManager(int_0)
    inventory_manager_1 = module_0.InventoryManager(list_0, str_0)
    var_0 = inventory_manager_1.list_groups()
    var_1 = inventory_manager_1.list_hosts()

def test_case_14():
    str_0 = '@vMCi,@u0+gV'
    inventory_manager_0 = module_0.InventoryManager(str_0)
    float_0 = 990.8954717848499
    list_0 = [float_0]
    set_0 = {inventory_manager_0, float_0}
    var_0 = inventory_manager_0.subset(set_0)
    var_1 = inventory_manager_0.parse_source(list_0)

def test_case_15():
    str_0 = "3vW.\r'd~w"
    int_0 = None
    bytes_0 = b'\x11,E\xc1U\xd7\xa1\xe6\xa9ao\x9d\xdf\x8d\xaa\xfd'
    dict_0 = {}
    str_1 = '/pynguin/#a\ni0< Do]{'
    inventory_manager_0 = module_0.InventoryManager(bytes_0, dict_0, str_1)
    var_0 = inventory_manager_0.subset(int_0)
    inventory_manager_1 = module_0.InventoryManager(str_0)
    dict_1 = {inventory_manager_1: str_0}
    var_1 = inventory_manager_1.subset(dict_1)

def test_case_16():
    list_0 = []
    var_0 = module_0.split_host_pattern(list_0)
    float_0 = 1585.6288
    float_1 = -295.10787
    dict_0 = {}
    inventory_manager_0 = module_0.InventoryManager(float_1, dict_0)
    var_1 = inventory_manager_0.list_hosts(float_0)
    var_2 = inventory_manager_0.get_groups_dict()

def test_case_17():
    str_0 = '@vMCi,@u0+gV'
    inventory_manager_0 = module_0.InventoryManager(str_0)
    var_0 = inventory_manager_0.list_hosts()
    float_0 = 990.8954717848499
    list_0 = [float_0]
    set_0 = {inventory_manager_0, float_0}
    var_1 = inventory_manager_0.subset(set_0)
    var_2 = inventory_manager_0.parse_source(list_0)
    var_3 = inventory_manager_0.list_hosts(str_0)
    var_4 = inventory_manager_0.list_hosts(list_0)

def test_case_18():
    float_0 = 1585.6288
    dict_0 = {}
    str_0 = 'algorithms'
    inventory_manager_0 = module_0.InventoryManager(float_0, str_0)
    str_1 = '6'
    inventory_manager_1 = module_0.InventoryManager(str_1)
    var_0 = inventory_manager_1.list_hosts(inventory_manager_0)
    str_2 = ''
    set_0 = {inventory_manager_0, inventory_manager_0}
    inventory_manager_2 = module_0.InventoryManager(str_2, set_0, dict_0)

def test_case_19():
    str_0 = 'w{`d-.9$'
    var_0 = module_0.split_host_pattern(str_0)
    bytes_0 = b''
    inventory_manager_0 = module_0.InventoryManager(bytes_0)
    int_0 = 3250
    str_1 = "M;H\re)'1?ok"
    var_1 = inventory_manager_0.get_hosts(int_0, str_1)
    var_2 = inventory_manager_0.clear_caches()
    var_3 = inventory_manager_0.clear_pattern_cache()
    var_4 = inventory_manager_0.subset(bytes_0)
    var_5 = inventory_manager_0.reconcile_inventory()
    var_6 = inventory_manager_0.clear_caches()
    var_7 = inventory_manager_0.clear_caches()

def test_case_20():
    list_0 = []
    str_0 = '9im>Y^706,J-]l4f\x0c'
    inventory_manager_0 = module_0.InventoryManager(list_0, str_0)
    var_0 = inventory_manager_0.list_hosts()

def test_case_21():
    str_0 = '@vMCi,@u0+gV'
    inventory_manager_0 = module_0.InventoryManager(str_0)
    var_0 = inventory_manager_0.list_hosts()
    float_0 = 990.8954717848499
    set_0 = {inventory_manager_0, float_0}
    var_1 = inventory_manager_0.subset(set_0)
    var_2 = inventory_manager_0.list_hosts(str_0)

def test_case_22():
    str_0 = 'host.*'
    str_1 = 'host1'
    str_2 = [str_0, str_1]
    var_0 = module_0.order_patterns(str_2)
    str_3 = 'host.example.com'
    str_4 = 'host.example.net'
    str_5 = [str_3, str_4]
    var_1 = module_0.order_patterns(str_5)
    str_6 = '&host.example.net'
    str_7 = [str_3, str_6]
    var_2 = module_0.order_patterns(str_7)
    str_8 = '&host.example.com'
    str_9 = '!host.example.net'
    str_10 = [str_8, str_9]
    var_3 = module_0.order_patterns(str_10)

def test_case_23():
    list_0 = []
    str_0 = '9im>Y^706,J-]l4f\x0c'
    float_0 = 1585.6288
    float_1 = -295.10787
    dict_0 = {}
    inventory_manager_0 = module_0.InventoryManager(float_1, dict_0)
    var_0 = inventory_manager_0.list_hosts(float_0)
    var_1 = inventory_manager_0.subset(list_0)
    inventory_manager_1 = module_0.InventoryManager(list_0, str_0)
    var_2 = inventory_manager_0.clear_pattern_cache()
    str_1 = '%De'
    var_3 = inventory_manager_1.parse_source(str_1)
    str_2 = 'N-7V!'
    set_0 = {str_2, var_1, var_2}
    inventory_manager_2 = module_0.InventoryManager(set_0)
    var_4 = module_0.order_patterns(set_0)
    var_5 = inventory_manager_1.get_groups_dict()
    var_6 = inventory_manager_1.list_hosts()

def test_case_24():
    list_0 = []
    str_0 = '9im>Y^706,J-]l4f\x0c'
    float_0 = -295.10787
    dict_0 = {}
    inventory_manager_0 = module_0.InventoryManager(float_0, dict_0)
    var_0 = inventory_manager_0.list_hosts(float_0)
    var_1 = inventory_manager_0.subset(list_0)
    inventory_manager_1 = module_0.InventoryManager(list_0, str_0)
    var_2 = inventory_manager_0.clear_pattern_cache()
    str_1 = '%De'
    var_3 = inventory_manager_1.parse_source(str_1)
    var_4 = inventory_manager_0.parse_sources()
    var_5 = inventory_manager_0.list_hosts(list_0)
    var_6 = inventory_manager_1.get_groups_dict()

def test_case_25():
    int_0 = 2533
    list_0 = [int_0]
    bool_0 = True
    set_0 = None
    dict_0 = {set_0: set_0, set_0: set_0, set_0: set_0}
    inventory_manager_0 = module_0.InventoryManager(dict_0)
    var_0 = inventory_manager_0.get_hosts(list_0, bool_0, bool_0)
    list_1 = []
    str_0 = '9im>Y^706,J-]l4f\x0c'
    float_0 = 1585.6288
    dict_1 = {}
    inventory_manager_1 = module_0.InventoryManager(float_0, str_0)
    str_1 = '6'
    inventory_manager_2 = module_0.InventoryManager(str_1)
    var_1 = inventory_manager_2.list_hosts(inventory_manager_1)
    tuple_0 = None
    var_2 = inventory_manager_2.get_hosts(tuple_0, dict_1)
    inventory_manager_3 = module_0.InventoryManager(list_1)
    var_3 = inventory_manager_3.parse_sources()
    var_4 = inventory_manager_1.clear_pattern_cache()

def test_case_26():
    str_0 = '/'
    str_1 = '<v8MCi%,@u0+gV'
    inventory_manager_0 = module_0.InventoryManager(str_1)
    float_0 = -1246.35
    var_0 = inventory_manager_0.list_hosts(float_0)
    var_1 = inventory_manager_0.list_hosts()
    complex_0 = None
    var_2 = inventory_manager_0.list_hosts(complex_0)
    var_3 = inventory_manager_0.get_host(str_0)
    float_1 = 1000.0
    list_0 = [float_1]
    inventory_manager_1 = module_0.InventoryManager(str_1, str_0)
    var_4 = inventory_manager_1.parse_source(list_0)
    var_5 = inventory_manager_1.clear_caches()
    float_2 = None
    tuple_0 = None
    inventory_manager_2 = module_0.InventoryManager(tuple_0, float_2)
    var_6 = inventory_manager_1.subset(inventory_manager_1)