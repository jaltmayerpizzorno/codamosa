# Automatically generated by Pynguin.
import ansible.playbook.play as module_0

def test_case_0():
    try:
        play_0 = module_0.Play()
        var_0 = play_0.get_roles()
        play_1 = module_0.Play()
        var_1 = play_1.get_handlers()
        bool_0 = True
        str_0 = 'fCE'
        var_2 = play_1.load(bool_0, str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'LDn-@s\r'
        play_0 = module_0.Play()
        var_0 = play_0.preprocess_data(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = False
        play_0 = module_0.Play()
        var_0 = play_0.deserialize(bool_0)
    except BaseException:
        pass

def test_case_3():
    try:
        play_0 = module_0.Play()
        var_0 = play_0.get_name()
        var_1 = play_0.get_vars()
        play_1 = module_0.Play()
        var_2 = play_1.get_name()
        var_3 = play_0.get_roles()
        var_4 = play_1.get_handlers()
        play_2 = module_0.Play()
        play_3 = module_0.Play()
        var_5 = play_3.compile()
        var_6 = play_2.compile_roles_handlers()
        var_7 = play_1.compile()
        var_8 = play_1.get_vars_files()
        play_4 = module_0.Play()
        var_9 = play_4.compile_roles_handlers()
        var_10 = play_4.copy()
        var_11 = play_1.copy()
        var_12 = play_0.get_vars()
        play_5 = module_0.Play()
        str_0 = 'listtags'
        tuple_0 = None
        bytes_0 = b'\xbd\xc1p'
        str_1 = 'Z1,"V$CBJB5bw%PO9n{'
        var_13 = play_3.load(str_0, tuple_0, bytes_0, str_1)
    except BaseException:
        pass