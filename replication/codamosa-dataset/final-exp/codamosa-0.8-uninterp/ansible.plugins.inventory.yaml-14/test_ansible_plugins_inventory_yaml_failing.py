# Automatically generated by Pynguin.
import ansible.plugins.inventory.yaml as module_0

def test_case_0():
    try:
        inventory_module_0 = module_0.InventoryModule()
        str_0 = 'xusr'
        float_0 = 95.6195
        dict_0 = {float_0: str_0, inventory_module_0: float_0, str_0: float_0, str_0: inventory_module_0}
        var_0 = inventory_module_0.parse(str_0, dict_0, dict_0, str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = False
        inventory_module_0 = module_0.InventoryModule()
        str_0 = "{bc=YGh=^',\r_g(NH$)"
        str_1 = 'Repo: %s/%s'
        float_0 = 408.61
        var_0 = inventory_module_0.parse(str_0, bool_0, str_1, float_0)
    except BaseException:
        pass