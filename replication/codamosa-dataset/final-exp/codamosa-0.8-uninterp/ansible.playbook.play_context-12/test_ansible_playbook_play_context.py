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
    bytes_0 = None
    play_context_0 = module_0.PlayContext()
    dict_0 = {}
    var_0 = play_context_0.set_become_plugin(dict_0)
    dict_1 = {bytes_0: bytes_0, bytes_0: play_context_0, bytes_0: bytes_0}
    var_1 = play_context_0.update_vars(dict_1)

def test_case_4():
    play_context_0 = module_0.PlayContext()
    dict_0 = {}
    var_0 = play_context_0.update_vars(dict_0)

def test_case_5():
    bytes_0 = None
    play_context_0 = module_0.PlayContext()
    dict_0 = {bytes_0: play_context_0, bytes_0: play_context_0, play_context_0: bytes_0, play_context_0: bytes_0, bytes_0: bytes_0}
    var_0 = play_context_0.set_attributes_from_play(play_context_0)
    var_1 = play_context_0.update_vars(dict_0)
    var_2 = play_context_0.set_attributes_from_cli()
    var_3 = play_context_0.update_vars(dict_0)
    var_4 = play_context_0.set_attributes_from_cli()