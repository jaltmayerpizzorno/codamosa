# Automatically generated by Pynguin.
import ansible.modules.rpm_key as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = '1$t~JS'
    var_0 = module_0.is_pubkey(str_0)

def test_case_2():
    int_0 = 3666
    var_0 = module_0.main()
    rpm_key_0 = module_0.RpmKey(int_0)
    rpm_key_1 = module_0.RpmKey(rpm_key_0)
    var_1 = rpm_key_1.normalize_keyid(int_0)
    int_1 = None
    dict_0 = {int_0: int_1, int_0: int_0, int_0: int_1}
    bool_0 = None
    set_0 = {bool_0}
    rpm_key_2 = module_0.RpmKey(set_0)
    int_2 = True
    var_2 = rpm_key_0.getfingerprint(int_2)
    var_3 = rpm_key_2.normalize_keyid(dict_0)
    float_0 = -1800.5
    var_4 = rpm_key_2.getkeyid(float_0)
    tuple_0 = (float_0,)
    bytes_0 = b'm'
    var_5 = rpm_key_2.drop_key(bytes_0)
    var_6 = rpm_key_2.execute_command(tuple_0)
    float_1 = None
    var_7 = rpm_key_2.fetch_key(float_1)