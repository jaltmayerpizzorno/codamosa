# Automatically generated by Pynguin.
import tornado.escape as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'Updates the dictionary with a single header line.\n\n        >>> h = HTTPHeaders()\n        >>> h.parse_line("Content-Type: text/html")\n        >>> h.get(\'content-type\')\n        \'text/html\'\n        '
    str_1 = module_0.xhtml_escape(str_0)

def test_case_2():
    bytes_0 = b''
    str_0 = module_0.xhtml_unescape(bytes_0)

def test_case_3():
    list_0 = []
    str_0 = module_0.json_encode(list_0)

def test_case_4():
    str_0 = 'Convenience method to synchronously fetch a URL.\n\n        The given path will be appended to the local server\'s host and\n        port.  Any additional keyword arguments will be passed directly to\n        `.AsyncHTTPClient.fetch` (and so could be used to pass\n        ``method="POST"``, ``body="..."``, etc).\n\n        If the path begins with http:// or https://, it will be treated as a\n        full URL and will be fetched as-is.\n\n        If ``raise_error`` is ``True``, a `tornado.httpclient.HTTPError` will\n        be raised if the response code is not 200. This is the same behavior\n        as the ``raise_error`` argument to `.AsyncHTTPClient.fetch`, but\n        the default is ``False`` here (it\'s ``True`` in `.AsyncHTTPClient`)\n        because tests often need to deal with non-200 response codes.\n\n        .. versionchanged:: 5.0\n           Added support for absolute URLs.\n\n        .. versionchanged:: 5.1\n\n           Added the ``raise_error`` argument.\n\n        .. deprecated:: 5.1\n\n           This method currently turns any exception into an\n           `.HTTPResponse` with status code 599. In Tornado 6.0,\n           errors other than `tornado.httpclient.HTTPError` will be\n           passed through, and ``raise_error=False`` will only\n           suppress errors that would be raised due to non-200\n           response codes.\n\n        '
    str_1 = module_0.squeeze(str_0)
    optional_0 = module_0.to_unicode(str_0)
    str_2 = module_0.linkify(str_1)
    str_3 = 'j$OYwh/S'
    var_0 = module_0.url_unescape(str_3, str_2)

def test_case_5():
    bytes_0 = b''
    bool_0 = True
    var_0 = module_0.url_unescape(bytes_0, bool_0)
    any_0 = module_0.recursive_unicode(var_0)
    str_0 = module_0.json_encode(bool_0)

def test_case_6():
    str_0 = '!Xm3$XW9'
    str_1 = module_0.xhtml_escape(str_0)
    bool_0 = None
    str_2 = module_0.url_escape(str_0, bool_0)
    bytes_0 = b'\xcfg\xc1'
    bool_1 = True
    str_3 = module_0.xhtml_unescape(str_1)
    bytes_1 = b'\xbb\xd0=\xc2'
    dict_0 = module_0.parse_qs_bytes(bytes_1)
    str_4 = module_0.url_escape(bytes_0, bool_1)

def test_case_7():
    str_0 = 'N`&pOaSH[\\KU\\=|'
    str_1 = module_0.json_encode(str_0)
    bool_0 = True
    str_2 = 'WK*Q)<vkpn_mRXZ'
    str_3 = module_0.json_encode(str_0)
    str_4 = module_0.squeeze(str_2)
    dict_0 = module_0.parse_qs_bytes(str_0, bool_0)
    str_5 = module_0.json_encode(str_0)
    str_6 = module_0.xhtml_escape(str_0)
    str_7 = module_0.json_encode(str_0)
    bool_1 = True
    var_0 = module_0.url_unescape(str_0)
    var_1 = module_0.url_unescape(str_0, str_7)
    list_0 = []
    str_8 = module_0.linkify(str_6, bool_1, str_6, list_0)
    any_0 = module_0.recursive_unicode(dict_0)

def test_case_8():
    str_0 = 'a www.google.com'
    str_1 = module_0.linkify(str_0)

def test_case_9():
    str_0 = 'yqgg 1-.z^]y'
    dict_0 = module_0.parse_qs_bytes(str_0)
    bool_0 = False
    dict_1 = module_0.parse_qs_bytes(str_0, bool_0)
    bool_1 = True
    optional_0 = module_0.utf8(str_0)
    str_1 = module_0.url_escape(str_0, bool_1)
    dict_2 = module_0.parse_qs_bytes(str_1)
    str_2 = module_0.linkify(str_0, bool_0, str_0)
    var_0 = module_0.url_unescape(str_0, str_0)
    str_3 = module_0.xhtml_escape(str_0)
    var_1 = module_0.url_unescape(str_2, bool_0)
    any_0 = module_0.recursive_unicode(var_1)
    str_4 = module_0.json_encode(bool_0)

def test_case_10():
    str_0 = 'a+b%20c'
    var_0 = module_0.url_unescape(str_0)
    bytes_0 = b'a+b+c'
    var_1 = module_0.url_unescape(bytes_0)
    bool_0 = False
    var_2 = module_0.url_unescape(bytes_0, bool_0)
    bytes_1 = b'a%2Bb+c'
    var_3 = None
    var_4 = module_0.url_unescape(bytes_1, var_3, bool_0)

