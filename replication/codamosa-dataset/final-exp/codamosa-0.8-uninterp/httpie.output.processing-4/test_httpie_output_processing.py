# Automatically generated by Pynguin.
import httpie.output.processing as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'application/json'
    conversion_0 = module_0.Conversion()
    optional_0 = conversion_0.get_converter(str_0)

def test_case_2():
    list_0 = []
    formatting_0 = module_0.Formatting(list_0)

def test_case_3():
    list_0 = []
    str_0 = 'S3e*Aq1.'
    formatting_0 = module_0.Formatting(list_0)
    str_1 = formatting_0.format_headers(str_0)

def test_case_4():
    str_0 = 'mCCE)u/!xwq2'
    list_0 = []
    formatting_0 = module_0.Formatting(list_0)
    str_1 = formatting_0.format_body(str_0, str_0)

def test_case_5():
    str_0 = ''
    dict_0 = {}
    conversion_0 = module_0.Conversion(**dict_0)
    optional_0 = conversion_0.get_converter(str_0)
    str_1 = 'O1 PV'
    list_0 = []
    str_2 = 'QN^\x0b_hQv{AcD}'
    formatting_0 = module_0.Formatting(list_0, str_2)
    str_3 = formatting_0.format_headers(str_1)