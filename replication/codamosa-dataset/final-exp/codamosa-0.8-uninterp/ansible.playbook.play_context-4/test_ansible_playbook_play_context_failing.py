# Automatically generated by Pynguin.
import ansible.playbook.play_context as module_0

def test_case_0():
    try:
        str_0 = 'ansible-vault create can take only one filename argument'
        play_context_0 = module_0.PlayContext(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'\xd6/\xdb\xac\xa7d\xde\xcdv\xf3\xb9'
        tuple_0 = ()
        play_context_0 = module_0.PlayContext(tuple_0)
        play_context_1 = module_0.PlayContext()
        var_0 = play_context_1.set_attributes_from_plugin(bytes_0)
    except BaseException:
        pass

def test_case_2():
    try:
        set_0 = set()
        play_context_0 = module_0.PlayContext()
        var_0 = play_context_0.set_task_and_variable_override(set_0, set_0, set_0)
    except BaseException:
        pass

def test_case_3():
    try:
        play_context_0 = module_0.PlayContext()
        var_0 = play_context_0.update_vars(play_context_0)
    except BaseException:
        pass

def test_case_4():
    try:
        float_0 = 1.5
        float_1 = -1982.795271
        play_context_0 = module_0.PlayContext(float_0, float_1)
    except BaseException:
        pass

def test_case_5():
    try:
        bytes_0 = b'H\xecO\x86=p\x80J|\x1b\x8b\x89+'
        play_context_0 = module_0.PlayContext()
        list_0 = []
        var_0 = play_context_0.set_become_plugin(bytes_0)
        int_0 = 3726
        var_1 = play_context_0.set_task_and_variable_override(play_context_0, list_0, int_0)
    except BaseException:
        pass