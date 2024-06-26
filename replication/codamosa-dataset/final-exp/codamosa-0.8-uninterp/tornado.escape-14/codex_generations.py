

# Generated at 2022-06-14 12:05:31.109608
# Unit test for function linkify
def test_linkify():
    # 正常使用
    assert linkify("Hello http://tornadoweb.org!") == "Hello <a href=\"http://tornadoweb.org\">http://tornadoweb.org</a>!"
    assert linkify("Hello www.tornadoweb.org!") == "Hello <a href=\"http://www.tornadoweb.org\">www.tornadoweb.org</a>!"
    assert linkify("Hello x@y.z, I still love you!") == "Hello x@y.z, I still love you!"
    assert linkify("你好 www.空间.cn") == "你好 <a href=\"http://www.空间.cn\">www.空间.cn</a>"

# Generated at 2022-06-14 12:05:42.932948
# Unit test for function linkify
def test_linkify():
    import re

# Generated at 2022-06-14 12:05:46.040252
# Unit test for function linkify
def test_linkify():
  text = 'Hello http://tornadoweb.org!'
  assert linkify(text) == 'Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>!'
  print('Passed!')
test_linkify()


# Generated at 2022-06-14 12:06:01.026336
# Unit test for function linkify
def test_linkify():
    assert linkify(u"http://example.com") == '<a href="http://example.com">http://example.com</a>'
    assert linkify(u"www.example.com") == '<a href="http://www.example.com">www.example.com</a>'
    assert linkify(u"Hello http://example.com") == 'Hello <a href="http://example.com">http://example.com</a>'
    assert linkify(u"http://example.com/./\u2603") == '<a href="http://example.com/./\u2603">http://example.com/./\u2603</a>' # noqa: E501

# Generated at 2022-06-14 12:06:19.395492
# Unit test for function linkify
def test_linkify():
    url = "http://www.google.com"
    assert linkify(url) == """<a href="http://www.google.com">http://www.google.com</a>"""
    url = "http://www.google.com/search?q=facebook"
    assert linkify(url) == """<a href="http://www.google.com/search?q=facebook">http://www.google.com/search?q=facebook</a>"""
    url = "https://www.google.com/search?q=facebook"
    assert linkify(url) == """<a href="https://www.google.com/search?q=facebook">https://www.google.com/search?q=facebook</a>"""
    url = "http://www.facebook.com/"

# Generated at 2022-06-14 12:06:22.684396
# Unit test for function linkify
def test_linkify():
    assert linkify("http://example.com") == u"<a href=\"http://example.com\">http://example.com</a>"
    #with pytest.raises(TypeError):
    #    linkify(1)
test_linkify()


# Generated at 2022-06-14 12:06:30.295736
# Unit test for function linkify
def test_linkify():
    print("")
    test_str = "http://www.baidu.com"
    res = linkify(test_str)
    print("test_linkify, test_str: %s, res: %s" % (test_str, res))
    

# Generated at 2022-06-14 12:06:36.459516
# Unit test for function linkify
def test_linkify():
    assert linkify("http://foo.com/", shorten=True) == '<a href="http://foo.com/">foo.com</a>'
    assert linkify("foo@foo.com", shorten=True) == '<a href="mailto:foo@foo.com">foo@foo.com</a>'
test_linkify()


# Generated at 2022-06-14 12:06:47.462693
# Unit test for function linkify
def test_linkify():
    text = "Hello http://www.google.com !"
    print(linkify(text, shorten=True))
# test_linkify()

# Copyright 2012 Facebook, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

# Automatically generated by refactor.py. Do not edit directly


# Generated at 2022-06-14 12:06:59.763436
# Unit test for function linkify
def test_linkify():
    assert linkify("http://example.com") == '<a href="http://example.com">http://example.com</a>'
    assert linkify("http://example.com extra") == '<a href="http://example.com">http://example.com</a> extra'
    assert linkify("http://example.com/foo/bar") == '<a href="http://example.com/foo/bar">http://example.com/foo/bar</a>'
    assert linkify("http://example.com/foo/bar extra") == '<a href="http://example.com/foo/bar">http://example.com/foo/bar</a> extra'
    assert linkify("hello http://example.com") == 'hello <a href="http://example.com">http://example.com</a>'
    assert linkify

