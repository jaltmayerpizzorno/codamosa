# Automatically generated by Pynguin.
import ansible.inventory.manager as module_0

def test_case_0():
    try:
        float_0 = -2249.573
        bytes_0 = None
        bool_0 = False
        dict_0 = {bytes_0: bytes_0, float_0: bytes_0, float_0: bool_0}
        var_0 = module_0.order_patterns(dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = 282
        str_0 = '/pynguin/6AJ'
        inventory_manager_0 = module_0.InventoryManager(str_0)
        var_0 = inventory_manager_0.add_host(int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'ehst'
        inventory_manager_0 = module_0.InventoryManager(str_0, str_0)
        list_0 = [str_0, str_0]
        var_0 = inventory_manager_0.subset(list_0)
        var_1 = inventory_manager_0.add_group(list_0)
    except BaseException:
        pass

def test_case_3():
    try:
        set_0 = set()
        list_0 = [set_0, set_0]
        set_1 = set()
        tuple_0 = (set_1, list_0)
        inventory_manager_0 = module_0.InventoryManager(list_0, tuple_0)
    except BaseException:
        pass

def test_case_4():
    try:
        list_0 = []
        inventory_manager_0 = module_0.InventoryManager(list_0)
        var_0 = inventory_manager_0.restrict_to_hosts(inventory_manager_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'pm6,>1pxFzs$I&[D'
        inventory_manager_0 = module_0.InventoryManager(str_0, str_0, str_0)
        str_1 = ':\n3ae,N~{'
        var_0 = inventory_manager_0.clear_pattern_cache()
        var_1 = inventory_manager_0.parse_source(str_1)
        var_2 = inventory_manager_0.refresh_inventory()
        var_3 = inventory_manager_0.get_groups_dict()
        bytes_0 = b'@W\xb1>\x0e'
        var_4 = inventory_manager_0.subset(bytes_0)
    except BaseException:
        pass

def test_case_6():
    try:
        int_0 = 1724
        str_0 = '/T'
        inventory_manager_0 = module_0.InventoryManager(int_0, str_0)
        var_0 = inventory_manager_0.reconcile_inventory()
        var_1 = inventory_manager_0.list_groups()
        var_2 = inventory_manager_0.clear_caches()
        list_0 = [int_0, str_0, inventory_manager_0, inventory_manager_0]
        var_3 = inventory_manager_0.list_hosts(list_0)
        var_4 = inventory_manager_0.reconcile_inventory()
        var_5 = inventory_manager_0.restrict_to_hosts(list_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'u'
        tuple_0 = (str_0,)
        dict_0 = {tuple_0: str_0, str_0: tuple_0, str_0: str_0, tuple_0: str_0, tuple_0: str_0, tuple_0: str_0}
        int_0 = 0
        inventory_manager_0 = module_0.InventoryManager(int_0, dict_0)
    except BaseException:
        pass

def test_case_8():
    try:
        bool_0 = None
        bytes_0 = b"i\xab\xde\x0cAN%'\xd4bD\xa6\x1bi9\xf3"
        set_0 = {bool_0, bool_0}
        inventory_manager_0 = module_0.InventoryManager(bytes_0, set_0)
        inventory_manager_1 = module_0.InventoryManager(inventory_manager_0)
        var_0 = inventory_manager_1.list_hosts()
        int_0 = 200011
        dict_0 = {int_0: int_0, int_0: int_0}
        inventory_manager_2 = module_0.InventoryManager(dict_0)
        var_1 = inventory_manager_2.get_hosts(bool_0)
        bool_1 = True
        str_0 = 'fjF\\us1TD6F0@'
        inventory_manager_3 = module_0.InventoryManager(bool_1, str_0)
        var_2 = inventory_manager_1.subset(inventory_manager_2)
        str_1 = ''
        tuple_0 = (inventory_manager_1, bytes_0)
        str_2 = 'None'
        tuple_1 = (tuple_0, str_1, str_2, tuple_0)
        inventory_manager_4 = module_0.InventoryManager(str_1, tuple_1)
    except BaseException:
        pass

def test_case_9():
    try:
        int_0 = 1724
        str_0 = '/T'
        inventory_manager_0 = module_0.InventoryManager(int_0, str_0)
        bytes_0 = b'\x90\xfbrH4\xf4\xf0\xb3\x98\xb5\xa3\t\xf8c\xce\x8aVL,'
        var_0 = inventory_manager_0.get_hosts(bytes_0)
        var_1 = inventory_manager_0.reconcile_inventory()
        var_2 = inventory_manager_0.list_groups()
        list_0 = [int_0, inventory_manager_0]
        var_3 = inventory_manager_0.list_hosts(list_0)
        var_4 = inventory_manager_0.remove_restriction()
        var_5 = inventory_manager_0.reconcile_inventory()
        bool_0 = True
        var_6 = inventory_manager_0.restrict_to_hosts(bool_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = None
        inventory_manager_0 = module_0.InventoryManager(str_0, str_0, str_0)
        float_0 = -679.0
        set_0 = {float_0, str_0, str_0}
        str_1 = ':\n3a@,N~{'
        var_0 = inventory_manager_0.parse_source(str_1)
        var_1 = inventory_manager_0.subset(var_0)
        var_2 = inventory_manager_0.list_hosts()
        var_3 = inventory_manager_0.refresh_inventory()
        var_4 = inventory_manager_0.get_groups_dict()
        tuple_0 = (str_0,)
        str_2 = 'W{?KgG'
        var_5 = inventory_manager_0.subset(str_2)
        bool_0 = True
        var_6 = inventory_manager_0.parse_source(tuple_0)
        var_7 = inventory_manager_0.parse_sources()
        bytes_0 = b'Y\xca;\xaaX\x9d\xaa\xf1T\x84\xa5'
        var_8 = inventory_manager_0.get_hosts(bool_0, set_0, bytes_0, bytes_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = 'pm6,xpxFzs$I&[D'
        str_1 = None
        inventory_manager_0 = module_0.InventoryManager(str_0, str_0, str_0)
        float_0 = -679.0
        set_0 = {float_0, str_0, str_0}
        str_2 = ':\n3ae,N~{'
        var_0 = inventory_manager_0.parse_source(str_2)
        var_1 = inventory_manager_0.subset(set_0)
        var_2 = inventory_manager_0.list_hosts()
        var_3 = inventory_manager_0.refresh_inventory()
        var_4 = inventory_manager_0.get_groups_dict()
        tuple_0 = (str_1,)
        var_5 = inventory_manager_0.reconcile_inventory()
        var_6 = inventory_manager_0.refresh_inventory()
        str_3 = "{.bbq2dRHy]/'*"
        var_7 = inventory_manager_0.subset(str_3)
        bool_0 = True
        bool_1 = False
        var_8 = inventory_manager_0.parse_source(bool_1, tuple_0)
        var_9 = inventory_manager_0.parse_sources()
        var_10 = inventory_manager_0.get_hosts(bool_1, tuple_0)
        int_0 = -4229
        var_11 = inventory_manager_0.get_hosts(int_0)
        inventory_manager_1 = module_0.InventoryManager(bool_1, str_2)
        var_12 = inventory_manager_1.get_hosts(bool_0)
        var_13 = inventory_manager_0.get_groups_dict()
        float_1 = 0.1
        var_14 = inventory_manager_0.restrict_to_hosts(float_1)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = 'Ji@9&5\x0c\x0bl\nK\n#$$'
        str_1 = '1;Hc`-oXKG(#*00\t'
        inventory_manager_0 = module_0.InventoryManager(str_1)
        var_0 = inventory_manager_0.get_host(str_0)
        str_2 = None
        inventory_manager_1 = module_0.InventoryManager(str_2, str_2, str_2)
        float_0 = -679.0
        set_0 = {inventory_manager_1, float_0, str_2, str_2}
        str_3 = ':\n3a@,N~{'
        var_1 = inventory_manager_1.parse_source(str_3)
        var_2 = inventory_manager_1.subset(var_1)
        var_3 = inventory_manager_1.list_hosts()
        var_4 = inventory_manager_1.get_groups_dict()
        tuple_0 = (str_2,)
        dict_0 = {tuple_0: str_2, str_2: tuple_0, tuple_0: str_2}
        var_5 = inventory_manager_1.reconcile_inventory()
        var_6 = inventory_manager_1.subset(str_3)
        list_0 = None
        bool_0 = True
        var_7 = inventory_manager_1.parse_source(bool_0, tuple_0)
        var_8 = inventory_manager_1.parse_sources(bool_0)
        var_9 = inventory_manager_1.get_hosts(inventory_manager_1)
        var_10 = inventory_manager_1.get_hosts(str_2)
        inventory_manager_2 = module_0.InventoryManager(dict_0, list_0, str_3)
        bytes_0 = b''
        var_11 = inventory_manager_1.subset(bytes_0)
        var_12 = inventory_manager_2.get_groups_dict()
        str_4 = ' solely of upper- and lower-case letters, digits, underscores, and hyphens'
        var_13 = inventory_manager_1.parse_sources()
        inventory_manager_3 = module_0.InventoryManager(set_0, str_4)
        var_14 = inventory_manager_1.reconcile_inventory()
        var_15 = inventory_manager_1.restrict_to_hosts(bytes_0)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = 'Ji@9&5\x0c\x0bl\nK\n#$$'
        inventory_manager_0 = module_0.InventoryManager(str_0)
        var_0 = inventory_manager_0.refresh_inventory()
        str_1 = None
        inventory_manager_1 = module_0.InventoryManager(str_1, str_1, str_1)
        float_0 = -679.0
        set_0 = {inventory_manager_0, float_0, float_0, str_1, str_1}
        str_2 = ':v,~{'
        var_1 = inventory_manager_1.parse_source(str_2)
        var_2 = inventory_manager_1.subset(var_1)
        var_3 = inventory_manager_1.list_hosts()
        var_4 = inventory_manager_1.refresh_inventory()
        var_5 = inventory_manager_1.get_groups_dict()
        var_6 = inventory_manager_1.list_hosts()
        tuple_0 = (str_1,)
        var_7 = inventory_manager_1.reconcile_inventory()
        var_8 = inventory_manager_1.refresh_inventory()
        var_9 = inventory_manager_1.subset(str_2)
        bool_0 = True
        var_10 = inventory_manager_1.parse_source(bool_0, tuple_0)
        var_11 = inventory_manager_1.parse_sources(bool_0)
        var_12 = inventory_manager_1.get_hosts(inventory_manager_1)
        var_13 = inventory_manager_1.get_hosts(str_1)
        var_14 = inventory_manager_1.parse_source(str_0, tuple_0)
        bytes_0 = b'\x9a\xba'
        var_15 = inventory_manager_1.subset(bytes_0)
        var_16 = inventory_manager_1.get_groups_dict()
        str_3 = ' solly ofupper-and lower-case letters, digits, underscores and hyphens'
        var_17 = inventory_manager_1.parse_sources()
        inventory_manager_2 = module_0.InventoryManager(set_0, str_3)
        var_18 = inventory_manager_2.reconcile_inventory()
        var_19 = inventory_manager_2.restrict_to_hosts(float_0)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = 'Ji@9&5\x0c\x0bl\nK\n#$$'
        inventory_manager_0 = module_0.InventoryManager(str_0)
        var_0 = inventory_manager_0.get_host(str_0)
        str_1 = None
        inventory_manager_1 = module_0.InventoryManager(str_1, str_1, str_1)
        float_0 = -679.0
        set_0 = {inventory_manager_0, float_0, float_0, str_1, str_1}
        str_2 = ':v,~'
        var_1 = inventory_manager_1.parse_source(str_2)
        var_2 = inventory_manager_1.subset(var_1)
        var_3 = inventory_manager_1.list_hosts()
        var_4 = inventory_manager_1.refresh_inventory()
        var_5 = inventory_manager_1.get_groups_dict()
        var_6 = inventory_manager_1.list_hosts()
        tuple_0 = (str_1,)
        var_7 = inventory_manager_1.reconcile_inventory()
        var_8 = inventory_manager_1.refresh_inventory()
        var_9 = inventory_manager_1.subset(str_2)
        bool_0 = True
        var_10 = inventory_manager_1.parse_source(bool_0, tuple_0)
        var_11 = inventory_manager_1.parse_sources(bool_0)
        var_12 = inventory_manager_1.get_hosts(inventory_manager_1)
        var_13 = inventory_manager_1.get_hosts(str_1)
        var_14 = inventory_manager_1.parse_source(str_0, tuple_0)
        bytes_0 = b'\x9a\xba'
        var_15 = inventory_manager_1.subset(bytes_0)
        var_16 = inventory_manager_1.get_groups_dict()
        str_3 = ' solly ofupper-and lower-case letters, digits, underscores and hyphens'
        var_17 = inventory_manager_1.parse_sources()
        inventory_manager_2 = module_0.InventoryManager(set_0, str_3)
        var_18 = inventory_manager_2.reconcile_inventory()
        var_19 = inventory_manager_2.restrict_to_hosts(float_0)
    except BaseException:
        pass

def test_case_15():
    try:
        bool_0 = False
        str_0 = '&)w7M/m\x0c=x;LZp'
        list_0 = []
        dict_0 = {str_0: bool_0, str_0: bool_0, bool_0: bool_0}
        str_1 = 'Nd5aC\rIelcL+iz]jlp%\x0b'
        inventory_manager_0 = module_0.InventoryManager(str_1)
        tuple_0 = ()
        inventory_manager_1 = module_0.InventoryManager(tuple_0)
        var_0 = inventory_manager_1.parse_sources()
        var_1 = inventory_manager_0.remove_restriction()
        inventory_manager_2 = module_0.InventoryManager(bool_0)
        var_2 = inventory_manager_2.reconcile_inventory()
        inventory_manager_3 = module_0.InventoryManager(dict_0)
        var_3 = inventory_manager_3.restrict_to_hosts(list_0)
    except BaseException:
        pass