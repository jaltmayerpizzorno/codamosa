# Automatically generated by Pynguin.
import ansible.modules.rpm_key as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'i.,Fp\t9F4'
    var_0 = module_0.is_pubkey(str_0)

def test_case_2():
    float_0 = -1765.854044
    tuple_0 = (float_0,)
    var_0 = module_0.main()
    bytes_0 = b'^%\xa7\x0eZ}\x0bJ"\xb8\x11\x0c\xe2\xa3o['
    str_0 = '5_F2[c['
    rpm_key_0 = module_0.RpmKey(str_0)
    var_1 = rpm_key_0.execute_command(bytes_0)
    bool_0 = False
    list_0 = [tuple_0, float_0]
    rpm_key_1 = module_0.RpmKey(list_0)
    var_2 = rpm_key_1.drop_key(bool_0)
    rpm_key_2 = module_0.RpmKey(tuple_0)