# Generated at 2022-06-14 12:07:15.117591
# Unit test for function linkify
def test_linkify():
    test = "http://www.google.com/"
    assert linkify(test) == "<a href=\"http://www.google.com/\">http://www.google.com/</a>"
    assert linkify(test, shorten=True) == "<a href=\"http://www.google.com/\">http://www.google.com/</a>"
    assert linkify(test, require_protocol=True) == "<a href=\"http://www.google.com/\">http://www.google.com/</a>"
    assert linkify(test, permitted_protocols=["http"]) == "<a href=\"http://www.google.com/\">http://www.google.com/</a>"

# --------------------------------------------------------------------

# Generated at 2022-06-14 12:07:20.957193
# Unit test for function linkify
def test_linkify():
    r = linkify("Hello http://grumpy-zebra.com!")
    assert r == 'Hello <a href="http://grumpy-zebra.com">http://grumpy-zebra.com</a>!'
## end unit testing

_email_regex = re.compile(r"(.*?)(?:\s|<|&lt;)([\w\-.]+@[\w\-.]+)(?:\s|>|&gt;)(.*?)")



# Generated at 2022-06-14 12:07:28.710845
# Unit test for function linkify
def test_linkify():
    #test
    assert linkify("hello world") == "hello world"
    assert linkify("hello http://www.google.com/ how are you doing today") == 'hello <a href="http://www.google.com/">http://www.google.com/</a> how are you doing today'

    assert linkify("hello http://www.google.com/ how are you doing today", extra_params="rel='nofollow'") == 'hello <a href="http://www.google.com/" rel=\'nofollow\'>http://www.google.com/</a> how are you doing today'

    assert linkify("hello www.google.com how are you doing today") == 'hello <a href="http://www.google.com">www.google.com</a> how are you doing today'


# Generated at 2022-06-14 12:07:30.648932
# Unit test for function linkify
def test_linkify():
    assert linkify("hello www.google.com") == """hello <a href="http://www.google.com">www.google.com</a>"""


# Generated at 2022-06-14 12:07:39.398409
# Unit test for function linkify
def test_linkify():
    assert "1" == linkify("1")
    assert "1" == linkify(b"1")
    assert (
        "1" == linkify("1", shorten=True)
    )  # shorten has no effect without a protocol
    assert (
        "1" == linkify("1", extra_params="class=external", shorten=True)
    )  # shorten has no effect without a protocol
    assert (
        '<a href="http://1">http://1</a>' == linkify("http://1")
    )  # linkify http://
    assert '<a href="1">1</a>' == linkify("1", require_protocol=False)  # linkify www.

# Generated at 2022-06-14 12:07:51.065191
# Unit test for function linkify
def test_linkify():
    text = "Hello http://tornadoweb.org!"
    if linkify(text) != 'Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>!':
        print ("linkify test 1 FAILED")
    else:
        print ("linkify test 1 PASSED")
    def extra_params_cb(url):
        if url.startswith("http://example.com"):
            return 'class="internal"'
        else:
            return 'class="external" rel="nofollow"'
    if linkify(text, extra_params=extra_params_cb) != 'Hello <a href="http://tornadoweb.org" class="external" rel="nofollow">http://tornadoweb.org</a>!':
        print ("linkify test 2 FAILED")

# Generated at 2022-06-14 12:07:56.345697
# Unit test for function linkify
def test_linkify():
    test_text = "Hello https://www.google.com !"
    if linkify(test_text) == "Hello <a href=\"https://www.google.com\">https://www.google.com</a> !":
        print('Test for "linkify" passed!')
    else:
        print('Test for "linkify" failed!')
    return



