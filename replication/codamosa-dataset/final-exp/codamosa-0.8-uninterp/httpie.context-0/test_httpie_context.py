# Automatically generated by Pynguin.
import httpie.context as module_0
import httpie.config as module_1

def test_case_0():
    pass

def test_case_1():
    environment_0 = module_0.Environment()

def test_case_2():
    environment_0 = module_0.Environment()
    var_0 = environment_0.__str__()

def test_case_3():
    environment_0 = module_0.Environment()
    var_0 = environment_0.__repr__()

def test_case_4():
    bool_0 = True
    environment_0 = module_0.Environment()
    var_0 = environment_0.log_error(bool_0)

def test_case_5():
    environment_0 = module_0.Environment()
    var_0 = environment_0.__repr__()
    list_0 = [environment_0, environment_0, environment_0, environment_0]
    environment_1 = module_0.Environment(list_0)
    environment_2 = module_0.Environment()
    list_1 = None
    var_1 = environment_0.__repr__()
    var_2 = environment_1.log_error(list_1)
    var_3 = environment_2.__repr__()

def test_case_6():
    int_0 = 627
    environment_0 = module_0.Environment(int_0)
    var_0 = environment_0.__repr__()
    config_0 = module_1.Config()
    list_0 = [config_0, config_0, config_0, config_0]
    var_1 = config_0.save(list_0)
    environment_1 = module_0.Environment()
    var_2 = environment_1.__str__()
    var_3 = environment_0.__str__()
    var_4 = environment_1.log_error(config_0)
    var_5 = config_0.load()