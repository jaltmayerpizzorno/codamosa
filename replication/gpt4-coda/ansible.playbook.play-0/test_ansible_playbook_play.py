# Automatically generated by Pynguin.
import ansible.playbook.play as module_0

def test_case_0():
    play_0 = module_0.Play()

def test_case_1():
    play_0 = module_0.Play()
    var_0 = play_0.__repr__()

def test_case_2():
    dict_0 = {}
    play_0 = module_0.Play()
    var_0 = play_0.load(dict_0, dict_0)
    var_1 = play_0.get_vars_files()
    play_1 = module_0.Play()

def test_case_3():
    play_0 = module_0.Play()
    var_0 = play_0.compile()

def test_case_4():
    play_0 = module_0.Play()
    var_0 = play_0.compile_roles_handlers()

def test_case_5():
    play_0 = module_0.Play()
    var_0 = play_0.get_vars()

def test_case_6():
    play_0 = module_0.Play()
    var_0 = play_0.get_vars_files()

def test_case_7():
    play_0 = module_0.Play()
    var_0 = play_0.get_roles()
    play_1 = module_0.Play()
    var_1 = play_1.get_tasks()
    var_2 = play_1.get_handlers()
    play_2 = module_0.Play()
    var_3 = play_2.compile_roles_handlers()
    var_4 = play_2.compile()

def test_case_8():
    play_0 = module_0.Play()
    var_0 = play_0.get_roles()

def test_case_9():
    play_0 = module_0.Play()
    var_0 = play_0.get_tasks()

def test_case_10():
    play_0 = module_0.Play()
    var_0 = play_0.serialize()

def test_case_11():
    play_0 = module_0.Play()
    dict_0 = {play_0: play_0}
    dict_1 = {play_0: dict_0, play_0: dict_0}
    play_1 = module_0.Play()
    var_0 = play_1.deserialize(dict_1)

def test_case_12():
    play_0 = module_0.Play()
    var_0 = play_0.copy()
    play_1 = module_0.Play()
    var_1 = play_1.get_vars()
    var_2 = play_1.__repr__()

def test_case_13():
    play_0 = module_0.Play()
    str_0 = 'action2'
    var_0 = play_0.serialize()
    var_1 = play_0.deserialize(var_0)
    var_2 = len(str_0)

def test_case_14():
    str_0 = 'tasks'
    str_1 = 'debug'
    str_2 = 'sg'
    str_3 = 'Hello world'
    play_0 = module_0.Play()
    str_4 = 'user'
    str_5 = 'ansible'
    str_6 = {str_2: str_3}
    str_7 = {str_1: str_6}
    str_8 = [str_7]
    str_9 = {str_4: str_5, str_0: str_8}
    var_0 = play_0.preprocess_data(str_9)