def test_case_11():
    str_0 = 'http://example.com'
    str_1 = module_0.linkify(str_0)
    bool_0 = False
    str_2 = module_0.linkify(str_0, bool_0)
    bool_1 = True
    str_3 = module_0.linkify(str_0, bool_1)
    bool_2 = False
    var_0 = module_0.url_unescape(str_0, str_0, bool_2)
    var_1 = module_0.url_unescape(str_0)

def test_case_12():
    str_0 = 'yqgg 1-.z^]y'
    dict_0 = module_0.parse_qs_bytes(str_0)
    bool_0 = False
    dict_1 = module_0.parse_qs_bytes(str_0, bool_0)
    bool_1 = True
    optional_0 = module_0.utf8(str_0)
    str_1 = module_0.url_escape(str_0, bool_1)
    dict_2 = module_0.parse_qs_bytes(str_1)
    str_2 = module_0.linkify(str_0, bool_0, str_0)
    var_0 = module_0.url_unescape(str_0, str_0)
    str_3 = module_0.xhtml_escape(str_0)
    optional_1 = module_0.to_unicode(str_2)
    any_0 = module_0.recursive_unicode(dict_2)
    str_4 = module_0.xhtml_unescape(str_1)
    str_5 = module_0.json_encode(var_0)

def test_case_13():
    str_0 = 'test http://example.com/test.html is\nwww.example.com/test'
    str_1 = module_0.linkify(str_0)

def test_case_14():
    str_0 = 'http://example.com https://example2.com example3.com/foo/bar www.example4.com'
    bool_0 = False
    str_1 = 'http://ww|.yahoo.com^index.html'
    str_2 = None
    str_3 = 'YW'
    list_0 = [str_1, str_2, str_2, str_3]
    str_4 = module_0.linkify(str_0, str_0, bool_0, list_0)

def test_case_15():
    str_0 = 'This is a test url http://www.yahoo.com'
    str_1 = 'This is a test url http://www.yahoo.com/index.html'
    bool_0 = False
    var_0 = module_0.url_unescape(str_1, str_0, bool_0)
    str_2 = 'Convenience method to synchronously fetch a URL.\n\n        The given path will be appended to the local server\'s host and\n        port.  Any additional keyword arguments will be passed directly to\n        `.AsyncHTTPClient.fetch` (and so could be used to pass\n        ``method="POST"``, ``body="..."``, etc).\n\n        If the path begins with http:// or https://, it will be treated as a\n        full URL and will be fetched as-is.\n\n        If ``raise_error`` is ``True``, a `tornado.httpclient.HTTPError` will\n        be raised if the response code is not 200. This is the same behavior\n        as the ``raise_error`` argument to `.AsyncHTTPClient.fetch`, but\n        the default is ``False`` here (it\'s ``True`` in `.AsyncHTTPClient`)\n        because tests often need to deal with non-200 response codes.\n\n        .. versionchanged:: 5.0\n           Added support for absolute URLs.\n\n        .. versionchanged:: 5.1\n\n           Added the ``raise_error`` argument.\n\n        .. deprecated:: 5.1\n\n           This method currently turns any exception into an\n           `.HTTPResponse` with status code 599. In Tornado 6.0,\n           errors other than `tornado.httpclient.HTTPError` will be\n           passed through, and ``raise_error=False`` will only\n           suppress errors that would be raised due to non-200\n           response codes.\n\n        '
    str_3 = module_0.json_encode(str_0)
    str_4 = module_0.url_escape(str_1)
    str_5 = module_0.linkify(str_1, str_0)
    any_0 = module_0.recursive_unicode(bool_0)
    optional_0 = module_0.to_unicode(str_2)
    str_6 = 'i$o'
    str_7 = '^\t"53M'
    list_0 = [str_6, str_7, str_4]
    str_8 = module_0.linkify(str_2, list_0)
    var_1 = module_0.url_unescape(str_4)
    any_1 = module_0.recursive_unicode(bool_0)
    str_9 = module_0.xhtml_unescape(str_8)

def test_case_16():
    str_0 = 'This is a test url http://www.yahoo.com/index.html'
    bool_0 = True
    str_1 = module_0.linkify(str_0, bool_0)
    list_0 = []
    str_2 = module_0.linkify(str_1, list_0)
    str_3 = module_0.xhtml_escape(str_1)
    any_0 = module_0.recursive_unicode(bool_0)
    str_4 = module_0.xhtml_unescape(str_3)
    str_5 = module_0.json_encode(str_2)