# Generated at 2022-06-14 12:08:06.026812
# Unit test for function linkify
def test_linkify():
    assert linkify("http://foo/?bar=baz&ruz=foo") == '<a href="http://foo/?bar=baz&ruz=foo">http://foo/?bar=baz&amp;ruz=foo</a>'
    assert linkify("http://foo/?bar=baz&ruz=foo", shorten=True) == '<a href="http://foo/?bar=baz&ruz=foo" title="http://foo/?bar=baz&amp;ruz=foo">http://foo/?bar=baz&amp;ruz=foo</a>'
    assert linkify("www.facebook.com", require_protocol=True) == 'www.facebook.com'

# Generated at 2022-06-14 12:08:12.628228
# Unit test for function linkify
def test_linkify():
    text = "I am link: https://www.google.com"
    print(linkify(text))

test_linkify()

# Copyright 2009 Facebook
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import numbers
import types

# Generated at 2022-06-14 12:08:20.445099
# Unit test for function linkify
def test_linkify():
    # Valid links
    assert linkify(
        "http://xkcd.com/353/",
        extra_params='rel="nofollow" class="external"',
        require_protocol=True,
        permitted_protocols=["http"],
    ) == '<a href="http://xkcd.com/353/" rel="nofollow" class="external">http://xkcd.com/353/</a>'

# Generated at 2022-06-14 12:08:30.575226
# Unit test for function linkify
def test_linkify():
    output = linkify("Hello http://tornadoweb.org!", extra_params="name='view'")
    print(output)
    
    
test_linkify()

# 定义一个统一校验链接的函数
# 返回一个统一的正确格式

# Generated at 2022-06-14 12:08:38.318417
# Unit test for function linkify
def test_linkify():
    # test with empty input text
    assert linkify("") == ""

    # test with invalid input text
    with pytest.raises(TypeError):
        linkify(list())

    with pytest.raises(TypeError):
        linkify(dict())

    with pytest.raises(TypeError):
        linkify(2)

    # test without extra_params
    assert linkify("http://example.com") == '<a href="http://example.com">http://example.com</a>'

    assert linkify("http://example.com/url-with-long-directory/another-long-directory/example") == '<a href="http://example.com/url-with-long-directory/another-long-directory/example">http://example.com/url-with-long-directory/another-...</a>'

# Generated at 2022-06-14 12:08:49.927555
# Unit test for function linkify
def test_linkify():
    assert linkify(
        "http://example.com/foo",
        extra_params='rel="nofollow" class="external"',
    ) == '<a href="http://example.com/foo" rel="nofollow" class="external">http://example.com/foo</a>'
    assert linkify(
        "http://example.com/foo",
        require_protocol=True,
        extra_params='rel="nofollow" class="external"',
    ) == '<a href="http://example.com/foo" rel="nofollow" class="external">http://example.com/foo</a>'

# Generated at 2022-06-14 12:09:04.909979
# Unit test for function linkify
def test_linkify():
    #Test for non-strings
    assert linkify(None) == None
    assert linkify(1) == '1'
    assert linkify(1.0) == '1.0'
    assert linkify(True) == 'True'
    assert linkify(False) == 'False'
    #Test simple cases
    assert linkify('http://example.com') == '<a href="http://example.com">http://example.com</a>'
    assert linkify('http://example.com/') == '<a href="http://example.com/">http://example.com/</a>'
    assert linkify('http://example.com?a=b') == '<a href="http://example.com?a=b">http://example.com?a=b</a>'

# Generated at 2022-06-14 12:09:07.296978
# Unit test for function linkify
def test_linkify():
    assert linkify("http://www.google.com") == '<a href="http://www.google.com">http://www.google.com</a>'
    assert linkify("http://www.example.com") == '<a href="http://www.example.com">http://www.example.com</a>'

if __name__ == "__main__":
    test_linkify()

