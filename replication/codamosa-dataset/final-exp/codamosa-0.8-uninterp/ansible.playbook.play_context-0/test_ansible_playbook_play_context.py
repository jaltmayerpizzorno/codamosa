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
    play_context_0 = None
    play_context_1 = module_0.PlayContext()
    var_0 = play_context_1.set_become_plugin(play_context_0)

def test_case_4():
    var_0 = dict()
    play_context_0 = module_0.PlayContext(var_0, var_0, var_0)
    var_1 = play_context_0.update_vars(var_0)