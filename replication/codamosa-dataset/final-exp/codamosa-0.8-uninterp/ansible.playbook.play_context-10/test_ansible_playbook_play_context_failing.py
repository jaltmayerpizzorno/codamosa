# Automatically generated by Pynguin.
import ansible.playbook.play_context as module_0

def test_case_0():
    try:
        str_0 = 'd\nLxRYevkc'
        play_context_0 = module_0.PlayContext(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'goQySA}<MRu6K)+U'
        tuple_0 = (str_0,)
        dict_0 = {tuple_0: str_0, tuple_0: tuple_0}
        play_context_0 = module_0.PlayContext()
        var_0 = play_context_0.set_attributes_from_plugin(dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        play_context_0 = module_0.PlayContext()
        int_0 = 1981
        var_0 = play_context_0.set_task_and_variable_override(play_context_0, int_0, int_0)
    except BaseException:
        pass

def test_case_3():
    try:
        play_context_0 = module_0.PlayContext()
        tuple_0 = (play_context_0,)
        play_context_1 = module_0.PlayContext()
        dict_0 = {play_context_1: play_context_1}
        play_context_2 = module_0.PlayContext(play_context_1, dict_0)
        var_0 = play_context_2.set_become_plugin(tuple_0)
        play_context_3 = module_0.PlayContext(tuple_0)
    except BaseException:
        pass

def test_case_4():
    try:
        play_context_0 = module_0.PlayContext()
        var_0 = play_context_0.update_vars(play_context_0)
    except BaseException:
        pass

def test_case_5():
    try:
        dict_0 = {}
        play_context_0 = module_0.PlayContext()
        var_0 = play_context_0.update_vars(dict_0)
        var_1 = play_context_0.set_attributes_from_cli()
        int_0 = -23
        play_context_1 = module_0.PlayContext(int_0)
    except BaseException:
        pass

def test_case_6():
    try:
        list_0 = []
        bool_0 = False
        play_context_0 = module_0.PlayContext(bool_0)
        var_0 = play_context_0.update_vars(list_0)
    except BaseException:
        pass

def test_case_7():
    try:
        int_0 = 1197
        float_0 = 512.0
        play_context_0 = module_0.PlayContext(int_0, float_0)
    except BaseException:
        pass

def test_case_8():
    try:
        dict_0 = {}
        play_context_0 = module_0.PlayContext()
        var_0 = play_context_0.update_vars(dict_0)
        var_1 = play_context_0.update_vars(dict_0)
        var_2 = play_context_0.set_attributes_from_cli()
        bool_0 = None
        str_0 = 'j?/[,e '
        bool_1 = True
        var_3 = play_context_0.set_task_and_variable_override(bool_0, str_0, bool_1)
    except BaseException:
        pass