# Automatically generated by Pynguin.
import tornado.locale as module_0
import datetime as module_1
import gettext as module_2

def test_case_0():
    try:
        str_0 = 'I'
        module_0.set_default_locale(str_0)
        datetime_0 = module_1.datetime()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = None
        module_0.load_gettext_translations(str_0, str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'xsrf_cookie_version'
        list_0 = [str_0]
        locale_0 = module_0.get(*list_0)
    except BaseException:
        pass

def test_case_3():
    try:
        locale_0 = module_0.get()
    except BaseException:
        pass

def test_case_4():
    try:
        locale_0 = module_0.get()
        str_0 = '\n    '
        module_0.load_translations(str_0, str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'en_US'
        locale_0 = module_0.Locale(str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = "'$nC-7Pl"
        locale_0 = module_0.get()
        str_1 = locale_0.list(str_0)
        module_0.load_translations(str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = ']n-M'
        int_0 = -636
        locale_0 = module_0.get()
        str_1 = locale_0.pgettext(str_0, str_0, int_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = '[wc}'
        int_0 = 2906
        str_1 = 'j'
        null_translations_0 = module_2.NullTranslations()
        gettext_locale_0 = module_0.GettextLocale(str_1, null_translations_0)
        str_2 = gettext_locale_0.translate(str_0, int_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = '\r~*P7`'
        null_translations_0 = module_2.NullTranslations()
        gettext_locale_0 = module_0.GettextLocale(str_0, null_translations_0)
        str_1 = gettext_locale_0.pgettext(str_0, str_0)
        str_2 = gettext_locale_0.pgettext(str_1, str_0, str_1)
    except BaseException:
        pass

def test_case_10():
    try:
        int_0 = None
        locale_0 = module_0.get()
        str_0 = 'm'
        locale_1 = module_0.get()
        str_1 = locale_1.friendly_number(int_0)
        str_2 = 'I'
        str_3 = '\'Ur@: T f,wocZh"'
        dict_0 = {str_0: str_1, str_0: str_3, str_1: str_1}
        str_4 = '<@15NC#zuLm#'
        str_5 = '"@,"f?CpF\\Y(C\r3@[nOT'
        str_6 = 'Y(\x0bKSp4F\x0b1_U'
        str_7 = 'Combines an object with a dictionary of defaults.\n\n    Used internally by AsyncHTTPClient implementations.\n    '
        str_8 = '_Oz'
        dict_1 = {str_5: str_6, str_7: str_1, str_8: str_1}
        dict_2 = {str_3: dict_0, str_3: dict_0, str_0: dict_0, str_4: dict_1}
        c_s_v_locale_0 = module_0.CSVLocale(str_0, dict_2)
        str_9 = c_s_v_locale_0.pgettext(str_2, str_2)
        bool_0 = True
        str_10 = '!'
        dict_3 = {}
        c_s_v_locale_1 = module_0.CSVLocale(str_10, dict_3)
        str_11 = c_s_v_locale_1.translate(str_1)
        str_12 = locale_0.format_date(int_0, int_0, bool_0, bool_0)
    except BaseException:
        pass

def test_case_11():
    try:
        datetime_0 = None
        locale_0 = module_0.get()
        bool_0 = locale_0.format_day(datetime_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = '\tz}NF_+-XZ!mC'
        bool_0 = True
        null_translations_0 = module_2.NullTranslations()
        gettext_locale_0 = module_0.GettextLocale(str_0, null_translations_0)
        str_1 = gettext_locale_0.pgettext(str_0, str_0, str_0, bool_0)
        var_0 = print(bool_0)
        module_0.load_translations(str_1)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = '7, 8, 13'
        float_0 = -4616.35141
        bool_0 = True
        str_1 = 'log_rotate_mode'
        list_0 = [str_0, str_1]
        locale_0 = module_0.get(*list_0)
        str_2 = '5%hJr\nZ'
        str_3 = None
        str_4 = 'p{L'
        dict_0 = {str_0: str_3, str_2: str_4}
        str_5 = '?w\t4.v:6W:~zabAo'
        dict_1 = {str_1: dict_0, str_5: dict_0}
        c_s_v_locale_0 = module_0.CSVLocale(str_2, dict_1)
        null_translations_0 = module_2.NullTranslations()
        gettext_locale_0 = module_0.GettextLocale(str_5, null_translations_0)
        str_6 = 'Called by IOLoop periodically to ask libcurl to process any\n        events it may have forgotten about.\n        '
        str_7 = '7$ZC.}++Nid0'
        dict_2 = {str_6: str_6, str_6: str_7}
        str_8 = 'Cannot reverse url regex '
        dict_3 = {str_7: dict_2, str_7: dict_2, str_8: dict_2}
        c_s_v_locale_1 = module_0.CSVLocale(str_4, dict_3)
        int_0 = 807
        str_9 = locale_0.format_date(float_0, int_0, bool_0, bool_0)
        int_1 = -897
        str_10 = locale_0.friendly_number(int_1)
        str_11 = locale_0.list(str_6)
        str_12 = locale_0.format_date(int_1, bool_0)
        str_13 = 'Ei\\.$xfkh_6-j'
        str_14 = locale_0.pgettext(str_11, str_13, int_1)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = None
        module_0.load_translations(str_0)
        str_1 = '^6%$R{I_`'
        str_2 = "!4J>DH'\tHD\\"
        list_0 = [str_1, str_2, str_2]
        locale_0 = module_0.get(*list_0)
        iterable_0 = module_0.get_supported_locales()
        null_translations_0 = module_2.NullTranslations()
        bool_0 = True
        float_0 = -2154.88
        bool_1 = True
        str_3 = ':|c{Kcta^Yb>gSUro'
        dict_0 = {str_2: str_0}
        str_4 = locale_0.list(list_0)
        locale_1 = module_0.get()
        str_5 = '0'
        str_6 = 'jBf\tb""1m_'
        str_7 = 'WiVQ'
        gettext_locale_0 = module_0.GettextLocale(str_2, null_translations_0)
        str_8 = gettext_locale_0.pgettext(str_6, str_7)
        dict_1 = {str_3: dict_0, str_3: dict_0, str_1: dict_0, str_5: dict_0}
        str_9 = 'The newest signed value version supported by this version of Tornado.\n\nSigned values newer th^n this version cannot ,e decoded.\n\n.. versionadded:: 3.2.1\n'
        c_s_v_locale_0 = module_0.CSVLocale(str_2, dict_1)
        str_10 = c_s_v_locale_0.translate(str_9)
        c_s_v_locale_1 = module_0.CSVLocale(str_1, dict_1)
        str_11 = locale_0.format_date(float_0, bool_0, bool_1)
        int_0 = 14
        str_12 = locale_0.friendly_number(int_0)
        str_13 = locale_0.list(iterable_0)
    except BaseException:
        pass

def test_case_15():
    try:
        int_0 = -234
        str_0 = 'yp+ik,Of?*]h4#5w('
        null_translations_0 = module_2.NullTranslations()
        gettext_locale_0 = module_0.GettextLocale(str_0, null_translations_0)
        str_1 = gettext_locale_0.translate(str_0, str_0, int_0)
        list_0 = [str_0]
        dict_0 = {}
        c_s_v_locale_0 = module_0.CSVLocale(str_0, dict_0)
        locale_0 = module_0.get(*list_0)
        dict_1 = None
        datetime_0 = module_1.datetime(**dict_1)
    except BaseException:
        pass

def test_case_16():
    try:
        float_0 = -3106.649073954526
        int_0 = -3777
        int_1 = -880
        bool_0 = None
        bool_1 = True
        locale_0 = module_0.get()
        str_0 = locale_0.format_date(float_0, int_1, bool_0, bool_0, bool_1)
        int_2 = 14
        int_3 = -239
        str_1 = locale_0.friendly_number(int_3)
        str_2 = locale_0.format_date(int_0, int_2)
        str_3 = locale_0.list(int_0)
    except BaseException:
        pass