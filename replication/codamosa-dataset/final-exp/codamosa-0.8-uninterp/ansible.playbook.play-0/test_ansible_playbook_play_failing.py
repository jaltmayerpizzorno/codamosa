# Automatically generated by Pynguin.
import ansible.playbook.play as module_0

def test_case_0():
    try:
        play_0 = module_0.Play()
        var_0 = play_0.compile_roles_handlers()
        var_1 = play_0.copy()
        var_2 = play_0.compile()
        tuple_0 = None
        set_0 = set()
        var_3 = play_0.get_vars()
        int_0 = False
        str_0 = 'Clear the existing server response cache.'
        var_4 = play_0.get_tasks()
        var_5 = play_0.load(tuple_0, set_0, int_0, str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        play_0 = module_0.Play()
        var_0 = play_0.preprocess_data(play_0)
    except BaseException:
        pass