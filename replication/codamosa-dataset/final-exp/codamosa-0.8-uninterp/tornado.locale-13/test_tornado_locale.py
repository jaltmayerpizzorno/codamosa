# Automatically generated by Pynguin.
import tornado.locale as module_0
import gettext as module_1

def test_case_0():
    pass

def test_case_1():
    locale_0 = module_0.get()

def test_case_2():
    str_0 = '#fC<BB3Zr'
    module_0.set_default_locale(str_0)

def test_case_3():
    str_0 = None
    module_0.load_translations(str_0)

def test_case_4():
    iterable_0 = module_0.get_supported_locales()

def test_case_5():
    float_0 = 547.3
    null_translations_0 = module_1.NullTranslations(float_0)
    null_translations_1 = module_1.NullTranslations()
    str_0 = '2sn{'
    null_translations_2 = module_1.NullTranslations()
    gettext_locale_0 = module_0.GettextLocale(str_0, null_translations_2)
    iterable_0 = module_0.get_supported_locales()
    list_0 = [str_0, str_0]
    locale_0 = module_0.get(*list_0)
    bool_0 = False
    str_1 = locale_0.format_date(float_0, bool_0)
    str_2 = '.E@-F'
    bool_1 = True
    str_3 = locale_0.translate(str_2, str_1, bool_1)

def test_case_6():
    float_0 = 19.69072340961975
    int_0 = None
    iterable_0 = module_0.get_supported_locales()
    str_0 = 'Q`L)XSTf/Q'
    bool_0 = False
    locale_0 = module_0.get()
    str_1 = locale_0.format_date(float_0, bool_0)
    str_2 = '/'
    null_translations_0 = module_1.NullTranslations()
    gettext_locale_0 = module_0.GettextLocale(str_2, null_translations_0)
    str_3 = gettext_locale_0.translate(str_0, int_0)
    str_4 = ']6ib'
    str_5 = '<D__&@Wm ,L(P'
    list_0 = [str_4, str_5]
    locale_1 = module_0.get(*list_0)
    null_translations_1 = module_1.NullTranslations(null_translations_0)
    gettext_locale_1 = module_0.GettextLocale(str_3, null_translations_0)
    str_6 = 'O+`K~#+K#*Z3.o<=,'
    str_7 = gettext_locale_0.pgettext(str_5, str_6)
    str_8 = locale_1.list(str_2)

def test_case_7():
    int_0 = 5399
    locale_0 = module_0.get()
    str_0 = locale_0.format_date(int_0)

def test_case_8():
    str_0 = 'ar'
    null_translations_0 = module_1.NullTranslations()
    gettext_locale_0 = module_0.GettextLocale(str_0, null_translations_0)
    str_1 = 'E4E'
    dict_0 = {}
    str_2 = None
    str_3 = 'Y\n+\x0cmMDv?5F"'
    dict_1 = {str_1: dict_0, str_2: dict_0, str_3: dict_0}
    c_s_v_locale_0 = module_0.CSVLocale(str_1, dict_1)
    str_4 = c_s_v_locale_0.translate(str_0, str_0, gettext_locale_0)

def test_case_9():
    locale_0 = module_0.get()
    str_0 = 'Uncaught exception'
    str_1 = '8f96oV'
    str_2 = locale_0.pgettext(str_0, str_1)
    str_3 = 'UIModule that simply renders the given template.\n\n    {% module Template("foo.html") %} is similar to {% include "foo.html" %},\n    but the module version gets its own namespace (with kwargs passed to\n    Template()) instead of inheriting the outer template\'s namespace.\n\n    Templates rendered through this module also get access to UIModule\'s\n    automatic JavaScript/CSS features.  Simply call set_resources\n    inside the template and give it keyword arguments corresponding to\n    the methods on UIModule: {{ set_resources(js_files=static_url("my.js")) }}\n    Note that these resources are output once per template file, not once\n    per instantiation of the template, so they must not depend on\n    any arguments to the template.\n    '
    str_4 = None
    locale_1 = module_0.get()
    str_5 = locale_1.pgettext(str_3, str_4)

def test_case_10():
    str_0 = 'W^/-$Md7N1u8'
    float_0 = -1211.2
    null_translations_0 = module_1.NullTranslations(float_0)
    gettext_locale_0 = module_0.GettextLocale(str_0, null_translations_0)
    str_1 = gettext_locale_0.pgettext(str_0, str_0)

def test_case_11():
    str_0 = 'An event blocks coroutines until its internal flag is set to True.\n\n    Similar to `threading.Event`.\n\n    A coroutine can wait for an event to be set. Once it is set, calls to\n    ``yield event.wait()`` will not block unless the event has been cleared:\n\n    .. testcode::\n\n        from tornado import gen\n        from tornado.ioloop import IOLoop\n        from tornado.locks import Event\n\n        event = Event()\n\n        async def waiter():\n            print("Waiting for event")\n            await event.wait()\n            print("Not waiting this time")\n            await event.wait()\n            print("Done")\n\n        async def setter():\n            print("About to set the event")\n            event.set()\n\n        async def runner():\n            await gen.multi([waiter(), setter()])\n\n        IOLoop.current().run_sync(runner)\n\n    .. testoutput::\n\n        Waiting for event\n        About to set the event\n        Not waiting this time\n        Done\n    '
    int_0 = -591
    str_1 = 'IIC#iY.4Cs%G8MH'
    null_translations_0 = module_1.NullTranslations(str_1)
    gettext_locale_0 = module_0.GettextLocale(str_1, null_translations_0)
    str_2 = gettext_locale_0.pgettext(str_0, str_0, str_0, int_0)

def test_case_12():
    str_0 = 'L]Pn%s$E^.r!<7EQu#\t'
    str_1 = '`oc'
    float_0 = -2195.0
    str_2 = 'kduK4'
    dict_0 = {str_2: str_2, str_2: str_0}
    str_3 = '08H#v'
    str_4 = '=hw%B^n(n;6'
    dict_1 = {str_2: dict_0, str_2: dict_0, str_3: dict_0, str_4: dict_0}
    c_s_v_locale_0 = module_0.CSVLocale(str_0, dict_1)
    str_5 = c_s_v_locale_0.pgettext(str_1, str_4, str_1, float_0)
    locale_0 = module_0.get()
    str_6 = locale_0.list(str_5)