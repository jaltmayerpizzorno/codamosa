# Automatically generated by Pynguin.
import tornado.locale as module_0
import gettext as module_1

def test_case_0():
    pass

def test_case_1():
    iterable_0 = module_0.get_supported_locales()
    locale_0 = module_0.get()

def test_case_2():
    iterable_0 = module_0.get_supported_locales()

def test_case_3():
    str_0 = 'zh_CN'
    list_0 = [str_0]
    locale_0 = module_0.get(*list_0)

def test_case_4():
    int_0 = -2695
    str_0 = None
    list_0 = [str_0]
    locale_0 = module_0.get(*list_0)
    str_1 = locale_0.format_date(int_0)

def test_case_5():
    locale_0 = module_0.get()

def test_case_6():
    float_0 = -1370.3182
    locale_0 = module_0.get()
    str_0 = locale_0.format_date(float_0)

def test_case_7():
    int_0 = -74
    str_0 = 'Content-Disposition'
    str_1 = '`2by2}m^\x0ct\\2lX!%vQBt'
    dict_0 = {str_0: str_0, str_0: str_1, str_1: str_1, str_0: str_1}
    str_2 = '/'
    dict_1 = {str_0: dict_0, str_2: dict_0, str_0: dict_0, str_1: dict_0}
    c_s_v_locale_0 = module_0.CSVLocale(str_0, dict_1)
    str_3 = c_s_v_locale_0.translate(str_2, str_2, int_0)

def test_case_8():
    str_0 = 'if'
    str_1 = '<ImV\\xKL8mCh;, AP'
    none_type_0 = None
    str_2 = '.IjlD5g8xo'
    str_3 = 'Stream is closed'
    dict_0 = {str_3: str_3}
    dict_1 = {str_2: dict_0}
    c_s_v_locale_0 = module_0.CSVLocale(str_2, dict_1)
    str_4 = c_s_v_locale_0.pgettext(str_0, str_1, none_type_0)

def test_case_9():
    str_0 = None
    str_1 = '\x0c$\\Rl_'
    null_translations_0 = module_1.NullTranslations()
    gettext_locale_0 = module_0.GettextLocale(str_1, null_translations_0)
    str_2 = 'jDwK:X]_x'
    int_0 = 904
    str_3 = gettext_locale_0.pgettext(str_2, str_0, str_1, int_0)

def test_case_10():
    str_0 = 'M>_Qy|k\\'
    bytes_0 = b'\xea\x01\xda'
    null_translations_0 = module_1.NullTranslations(bytes_0)
    gettext_locale_0 = module_0.GettextLocale(str_0, null_translations_0)
    str_1 = gettext_locale_0.pgettext(str_0, str_0)

def test_case_11():
    str_0 = ',"8S'
    module_0.set_default_locale(str_0)
    null_translations_0 = module_1.NullTranslations()
    locale_0 = module_0.get()
    int_0 = 0
    str_1 = locale_0.friendly_number(int_0)
    dict_0 = {str_0: str_0, str_0: str_0}
    var_0 = null_translations_0.gettext(dict_0)
    str_2 = locale_0.list(str_1)
    null_translations_1 = module_1.NullTranslations(null_translations_0)
    gettext_locale_0 = module_0.GettextLocale(str_0, null_translations_1)
    var_1 = null_translations_1.install()
    list_0 = [str_1]
    locale_1 = module_0.get(*list_0)
    str_3 = locale_1.format_date(int_0, int_0)
    null_translations_2 = module_1.NullTranslations()
    gettext_locale_1 = module_0.GettextLocale(str_1, null_translations_2)
    str_4 = "?#\n:?v]KtGJ3S'k=j"
    str_5 = gettext_locale_1.pgettext(str_4, str_3, str_3, int_0)

