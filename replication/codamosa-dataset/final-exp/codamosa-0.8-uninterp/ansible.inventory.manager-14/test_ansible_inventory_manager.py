# Automatically generated by Pynguin.
import ansible.inventory.manager as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = '`!Xn/chjQXVO\x0bs+HPChL'
    var_0 = module_0.order_patterns(str_0)

def test_case_2():
    float_0 = -1862.70927
    var_0 = module_0.split_host_pattern(float_0)

def test_case_3():
    bytes_0 = b''
    inventory_manager_0 = module_0.InventoryManager(bytes_0)
    var_0 = inventory_manager_0.get_hosts()

def test_case_4():
    str_0 = '%W'
    inventory_manager_0 = module_0.InventoryManager(str_0, str_0)

def test_case_5():
    str_0 = 'PkuN\tPX"%Xvdsh7\\'
    inventory_manager_0 = module_0.InventoryManager(str_0)

def test_case_6():
    str_0 = 'Q'
    str_1 = 'x(pGp/$'
    inventory_manager_0 = module_0.InventoryManager(str_1)
    var_0 = inventory_manager_0.get_groups_dict()
    inventory_manager_1 = module_0.InventoryManager(str_0)
    var_1 = inventory_manager_1.clear_caches()

def test_case_7():
    float_0 = 2603.7788824643394
    str_0 = "\x0c#<D8'%S)\rb%cT&[1,"
    inventory_manager_0 = module_0.InventoryManager(str_0)
    var_0 = inventory_manager_0.get_host(float_0)
    var_1 = inventory_manager_0.remove_restriction()
    str_1 = '&V{LS2:'
    var_2 = inventory_manager_0.get_hosts(str_1, inventory_manager_0)
    var_3 = inventory_manager_0.list_hosts()

def test_case_8():
    str_0 = '/'
    inventory_manager_0 = module_0.InventoryManager(str_0, str_0)

def test_case_9():
    var_0 = None
    inventory_manager_0 = module_0.InventoryManager(var_0)
    var_1 = inventory_manager_0.parse_source(inventory_manager_0)

def test_case_10():
    str_0 = '\rwOt`vd29\x0b9,|x{nbz'
    inventory_manager_0 = module_0.InventoryManager(str_0)
    bool_0 = False
    var_0 = inventory_manager_0.refresh_inventory()
    inventory_manager_1 = module_0.InventoryManager(bool_0)
    var_1 = inventory_manager_1.parse_source(str_0)
    var_2 = inventory_manager_1.clear_caches()

def test_case_11():
    str_0 = '127.0.0.1'
    inventory_manager_0 = module_0.InventoryManager(str_0, str_0)
    var_0 = inventory_manager_0.get_hosts(str_0)

def test_case_12():
    str_0 = '1R71%vI.1'
    inventory_manager_0 = module_0.InventoryManager(str_0, str_0)
    var_0 = inventory_manager_0.get_hosts(str_0)

def test_case_13():
    str_0 = "'du'&5q-wx>J"
    inventory_manager_0 = module_0.InventoryManager(str_0)
    var_0 = inventory_manager_0.subset(str_0)
    var_1 = inventory_manager_0.list_hosts()

def test_case_14():
    str_0 = ''
    inventory_manager_0 = module_0.InventoryManager(str_0, str_0)
    str_1 = 'test'
    var_0 = inventory_manager_0.subset(str_1)

def test_case_15():
    bytes_0 = b'\x99Z\xe4%+\xb8\x9a\x15\x9a\x03\xd5\x00>\xa9\x05D'
    inventory_manager_0 = module_0.InventoryManager(bytes_0)
    float_0 = None
    var_0 = inventory_manager_0.subset(float_0)
    inventory_manager_1 = module_0.InventoryManager(inventory_manager_0)
    var_1 = inventory_manager_1.parse_sources()
    set_0 = None
    var_2 = module_0.split_host_pattern(set_0)

def test_case_16():
    bytes_0 = b'\x80\x1a \n\xabro\xd5K\xc5\xb3%\xa2Kf\x8b\xbd\xc6\x9bh'
    str_0 = 'EKj\x0bs2b+bK*u.\tQ/'
    inventory_manager_0 = module_0.InventoryManager(bytes_0, str_0)
    inventory_manager_1 = module_0.InventoryManager(inventory_manager_0)
    var_0 = inventory_manager_1.remove_restriction()

def test_case_17():
    str_0 = 'm\x0b$'
    set_0 = {str_0, str_0}
    inventory_manager_0 = module_0.InventoryManager(set_0)
    var_0 = inventory_manager_0.clear_pattern_cache()
    str_1 = '?6K/gc<Y[ToM'
    inventory_manager_1 = module_0.InventoryManager(str_0, str_1)
    var_1 = inventory_manager_1.get_groups_dict()

def test_case_18():
    str_0 = '3Z.\t 1\x0c_iS~'
    var_0 = module_0.split_host_pattern(str_0)

def test_case_19():
    str_0 = '}Npl,eiSGZ1,'
    inventory_manager_0 = module_0.InventoryManager(str_0, str_0)
    str_1 = 'localhost'
    var_0 = inventory_manager_0.get_hosts(str_1)
    var_1 = len(var_0)

def test_case_20():
    str_0 = '127.0. .m1'
    inventory_manager_0 = module_0.InventoryManager(str_0, str_0)
    var_0 = inventory_manager_0.get_hosts(str_0, inventory_manager_0, inventory_manager_0)

