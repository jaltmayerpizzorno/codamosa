# Automatically generated by Pynguin.
import ansible.playbook.included_file as module_0

def test_case_0():
    pass

def test_case_1():
    bool_0 = True
    bytes_0 = b'\xf6\x9c]({\xba8\xd9\x93\xe6\xe8'
    set_0 = {bytes_0}
    included_file_0 = module_0.IncludedFile(bool_0, bytes_0, set_0, bytes_0)
    var_0 = included_file_0.__repr__()

def test_case_2():
    int_0 = 1666
    list_0 = []
    bytes_0 = b'\x1e2\xa3\x9b'
    int_1 = 401
    int_2 = None
    dict_0 = {int_1: int_2}
    str_0 = '0qA[\n~uUxA'
    float_0 = 0.0001
    bool_0 = False
    tuple_0 = (dict_0, bytes_0, float_0)
    included_file_0 = module_0.IncludedFile(dict_0, str_0, float_0, bool_0, tuple_0)
    included_file_1 = module_0.IncludedFile(list_0, bytes_0, int_1, included_file_0)
    var_0 = included_file_1.add_host(int_0)

def test_case_3():
    str_0 = '\n    Transform a key, either taken from a known_host file or provided by the\n    user, into a normalized form.\n    The host part (which might include multiple hostnames or be hashed) gets\n    replaced by the provided host. Also, any spurious information gets removed\n    from the end (like the username@host tag usually present in hostkeys, but\n    absent in known_hosts files)\n    '
    dict_0 = {}
    list_0 = []
    str_1 = 'S\nY!_'
    bool_0 = True
    tuple_0 = (str_1, str_0, bool_0, dict_0)
    str_2 = '\tgme2e@v@'
    bytes_0 = b''
    int_0 = 218
    included_file_0 = module_0.IncludedFile(str_2, bytes_0, dict_0, int_0, tuple_0)
    str_3 = ''
    included_file_1 = module_0.IncludedFile(list_0, int_0, list_0, bool_0, str_3)
    var_0 = included_file_1.__eq__(included_file_0)