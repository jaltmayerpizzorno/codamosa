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
    int_0 = 1000
    play_context_0 = module_0.PlayContext()
    var_0 = play_context_0.set_become_plugin(int_0)

def test_case_4():
    play_context_0 = module_0.PlayContext()
    var_0 = play_context_0.set_attributes_from_cli()
    int_0 = -197
    play_context_1 = module_0.PlayContext()
    ansible_error_0 = None
    dict_0 = {var_0: play_context_1, int_0: play_context_0, play_context_0: ansible_error_0}
    var_1 = play_context_1.update_vars(dict_0)
    str_0 = 'smart'
    var_2 = play_context_0.set_become_plugin(str_0)