# Generated at 2022-06-14 12:09:17.804448
# Unit test for function linkify
def test_linkify():
    assert linkify("www.baidu.com")=='<a href="http://www.baidu.com">www.baidu.com</a>'
    assert linkify("www.baidu.com/test.html?a=1")=='<a href="http://www.baidu.com/test.html?a=1">www.baidu.com/test.html?a=1</a>'
    assert linkify("http://www.baidu.com")=='<a href="http://www.baidu.com">http://www.baidu.com</a>'

# Generated at 2022-06-14 12:09:20.058050
# Unit test for function linkify
def test_linkify():
    text = '<a href="www.tornadoweb.org">www.tornadoweb.org</a>'
    assert linkify(text) == '<a href="http://www.tornadoweb.org">www.tornadoweb.org</a>'


# Generated at 2022-06-14 12:09:31.586651
# Unit test for function linkify
def test_linkify():
    assert linkify("http://www.facebook.com/tornadoweb") ==  u'<a href="http://www.facebook.com/tornadoweb">http://www.facebook.com/tornadoweb</a>'
    assert linkify("www.facebook.com/tornadoweb") ==  u'<a href="http://www.facebook.com/tornadoweb">www.facebook.com/tornadoweb</a>'
    assert linkify("Hello http://tornadoweb.org!") == u'Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>!'

# Generated at 2022-06-14 12:09:41.719190
# Unit test for function linkify
def test_linkify():
    text = """\
Hello http://www.tornadoweb.org/en/stable/!

Tornado is listed on http://pypi.python.org/pypy/tornado so you can do:
    easy_install tornado

There are many questions on StackOverflow about Tornado:
http://stackoverflow.com/questions/tagged/tornado
"""


# Generated at 2022-06-14 12:09:57.911464
# Unit test for function linkify
def test_linkify():
    assert(linkify('http://tornadoweb.org') == '<a href="http://tornadoweb.org">http://tornadoweb.org</a>')
    assert(linkify('Hello http://tornadoweb.org') == 'Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>')
    assert(linkify('Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>') == 'Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>')
    assert(linkify('') == '')
    assert(linkify(None) == '')

# Generated at 2022-06-14 12:10:12.262904
# Unit test for function linkify
def test_linkify():
    # test basic linkify
    assert linkify("Hello http://tornadoweb.org!") == 'Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>!'
    assert linkify("Hello www.tornadoweb.org!") == 'Hello <a href="http://www.tornadoweb.org">www.tornadoweb.org</a>!'
    
    assert linkify("Welcome to http://www.example.com!", shorten=True) == 'Welcome to <a href="http://www.example.com">http://www.example.com</a>!'
    assert linkify("Hello http://tornadoweb.org!", shorten=True) == 'Hello <a href="http://tornadoweb.org">tornadoweb.org</a>!'

# Generated at 2022-06-14 12:10:14.030216
# Unit test for function linkify
def test_linkify():
    text = "Hello http://tornadoweb.org!"
    res = linkify(text)
    print(res)
test_linkify()


# Generated at 2022-06-14 12:10:25.564965
# Unit test for function linkify
def test_linkify():
    assert linkify("http://www.google.com") == u'<a href="http://www.google.com">http://www.google.com</a>'
    assert linkify("google link: www.google.com") == u'google link: <a href="http://www.google.com">www.google.com</a>'
    assert linkify("[text](http://www.google.com)") == u'<a href="http://www.google.com">[text](http://www.google.com)</a>'
    assert linkify("some www.google.com link") == u'some <a href="http://www.google.com">www.google.com</a> link'

# Generated at 2022-06-14 12:10:28.692024
# Unit test for function linkify
def test_linkify():
    assert linkify("http://www.google.com") =='<a href="http://www.google.com">http://www.google.com</a>'
    assert linkify("email@address.com") =='<a href="email@address.com">email@address.com</a>'


