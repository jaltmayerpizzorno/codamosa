# Automatically generated by Pynguin.
import tornado.locale as module_0
import gettext as module_1

def test_case_0():
    try:
        locale_0 = module_0.get()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '0xL$CeQ+54UIg\\5LN'
        module_0.set_default_locale(str_0)
        str_1 = 'QR'
        str_2 = ''
        int_0 = 2205
        locale_0 = module_0.get()
        str_3 = locale_0.pgettext(str_1, str_2, int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = None
        module_0.load_gettext_translations(str_0, str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        locale_0 = module_0.get()
        str_0 = "]=5{*`/VH'E\t"
        locale_1 = module_0.Locale(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = -1056
        bool_0 = True
        locale_0 = module_0.get()
        str_0 = locale_0.format_date(int_0, bool_0)
        datetime_0 = None
        bool_1 = locale_0.format_day(datetime_0)
    except BaseException:
        pass

def test_case_5():
    try:
        int_0 = 25
        locale_0 = module_0.get()
        str_0 = locale_0.format_date(int_0)
        str_1 = locale_0.list(int_0)
    except BaseException:
        pass

def test_case_6():
    try:
        int_0 = 68
        str_0 = '^ZX|x1T;+sW{'
        str_1 = '=@2DE9E'
        list_0 = [str_0, str_0, str_1]
        locale_0 = module_0.get(*list_0)
        str_2 = locale_0.friendly_number(int_0)
        str_3 = 'x\r\x0b`,|eO#0F'
        locale_1 = module_0.Locale(str_3)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = None
        int_0 = 1470
        str_1 = '~'
        list_0 = [str_0, str_0, str_1, str_1]
        locale_0 = module_0.get(*list_0)
        str_2 = locale_0.friendly_number(int_0)
        str_3 = None
        module_0.load_gettext_translations(str_0, str_3)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = "B\r'}Hx*Lr+$>"
        str_1 = 'Malformed WebSocket request received'
        dict_0 = {}
        c_s_v_locale_0 = module_0.CSVLocale(str_1, dict_0)
        str_2 = c_s_v_locale_0.translate(str_0, str_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'Q7ky$YV\x0c`'
        str_1 = 'Error raised by SimpleAsyncHTTPClient on timeout.\n\n    For historical reasons, this is a subclass of `.HTTPClientError`\n    which simulates a response code of 599.\n\n    .. versionadded:: 5.1\n    '
        dict_0 = {}
        str_2 = '#I Xw_m'
        str_3 = 'C,~/&5b'
        dict_1 = {str_1: dict_0, str_2: dict_0, str_1: dict_0, str_3: dict_0}
        c_s_v_locale_0 = module_0.CSVLocale(str_0, dict_1)
        str_4 = c_s_v_locale_0.pgettext(str_0, str_0)
        locale_0 = module_0.Locale(str_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = None
        null_translations_0 = module_1.NullTranslations()
        gettext_locale_0 = module_0.GettextLocale(str_0, null_translations_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = "\x0bkm'f+NCD+{"
        str_1 = 'en_US'
        null_translations_0 = module_1.NullTranslations()
        gettext_locale_0 = module_0.GettextLocale(str_1, null_translations_0)
        str_2 = gettext_locale_0.translate(str_1, str_0)
    except BaseException:
        pass

def test_case_12():
    try:
        int_0 = -2017
        bool_0 = False
        locale_0 = module_0.get()
        str_0 = '[x%S`n*;@\\]f'
        str_1 = ''
        str_2 = 'zh_CN'
        list_0 = [str_0, str_1, str_2]
        locale_1 = module_0.get(*list_0)
        bool_1 = True
        bool_2 = False
        str_3 = locale_1.format_date(int_0, int_0, bool_2, bool_0, bool_1)
        locale_2 = module_0.Locale(str_1)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = '\t2Lav!km("'
        list_0 = [str_0, str_0]
        list_1 = [str_0, str_0, str_0, str_0]
        locale_0 = module_0.get(*list_1)
        str_1 = locale_0.list(list_0)
        str_2 = '^*>'
        str_3 = 'German'
        str_4 = '\nH]cb_.xgtTPQz\n'
        str_5 = ''
        dict_0 = {str_3: str_2, str_1: str_1, str_4: str_5, str_5: str_0}
        dict_1 = {str_3: dict_0, str_5: dict_0}
        c_s_v_locale_0 = module_0.CSVLocale(str_2, dict_1)
        str_6 = c_s_v_locale_0.translate(str_1)
        float_0 = -321.3
        bool_0 = True
        str_7 = locale_0.format_date(float_0, bool_0, bool_0)
        bool_1 = False
        str_8 = 'uqMV\x0bQP%'
        locale_1 = module_0.get()
        str_9 = locale_1.format_date(float_0, bool_1)
        int_0 = 2109
        str_10 = locale_1.friendly_number(int_0)
        module_0.load_translations(str_8)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = 'Q7ky$YVy`'
        dict_0 = {}
        str_1 = 'C,~/&5b'
        int_0 = -1040
        str_2 = 'zh_CN'
        bytes_0 = b'\x95\x11\xddV+>:\xf7}\xbf\xd8\\\xf6\xf2\x9c\xe8_[\xe2\xe1'
        null_translations_0 = module_1.NullTranslations(bytes_0)
        gettext_locale_0 = module_0.GettextLocale(str_0, null_translations_0)
        str_3 = gettext_locale_0.pgettext(str_0, str_2)
        str_4 = 'bg_BG'
        str_5 = 'A condition allows one or more coroutines to wait until notified.\n\n    Like a standard `threading.Condition`, but does not need an underlying lock\n    that is acquired and released.\n\n    With a `Condition`, coroutines can wait to be notified by other coroutines:\n\n    .. testcode::\n\n        from tornado import gen\n        from tornado.ioloop import IOLoop\n        from tornado.locks import Condition\n\n        condition = Condition()\n\n        async def waiter():\n            print("I\'ll wait right here")\n            await condition.wait()\n            print("I\'m done waiting")\n\n        async def notifier():\n            print("About to notify")\n            condition.notify()\n            print("Done notifying")\n\n        async def runner():\n            # Wait for waiter() and notifier() in parallel\n            await gen.multi([waiter(), notifier()])\n\n        IOLoop.current().run_sync(runner)\n\n    .. testoutput::\n\n        I\'ll wait right here\n        About to notify\n        Done notifying\n        I\'m done waiting\n\n    `wait` takes an optional ``timeout`` argument, which is either an absolute\n    timestamp::\n\n        io_loop = IOLoop.current()\n\n        # Wait up to 1 second for a notification.\n        await condition.wait(timeout=io_loop.time() + 1)\n\n    ...or a `datetime.timedelta` for a timeout relative to the current time::\n\n        # Wait up to 1 second.\n        await condition.wait(timeout=datetime.timedelta(seconds=1))\n\n    The method returns False if there\'s no notification before the deadline.\n\n    .. versionchanged:: 5.0\n       Previously, waiters could be notified synchronously from within\n       `notify`. Now, the notification will always be received on the\n       next iteration of the `.IOLoop`.\n    '
        str_6 = 'Pn{B>JVA>'
        list_0 = [str_4, str_6, str_5, str_6]
        locale_0 = module_0.get(*list_0)
        str_7 = 'F#_7Y4\x0b&ejT}sQ3hQy'
        dict_1 = {str_7: dict_0, str_5: dict_0}
        c_s_v_locale_0 = module_0.CSVLocale(str_7, dict_1)
        str_8 = locale_0.format_date(int_0)
        dict_2 = {str_0: dict_0, str_1: dict_0, str_0: dict_0, str_1: dict_0}
        c_s_v_locale_1 = module_0.CSVLocale(str_0, dict_2)
        str_9 = c_s_v_locale_1.pgettext(str_0, str_0)
        int_1 = None
        str_10 = locale_0.friendly_number(int_0)
        int_2 = 6
        str_11 = locale_0.format_date(int_1, int_2)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = 'Q7ky$YVy`'
        dict_0 = {}
        str_1 = '0UZ[K19'
        list_0 = [str_0, str_1]
        locale_0 = module_0.get(*list_0)
        str_2 = locale_0.list(str_0)
        int_0 = -1040
        str_3 = 'h)N'
        bytes_0 = b'\x95\x11\xddV+>:\xf7}\xbf\xd8\\\xf6\xf2\x9c\xe8_[\xe2\xe1'
        null_translations_0 = module_1.NullTranslations(bytes_0)
        gettext_locale_0 = module_0.GettextLocale(str_0, null_translations_0)
        str_4 = gettext_locale_0.pgettext(str_0, str_3)
        str_5 = 'bg_BG'
        str_6 = 'A condition allows one or more coroutines to wait until notified.\n\n    Like a standard `threading.Condition`, but does not need an underlying lock\n    that is acquired and released.\n\n    With a `Condition`, coroutines can wait to be notified by other coroutines:\n\n    .. testcode::\n\n        from tornado import gen\n        from tornado.ioloop import IOLoop\n        from tornado.locks import Condition\n\n        condition = Condition()\n\n        async def waiter():\n            print("I\'ll wait right here")\n            await condition.wait()\n            print("I\'m done waiting")\n\n        async def notifier():\n            print("About to notify")\n            condition.notify()\n            print("Done notifying")\n\n        async def runner():\n            # Wait for waiter() and notifier() in parallel\n            await gen.multi([waiter(), notifier()])\n\n        IOLoop.current().run_sync(runner)\n\n    .3 testoutput::\n\n        I\'ll wait right here\n        About to notify\n        Done notifying\n        I\'m done waiting\n\n    `wait` takes an optional ``timeout`` argument, which is either an absolute\n    timestamp::\n\n        io_loop = IOLoop.current()\n\n        # Wait up to 1 second for a notification.\n        await condition.wait(timeout=io_loop.time() + 1)\n\n    ...or a `datetime.timedelta` for a timeout relative to the current time::\n\n        # Wait up to 1 second.\n        await condition.wait(timeout=datetime.timedelta(seconds=1))\n\n    The method returns False if there\'s no notification before the deadline.\n\n    .. versionchanged:: 5.0\n       Previously, waiters could be notified synchronously from within\n       `notify`. Now, the notification will always be received on the\n       next iteration of the `.IOLoop`.\n    '
        str_7 = 'Pn{B>JVA>'
        list_1 = [str_5, str_7, str_6, str_7]
        locale_1 = module_0.get(*list_1)
        str_8 = 'F#_7Y4\x0b&ejT}sQ3hQy'
        dict_1 = {str_8: dict_0, str_6: dict_0}
        c_s_v_locale_0 = module_0.CSVLocale(str_8, dict_1)
        str_9 = locale_1.format_date(int_0)
        str_10 = "vnJ!NWW wXB*'P"
        str_11 = gettext_locale_0.pgettext(str_1, str_10, str_1)
    except BaseException:
        pass

def test_case_16():
    try:
        int_0 = 33
        locale_0 = module_0.get()
        str_0 = locale_0.format_date(int_0)
        module_0.load_translations(str_0)
    except BaseException:
        pass

def test_case_17():
    try:
        int_0 = -2002
        bool_0 = True
        locale_0 = module_0.get()
        str_0 = '[x%S`n*;@\\]f'
        str_1 = ''
        list_0 = [str_0, str_1, str_0]
        locale_1 = module_0.get(*list_0)
        bool_1 = False
        str_2 = locale_1.format_date(int_0, int_0, bool_1, bool_0, bool_1)
        locale_2 = module_0.get()
        int_1 = 443
        str_3 = 'Ml4NatI6'
        str_4 = locale_0.translate(str_3)
        str_5 = locale_0.friendly_number(int_1)
        str_6 = locale_1.list(str_5)
        str_7 = "V(Ojkx'b[.h(!~*_lcud"
        locale_3 = module_0.Locale(str_7)
    except BaseException:
        pass

def test_case_18():
    try:
        str_0 = 'Q7ky$YVy`'
        dict_0 = {}
        str_1 = 'C,~/&5b'
        iterable_0 = module_0.get_supported_locales()
        int_0 = -1043
        str_2 = 'zh_CN'
        bytes_0 = b'\x95\x11\xddV+>:\xf7}\xbf\xd8\\\xf6\xf2\x9c\xe8_[\xe2\xe1'
        null_translations_0 = module_1.NullTranslations(bytes_0)
        gettext_locale_0 = module_0.GettextLocale(str_0, null_translations_0)
        str_3 = gettext_locale_0.pgettext(str_0, str_2)
        str_4 = '\x0b4?"LQ'
        str_5 = 'A condition allows one or more coroutines to wait until notified.\n\n    Like a standard `threading.Condition`, but does not need an underlying lock\n    that is acquired and released.\n\n    With a `Condition`, coroutines can wait to be notified by other coroutines:\n\n    .. testcode::\n\n        from tornado import gen\n        from tornado.ioloop import IOLoop\n        from tornado.locks import Condition\n\n        condition = Condition()\n\n        async def waiter():\n            print("I\'ll wait right here")\n            await condition.wait()\n            print("I\'m done waiting")\n\n        async def notifier():\n            print("About to notify")\n            condition.notify()\n            print("Done notifying")\n\n        async def runner():\n            # Wait for waiter() and notifier() in parallel\n            await gen.multi([waiter(), notifier()])\n\n        IOLoop.current().run_sync(runner)\n\n    .. testoutput::\n\n        I\'ll wait right here\n        About to notify\n        Done notifying\n        I\'m done waiting\n\n    `wait` takes an optional ``timeout`` argument, which is either an absolute\n    timestamp::\n\n        io_loop = IOLoop.current()\n\n        # Wait up to 1 second for a notification.\n        await condition.wait(timeout=io_loop.time() + 1)\n\n    ...or a `datetime.timedelta` for a timeout relative to the current time::\n\n        # Wait up to 1 second.\n        await condition.wait(timeout=datetime.timedelta(seconds=1))\n\n    The method returns False if there\'s no notification before the deadline.\n\n    .. versionchanged:: 5.0\n       Previously, waiters could be notified synchronously from within\n       `notify`. Now, the notification will always be received on the\n       next iteration of the `.IOLoop`.\n    '
        str_6 = 'kJ5'
        str_7 = 'Returns url string for a given route name and arguments\n        or ``None`` if no match is found.\n\n        :arg str name: route name.\n        :arg args: url parameters.\n        :returns: parametrized url string for a given route name (or ``None``).\n        '
        str_8 = gettext_locale_0.pgettext(str_6, str_7, str_7, int_0)
        str_9 = '9'
        str_10 = 'gK0]'
        str_11 = 'Instance method called when an IOLoop ceases to be current.\n\n        May be overridden by subclasses as a counterpart to make_current.\n        '
        dict_1 = {str_9: str_5, str_10: int_0, str_11: str_3}
        var_0 = null_translations_0.set_output_charset(dict_1)
        str_12 = 'Pn{B>JVA>'
        list_0 = [str_4, str_12, str_12, str_5, str_12, str_3]
        locale_0 = module_0.get(*list_0)
        str_13 = 'F#_7Y4\x0b&ejT}sQ3hQy'
        dict_2 = {str_13: dict_0, str_5: dict_0}
        c_s_v_locale_0 = module_0.CSVLocale(str_13, dict_2)
        str_14 = locale_0.format_date(int_0)
        dict_3 = {str_0: dict_0, str_1: dict_0, str_0: dict_0, str_1: dict_0}
        c_s_v_locale_1 = module_0.CSVLocale(str_0, dict_3)
        str_15 = c_s_v_locale_1.pgettext(str_0, str_0)
        str_16 = None
        module_0.load_translations(str_16)
        str_17 = locale_0.list(iterable_0)
    except BaseException:
        pass

def test_case_19():
    try:
        int_0 = -2002
        bool_0 = True
        locale_0 = module_0.get()
        str_0 = '[x%S`n*;@\\]f'
        str_1 = ''
        str_2 = 'zaCN'
        list_0 = [str_0, str_1, str_2]
        locale_1 = module_0.get(*list_0)
        bool_1 = True
        bool_2 = False
        str_3 = locale_1.format_date(int_0, int_0, bool_2, bool_0, bool_1)
        locale_2 = module_0.get()
        int_1 = 443
        str_4 = locale_0.friendly_number(int_1)
        str_5 = locale_1.list(str_4)
        str_6 = "V(Ojkx'b[.h(!~*_lcud"
        locale_3 = module_0.Locale(str_6)
    except BaseException:
        pass

def test_case_20():
    try:
        str_0 = 'Catalan'
        int_0 = 1148
        str_1 = '-]{)OGjQZES8/_>'
        null_translations_0 = module_1.NullTranslations()
        gettext_locale_0 = module_0.GettextLocale(str_1, null_translations_0)
        str_2 = gettext_locale_0.translate(str_0, str_0, int_0)
        str_3 = 'test'
        str_4 = None
        module_0.load_gettext_translations(str_4, str_3)
    except BaseException:
        pass

def test_case_21():
    try:
        iterable_0 = module_0.get_supported_locales()
        str_0 = 'ar'
        locale_0 = module_0.Locale(str_0)
    except BaseException:
        pass