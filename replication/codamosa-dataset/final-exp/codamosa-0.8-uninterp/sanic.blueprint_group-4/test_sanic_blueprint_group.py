# Automatically generated by Pynguin.
import sanic.blueprint_group as module_0
import sanic.blueprints as module_1

def test_case_0():
    pass

def test_case_1():
    blueprint_group_0 = module_0.BlueprintGroup()

def test_case_2():
    str_0 = '/UCe/T\x0c-<'
    blueprint_0 = module_1.Blueprint(str_0)
    str_1 = 't<9.L<+ZXYNU!Sf'
    blueprint_group_0 = module_0.BlueprintGroup(str_1)
    blueprint_group_0.append(blueprint_0)
    blueprint_group_1 = module_0.BlueprintGroup()

def test_case_3():
    str_0 = '8vJ]6A'
    blueprint_group_0 = module_0.BlueprintGroup(str_0)
    var_0 = blueprint_group_0.__iter__()

def test_case_4():
    str_0 = 'J\x0buwbXvC'
    list_0 = [str_0]
    blueprint_0 = module_1.Blueprint(str_0, str_0, str_0)
    blueprint_group_0 = module_0.BlueprintGroup(blueprint_0, blueprint_0)
    int_0 = blueprint_group_0.__len__()
    blueprint_group_1 = module_0.BlueprintGroup()
    var_0 = blueprint_group_1.middleware(*list_0)
    blueprint_group_2 = module_0.BlueprintGroup(str_0)
    list_1 = []
    var_1 = blueprint_group_2.middleware(*list_1)
    int_1 = blueprint_group_2.__len__()

def test_case_5():
    int_0 = -455
    list_0 = [int_0, int_0, int_0]
    str_0 = 'YM;^UP e)t'
    set_0 = {str_0, str_0}
    blueprint_group_0 = module_0.BlueprintGroup(str_0, set_0)
    var_0 = blueprint_group_0.middleware(*list_0)

def test_case_6():
    str_0 = 'X!c$D8\\"LI6x=c'
    int_0 = 504
    list_0 = [int_0]
    blueprint_group_0 = module_0.BlueprintGroup(list_0)
    blueprint_0 = module_1.Blueprint(str_0, str_0, int_0, blueprint_group_0)
    blueprint_group_1 = module_0.BlueprintGroup()
    blueprint_group_1.append(blueprint_0)

def test_case_7():
    str_0 = '@~*Gj`~Ex\x0ch2'
    blueprint_0 = module_1.Blueprint(str_0)
    blueprint_group_0 = module_0.BlueprintGroup(blueprint_0)
    var_0 = blueprint_group_0.middleware()
    dict_0 = {}
    blueprint_group_1 = module_0.BlueprintGroup()
    blueprint_group_2 = module_0.BlueprintGroup()
    var_1 = blueprint_group_2.middleware(**dict_0)
    var_2 = blueprint_group_2.__iter__()
    list_0 = [var_0]
    var_3 = blueprint_group_0.middleware(*list_0)
    int_0 = 650
    blueprint_group_3 = module_0.BlueprintGroup(dict_0, int_0)