# Automatically generated by Pynguin.
import dataclasses_json.cfg as module_0
import marshmallow.fields as module_1

def test_case_0():
    pass

def test_case_1():
    dict_0 = module_0.config()

def test_case_2():
    global_config_0 = module_0._GlobalConfig()
    dict_0 = {global_config_0: global_config_0, global_config_0: global_config_0}
    var_0 = None
    str_0 = '`%1SEHs,<z%NKf*M\x0c'
    str_1 = ')\tk$6L.LBAT'
    dict_1 = {str_0: str_0, str_1: str_0, str_0: var_0}
    field_0 = module_1.Field(dump_default=dict_0, default=global_config_0, validate=var_0, **dict_1)
    bool_0 = False
    tuple_0 = (bool_0, dict_1)
    dict_2 = module_0.config(dict_0, encoder=field_0, mm_field=field_0, exclude=tuple_0)

def test_case_3():
    global_config_0 = module_0._GlobalConfig()
    dict_0 = {global_config_0: global_config_0, global_config_0: global_config_0, global_config_0: global_config_0, global_config_0: global_config_0}
    dict_1 = module_0.config(encoder=dict_0)

def test_case_4():
    global_config_0 = module_0._GlobalConfig()
    dict_0 = {global_config_0: global_config_0, global_config_0: global_config_0}
    str_0 = '`%1SEHs,<z%NKf*M\x0c'
    str_1 = ')\tk$6L.LBAT'
    bool_0 = False
    global_config_1 = module_0._GlobalConfig()
    none_type_0 = None
    dict_1 = module_0.config(dict_0, encoder=none_type_0)
    str_2 = '$^fy)&TFnk#W='
    set_0 = {bool_0, str_1}
    list_0 = [str_2, dict_0]
    dict_2 = module_0.config(encoder=set_0, decoder=list_0, field_name=str_0)