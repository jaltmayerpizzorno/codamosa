# Automatically generated by Pynguin.
import ansible.inventory.manager as module_0

def test_case_0():
    try:
        bytes_0 = b'\xec\xb0\xe9u\x19*KA\x1a\xadhu\x1b\xd5'
        var_0 = module_0.order_patterns(bytes_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'xU~'
        bool_0 = False
        list_0 = []
        var_0 = module_0.split_host_pattern(list_0)
        int_0 = 2197
        set_0 = set()
        tuple_0 = (list_0, int_0, set_0)
        float_0 = -5109.9
        tuple_1 = (tuple_0, float_0)
        inventory_manager_0 = module_0.InventoryManager(tuple_1, str_0, set_0)
        var_1 = inventory_manager_0.parse_sources()
        inventory_manager_1 = module_0.InventoryManager(str_0, bool_0)
    except BaseException:
        pass

def test_case_2():
    try:
        float_0 = -1454.407
        tuple_0 = None
        list_0 = [float_0, float_0, float_0, tuple_0]
        str_0 = '\nM0'
        inventory_manager_0 = module_0.InventoryManager(list_0, str_0)
        var_0 = inventory_manager_0.add_group(tuple_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = ''
        inventory_manager_0 = module_0.InventoryManager(str_0, str_0)
        bytes_0 = b'\x96 \x95{\xb1\x8av\x9fn\xd6\xfc\xad&'
        var_0 = inventory_manager_0.restrict_to_hosts(bytes_0)
    except BaseException:
        pass

def test_case_4():
    try:
        dict_0 = {}
        float_0 = -558.62486
        str_0 = 'tag:yaml.org,2002:seq'
        bool_0 = None
        tuple_0 = (float_0, str_0, bool_0)
        list_0 = [tuple_0, str_0, tuple_0]
        inventory_manager_0 = module_0.InventoryManager(dict_0, list_0)
    except BaseException:
        pass

def test_case_5():
    try:
        int_0 = -365
        complex_0 = None
        str_0 = 'P8S'
        inventory_manager_0 = module_0.InventoryManager(str_0)
        var_0 = inventory_manager_0.restrict_to_hosts(complex_0)
        dict_0 = {int_0: int_0, int_0: int_0}
        str_1 = 'GvfkIt&d+7;T^V'
        tuple_0 = (str_1,)
        var_1 = inventory_manager_0.list_hosts(int_0)
        list_0 = [str_1, dict_0, tuple_0]
        tuple_1 = (tuple_0, list_0)
        var_2 = inventory_manager_0.parse_sources()
        inventory_manager_1 = module_0.InventoryManager(dict_0, str_1, tuple_1)
        tuple_2 = (str_0, tuple_1, tuple_0)
        var_3 = inventory_manager_1.list_hosts(tuple_2)
    except BaseException:
        pass

def test_case_6():
    try:
        int_0 = -365
        dict_0 = {int_0: int_0, int_0: int_0}
        str_0 = 's0,b5-uw"*"?'
        str_1 = 'n[kvUM'
        tuple_0 = (str_0,)
        list_0 = [str_1, dict_0, tuple_0]
        tuple_1 = (tuple_0, list_0)
        inventory_manager_0 = module_0.InventoryManager(dict_0, str_0, tuple_1)
        var_0 = inventory_manager_0.clear_caches()
        bytes_0 = b'7\x15\xbf\xc7\xb8iR'
        inventory_manager_1 = module_0.InventoryManager(bytes_0)
        int_1 = -227
        float_0 = 425.617795
        inventory_manager_2 = module_0.InventoryManager(float_0)
        var_1 = inventory_manager_2.get_hosts(int_0, int_1, list_0, dict_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = ':'
        bool_0 = True
        inventory_manager_0 = module_0.InventoryManager(bool_0)
        bytes_0 = None
        var_0 = inventory_manager_0.get_groups_dict()
        set_0 = {str_0, str_0, bytes_0}
        inventory_manager_1 = module_0.InventoryManager(set_0, str_0)
        var_1 = inventory_manager_1.parse_source(inventory_manager_0)
        list_0 = []
        var_2 = inventory_manager_0.list_hosts(list_0)
        bool_1 = False
        float_0 = -2797.123
        inventory_manager_2 = module_0.InventoryManager(bool_1, float_0)
    except BaseException:
        pass

def test_case_8():
    try:
        int_0 = 979
        str_0 = '\x0b}i0\n,n,-qqX?r\rNm,'
        var_0 = module_0.split_host_pattern(str_0)
        var_1 = module_0.order_patterns(int_0)
    except BaseException:
        pass

def test_case_9():
    try:
        dict_0 = None
        list_0 = [dict_0, dict_0, dict_0]
        set_0 = set()
        inventory_manager_0 = module_0.InventoryManager(set_0)
        var_0 = inventory_manager_0.restrict_to_hosts(list_0)
    except BaseException:
        pass

def test_case_10():
    try:
        dict_0 = {}
        str_0 = 's0,b5uw"*"?'
        tuple_0 = (str_0,)
        inventory_manager_0 = module_0.InventoryManager(dict_0, str_0, tuple_0)
        str_1 = '@!mP'
        var_0 = inventory_manager_0.subset(str_1)
    except BaseException:
        pass

def test_case_11():
    try:
        int_0 = 290
        inventory_manager_0 = module_0.InventoryManager(int_0)
        var_0 = inventory_manager_0.refresh_inventory()
        str_0 = 'uhD<qzJ~['
        set_0 = {str_0}
        var_1 = inventory_manager_0.reconcile_inventory()
        int_1 = None
        tuple_0 = (str_0, int_1)
        var_2 = module_0.order_patterns(tuple_0)
        var_3 = inventory_manager_0.parse_source(set_0)
        var_4 = inventory_manager_0.refresh_inventory()
        dict_0 = {}
        str_1 = 's0,b5-uw"*"?'
        tuple_1 = (str_1,)
        var_5 = inventory_manager_0.clear_pattern_cache()
        inventory_manager_1 = module_0.InventoryManager(dict_0, str_1, tuple_1)
        bytes_0 = None
        var_6 = inventory_manager_0.subset(bytes_0)
        var_7 = inventory_manager_0.list_hosts(dict_0)
    except BaseException:
        pass

def test_case_12():
    try:
        var_0 = None
        str_0 = '?t'
        bytes_0 = b'\x90\xbbi\x8a\x97\xbf\x86'
        inventory_manager_0 = module_0.InventoryManager(str_0)
        var_1 = inventory_manager_0.subset(bytes_0)
        str_1 = 'localhost'
        var_2 = sorted(str_1)
        inventory_manager_1 = module_0.InventoryManager(var_0, str_0)
        bool_0 = False
        var_3 = inventory_manager_1.list_hosts(str_1)
        var_4 = inventory_manager_0.list_hosts(str_1)
        var_5 = inventory_manager_1.list_hosts(str_1)
        var_6 = inventory_manager_0.list_hosts()
        var_7 = inventory_manager_0.restrict_to_hosts(inventory_manager_0)
    except BaseException:
        pass

def test_case_13():
    try:
        var_0 = None
        str_0 = '?t'
        bytes_0 = b'\x90\xbbi\x8a\x97\xbf\x86'
        str_1 = 'ANSIBALLZ: Acquiring lock'
        inventory_manager_0 = module_0.InventoryManager(str_1)
        var_1 = inventory_manager_0.subset(bytes_0)
        float_0 = -1615.0
        var_2 = inventory_manager_0.parse_source(float_0)
        str_2 = 'localhost'
        var_3 = sorted(str_2)
        inventory_manager_1 = module_0.InventoryManager(var_0, str_0)
        bool_0 = False
        str_3 = [str_2, str_2, str_1]
        var_4 = inventory_manager_0.list_hosts(str_3)
        var_5 = inventory_manager_1.list_hosts(str_2)
    except BaseException:
        pass

def test_case_14():
    try:
        var_0 = None
        str_0 = '?t'
        var_1 = sorted(str_0)
        inventory_manager_0 = module_0.InventoryManager(var_0, str_0)
        var_2 = inventory_manager_0.list_hosts(str_0)
        var_3 = inventory_manager_0.list_hosts()
        str_1 = ',~;BcuQ]\\HWgUa'
        var_4 = inventory_manager_0.list_hosts(str_1)
    except BaseException:
        pass

def test_case_15():
    try:
        var_0 = None
        str_0 = '?t'
        bytes_0 = b'*\x1d\xbb\x9d\x8a\x97\\\x86'
        str_1 = 'ANSIBALLZ: Acquiring lock'
        inventory_manager_0 = module_0.InventoryManager(str_1)
        var_1 = inventory_manager_0.subset(bytes_0)
        int_0 = 2811
        float_0 = -1615.0
        var_2 = inventory_manager_0.parse_source(float_0)
        str_2 = '8'
        str_3 = 'localhost'
        inventory_manager_1 = module_0.InventoryManager(var_0, str_0)
        var_3 = inventory_manager_0.get_host(int_0)
        bool_0 = False
        var_4 = inventory_manager_1.list_hosts(str_2)
        var_5 = inventory_manager_0.list_hosts(str_2)
        var_6 = inventory_manager_1.list_hosts(str_3)
        var_7 = inventory_manager_0.list_hosts()
        str_4 = ',~;BcuQ]\\HWgUa'
        var_8 = inventory_manager_0.list_hosts(str_4)
    except BaseException:
        pass