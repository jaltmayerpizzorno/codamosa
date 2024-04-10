# Automatically generated by Pynguin.
import tornado.locale as module_0
import gettext as module_1
import datetime as module_2

def test_case_0():
    try:
        str_0 = 'AH)E^NysG[b'
        module_0.load_gettext_translations(str_0, str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'H~'
        locale_0 = module_0.Locale(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'Asynchronously reads all data from the socket until it is closed.\n\n        This will buffer all available data until ``max_buffer_size``\n        is reached. If flow control or cancellation are desired, use a\n        loop with `read_bytes(partial=True) <.read_bytes>` instead.\n\n        .. versionchanged:: 4.0\n            The callback argument is now optional and a `.Future` will\n            be returned if it is omitted.\n\n        .. versionchanged:: 6.0\n\n           The ``callback`` and ``streaming_callback`` arguments have\n           been removed. Use the returned `.Future` (and `read_bytes`\n           with ``partial=True`` for ``streaming_callback``) instead.\n\n        '
        iterable_0 = module_0.get_supported_locales()
        int_0 = 1174
        locale_0 = module_0.get()
        str_1 = locale_0.friendly_number(int_0)
        locale_1 = module_0.Locale(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = ''
        str_1 = 'Provides an iterator to yield the results of awaitables as they finish.\n\n    Yielding a set of awaitables like this:\n\n    ``results = yield [awaitable1, awaitable2]``\n\n    pauses the coroutine until both ``awaitable1`` and ``awaitable2``\n    return, and then restarts the coroutine with the results of both\n    awaitables. If either awaitable raises an exception, the\n    expression will raise that exception and all the results will be\n    lost.\n\n    If you need to get the result of each awaitable as soon as possible,\n    or if you need the result of some awaitables even if others produce\n    errors, you can use ``WaitIterator``::\n\n      wait_iterator = gen.WaitIterator(awaitable1, awaitable2)\n      while not wait_iterator.done():\n          try:\n              result = yield wait_iterator.next()\n          except Exception as e:\n              print("Error {} from {}".format(e, wait_iterator.current_future))\n          else:\n              print("Result {} received from {} at {}".format(\n                  result, wait_iterator.current_future,\n                  wait_iterator.current_index))\n\n    Because results are returned as soon as they are available the\n    output from the iterator *will not be in the same order as the\n    input arguments*. If you need to know which future produced the\n    current result, you can use the attributes\n    ``WaitIterator.current_future``, or ``WaitIterator.current_index``\n    to get the index of the awaitable from the input list. (if keyword\n    arguments were used in the construction of the `WaitIterator`,\n    ``current_index`` will use the corresponding keyword).\n\n    On Python 3.5, `WaitIterator` implements the async iterator\n    protocol, so it can be used with the ``async for`` statement (note\n    that in this version the entire iteration is aborted if any value\n    raises an exception, while the previous example can continue past\n    individual errors)::\n\n      async for result in gen.WaitIterator(future1, future2):\n          print("Result {} received from {} at {}".format(\n              result, wait_iterator.current_future,\n              wait_iterator.current_index))\n\n    .. versionadded:: 4.1\n\n    .. versionchanged:: 4.3\n       Added ``async for`` support in Python 3.5.\n\n    '
        int_0 = -4872
        list_0 = []
        locale_0 = module_0.get(*list_0)
        str_2 = locale_0.pgettext(str_0, str_1, int_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'n5'
        int_0 = -2861
        str_1 = 'y-iAhv"-6Ll0<*'
        str_2 = '1<Z` kwZXTBNQ(F'
        str_3 = '*\nZ2zi]iQ0Q'
        str_4 = None
        dict_0 = {str_1: str_1, str_2: str_2, str_3: str_1, str_4: str_2}
        str_5 = "qB&C/]+#'/P)o) 2-[C "
        str_6 = None
        dict_1 = {str_1: dict_0, str_5: dict_0, str_6: dict_0, str_4: dict_0}
        c_s_v_locale_0 = module_0.CSVLocale(str_1, dict_1)
        str_7 = c_s_v_locale_0.pgettext(str_0, str_0, int_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = ''
        null_translations_0 = module_1.NullTranslations()
        var_0 = null_translations_0.install()
        gettext_locale_0 = module_0.GettextLocale(str_0, null_translations_0)
        str_1 = gettext_locale_0.translate(str_0)
        str_2 = 'oob'
        str_3 = gettext_locale_0.pgettext(str_2, str_2)
        str_4 = "?'f`+gLvyOR"
        int_0 = 365
        str_5 = gettext_locale_0.translate(str_4, int_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'l{ 12|&'
        module_0.set_default_locale(str_0)
        set_0 = set()
        str_1 = '${_L|a%&'
        null_translations_0 = module_1.NullTranslations()
        gettext_locale_0 = module_0.GettextLocale(str_1, null_translations_0)
        str_2 = gettext_locale_0.translate(str_0, str_0, set_0)
        module_0.load_gettext_translations(str_0, str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        int_0 = 1
        timedelta_0 = module_2.timedelta()
        bool_0 = True
        list_0 = []
        locale_0 = module_0.get(*list_0)
        str_0 = locale_0.format_date(int_0, bool_0)
        str_1 = "|cREK\tv@Z:clb'z"
        str_2 = 'd2N'
        null_translations_0 = module_1.NullTranslations()
        gettext_locale_0 = module_0.GettextLocale(str_2, null_translations_0)
        str_3 = gettext_locale_0.pgettext(str_1, str_1, str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        null_translations_0 = module_1.NullTranslations()
        int_0 = -1828
        locale_0 = module_0.get()
        str_0 = '@tornado.web.authenticated'
        str_1 = 'Try to convert an ``ssl_options`` dictionary to an\n    `~ssl.SSLContext` object.\n\n    The ``ssl_options`` dictionary contains keywords to be passed to\n    `ssl.wrap_socket`.  In Python 2.7.9+, `ssl.SSLContext` objects can\n    be used instead.  This function converts the dict form to its\n    `~ssl.SSLContext` equivalent, and may be used when a component which\n    accepts both forms needs to upgrade to the `~ssl.SSLContext` version\n    to use features like SNI or NPN.\n    '
        list_0 = [str_0, str_1]
        locale_1 = module_0.get(*list_0)
        locale_2 = module_0.get()
        str_2 = locale_0.friendly_number(int_0)
        datetime_0 = module_2.datetime()
    except BaseException:
        pass

def test_case_9():
    try:
        int_0 = 480
        bool_0 = False
        str_0 = 'try'
        list_0 = [str_0]
        locale_0 = module_0.get(*list_0)
        int_1 = 560
        str_1 = locale_0.friendly_number(int_1)
        str_2 = locale_0.format_date(int_0, int_0, bool_0)
        locale_1 = module_0.Locale(str_2)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = 'Asynchronously reads all data from the socket until it is closed.\n\n        This will buffer all available data until ``max_buffer_size``\n        is reached. If flow control or cancellation are desired, use a\n        loop with `read_bytes(partial=True) <.read_bytes>` instead.\n\n        .. versionchanged:: 4.0\n            The callback argument is now optional and a `.Future` will\n            be returned if it is omitted.\n\n        .. versionchanged:: 6.0\n\n           The ``callback`` and ``streaming_callback`` arguments have\n           been removed. Use the returned `.Future` (and `read_bytes`\n           with ``partial=True`` for ``streaming_callback``) instead.\n\n        '
        iterable_0 = module_0.get_supported_locales()
        int_0 = 1174
        locale_0 = module_0.get()
        str_1 = locale_0.friendly_number(int_0)
        str_2 = "K',iouf\x0bw]s3tug"
        str_3 = '^c'
        str_4 = '('
        dict_0 = {str_0: str_3, str_4: str_2}
        str_5 = locale_0.list(str_4)
        str_6 = 'x-Lh~k/-2*b\n|'
        null_translations_0 = module_1.NullTranslations()
        gettext_locale_0 = module_0.GettextLocale(str_6, null_translations_0)
        dict_1 = {str_4: dict_0, str_3: dict_0, str_2: dict_0, str_4: dict_0}
        c_s_v_locale_0 = module_0.CSVLocale(str_3, dict_1)
        datetime_0 = module_2.datetime()
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = '_{T4h2`U~o'
        str_1 = 'HLB~'
        null_translations_0 = module_1.NullTranslations()
        gettext_locale_0 = module_0.GettextLocale(str_1, null_translations_0)
        str_2 = gettext_locale_0.pgettext(str_0, str_1)
        locale_0 = module_0.get()
        var_0 = null_translations_0.pgettext(locale_0, locale_0)
        str_3 = '@tornado.web.authenticated'
        str_4 = 'Try to convert an ``ssl_options`` dictionary to an\n    `~ssl.SSLContext` object.\n\n    The ``ssl_options`` dictionary contains keywords to be passed to\n    `ssl.wrap_socket`.  In Python 2.7.9+, `ssl.SSLContext` objects can\n    be used instead.  This function converts the dict form to its\n    `~ssl.SSLContext` equivalent, and may be used when a component which\n    accepts both forms needs to upgrade to the `~ssl.SSLContext` version\n    to use features like SNI or NPN.\n    '
        list_0 = [str_3, str_0, str_4]
        locale_1 = module_0.get(*list_0)
        locale_2 = module_0.Locale(str_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = '_{T4h2`U~o'
        str_1 = 'HLB~'
        null_translations_0 = module_1.NullTranslations()
        gettext_locale_0 = module_0.GettextLocale(str_1, null_translations_0)
        str_2 = gettext_locale_0.pgettext(str_0, str_1)
        int_0 = -1828
        bool_0 = True
        int_1 = None
        str_3 = '@tornado.web.authenticated'
        str_4 = 'Try to convert an ``ssl_options`` dictionary to an\n    `~ssl.SSLContext` object.\n\n    The ``ssl_options`` dictionary contains keywords to be passed to\n    `ssl.wrap_socket`.  In Python 2.7.9+, `ssl.SSLContext` objects can\n    be used instead.  This function converts the dict form to its\n    `~ssl.SSLContext` equivalent, and may be used when a component which\n    accepts both forms needs to upgrade to the `~ssl.SSLContext` version\n    to use features like SNI or NPN.\n    '
        list_0 = [str_3, str_0, str_4]
        locale_0 = module_0.get(*list_0)
        locale_1 = module_0.get()
        str_5 = locale_1.format_date(int_0, bool_0)
        str_6 = locale_0.format_date(int_0)
        int_2 = -565
        bool_1 = True
        str_7 = '\t6+IYApaXx\r#r[fOHvtb'
        list_1 = [str_4, str_7]
        locale_2 = module_0.get(*list_1)
        str_8 = locale_2.format_date(int_1, int_2, bool_1, bool_1)
    except BaseException:
        pass

def test_case_13():
    try:
        int_0 = 14
        var_0 = int_0 - int_0
        str_0 = 'zh_CN'
        module_0.set_default_locale(str_0)
        list_0 = [str_0, str_0]
        locale_0 = module_0.get(*list_0)
        bool_0 = False
        bool_1 = True
        str_1 = locale_0.format_date(int_0, bool_0, bool_1)
        str_2 = 'fa'
        locale_1 = module_0.Locale(str_2)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = 'Asynchronously reads all data from the socket until it is closed.\n\n        This will buffer all available data until ``max_buffer_size``\n        is reached. If flow control or cancellation are desired, use a\n        loop with `read_bytes(partial=True) <.read_bytes>` instead.\n\n        .. versionchanged:: 4.0\n            The callback argument is now optional and a `.Future` will\n            be returned if it is omitted.\n\n        .. versionchanged:: 6.0\n\n           The ``callback`` and ``streaming_callback`` arguments have\n           been removed. Use the returned `.Future` (and `read_bytes`\n           with ``partial=True`` for ``streaming_callback``) instead.\n\n        '
        iterable_0 = module_0.get_supported_locales()
        int_0 = 1174
        locale_0 = module_0.get()
        str_1 = locale_0.friendly_number(int_0)
        str_2 = "K',iouf\x0bw]s3tug"
        str_3 = '^c'
        str_4 = ''
        dict_0 = {str_0: str_3, str_4: str_2}
        str_5 = locale_0.list(str_4)
        str_6 = 'x-Lh~k/-2*b\n|'
        null_translations_0 = module_1.NullTranslations()
        gettext_locale_0 = module_0.GettextLocale(str_6, null_translations_0)
        dict_1 = {str_4: dict_0, str_3: dict_0, str_2: dict_0, str_4: dict_0}
        c_s_v_locale_0 = module_0.CSVLocale(str_3, dict_1)
        datetime_0 = module_2.datetime()
    except BaseException:
        pass

def test_case_15():
    try:
        int_0 = 14
        var_0 = int_0 * int_0
        var_1 = int_0 - var_0
        str_0 = 'fa'
        locale_0 = module_0.Locale(str_0)
    except BaseException:
        pass

def test_case_16():
    try:
        locale_0 = module_0.get()
        datetime_0 = None
        bool_0 = False
        bool_1 = locale_0.format_day(datetime_0, bool_0)
    except BaseException:
        pass