# Generated at 2022-06-14 12:10:40.393817
# Unit test for function linkify
def test_linkify():
    assert '<a href="http://tornadoweb.org">http://tornadoweb.org</a>' \
        == linkify('http://tornadoweb.org')
    assert '<a href="http://tornadoweb.org/">http://tornadoweb.org/</a>' \
        == linkify('<http://tornadoweb.org/>')
    assert '<a href="http://tornadoweb.org/">http://tornadoweb.org/</a>\n' \
        '<a href="http://tornadoweb.com/">http://tornadoweb.com/</a>' \
        == linkify('<http://tornadoweb.org/>\nhttp://tornadoweb.com/')

# Generated at 2022-06-14 12:10:43.973518
# Unit test for function linkify
def test_linkify():
    print(linkify("http://www.google.com"))
    print(linkify("Hello http://tornadoweb.org!"))
    print("http://www.google.com".index("http://"))

test_linkify()


# Generated at 2022-06-14 12:10:48.231675
# Unit test for function linkify

# Generated at 2022-06-14 12:10:50.395215
# Unit test for function linkify
def test_linkify():
    print(linkify("Python's official website http://www.python.org", shorten=True))
    print(linkify("Python's official website http://www.python.org"))


# Generated at 2022-06-14 12:10:58.292238
# Unit test for function linkify
def test_linkify():
    text = linkify(text="Hello http://tornadoweb.org/")
    assert text == 'Hello <a href="http://tornadoweb.org/">http://tornadoweb.org/</a>'

# Generated at 2022-06-14 12:11:03.957473
# Unit test for function linkify
def test_linkify():
    # some simple test cases
    assert linkify("Hello!") == "Hello!"
    assert linkify("Hello, world!") == "Hello, world!"
    assert linkify("Hello www.example.com") == 'Hello <a href="http://www.example.com">www.example.com</a>'
    assert linkify("http://www.example.com") == '<a href="http://www.example.com">http://www.example.com</a>'

    # test new features
    assert linkify("http://www.example.com", shorten=True) == '<a href="http://www.example.com">http://www.example...</a>'

# Generated at 2022-06-14 12:11:17.185818
# Unit test for function linkify
def test_linkify():
    s = """
    This is a text with a link http://www.google.com in the middle
    and http://t.co shortener.
    """
    linkified_s = linkify(s)
    assert linkified_s == '\n    This is a text with a link <a href="http://www.google.com">http://www.google.com</a> in the middle\n    and <a href="http://t.co">http://t.co</a> shortener.\n    '
    s = """
    This is a text without http:// link.
    """
    linkified_s = linkify(s)
    assert linkified_s == '\n    This is a text without http:// link.\n    '


# Generated at 2022-06-14 12:11:20.967410
# Unit test for function linkify
def test_linkify():
    assert linkify("http://example.com") == '<a href="http://example.com">http://example.com</a>'



# Generated at 2022-06-14 12:11:31.142010
# Unit test for function linkify
def test_linkify():
    assert linkify("http://x.com")=='<a href="http://x.com">http://x.com</a>'
    assert linkify("http://x.com/foo")=='<a href="http://x.com/foo">http://x.com/foo</a>'
    assert linkify("http://x.com/foo bar")=='<a href="http://x.com/foo">http://x.com/foo</a> bar'
    assert linkify("http://x.com/foo?bar=baz")=='<a href="http://x.com/foo?bar=baz">http://x.com/foo?bar=baz</a>'

# Generated at 2022-06-14 12:11:40.964050
# Unit test for function linkify
def test_linkify():
    print(linkify("Hello http://tornadoweb.org!"))
    print(linkify("http://www.google.com"))
    print(linkify("Hello http://tornadoweb.org and www.google.com", shorten=True))


# Generated at 2022-06-14 12:11:49.586872
# Unit test for function linkify
def test_linkify():
    assert linkify("http://example.com") == '<a href="http://example.com">http://example.com</a>'
    assert linkify("http://example.com/foo&bar") == '<a href="http://example.com/foo&amp;bar">http://example.com/foo&amp;bar</a>'
    assert linkify("http://example.com/foo&amp;bar") == '<a href="http://example.com/foo&amp;bar">http://example.com/foo&amp;bar</a>'
    assert linkify("http://example.com/foo&bar", extra_params="class=external") == '<a href="http://example.com/foo&amp;bar" class=external>http://example.com/foo&amp;bar</a>'