def test_case_21():
    float_0 = -766.09
    int_0 = 158
    set_0 = {float_0, int_0}
    str_0 = "'d&5q-wx>J"
    inventory_manager_0 = module_0.InventoryManager(str_0)
    var_0 = inventory_manager_0.subset(str_0)
    var_1 = inventory_manager_0.parse_source(set_0)
    var_2 = inventory_manager_0.list_hosts(inventory_manager_0)
    var_3 = inventory_manager_0.list_hosts()
    var_4 = inventory_manager_0.parse_source(float_0)
    var_5 = inventory_manager_0.list_hosts()
    int_1 = None
    var_6 = inventory_manager_0.restrict_to_hosts(int_1)

def test_case_22():
    str_0 = 'tests/inventory'
    inventory_manager_0 = module_0.InventoryManager(str_0)
    var_0 = inventory_manager_0.clear_pattern_cache()
    str_1 = 'all'
    var_1 = inventory_manager_0.list_hosts(str_1)
    var_2 = print(var_1)
    str_2 = 'host1'
    var_3 = inventory_manager_0.subset(inventory_manager_0)
    var_4 = inventory_manager_0.list_hosts(str_2)
    var_5 = inventory_manager_0.get_hosts(str_1)

def test_case_23():
    str_0 = 'host1'
    str_1 = 'host2'
    str_2 = 'host3'
    var_0 = module_0.order_patterns(str_1)
    str_3 = '!host2'
    str_4 = [str_0, str_3, str_2]
    var_1 = module_0.order_patterns(str_4)
    str_5 = '&host2'
    str_6 = [str_0, str_5, str_2]
    var_2 = module_0.order_patterns(str_6)
    str_7 = [str_4, str_5, str_2]
    var_3 = module_0.order_patterns(str_7)

def test_case_24():
    str_0 = 'mV]43i,V!(+]}y}'
    float_0 = 2603.7788824643394
    str_1 = "\x0c#<D8'%S)\rb%cT&[1,"
    inventory_manager_0 = module_0.InventoryManager(str_1)
    var_0 = inventory_manager_0.get_host(float_0)
    str_2 = '&V{LS2:'
    var_1 = inventory_manager_0.get_hosts(str_2, inventory_manager_0)
    set_0 = {str_0, str_0}
    var_2 = inventory_manager_0.list_hosts()
    dict_0 = {}
    inventory_manager_1 = module_0.InventoryManager(dict_0, set_0)
    var_3 = inventory_manager_1.remove_restriction()
    var_4 = inventory_manager_1.parse_source(inventory_manager_0)
    inventory_manager_2 = module_0.InventoryManager(str_0, set_0)
    tuple_0 = ()
    var_5 = inventory_manager_1.get_host(tuple_0)
    bytes_0 = b'Tc\x1d\x062\x04\xce\xba'
    var_6 = inventory_manager_2.subset(bytes_0)
    list_0 = [bytes_0, str_2, str_1, str_1]
    var_7 = inventory_manager_1.subset(list_0)
    var_8 = inventory_manager_1.list_hosts()

def test_case_25():
    str_0 = "\x0c#<D8'%S)\rb%cT&[1,"
    set_0 = {str_0, str_0}
    dict_0 = {}
    inventory_manager_0 = module_0.InventoryManager(dict_0, set_0)
    var_0 = inventory_manager_0.remove_restriction()
    inventory_manager_1 = module_0.InventoryManager(str_0, set_0)
    tuple_0 = ()
    var_1 = inventory_manager_0.get_host(tuple_0)
    var_2 = inventory_manager_1.get_hosts()
    var_3 = inventory_manager_0.list_hosts()
    int_0 = 569
    var_4 = inventory_manager_1.subset(dict_0)
    var_5 = inventory_manager_1.list_hosts(int_0)
    var_6 = inventory_manager_0.subset(tuple_0)
    var_7 = inventory_manager_0.list_hosts()

def test_case_26():
    str_0 = '\n            [ungrouped]\n            localhost\n            [group1]\n            localhost\n            [group2]\n            group1:!localhost\n            [group3]\n            otherhost\n            [group4]\n            group2:!group1:!localhost\n    '
    str_1 = 'group1'
    str_2 = '!localhost'
    set_0 = {str_0, str_2, str_0, str_2}
    str_3 = '\t!P\x0bzma+,]IJ((6M&8'
    bool_0 = False
    inventory_manager_0 = module_0.InventoryManager(bool_0)
    var_0 = inventory_manager_0.get_hosts(str_3, set_0)
    bytes_0 = b'\xe8c\x7f\x90>\x03Z\xaf"\xd8h\x94\x1a_'
    bytes_1 = b'\n\x81'
    tuple_0 = (set_0, bytes_1)
    tuple_1 = (bytes_0, tuple_0, set_0)
    tuple_2 = (tuple_1,)
    inventory_manager_1 = module_0.InventoryManager(tuple_2)
    dict_0 = {}
    set_1 = set()
    list_0 = [dict_0, str_0, str_0, str_1]
    int_0 = -268
    tuple_3 = (dict_0, set_1, list_0, int_0)
    bool_1 = False
    inventory_manager_2 = module_0.InventoryManager(int_0, tuple_3, bool_1)