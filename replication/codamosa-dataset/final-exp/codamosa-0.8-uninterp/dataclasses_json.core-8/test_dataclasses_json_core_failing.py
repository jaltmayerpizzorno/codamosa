# Automatically generated by Pynguin.
import dataclasses_json.core as module_0
import decimal as module_1

def test_case_0():
    try:
        extended_encoder_0 = module_0._ExtendedEncoder()
        var_0 = extended_encoder_0.default(extended_encoder_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '3d3f2fc1-460b-49f9-9bbd-0a0b945eb89e'
        decimal_0 = module_1.Decimal()
        extended_encoder_0 = module_0._ExtendedEncoder()
        var_0 = extended_encoder_0.default(decimal_0)
        var_1 = extended_encoder_0.encode(str_0)
        var_2 = extended_encoder_0.default(decimal_0)
        float_0 = None
        var_3 = extended_encoder_0.default(float_0)
    except BaseException:
        pass