# Generated at 2022-06-14 12:11:54.085974
# Unit test for function linkify
def test_linkify():
    assert linkify("http://example.com") == '<a href="http://example.com">http://example.com</a>'
    assert linkify("http://user:pass@example.com") == '<a href="http://user:pass@example.com">http://user:pass@example.com</a>'
    assert linkify("https://example.com") == '<a href="https://example.com">https://example.com</a>'
    assert linkify("http://example.com/foo?bar=baz&x=y#ccc") == '<a href="http://example.com/foo?bar=baz&amp;x=y#ccc">http://example.com/foo?bar=baz&amp;x=y#ccc</a>'

# Generated at 2022-06-14 12:12:02.652873
# Unit test for function linkify
def test_linkify():
    assert linkify('http://test.com') == '<a href="http://test.com">http://test.com</a>'
    assert linkify('http://test.com/abc?123') == '<a href="http://test.com/abc?123">http://test.com/abc?123</a>'
    assert linkify('www.test.com') == '<a href="http://www.test.com">www.test.com</a>'
    assert linkify('www.test.com/abc?123') == '<a href="http://www.test.com/abc?123">www.test.com/abc?123</a>'

# Generated at 2022-06-14 12:12:14.766460
# Unit test for function linkify
def test_linkify():
    assert linkify(None) is None
    assert linkify(1) == "1"
    assert linkify("") == ""
    assert linkify("hello") == "hello"
    assert linkify("hello http://tornadoweb.org") == 'hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>'
    assert linkify("hello http://tornadoweb.org", extra_params='class="external"') == 'hello <a href="http://tornadoweb.org" class="external">http://tornadoweb.org</a>'


# Based on http://wiki.python.org/moin/EscapingHtml
# Avoid using these if possible; they should only be used to clean up
# data when the input is not under the application's control.

# Generated at 2022-06-14 12:12:26.812882
# Unit test for function linkify
def test_linkify():
    assert linkify("http://www.google.com") == '<a href="http://www.google.com">http://www.google.com</a>'
    assert linkify("http://www.google.com/") == '<a href="http://www.google.com/">http://www.google.com/</a>'
    assert linkify("http://www.google.com/search?q=asdf") == '<a href="http://www.google.com/search?q=asdf">http://www.google.com/search?q=asdf</a>'
    assert linkify("https://www.google.com") == '<a href="https://www.google.com">https://www.google.com</a>'

# Generated at 2022-06-14 12:12:37.652334
# Unit test for function linkify
def test_linkify():
    def extra_params(url):
       return 'target="_blank" rel="nofollow"'

    assert linkify("Hello http://tornadoweb.org!") == 'Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>!'
    assert linkify("Hello http://tornadoweb.org!", extra_params=extra_params) == 'Hello <a href="http://tornadoweb.org" target="_blank" rel="nofollow">http://tornadoweb.org</a>!'
    assert linkify("Hello http://tornadoweb.org!", shorten=True) == 'Hello <a href="http://tornadoweb.org">http:...</a>!'

# Generated at 2022-06-14 12:12:52.336775
# Unit test for function linkify
def test_linkify():
    assert linkify("foo bar") == u"foo bar"
    assert linkify("foo bar http://www.google.com baz") == u'foo bar <a href="http://www.google.com">http://www.google.com</a> baz'
    assert linkify("foo http://www.google.com/foo.jpg bar") == u'foo <a href="http://www.google.com/foo.jpg">http://www.google.com/foo.jpg</a> bar'
    assert linkify("foo https://www.google.com/foo.jpg bar") == u'foo <a href="https://www.google.com/foo.jpg">https://www.google.com/foo.jpg</a> bar'

