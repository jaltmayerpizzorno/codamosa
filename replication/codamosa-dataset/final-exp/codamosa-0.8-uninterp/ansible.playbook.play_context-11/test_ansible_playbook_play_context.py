# Automatically generated by Pynguin.
import ansible.playbook.play_context as module_0

def test_case_0():
    pass

def test_case_1():
    play_context_0 = module_0.PlayContext()

def test_case_2():
    play_context_0 = module_0.PlayContext()
    var_0 = play_context_0.set_attributes_from_cli()

def test_case_3():
    str_0 = 'B~E\t[%j4=K@wI'
    play_context_0 = module_0.PlayContext()
    var_0 = play_context_0.set_become_plugin(str_0)

def test_case_4():
    str_0 = 'persisteTt'
    play_context_0 = module_0.PlayContext()
    dict_0 = {play_context_0: play_context_0, str_0: str_0}
    var_0 = play_context_0.update_vars(dict_0)

def test_case_5():
    play_context_0 = module_0.PlayContext()
    play_context_1 = module_0.PlayContext()
    var_0 = play_context_0.set_attributes_from_cli()
    str_0 = '6o@cY'
    list_0 = None
    float_0 = 2319.262
    tuple_0 = (float_0,)
    tuple_1 = ()
    dict_0 = {list_0: play_context_1, play_context_0: tuple_0, str_0: play_context_1, tuple_1: str_0}
    var_1 = play_context_0.update_vars(dict_0)
    set_0 = set()
    play_context_2 = module_0.PlayContext(set_0)
    bytes_0 = b'\t\xe8\xfeLZ\x00f\xb0V\x94d<\xacJ'
    var_2 = play_context_1.set_become_plugin(bytes_0)
    var_3 = play_context_2.set_attributes_from_play(play_context_2)
    var_4 = play_context_2.update_vars(dict_0)