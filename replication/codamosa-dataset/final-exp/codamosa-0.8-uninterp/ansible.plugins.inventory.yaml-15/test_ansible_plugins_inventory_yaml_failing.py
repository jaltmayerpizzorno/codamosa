# Automatically generated by Pynguin.
import ansible.plugins.inventory.yaml as module_0

def test_case_0():
    try:
        str_0 = ' s=GXeLsg@#TY'
        bytes_0 = b'\xcf@\xfdC\xf3\xf5E\xf2D\x1c\x86U'
        set_0 = {bytes_0, str_0}
        inventory_module_0 = module_0.InventoryModule()
        var_0 = inventory_module_0.parse(str_0, bytes_0, set_0)
    except BaseException:
        pass

def test_case_1():
    try:
        set_0 = set()
        inventory_module_0 = module_0.InventoryModule()
        var_0 = inventory_module_0.verify_file(set_0)
        bytes_0 = None
        str_0 = '\n    name: debug\n    short_description: Executes tasks in interactive debug session.\n    description:\n        - Task execution is \'linear\' but controlled by an interactive debug session.\n    version_added: "2.1"\n    author: Kishin Yagami (!UNKNOWN)\n'
        var_1 = inventory_module_0.parse(set_0, bytes_0, str_0, set_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'test_InventoryModule_verify_file.test'
        inventory_module_0 = module_0.InventoryModule()
        var_0 = inventory_module_0.verify_file(str_0)
    except BaseException:
        pass