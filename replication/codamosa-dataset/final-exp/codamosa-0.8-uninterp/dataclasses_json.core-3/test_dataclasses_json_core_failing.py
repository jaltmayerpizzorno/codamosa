# Automatically generated by Pynguin.
import dataclasses_json.core as module_0

def test_case_0():
    try:
        int_0 = -979
        dict_0 = {}
        extended_encoder_0 = module_0._ExtendedEncoder(ensure_ascii=int_0)
        var_0 = extended_encoder_0.default(dict_0)
        str_0 = 'Y7u.mF)W[zMr.@'
        extended_encoder_1 = module_0._ExtendedEncoder(check_circular=str_0)
        var_1 = extended_encoder_1.default(int_0)
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
        str_0 = '/iD~<\rMF5\x0c*G4mVv+z'
        str_1 = '?k\n>M,M)}6P\nS'
        dict_0 = {str_0: str_0, str_0: str_0, str_1: str_0, str_1: str_0}
        int_0 = 2068
        str_2 = 'decoder'
        extended_encoder_0 = module_0._ExtendedEncoder(skipkeys=int_0, check_circular=str_2, indent=str_0)
        var_0 = extended_encoder_0.default(str_1)
        field_override_0 = module_0.FieldOverride(**dict_0)
    except BaseException:
        pass