def test_case_12():
    str_0 = 'A test case that starts up an HTTP server.\n\n    Subclasses must override `get_app()`, which returns the\n    `tornado.web.Application` (or other `.HTTPServer` callback) to be tested.\n    Tests will typically use the provided ``self.http_client`` to fetch\n    URLs from this server.\n\n    Example, assuming the "Hello, world" example from the user guide is in\n    ``hello.py``::\n\n        import hello\n\n        class TestHelloApp(AsyncHTTPTestCase):\n            def get_app(self):\n                return hello.make_app()\n\n            def test_homepage(self):\n                response = self.fetch(\'/\')\n                self.assertEqual(response.code, 200)\n                self.assertEqual(response.body, \'Hello, world\')\n\n    That call to ``self.fetch()`` is equivalent to ::\n\n        self.http_client.fetch(self.get_url(\'/\'), self.stop)\n        response = self.wait()\n\n    which illustrates how AsyncTestCase can turn an asynchronous operation,\n    like ``http_client.fetch()``, into a synchronous operation. If you need\n    to do other asynchronous operations in tests, you\'ll probably need to use\n    ``stop()`` and ``wait()`` yourself.\n    '
    str_1 = 'Malformed HTTP request line'
    str_2 = '*RJc=BZGbRl(ay '
    null_translations_0 = module_1.NullTranslations()
    str_3 = "U'"
    dict_0 = None
    str_4 = '4~Yu9I@Z7aIAhTq4a:c'
    dict_1 = {str_3: dict_0, str_2: dict_0, str_4: dict_0, str_2: dict_0}
    c_s_v_locale_0 = module_0.CSVLocale(str_2, dict_1)
    gettext_locale_0 = module_0.GettextLocale(str_0, null_translations_0)
    str_5 = gettext_locale_0.pgettext(str_0, str_2)
    list_0 = [str_1, str_1]
    locale_0 = module_0.get(*list_0)
    str_6 = "a'yHZ*M'F"
    str_7 = '/r:A<W\nc1K:3y>W=lzCH'
    float_0 = 20.0
    var_0 = null_translations_0.pgettext(locale_0, float_0)
    str_8 = None
    str_9 = gettext_locale_0.translate(str_1)
    str_10 = '#.z.lkIxY -C.Wi'
    str_11 = None
    str_12 = 'hcmG'
    str_13 = '\'"'
    dict_2 = {str_8: str_5, str_10: str_11, str_12: str_13}
    str_14 = 'J'
    str_15 = locale_0.translate(str_14)
    dict_3 = {str_7: dict_2, str_13: dict_2, str_15: dict_2}
    c_s_v_locale_1 = module_0.CSVLocale(str_6, dict_3)
    int_0 = 5
    bool_0 = True
    bool_1 = True
    str_16 = locale_0.format_date(float_0, int_0, bool_0, bool_1)
    str_17 = gettext_locale_0.pgettext(str_4, str_1)

def test_case_13():
    str_0 = 'A test case that starts up an HTTP server.\n\n    Subclasses must override `get_app()`, which returns the\n    `tornado.web.Application` (or other `.HTTPServer` callback) to be tested.\n    Tests will typically use the provided ``self.http_client`` to fetch\n    URLs from this server.\n\n    Example, assuming the "Hello, world" example from the user guide is in\n    ``hello.py``::\n\n        import hello\n\n        class TestHelloApp(AsyncHTTPTestCase):\n            def get_app(self):\n                return hello.make_app()\n\n            def test_homepage(self):\n                response = self.fetch(\'/\')\n                self.assertEqual(response.code, 200)\n                self.assertEqual(response.body, \'Hello, world\')\n\n    That call to ``self.fetch()`` is equivalent to ::\n\n        self.http_client.fetch(self.get_url(\'/\'), self.stop)\n        response = self.wait()\n\n    which illustrates how AsyncTestCase can turn an asynchronous operation,\n    like ``http_client.fetch()``, into a synchronous operation. If you need\n    to do other asynchronous operations in tests, you\'ll probably need to use\n    ``stop()`` and ``wait()`` yourself.\n    '
    str_1 = 'Malformed HTTP request line'
    str_2 = '*RJc=BZGbRl(ay '
    null_translations_0 = module_1.NullTranslations()
    str_3 = "U'"
    dict_0 = None
    str_4 = '4~Yu9I@Z7aIAhTq4a:c'
    dict_1 = {str_3: dict_0, str_2: dict_0, str_4: dict_0, str_2: dict_0}
    c_s_v_locale_0 = module_0.CSVLocale(str_2, dict_1)
    gettext_locale_0 = module_0.GettextLocale(str_0, null_translations_0)
    str_5 = gettext_locale_0.pgettext(str_0, str_2)
    list_0 = [str_1, str_1]
    locale_0 = module_0.get(*list_0)
    str_6 = "a'yHZ*M'F"
    str_7 = '/r:A<W\nc1K:3y>W=lzCH'
    float_0 = 20.0
    var_0 = null_translations_0.pgettext(locale_0, float_0)
    str_8 = None
    str_9 = gettext_locale_0.translate(str_1)
    str_10 = '#.z.lkIxY -C.Wi'
    str_11 = None
    str_12 = 'hcmG'
    str_13 = '\'"'
    dict_2 = {str_8: str_5, str_10: str_11, str_12: str_13}
    str_14 = 'J'
    str_15 = locale_0.translate(str_14)
    dict_3 = {str_7: dict_2, str_13: dict_2, str_15: dict_2}
    c_s_v_locale_1 = module_0.CSVLocale(str_6, dict_3)
    int_0 = 5
    bool_0 = True
    int_1 = 2956
    str_16 = locale_0.format_date(float_0, int_1, bool_0, bool_0, bool_0)
    str_17 = '_TY@\tW<k}8W;~njrVs'
    str_18 = "+)mqM~pT&'k-"
    str_19 = gettext_locale_0.pgettext(str_17, str_18, str_14, int_0)

