# Automatically generated by Pynguin.
import ansible.playbook.play_context as module_0

def test_case_0():
    try:
        bool_0 = True
        play_context_0 = module_0.PlayContext(bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        play_context_0 = module_0.PlayContext()
        var_0 = play_context_0.set_attributes_from_cli()
        float_0 = 862.823868
        var_1 = play_context_0.set_become_plugin(float_0)
        var_2 = play_context_0.set_attributes_from_cli()
        str_0 = 'yS'
        var_3 = play_context_0.set_attributes_from_plugin(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        play_context_0 = module_0.PlayContext()
        bytes_0 = b'\xacB\x11\xb9{\xe7\xa4\xb7+\xa8V{|j\xda\xc7\xef\xa3'
        bool_0 = True
        float_0 = 1255.94
        var_0 = play_context_0.set_task_and_variable_override(bytes_0, bool_0, float_0)
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
        str_0 = 'persistent'
        play_context_0 = module_0.PlayContext()
        var_0 = play_context_0.update_vars(str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        play_context_0 = module_0.PlayContext()
        float_0 = -408.4296917955501
        play_context_1 = module_0.PlayContext(float_0, play_context_0)
    except BaseException:
        pass

def test_case_6():
    try:
        play_context_0 = module_0.PlayContext()
        var_0 = play_context_0.set_attributes_from_cli()
        str_0 = '&G@Nn'
        dict_0 = {}
        var_1 = play_context_0.set_task_and_variable_override(play_context_0, str_0, dict_0)
    except BaseException:
        pass