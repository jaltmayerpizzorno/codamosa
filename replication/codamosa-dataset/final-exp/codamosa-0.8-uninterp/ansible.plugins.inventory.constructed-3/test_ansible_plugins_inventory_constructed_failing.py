# Automatically generated by Pynguin.
import ansible.plugins.inventory.constructed as module_0

def test_case_0():
    try:
        str_0 = 'IthL(S\x0b(|\\f>BBqAVv'
        bytes_0 = b'V\x96\xb5\x02\xc0'
        int_0 = 704
        inventory_module_0 = module_0.InventoryModule()
        var_0 = inventory_module_0.get_all_host_vars(str_0, bytes_0, int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'O\x86\xb7\x00J\xa2'
        str_0 = 'install_python_apt'
        bytes_1 = b'\x1d\x8b3\xa8:\x0c\x1d'
        tuple_0 = (bytes_1,)
        inventory_module_0 = module_0.InventoryModule()
        var_0 = inventory_module_0.host_vars(bytes_0, str_0, tuple_0)
    except BaseException:
        pass

def test_case_2():
    try:
        inventory_module_0 = module_0.InventoryModule()
        str_0 = '^'
        str_1 = "v!22W1&s\\);U7'V"
        dict_0 = {inventory_module_0: inventory_module_0, str_0: str_0}
        var_0 = inventory_module_0.parse(str_0, str_1, dict_0)
    except BaseException:
        pass

def test_case_3():
    try:
        float_0 = 4072.248
        str_0 = 'p\x0c'
        int_0 = 3442
        tuple_0 = ()
        set_0 = {str_0, str_0, float_0}
        inventory_module_0 = module_0.InventoryModule()
        var_0 = inventory_module_0.parse(int_0, tuple_0, set_0)
    except BaseException:
        pass