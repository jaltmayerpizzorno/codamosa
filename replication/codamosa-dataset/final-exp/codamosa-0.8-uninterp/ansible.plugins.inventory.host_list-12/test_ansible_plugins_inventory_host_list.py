# Automatically generated by Pynguin.
import ansible.plugins.inventory.host_list as module_0

def test_case_0():
    inventory_module_0 = module_0.InventoryModule()
    inventory_module_1 = module_0.InventoryModule()

def test_case_1():
    inventory_module_0 = module_0.InventoryModule()
    str_0 = 'host1,host2'
    var_0 = inventory_module_0.verify_file(str_0)
    str_1 = '/etc/hosts'
    var_1 = inventory_module_0.verify_file(str_1)
    str_2 = 'subdir/hosts'
    var_2 = inventory_module_0.verify_file(str_2)

def test_case_2():
    inventory_module_0 = module_0.InventoryModule()
    list_0 = []
    var_0 = inventory_module_0.verify_file(list_0)

def test_case_3():
    inventory_module_0 = module_0.InventoryModule()
    str_0 = "=7_'VxH/u?e##bB_FJ"
    bool_0 = True
    str_1 = '\n    Transform a key, either taken from a known_host file or provided by the\n    user, into a normalized form.\n    The host part (which might include multiple hostnames or be hashed) gets\n    replaced by the provided host. Also, any spurious information gets removed\n    from the end (like the username@host tag usually present in hostkeys, but\n    absent in known_hosts files)\n    '
    float_0 = 1223.3
    inventory_module_1 = module_0.InventoryModule()
    float_1 = 274.60328
    str_2 = 'JM(0'
    dict_0 = None
    tuple_0 = (float_1, str_2, dict_0, inventory_module_0)
    tuple_1 = (float_0, inventory_module_0, tuple_0)
    var_0 = inventory_module_0.verify_file(tuple_1)
    inventory_module_2 = module_0.InventoryModule()
    var_1 = inventory_module_2.verify_file(str_1)
    dict_1 = {var_1: str_1, bool_0: str_0, str_1: str_1}
    var_2 = inventory_module_0.verify_file(dict_1)
    inventory_module_3 = module_0.InventoryModule()
    list_0 = [str_0]
    tuple_2 = ()
    str_3 = ''
    var_3 = inventory_module_3.parse(list_0, tuple_2, str_3, list_0)