# Automatically generated by Pynguin.
import isort.exceptions as module_0
import builtins as module_1

def test_case_0():
    str_0 = 'Vrh}@rQn|Y*vO'
    invalid_settings_path_0 = module_0.InvalidSettingsPath(str_0)

def test_case_1():
    str_0 = None
    str_1 = '(l0\t\x0bnY'
    invalid_settings_path_0 = module_0.InvalidSettingsPath(str_1)
    existing_syntax_errors_0 = module_0.ExistingSyntaxErrors(str_0)

def test_case_2():
    str_0 = 'p?\\gSq$"\r'
    introduced_syntax_errors_0 = module_0.IntroducedSyntaxErrors(str_0)
    str_1 = ':,'
    assignments_format_mismatch_0 = module_0.AssignmentsFormatMismatch(str_1)
    missing_section_0 = module_0.MissingSection(str_1, str_0)

def test_case_3():
    str_0 = 'P^dsC$-W\n'
    file_skip_comment_0 = module_0.FileSkipComment(str_0)

def test_case_4():
    str_0 = ';s/Dz'
    file_skip_setting_0 = module_0.FileSkipSetting(str_0)

def test_case_5():
    str_0 = 'Z'
    formatting_plugin_does_not_exist_0 = module_0.FormattingPluginDoesNotExist(str_0)

def test_case_6():
    str_0 = '2.!nEYGS%YA'
    formatting_plugin_does_not_exist_0 = module_0.FormattingPluginDoesNotExist(str_0)
    str_1 = '21c#SES^R`'
    list_0 = [formatting_plugin_does_not_exist_0, formatting_plugin_does_not_exist_0]
    exception_0 = module_1.Exception(*list_0)
    literal_parsing_failure_0 = module_0.LiteralParsingFailure(str_1, exception_0)

def test_case_7():
    str_0 = 'i6uz<,E"[l\nuf cdb'
    assignments_format_mismatch_0 = module_0.AssignmentsFormatMismatch(str_0)

def test_case_8():
    str_0 = 'a'
    str_1 = 'source'
    str_2 = 'value'
    str_3 = 'Cb'
    str_4 = {str_1: str_3, str_2: str_0}
    str_5 = {str_0: str_4}
    unsupported_settings_0 = module_0.UnsupportedSettings(str_5)

def test_case_9():
    str_0 = 'wG\x0ch'
    unsupported_encoding_0 = module_0.UnsupportedEncoding(str_0)

def test_case_10():
    str_0 = '.7'
    missing_section_0 = module_0.MissingSection(str_0, str_0)

def test_case_11():
    type_0 = None
    literal_sort_type_mismatch_0 = module_0.LiteralSortTypeMismatch(type_0, type_0)