# Automatically generated by Pynguin.
import ansible.cli.inventory as module_0

def test_case_0():
    pass

def test_case_1():
    bytes_0 = b'\xde@\xaf`&yp\xe4Sje\x1d\na\xf9\xfd\xfa-Z'
    inventory_c_l_i_0 = module_0.InventoryCLI(bytes_0)

def test_case_2():
    str_0 = '3x45`TP0t|(VKkz<zbd5'
    inventory_c_l_i_0 = module_0.InventoryCLI(str_0)
    var_0 = inventory_c_l_i_0.run()
    str_1 = 'SN=M_k(OH8x2\x0b"{>0,~'
    list_0 = [str_1, str_1]
    inventory_c_l_i_1 = module_0.InventoryCLI(list_0)
    var_1 = inventory_c_l_i_1.init_parser()
    str_2 = 'r0WF'
    inventory_c_l_i_2 = module_0.InventoryCLI(str_2)
    var_2 = inventory_c_l_i_2.post_process_args(str_1)