# Generated at 2022-06-14 12:12:54.420937
# Unit test for function linkify
def test_linkify():
    out = linkify("https://www.google.com")
    assert out == u'<a href="https://www.google.com">https://www.google.com</a>'

# Generated at 2022-06-14 12:13:01.012709
# Unit test for function linkify
def test_linkify():
    text = 'python http://example.com'
    text1 = linkify(text)
    print(text1)

# This is a modified version of xhtml_escape from tornado.escape.
# It is modified to not use XML entities at all, to avoid confusion with
# the existing HTML entities (such as &quot;)
# Ensure that g("<") == "&lt;"

# Generated at 2022-06-14 12:13:08.498972
# Unit test for function linkify
def test_linkify():
    text = 'Hello http://tornadoweb.org!'
    assert linkify(text) == 'Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>!'
    text = 'Hello www.tornadoweb.org!'
    assert linkify(text, require_protocol=False) == 'Hello <a href="http://www.tornadoweb.org">www.tornadoweb.org</a>!'
    text = 'Hello www.tornadoweb.org!'
    assert linkify(text) == 'Hello www.tornadoweb.org!'
    text = 'Hello http://tornadoweb.org!'

# Generated at 2022-06-14 12:13:19.245143
# Unit test for function linkify
def test_linkify():
    print(linkify('http://example.com'))
    print(linkify('www.example.com'))
    print(linkify('www.example.com', require_protocol=False))
    print(linkify('http://example.com/some/path'))
    print(linkify('http://example.com.'))
    print(linkify('http://example.com./'))
    print(linkify('http://example.com/.'))
    print(linkify('http://example.com/..'))
    print(linkify('foo http:/example.com bar'))
    print(linkify('foo http://www.example.com bar'))
    print(linkify('foo http://www.example.com:8000 bar'))
    print(linkify('foo https://www.example.com bar'))
   

# Generated at 2022-06-14 12:13:25.014985
# Unit test for function linkify
def test_linkify():
    assert linkify("http://www.example.com") == '<a href="http://www.example.com">http://www.example.com</a>'
    assert linkify("www.example.com", require_protocol=True) == 'www.example.com'


# Generated at 2022-06-14 12:13:36.365232
# Unit test for function linkify
def test_linkify():
    print(linkify("Hello http://example.com"))
    print(linkify("Hello   http://example.com"))
    text = (
        "I have a link http://example.com/foo?bar=baz&x=y#anchor to the site. "
        "Another link is http://example.com/bar?baz=foo&q=1."
    )
    print(linkify(text))
    print(linkify(text, require_protocol=False))
    print(linkify(text, require_protocol=False))
    print(linkify(text, require_protocol=False, permitted_protocols=["http"]))
    print(
        linkify(text, require_protocol=False, permitted_protocols=["https"])
    )

# Generated at 2022-06-14 12:13:43.073812
# Unit test for function linkify
def test_linkify():
    """Unit test for linkify function"""
    assert ("<a href=\"http://tornadoweb.org\">http://tornadoweb.org</a>") == linkify(
        "Hello http://tornadoweb.org!"
    )
    assert (
        "<a href=\"http://tornadoweb.org\">http://tornadoweb.org</a>."
    ) == linkify("Hello http://tornadoweb.org.")



# Generated at 2022-06-14 12:13:52.480129
# Unit test for function linkify
def test_linkify():
    assert linkify("a http://example.com b") == \
           "a <a href=\"http://example.com\">http://example.com</a> b"
    assert linkify("a http://example.com/ b") == \
           "a <a href=\"http://example.com/\">http://example.com/</a> b"
    assert linkify("a www.example.com b") == \
           "a <a href=\"http://www.example.com\">www.example.com</a> b"
    assert linkify("a thing.com/with_underscores b") == \
           "a <a href=\"http://thing.com/with_underscores\">thing.com/with_underscores</a> b"

