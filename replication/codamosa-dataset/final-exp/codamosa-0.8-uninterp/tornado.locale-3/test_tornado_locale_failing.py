# Automatically generated by Pynguin.
import tornado.locale as module_0
import gettext as module_1
import datetime as module_2

def test_case_0():
    try:
        str_0 = None
        str_1 = '&t">(bIb{[0'
        str_2 = ''
        list_0 = [str_1, str_2, str_2]
        locale_0 = module_0.get(*list_0)
        str_3 = locale_0.translate(str_0)
        str_4 = 'A,y\x0c<&f'
        str_5 = '~)U]'
        str_6 = 'expires_days'
        null_translations_0 = module_1.NullTranslations()
        gettext_locale_0 = module_0.GettextLocale(str_6, null_translations_0)
        module_0.set_default_locale(str_5)
        module_0.set_default_locale(str_4)
        str_7 = 'S+bmhUd:/93UQw'
        int_0 = -638
        str_8 = locale_0.translate(str_3)
        str_9 = locale_0.friendly_number(int_0)
        dict_0 = {str_4: str_4}
        locale_1 = module_0.get()
        str_10 = locale_1.pgettext(str_7, str_4, dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        locale_0 = module_0.get()
        dict_0 = {}
        int_0 = 334
        str_0 = locale_0.format_date(int_0)
        str_1 = '>VYWCM'
        str_2 = None
        str_3 = '@S7b+[zQKB'
        c_s_v_locale_0 = module_0.CSVLocale(str_3, dict_0)
        str_4 = c_s_v_locale_0.pgettext(str_0, str_2)
        str_5 = 'r.o%ZK du8-qg'
        iterable_0 = module_0.get_supported_locales()
        null_translations_0 = module_1.NullTranslations()
        gettext_locale_0 = module_0.GettextLocale(str_1, null_translations_0)
        null_translations_1 = module_1.NullTranslations(gettext_locale_0)
        str_6 = '\x0bjVvI]Ac/_+bj'
        list_0 = [str_6]
        locale_1 = module_0.get(*list_0)
        iterable_1 = module_0.get_supported_locales()
        gettext_locale_1 = module_0.GettextLocale(str_5, null_translations_1)
        gettext_locale_2 = module_0.GettextLocale(str_4, null_translations_0)
    except BaseException:
        pass

def test_case_2():
    try:
        null_translations_0 = module_1.NullTranslations()
        str_0 = '\riY1k6|%p@w(Sr7c\n;;'
        locale_0 = module_0.Locale(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = None
        locale_0 = module_0.get()
        str_0 = locale_0.format_date(int_0, int_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'screen_name'
        locale_0 = module_0.get()
        str_1 = locale_0.translate(str_0, str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'p;R~vUU44#[7M[B\nA'
        module_0.set_default_locale(str_0)
        str_1 = 'oG hxKh*!@MO/,29M'
        null_translations_0 = module_1.NullTranslations()
        locale_0 = module_0.get()
        str_2 = locale_0.pgettext(str_1, str_0, str_1, null_translations_0)
        locale_1 = module_0.Locale(str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'h7OHD:;,'
        locale_0 = module_0.get()
        null_translations_0 = module_1.NullTranslations()
        gettext_locale_0 = module_0.GettextLocale(str_0, null_translations_0)
        gettext_locale_1 = module_0.GettextLocale(str_0, null_translations_0)
        str_1 = gettext_locale_1.pgettext(str_0, str_0, str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        locale_0 = module_0.get()
        int_0 = 334
        str_0 = locale_0.format_date(int_0)
        str_1 = '>VYWCM'
        iterable_0 = module_0.get_supported_locales()
        null_translations_0 = module_1.NullTranslations()
        gettext_locale_0 = module_0.GettextLocale(str_1, null_translations_0)
        null_translations_1 = module_1.NullTranslations(gettext_locale_0)
        str_2 = '!BH'
        list_0 = [str_2]
        locale_1 = module_0.get(*list_0)
        iterable_1 = module_0.get_supported_locales()
        str_3 = locale_0.list(iterable_1)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'Returns a new template loader for the given path.\n\n        May be overridden by subclasses.  By default returns a\n        directory-based loader on the given path, using the\n        ``autoescape`` and ``template_whitespace`` application\n        settings.  If a ``template_loader`` application setting is\n        supplied, uses that instead.\n        '
        null_translations_0 = module_1.NullTranslations()
        gettext_locale_0 = module_0.GettextLocale(str_0, null_translations_0)
        str_1 = '\riY1k6|%p@w(Sr7c\n;;'
        list_0 = [str_1, str_0, str_0, gettext_locale_0]
        str_2 = gettext_locale_0.translate(str_1, list_0)
    except BaseException:
        pass

def test_case_9():
    try:
        int_0 = 334
        null_translations_0 = module_1.NullTranslations()
        str_0 = 'ds#q:\x0b}|:Om9'
        str_1 = '))jqR^"%v_][_z'
        list_0 = [str_0, str_1]
        locale_0 = module_0.get(*list_0)
        str_2 = locale_0.friendly_number(int_0)
        dict_0 = {}
        datetime_0 = module_2.datetime(**dict_0)
    except BaseException:
        pass

def test_case_10():
    try:
        locale_0 = module_0.get()
        int_0 = 334
        str_0 = locale_0.format_date(int_0)
        str_1 = '>VYWCM'
        null_translations_0 = module_1.NullTranslations()
        list_0 = [str_1]
        locale_1 = module_0.get(*list_0)
        int_1 = -3330
        str_2 = locale_1.friendly_number(int_1)
        dict_0 = {}
        datetime_0 = module_2.datetime(**dict_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = ''
        locale_0 = module_0.get()
        str_1 = locale_0.list(str_0)
        str_2 = 'IJv*a&\\z9ckrjvM'
        locale_1 = module_0.Locale(str_2)
    except BaseException:
        pass

def test_case_12():
    try:
        datetime_0 = None
        bool_0 = True
        locale_0 = module_0.get()
        str_0 = '(^"2x7FPR\x0bG~\x0c1'
        str_1 = '\\J-A'
        str_2 = 'f !b+WjP'
        dict_0 = None
        str_3 = '-a\nu\tp'
        str_4 = 'x'
        dict_1 = {str_2: dict_0, str_3: dict_0, str_4: dict_0}
        c_s_v_locale_0 = module_0.CSVLocale(str_1, dict_1)
        str_5 = c_s_v_locale_0.pgettext(str_0, str_0)
        bool_1 = locale_0.format_day(datetime_0, bool_0)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = None
        str_1 = '&t">(bIb{0'
        module_0.load_translations(str_0)
        str_2 = ''
        list_0 = [str_1, str_2, str_2]
        locale_0 = module_0.get(*list_0)
        str_3 = locale_0.translate(str_0)
        str_4 = 'A]$z`|)"w)0~,}}~}pN'
        str_5 = ';_'
        str_6 = 'r{*ZQPl'
        list_1 = [str_4, locale_0]
        null_translations_0 = module_1.NullTranslations(list_1)
        gettext_locale_0 = module_0.GettextLocale(str_6, null_translations_0)
        var_0 = null_translations_0.info()
        str_7 = gettext_locale_0.pgettext(str_5, str_4)
        null_translations_1 = module_1.NullTranslations()
        str_8 = locale_0.translate(str_2)
        gettext_locale_1 = module_0.GettextLocale(str_5, null_translations_1)
        module_0.load_translations(str_3)
        float_0 = 1.5
        str_9 = locale_0.format_date(float_0)
        list_2 = [list_1, str_9, list_0]
        var_1 = null_translations_0.add_fallback(list_2)
        module_0.set_default_locale(str_5)
        var_2 = null_translations_1.add_fallback(gettext_locale_1)
        int_0 = -638
        str_10 = locale_0.translate(str_3)
        str_11 = gettext_locale_1.translate(str_5, str_1, int_0)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = '</=vi<C5cc2\x0b*d\rp'
        str_1 = 'B'
        str_2 = '1<pngE\tE'
        float_0 = 1.0
        str_3 = 'U({6x'
        str_4 = None
        dict_0 = {str_1: str_0, str_4: str_3}
        str_5 = 'a6*{=md3d*CL'
        str_6 = ''
        str_7 = ''
        str_8 = ')Z!W^l*_q5h\x0bWYB'
        str_9 = 'x)Ch6cl^2Pi~vyYV8=0'
        str_10 = 'hqTNi>\r\\-Xusmxrn`v+i'
        str_11 = '{j 3F|I,A!_23sk~_ijf'
        str_12 = '\r\x0c}_'
        dict_1 = {str_8: str_9, str_0: str_10, str_11: str_4, str_7: str_12}
        dict_2 = {str_3: dict_0, str_5: dict_0, str_6: dict_0, str_7: dict_1}
        c_s_v_locale_0 = module_0.CSVLocale(str_2, dict_2)
        str_13 = c_s_v_locale_0.pgettext(str_1, str_0, str_0, float_0)
        str_14 = 'U5"UAuv5N/>c'
        str_15 = None
        dict_3 = {str_1: str_2, str_2: str_1, str_2: str_2, str_14: str_15}
        dict_4 = {str_0: dict_3}
        c_s_v_locale_1 = module_0.CSVLocale(str_0, dict_4)
        str_16 = c_s_v_locale_1.pgettext(str_0, str_0)
        module_0.set_default_locale(str_0)
        module_0.set_default_locale(str_0)
        locale_0 = module_0.Locale(str_0)
    except BaseException:
        pass