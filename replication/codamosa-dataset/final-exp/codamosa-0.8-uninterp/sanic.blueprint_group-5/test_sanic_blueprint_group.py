# Automatically generated by Pynguin.
import sanic.blueprint_group as module_0
import sanic.blueprints as module_1

def test_case_0():
    pass

def test_case_1():
    blueprint_group_0 = module_0.BlueprintGroup()

def test_case_2():
    blueprint_group_0 = module_0.BlueprintGroup()
    var_0 = blueprint_group_0.__iter__()

def test_case_3():
    blueprint_group_0 = module_0.BlueprintGroup()
    int_0 = blueprint_group_0.__len__()

def test_case_4():
    blueprint_group_0 = module_0.BlueprintGroup()
    var_0 = blueprint_group_0.middleware()
    list_0 = [var_0, blueprint_group_0, blueprint_group_0, blueprint_group_0]
    str_0 = '4q9^ kx6;T47e]q'
    blueprint_group_1 = module_0.BlueprintGroup()
    var_1 = blueprint_group_1.middleware(*list_0)
    blueprint_0 = module_1.Blueprint(str_0)
    int_0 = 1388
    blueprint_group_0.insert(int_0, blueprint_0)

def test_case_5():
    blueprint_group_0 = module_0.BlueprintGroup()
    var_0 = blueprint_group_0.middleware()

def test_case_6():
    str_0 = '^7'
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    list_0 = [str_0, str_0, str_0, dict_0]
    blueprint_group_0 = module_0.BlueprintGroup()
    var_0 = blueprint_group_0.middleware(*list_0)

def test_case_7():
    blueprint_group_0 = module_0.BlueprintGroup()
    var_0 = blueprint_group_0.middleware()
    list_0 = [var_0, blueprint_group_0, blueprint_group_0, blueprint_group_0]
    str_0 = '/706e2bYw z'
    list_1 = [str_0, str_0, var_0, var_0]
    blueprint_group_1 = module_0.BlueprintGroup(str_0, list_1)
    var_1 = blueprint_group_1.middleware(*list_0)

def test_case_8():
    str_0 = '/bp1'
    blueprint_group_0 = module_0.BlueprintGroup(str_0)
    var_0 = blueprint_group_0.url_prefix
    str_1 = 'v1'
    blueprint_group_1 = module_0.BlueprintGroup(str_1)
    var_1 = blueprint_group_1.version
    bool_0 = True
    blueprint_group_2 = module_0.BlueprintGroup(bool_0)
    var_2 = blueprint_group_2.strict_slashes
    blueprint_group_3 = module_0.BlueprintGroup()
    var_3 = blueprint_group_3.strict_slashes