def test_case_17():
    str_0 = 'This is a test url http://www.yahoo.com'
    str_1 = 'This is a test url http://www.yahoo.com^index.html'
    bool_0 = False
    var_0 = module_0.url_unescape(str_1, str_0, bool_0)
    str_2 = 'Convenience method to synchronously fetch a URL.\n\n        The given path will be appended to the local server\'s host and\n        port.  Any additional keyword arguments will be passed directly to\n        `.AsyncHTTPClient.fetch` (and so could be used to pass\n        ``method="POST"``, ``body="..."``, etc).\n\n        If the path begins with http:// or https://, it will be treated as a\n        full URL and will be fetched as-is.\n\n        If ``raise_error`` is ``True``, a `tornado.httpclient.HTTPError` will\n        be raised if the response code is not 200. This is the same behavior\n        as the ``raise_error`` argument to `.AsyncHTTPClient.fetch`, but\n        the default is ``False`` here (it\'s ``True`` in `.AsyncHTTPClient`)\n        because tests often need to deal with non-200 response codes.\n\n        .. versionchanged:: 5.0\n           Added support for absolute URLs.\n\n        .. versionchanged:: 5.1\n\n           Added the ``raise_error`` argument.\n\n        .. deprecated:: 5.1\n\n           This method currently turns any exception into an\n           `.HTTPResponse` with status code 599. In Tornado 6.0,\n           errors other than `tornado.httpclient.HTTPError` will be\n           passed through, and ``raise_error=False`` will only\n           suppress errors that would be raised due to non-200\n           response codes.\n\n        '
    str_3 = '~Z3U^O)twY0'
    optional_0 = module_0.to_unicode(str_2)
    dict_0 = module_0.parse_qs_bytes(str_0, bool_0)
    bool_1 = True
    list_0 = [str_3, str_3]
    str_4 = module_0.linkify(str_2, bool_0, str_3, bool_1, list_0)
    optional_1 = module_0.to_unicode(str_2)
    str_5 = module_0.linkify(str_1, str_4)
    any_0 = module_0.recursive_unicode(bool_0)
    any_1 = module_0.recursive_unicode(any_0)
    str_6 = 'flJ;j{#YH=-'
    list_1 = [str_6, str_0, str_2, str_1]
    str_7 = module_0.linkify(str_2, list_1)
    var_1 = module_0.url_unescape(str_3)
    str_8 = module_0.xhtml_unescape(str_4)
    str_9 = module_0.json_encode(list_0)
    str_10 = module_0.json_encode(str_4)

def test_case_18():
    str_0 = '\n    This is an example of linkify http://example.com,\n    www.example.com and sub1.example.com/page,\n    as well as a mailto:test@example.com.\n    '
    str_1 = 'This is an example of linkify <a href="http://example.com">http://example.com</a>,\n<a href="http://www.example.com">www.example.com</a> and <a href="http://sub1.example.com/page">sub1.example.com/page</a>,\nas well as a <a href="mailto:test@example.com">mailto:test@example.com</a>.'
    bool_0 = True
    str_2 = '2$ZZg+)6PEw%,'
    str_3 = 'http://example.com/index.html?x=y'
    list_0 = [str_2, str_3]
    str_4 = module_0.linkify(str_1, bool_0, str_0, list_0)
    str_5 = module_0.linkify(str_4, str_4)

def test_case_19():
    str_0 = 'This is a test url http://www.yahoo.com'
    str_1 = 'This is a test url http://www.yahoo.com^index.html'
    str_2 = 'Convenience method to synchronously fetch a URL.\n\n        The given path will be appended to the local server\'s host and\n        port.  Any additional keyword arguments will be passed directly to\n        `.AsyncHTTPClient.fetch` (and so could be used to pass\n        ``method="POST"``, ``body="..."``, etc).\n\n        If the path begins with http:// or https://, it will be treated as a\n        full URL and will be fetched as-is.\n\n        If ``raise_error`` is ``True``, a `tornado.httpclient.HTTPError` will\n        be raised if the response code is not 200. This is the same behavior\n        as the ``raise_error`` argument to `.AsyncHTTPClient.fetch`, but\n        the default is ``False`` here (it\'s ``True`` in `.AsyncHTTPClient`)\n        because tests often need to deal with non-200 response codes.\n\n        .. versionchanged:: 5.0\n           Added support for absolute URLs.\n\n        .. versionchanged:: 5.1\n\n           Added the ``raise_error`` argument.\n\n        .. deprecated:: 5.1\n\n           This method currently turns any exception into an\n           `.HTTPResponse` with status code 599. In Tornado 6.0,\n           errors other than `tornado.httpclient.HTTPError` will be\n           passed through, and ``raise_error=False`` will only\n           suppress errors that would be raised due to non-200\n           response codes.\n\n        '
    str_3 = module_0.squeeze(str_0)
    str_4 = module_0.json_encode(str_0)
    str_5 = '~Z3U^O)twY0'
    optional_0 = module_0.to_unicode(str_4)
    str_6 = module_0.url_escape(str_3)
    bool_0 = None
    str_7 = module_0.linkify(str_1, str_3)
    any_0 = module_0.recursive_unicode(bool_0)
    optional_1 = module_0.to_unicode(str_2)
    any_1 = module_0.json_decode(str_4)
    str_8 = '?9'
    str_9 = '\t"53M'
    list_0 = [str_8, str_9]
    str_10 = module_0.linkify(str_2, list_0)
    var_0 = module_0.url_unescape(str_5)
    any_2 = module_0.recursive_unicode(str_3)