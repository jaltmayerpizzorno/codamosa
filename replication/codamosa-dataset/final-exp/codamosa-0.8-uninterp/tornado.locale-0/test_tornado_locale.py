# Automatically generated by Pynguin.
import tornado.locale as module_0
import gettext as module_1

def test_case_0():
    pass

def test_case_1():
    locale_0 = module_0.get()

def test_case_2():
    str_0 = 'proxy_auth_mode'
    module_0.set_default_locale(str_0)

def test_case_3():
    str_0 = '/usr/share/locale'
    float_0 = -318.0
    dict_0 = {}
    c_s_v_locale_0 = module_0.CSVLocale(str_0, dict_0)
    str_1 = c_s_v_locale_0.pgettext(str_0, str_0, str_0, float_0)
    module_0.load_translations(str_0, str_1)

def test_case_4():
    iterable_0 = module_0.get_supported_locales()
    str_0 = '3'
    str_1 = 'G-HP7Sn.[8jZ[L\nF'
    str_2 = '}oGcLcWjK)]'
    locale_0 = module_0.get()
    list_0 = [str_2, str_2, str_2, str_2]
    null_translations_0 = module_1.NullTranslations(list_0)
    gettext_locale_0 = module_0.GettextLocale(str_2, null_translations_0)
    str_3 = gettext_locale_0.pgettext(str_0, str_1)

def test_case_5():
    int_0 = -4901
    str_0 = 'pO86c@9mJFDr`}Xd*1b'
    list_0 = [str_0]
    locale_0 = module_0.get(*list_0)
    str_1 = 'yYm\\u?u7Geb^^-%z#'
    str_2 = 'r/Jbu6lyNF\rEX++\x0bnj#E'
    list_1 = [str_1, str_2, str_0]
    locale_1 = module_0.get(*list_1)
    str_3 = locale_0.friendly_number(int_0)

def test_case_6():
    str_0 = ')lIM/'
    list_0 = []
    locale_0 = module_0.get(*list_0)
    str_1 = locale_0.list(str_0)

def test_case_7():
    int_0 = 1123
    list_0 = []
    locale_0 = module_0.get(*list_0)
    str_0 = 'ZB(ti}]Ow|PPoU1a'
    str_1 = "F<t\t'b7Vy?oI"
    str_2 = '{W |Wf? w_6).]x'
    str_3 = '|\n'
    str_4 = ''
    dict_0 = {str_3: str_4}
    dict_1 = {str_2: dict_0, str_3: dict_0}
    c_s_v_locale_0 = module_0.CSVLocale(str_2, dict_1)
    str_5 = c_s_v_locale_0.pgettext(str_0, str_1)
    str_6 = locale_0.friendly_number(int_0)

def test_case_8():
    str_0 = ':3#m'
    str_1 = 'I0=_z\nl[\x0bmZ{r:#^z-uB'
    null_translations_0 = module_1.NullTranslations()
    gettext_locale_0 = module_0.GettextLocale(str_1, null_translations_0)
    str_2 = gettext_locale_0.pgettext(str_0, str_0)

def test_case_9():
    str_0 = ')&pYW1/oz$k,on5\t5'
    bool_0 = True
    str_1 = '}]'
    null_translations_0 = module_1.NullTranslations()
    gettext_locale_0 = module_0.GettextLocale(str_1, null_translations_0)
    str_2 = gettext_locale_0.pgettext(str_0, str_0, str_0, bool_0)

def test_case_10():
    locale_0 = module_0.get()

def test_case_11():
    int_0 = 240
    locale_0 = module_0.get()
    str_0 = locale_0.format_date(int_0)

def test_case_12():
    str_0 = None
    int_0 = -471
    locale_0 = module_0.get()
    str_1 = locale_0.translate(str_0, str_0, int_0)
    list_0 = [str_0]
    locale_1 = module_0.get(*list_0)
    str_2 = 'w\x0b\\OL.,IcR\x0b2$hte['
    null_translations_0 = module_1.NullTranslations()
    str_3 = locale_0.translate(str_2)
    gettext_locale_0 = module_0.GettextLocale(str_2, null_translations_0)
    str_4 = gettext_locale_0.translate(str_0)

def test_case_13():
    str_0 = '/usr/share/locale'
    str_1 = 'tornado'
    module_0.load_gettext_translations(str_0, str_1)

def test_case_14():
    str_0 = 'This is a test!'
    int_0 = 1
    str_1 = 'log_function'
    str_2 = 'Returns a list of the body arguments with the given name.\n\n        If the argument is not present, returns an empty list.\n\n        .. versionadded:: 3.2\n        '
    str_3 = '7E]\rdJt}b\x0b`{'
    dict_0 = {str_0: str_3}
    str_4 = 'bv-\t'
    str_5 = 'BlL(kZ!N5>GZ'
    dict_1 = {str_2: dict_0, str_4: dict_0, str_5: dict_0}
    c_s_v_locale_0 = module_0.CSVLocale(str_0, dict_1)
    str_6 = c_s_v_locale_0.pgettext(str_0, str_1, str_1, int_0)
    str_7 = None
    str_8 = c_s_v_locale_0.translate(str_7)