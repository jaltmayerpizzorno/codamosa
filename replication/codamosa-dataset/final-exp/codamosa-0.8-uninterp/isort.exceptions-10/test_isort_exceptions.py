# Automatically generated by Pynguin.
import isort.exceptions as module_0
import builtins as module_1

def test_case_0():
    pass

def test_case_1():
    str_0 = ';?|vdC5;p_R`P14'
    file_skip_comment_0 = module_0.FileSkipComment(str_0)
    file_skip_setting_0 = module_0.FileSkipSetting(str_0)
    str_1 = None
    introduced_syntax_errors_0 = module_0.IntroducedSyntaxErrors(str_1)
    file_skipped_0 = module_0.FileSkipped(str_0, str_0)
    str_2 = 'B`an^\x0cnZcJ'
    invalid_settings_path_0 = module_0.InvalidSettingsPath(str_2)
    type_0 = None
    literal_sort_type_mismatch_0 = module_0.LiteralSortTypeMismatch(type_0, type_0)

def test_case_2():
    str_0 = None
    file_skip_comment_0 = module_0.FileSkipComment(str_0)
    exception_0 = module_1.Exception()
    introduced_syntax_errors_0 = module_0.IntroducedSyntaxErrors(str_0)
    literal_parsing_failure_0 = module_0.LiteralParsingFailure(str_0, exception_0)
    literal_parsing_failure_1 = module_0.LiteralParsingFailure(str_0, exception_0)
    introduced_syntax_errors_1 = module_0.IntroducedSyntaxErrors(str_0)

def test_case_3():
    str_0 = '['
    file_skip_comment_0 = module_0.FileSkipComment(str_0)

def test_case_4():
    str_0 = 'X0:$"(b$1Egj+:gLYY)'
    str_1 = ';'
    profile_does_not_exist_0 = module_0.ProfileDoesNotExist(str_1)
    file_skip_comment_0 = module_0.FileSkipComment(str_1)
    exception_0 = module_1.Exception()
    str_2 = '/#'
    introduced_syntax_errors_0 = module_0.IntroducedSyntaxErrors(str_2)
    literal_parsing_failure_0 = module_0.LiteralParsingFailure(str_0, exception_0)

def test_case_5():
    str_0 = 'Or49/JfT}Cv'
    formatting_plugin_does_not_exist_0 = module_0.FormattingPluginDoesNotExist(str_0)

def test_case_6():
    str_0 = 'H3'
    assignments_format_mismatch_0 = module_0.AssignmentsFormatMismatch(str_0)

def test_case_7():
    str_0 = 'value'
    str_1 = 'source'
    bool_0 = True
    str_2 = 'cli'
    var_0 = {str_0: bool_0, str_1: str_2}
    var_1 = {str_1: var_0}
    unsupported_settings_0 = module_0.UnsupportedSettings(var_1)

def test_case_8():
    str_0 = '1?'
    file_skip_comment_0 = module_0.FileSkipComment(str_0)
    str_1 = '\tF4H'
    str_2 = '%I@3G;$?Ym\x0b0"'
    existing_syntax_errors_0 = module_0.ExistingSyntaxErrors(str_2)
    str_3 = '|#9)JKo'
    file_skipped_0 = module_0.FileSkipped(str_1, str_3)
    str_4 = '{\x0bm3OfF[x/v<[Zq'
    str_5 = 'z'
    existing_syntax_errors_1 = module_0.ExistingSyntaxErrors(str_5)
    missing_section_0 = module_0.MissingSection(str_4, str_4)