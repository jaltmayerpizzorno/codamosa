# Automatically generated by Pynguin.
import dataclasses_json.core as module_0

def test_case_0():
    try:
        list_0 = []
        extended_encoder_0 = module_0._ExtendedEncoder(ensure_ascii=list_0)
        str_0 = ''
        list_1 = [str_0]
        var_0 = extended_encoder_0.default(list_1)
        float_0 = -2048.711467
        var_1 = extended_encoder_0.default(float_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = False
        extended_encoder_0 = module_0._ExtendedEncoder(ensure_ascii=bool_0)
        var_0 = extended_encoder_0.default(bool_0)
    except BaseException:
        pass