def test_case_14():
    str_0 = ',"8S'
    module_0.set_default_locale(str_0)
    locale_0 = module_0.get()
    int_0 = -2678
    bool_0 = False
    str_1 = locale_0.format_date(int_0, int_0, bool_0)

def test_case_15():
    str_0 = ',"8S'
    module_0.set_default_locale(str_0)
    str_1 = "k\r'?op"
    null_translations_0 = module_1.NullTranslations()
    locale_0 = module_0.get()
    int_0 = 1165
    str_2 = locale_0.friendly_number(int_0)
    dict_0 = {str_1: str_0, str_0: str_0}
    var_0 = null_translations_0.gettext(dict_0)
    null_translations_1 = module_1.NullTranslations(null_translations_0)
    gettext_locale_0 = module_0.GettextLocale(str_0, null_translations_1)
    int_1 = 3136
    list_0 = [str_1, str_0]
    locale_1 = module_0.get(*list_0)
    str_3 = locale_1.format_date(int_0, int_1)
    str_4 = ".iRyc2/90a'NjW+"
    gettext_locale_1 = module_0.GettextLocale(str_0, null_translations_0)
    gettext_locale_2 = module_0.GettextLocale(str_4, null_translations_1)

def test_case_16():
    str_0 = ',"8S'
    module_0.set_default_locale(str_0)
    null_translations_0 = module_1.NullTranslations()
    locale_0 = module_0.get()
    str_1 = ''
    str_2 = locale_0.list(str_1)
    null_translations_1 = module_1.NullTranslations(null_translations_0)
    gettext_locale_0 = module_0.GettextLocale(str_0, null_translations_1)

def test_case_17():
    str_0 = None
    module_0.load_translations(str_0)

def test_case_18():
    str_0 = 'eRs'
    null_translations_0 = module_1.NullTranslations()
    locale_0 = module_0.get()
    str_1 = 'ktrL6'
    int_0 = 0
    str_2 = locale_0.friendly_number(int_0)
    str_3 = locale_0.list(str_1)
    null_translations_1 = module_1.NullTranslations(null_translations_0)
    gettext_locale_0 = module_0.GettextLocale(str_0, null_translations_1)
    str_4 = 'Es@,BCUXEbV'
    list_0 = [str_2]
    str_5 = None
    module_0.load_translations(str_5)
    locale_1 = module_0.get(*list_0)
    str_6 = locale_1.format_date(int_0, int_0)
    str_7 = 'kwB*;@,]\n'
    null_translations_2 = module_1.NullTranslations()
    str_8 = None
    str_9 = gettext_locale_0.pgettext(str_8, str_2)
    none_type_0 = None
    null_translations_3 = module_1.NullTranslations()
    gettext_locale_1 = module_0.GettextLocale(str_0, null_translations_3)
    float_0 = -987.0
    set_0 = {float_0, str_7, null_translations_2}
    var_0 = null_translations_0.set_output_charset(set_0)
    str_10 = gettext_locale_1.translate(str_0, none_type_0)
    dict_0 = {}
    dict_1 = {str_6: dict_0}
    c_s_v_locale_0 = module_0.CSVLocale(str_7, dict_1)
    str_11 = '\x0c$\\Rl_'
    null_translations_4 = module_1.NullTranslations(null_translations_2)
    gettext_locale_2 = module_0.GettextLocale(str_11, null_translations_4)
    str_12 = gettext_locale_0.pgettext(str_4, str_0, str_7, int_0)