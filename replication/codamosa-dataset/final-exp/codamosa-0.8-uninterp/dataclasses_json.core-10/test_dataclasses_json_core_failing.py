# Automatically generated by Pynguin.
import dataclasses_json.core as module_0

def test_case_0():
    try:
        extended_encoder_0 = module_0._ExtendedEncoder()
        int_0 = 1
        int_1 = 2
        int_2 = 3
        int_3 = [int_0, int_1, int_2]
        var_0 = extended_encoder_0.default(int_3)
        str_0 = 'a'
        int_4 = {str_0: int_0}
        var_1 = extended_encoder_0.default(int_4)
        var_2 = extended_encoder_0.default(int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        extended_encoder_0 = module_0._ExtendedEncoder()
        var_0 = extended_encoder_0.default(extended_encoder_0)
    except BaseException:
        pass

def test_case_2():
    try:
        extended_encoder_0 = module_0._ExtendedEncoder()
        set_0 = {extended_encoder_0, extended_encoder_0}
        var_0 = extended_encoder_0.encode(set_0)
    except BaseException:
        pass