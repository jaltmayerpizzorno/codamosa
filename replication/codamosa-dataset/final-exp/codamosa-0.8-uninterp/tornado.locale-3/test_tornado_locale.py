# Automatically generated by Pynguin.
import tornado.locale as module_0
import gettext as module_1
import datetime as module_2

def test_case_0():
    pass

def test_case_1():
    locale_0 = module_0.get()

def test_case_2():
    str_0 = 'tV=lSY*+1rT:f4Fsp5'
    module_0.set_default_locale(str_0)

def test_case_3():
    str_0 = './'
    module_0.load_translations(str_0)

def test_case_4():
    str_0 = './'
    module_0.load_gettext_translations(str_0, str_0)

def test_case_5():
    iterable_0 = module_0.get_supported_locales()

def test_case_6():
    str_0 = '*KL$9KVAk'
    str_1 = 'EUMt\\XMh3\\'
    list_0 = [str_1]
    locale_0 = module_0.get(*list_0)
    str_2 = locale_0.list(str_0)
    str_3 = '\n=3\x0b%:y\n0N\x0c?(|9^pe~'
    dict_0 = None
    dict_1 = {str_3: dict_0, str_3: dict_0}
    c_s_v_locale_0 = module_0.CSVLocale(str_0, dict_1)

def test_case_7():
    locale_0 = module_0.get()

def test_case_8():
    float_0 = -2949.111
    bool_0 = False
    locale_0 = module_0.get()
    str_0 = locale_0.format_date(float_0, bool_0)

def test_case_9():
    str_0 = 'h7OHD:;,'
    locale_0 = module_0.get()
    str_1 = locale_0.translate(str_0)
    str_2 = locale_0.list(str_0)

def test_case_10():
    int_0 = -609
    locale_0 = module_0.get()
    str_0 = locale_0.friendly_number(int_0)

def test_case_11():
    str_0 = 'rVoNNrc'
    locale_0 = module_0.get()
    str_1 = locale_0.pgettext(str_0, str_0)

def test_case_12():
    str_0 = "5&6!y'\r^l.D"
    str_1 = 'AQ'
    str_2 = 'V9~q5y.6b63\nd$(\\\r:\\'
    str_3 = ''
    str_4 = '~5'
    dict_0 = {str_3: str_4}
    dict_1 = {str_2: dict_0}
    c_s_v_locale_0 = module_0.CSVLocale(str_2, dict_1)
    str_5 = c_s_v_locale_0.pgettext(str_0, str_1)

def test_case_13():
    str_0 = 'Yw{d'
    null_translations_0 = module_1.NullTranslations()
    gettext_locale_0 = module_0.GettextLocale(str_0, null_translations_0)

def test_case_14():
    str_0 = '\x0b%ML.K\r~81z\x0c9'
    str_1 = '?\x0b`O'
    int_0 = 2858
    str_2 = 'vG=r\x0cI<q>[%NVX'
    null_translations_0 = module_1.NullTranslations()
    gettext_locale_0 = module_0.GettextLocale(str_2, null_translations_0)
    str_3 = gettext_locale_0.pgettext(str_0, str_1, str_0, int_0)

def test_case_15():
    str_0 = 'DDo+%pjKZU(%,!\rw6;`'
    str_1 = 'S?&%!G.Ogig.YNy"k,T8'
    null_translations_0 = module_1.NullTranslations()
    gettext_locale_0 = module_0.GettextLocale(str_1, null_translations_0)
    str_2 = gettext_locale_0.pgettext(str_0, str_0)

def test_case_16():
    int_0 = 226
    int_1 = -2520
    bool_0 = False
    locale_0 = module_0.get()
    str_0 = locale_0.format_date(int_0, int_1, bool_0)

def test_case_17():
    str_0 = 'r'
    str_1 = '@=@gMr+fxZ'
    module_0.set_default_locale(str_1)
    str_2 = None
    str_3 = '.t"Q>bIb{[0'
    list_0 = [str_3, str_2, str_2]
    locale_0 = module_0.get(*list_0)
    str_4 = locale_0.translate(str_2)
    str_5 = 'A,y\x0c<&f'
    null_translations_0 = module_1.NullTranslations()
    gettext_locale_0 = module_0.GettextLocale(str_0, null_translations_0)
    module_0.load_translations(str_4)
    float_0 = 1.5
    str_6 = locale_0.format_date(float_0)
    module_0.set_default_locale(str_5)
    var_0 = null_translations_0.add_fallback(gettext_locale_0)
    int_0 = -638
    str_7 = 'G,AL]IN7H);'
    str_8 = 'jFGoSZV[-9#6V3'
    str_9 = locale_0.list(str_7)
    bool_0 = False
    bool_1 = True
    str_10 = locale_0.format_date(int_0, int_0, bool_0, bool_1)
    int_1 = -147
    str_11 = 'G,AL]IN7H);'
    str_12 = locale_0.pgettext(str_10, str_11, str_8, int_1)

def test_case_18():
    str_0 = 'fa'
    int_0 = 10
    timedelta_0 = module_2.timedelta()
    null_translations_0 = module_1.NullTranslations()
    null_translations_1 = module_1.NullTranslations(null_translations_0)
    gettext_locale_0 = module_0.GettextLocale(str_0, null_translations_1)

def test_case_19():
    str_0 = '"vi"1)Gq1h|J%\'Y<'
    int_0 = 15
    locale_0 = module_0.get()
    str_1 = locale_0.format_date(int_0)
    str_2 = 'b'
    null_translations_0 = module_1.NullTranslations()
    gettext_locale_0 = module_0.GettextLocale(str_2, null_translations_0)
    str_3 = gettext_locale_0.pgettext(str_0, str_0)
    module_0.set_default_locale(str_2)
    str_4 = None
    str_5 = '.t"Q>bIb{[0'
    str_6 = "x`-48=!@+PAIM2s'P|"
    list_0 = [str_5, str_6, str_6]
    locale_1 = module_0.get(*list_0)
    str_7 = locale_1.translate(str_4)
    str_8 = 'A,y\x0c<&f'
    str_9 = 'expires_days'
    null_translations_1 = module_1.NullTranslations()
    gettext_locale_1 = module_0.GettextLocale(str_9, null_translations_1)
    module_0.set_default_locale(str_8)
    module_0.load_translations(str_7)
    module_0.set_default_locale(str_8)
    str_10 = 'S+bmhUd:/93UQw'
    int_1 = -634
    str_11 = locale_1.translate(str_7)
    str_12 = 'G,AL]IN7H);'
    str_13 = '\\A2 "C~'
    str_14 = locale_1.list(str_12)
    dict_0 = {str_9: str_10, str_10: str_13, str_9: str_8}
    dict_1 = {str_12: dict_0, str_10: dict_0, str_11: dict_0}
    int_2 = -1524
    bool_0 = True
    bool_1 = None
    str_15 = locale_1.format_date(int_1, int_2, bool_1, bool_1, bool_0)
    c_s_v_locale_0 = module_0.CSVLocale(str_6, dict_1)
    str_16 = '[oRgDB0QO>t'
    str_17 = 'G,AL]IN7H);'
    str_18 = locale_1.pgettext(str_16, str_17, str_13, int_1)