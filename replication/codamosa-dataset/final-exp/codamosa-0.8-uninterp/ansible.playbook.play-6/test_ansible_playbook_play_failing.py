# Automatically generated by Pynguin.
import ansible.playbook.play as module_0

def test_case_0():
    try:
        play_0 = module_0.Play()
        var_0 = play_0.get_handlers()
        bytes_0 = b'\xcb\xf1\x14\xb2U\xf3d\x16\xa4q\xba'
        float_0 = -1635.0984
        bool_0 = True
        var_1 = play_0.load(bytes_0, float_0, bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        play_0 = module_0.Play()
        var_0 = play_0.preprocess_data(play_0)
    except BaseException:
        pass

def test_case_2():
    try:
        play_0 = module_0.Play()
        str_0 = 'hosts'
        str_1 = 'name'
        str_2 = 'roles'
        str_3 = 'master'
        str_4 = 'one'
        str_5 = 'role'
        str_6 = '_role_name'
        str_7 = 'kkjjj'
        str_8 = {str_6: str_7}
        str_9 = {str_5: str_8}
        str_10 = [str_9, str_0]
        str_11 = {str_0: str_3, str_1: str_4, str_2: str_10}
        var_0 = play_0.deserialize(str_11)
    except BaseException:
        pass

def test_case_3():
    try:
        play_0 = module_0.Play()
        var_0 = play_0.get_vars_files()
        play_1 = module_0.Play()
        var_1 = play_1.compile()
        dict_0 = {}
        bytes_0 = b'\xd2'
        tuple_0 = (dict_0, bytes_0)
        var_2 = play_1.deserialize(tuple_0)
    except BaseException:
        pass

def test_case_4():
    try:
        play_0 = module_0.Play()
        var_0 = play_0.get_tasks()
        var_1 = play_0.compile()
        play_1 = module_0.Play()
        str_0 = 'socket path %s does not exist or cannot be found. See Troubleshooting socket path issues in the Network Debug and Troubleshooting Guide'
        str_1 = '\n?3Dm>U*]8KSJp9'
        bytes_0 = b'\x8d\xe6\x88\xba\x04M\xda\x120H\xf7\xe2\xeeI\x8d\xb4\x8d\xbdr='
        int_0 = -663
        var_2 = play_1.load(str_0, str_1, bytes_0, int_0)
    except BaseException:
        pass