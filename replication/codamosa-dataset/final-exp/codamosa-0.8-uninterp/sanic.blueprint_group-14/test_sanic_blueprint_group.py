# Automatically generated by Pynguin.
import sanic.blueprints as module_0
import sanic.blueprint_group as module_1

def test_case_0():
    pass

def test_case_1():
    int_0 = -1934
    str_0 = 'REAL_IP_HEADER'
    blueprint_0 = module_0.Blueprint(str_0)
    str_1 = '\\aT~77#^~GBD}3/u-p'
    blueprint_group_0 = module_1.BlueprintGroup(str_1)
    blueprint_group_0.insert(int_0, blueprint_0)
    blueprint_group_1 = module_1.BlueprintGroup()
    var_0 = blueprint_group_1.middleware()
    tuple_0 = ()
    blueprint_group_2 = module_1.BlueprintGroup(tuple_0)
    int_1 = blueprint_group_1.__len__()
    var_1 = blueprint_group_2.middleware()
    var_2 = blueprint_group_0.__iter__()

def test_case_2():
    bytes_0 = b'\r\x0eu\x97G{2\xf5~\x7f\xd0L\x7f\xeb\xf3\xf6\xbe\xf9D7'
    blueprint_group_0 = module_1.BlueprintGroup(bytes_0)
    var_0 = blueprint_group_0.__iter__()

def test_case_3():
    bytes_0 = b'\xef\xdd|\xd4c\xcb\xd9\xa9\xa4[A'
    blueprint_group_0 = module_1.BlueprintGroup(bytes_0)
    int_0 = blueprint_group_0.__len__()

def test_case_4():
    bytes_0 = b'2k'
    blueprint_group_0 = module_1.BlueprintGroup(bytes_0)
    var_0 = blueprint_group_0.middleware()

def test_case_5():
    blueprint_group_0 = module_1.BlueprintGroup()
    var_0 = blueprint_group_0.middleware()
    int_0 = blueprint_group_0.__len__()
    tuple_0 = ()
    blueprint_group_1 = module_1.BlueprintGroup(tuple_0)
    int_1 = blueprint_group_1.__len__()
    float_0 = 15.0
    list_0 = [var_0, float_0, float_0, int_1]
    var_1 = blueprint_group_0.middleware(*list_0)