# Generated at 2022-06-14 12:14:02.660800
# Unit test for function linkify
def test_linkify():
    print(linkify("Hello"))
    print(linkify("Hello http://tornadoweb.org!"))
    print(linkify("Hello http://tornadoweb.org!", shorten=True))
    print(linkify("Hello https://tornadoweb.org!", shorten=True, extra_params='rel="nofollow" class="external"'))
    print(linkify("Hello http://tw.yahoo.com!", shorten=True, extra_params=lambda url: 'rel="nofollow" class="external"'))
    print(linkify("Hello http://tw.yahoo.com!", require_protocol=True, permitted_protocols=["http", "ftp", "mailto"]))

if __name__=="__main__":
    test_linkify()


# Generated at 2022-06-14 12:14:11.131762
# Unit test for function linkify
def test_linkify():
    test_string = "world  http://www.google.com"
    assert linkify(test_string) == 'world  <a href="http://www.google.com">http://www.google.com</a>'
test_linkify()


# Generated at 2022-06-14 12:14:20.984322
# Unit test for function linkify
def test_linkify():
    assert linkify("http://example.com") == '<a href="http://example.com">http://example.com</a>'
    assert linkify("http://example.com/\ntest") == '<a href="http://example.com/\ntest">http://example.com/\ntest</a>'
    assert linkify("foo http://example.com/") == 'foo <a href="http://example.com/">http://example.com/</a>'
    assert linkify("a foo http://example.com/ b") == 'a foo <a href="http://example.com/">http://example.com/</a> b'

# Generated at 2022-06-14 12:14:22.421260
# Unit test for function linkify
def test_linkify():
  text = input('Enter text')
  print('The linkified text is ' + linkify(text))

# Generated at 2022-06-14 12:14:25.808098
# Unit test for function linkify
def test_linkify():
    text = "hello world http://example.com"

# Generated at 2022-06-14 12:14:41.146574
# Unit test for function linkify
def test_linkify():
    text = "This is a test http://www.facebook.com/ of my function"
    assert linkify(text) == 'This is a test <a href="http://www.facebook.com/">http://www.facebook.com/</a> of my function'
    assert linkify(text, shorten=True, extra_params=None, require_protocol=True, permitted_protocols=['http', 'https']) == 'This is a test <a href="http://www.facebook.com/">http://www.facebook.com/</a> of my function'

# Generated at 2022-06-14 12:14:48.644796
# Unit test for function linkify
def test_linkify():
    """Tests the function linkify.
    """
    assert linkify("https://www.google.com/search?q=twitter&tbm=isch") == '<a href="https://www.google.com/search?q=twitter&amp;tbm=isch">https://www.google.com/search?q=twitter&amp;tbm=isch</a>'
    assert linkify("https://www.google.com/search?q=twitter&tbm=isch", shorten=True) == '<a href="https://www.google.com/search?q=twitter&amp;tbm=isch">https://www.google.com/...</a>'

# Generated at 2022-06-14 12:14:58.250734
# Unit test for function linkify
def test_linkify():
    text = """Hello http://tornadoweb.org!
Adios.


http://www.tornadoweb.org/en/stable/
"""
    html = linkify(text)
    assert len(re.findall(r"Hello <a", html)) == 1
    assert len(re.findall(r"</a>!", html)) == 1
    assert len(re.findall(r"Adios", html)) == 1
    assert len(re.findall(r"www.tornadoweb.org", html)) == 1
    assert len(re.findall(r"en/stable", html)) == 1



# Generated at 2022-06-14 12:15:07.312266
# Unit test for function linkify
def test_linkify():
    assert linkify("http://google.com") == u'<a href="http://google.com">http://google.com</a>'
    assert linkify("http://google.com/foo?bar=baz&x=y#z") == u'<a href="http://google.com/foo?bar=baz&amp;x=y#z">http://google.com/foo?bar=baz&amp;x=y#z</a>'
    assert linkify("http://x.com/foo?bar=baz&x=y#z", shorten=True) == u'<a href="http://x.com/foo?bar=baz&amp;x=y#z">http://x.com/foo?bar=baz&amp;x=...</a>'