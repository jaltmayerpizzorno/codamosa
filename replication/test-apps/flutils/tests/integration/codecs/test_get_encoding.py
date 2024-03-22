import unittest
from locale import getpreferredencoding
from sys import getdefaultencoding

from flutils.codecs import get_encoding


class TestGetEncoding(unittest.TestCase):

    def test_name_none(self) -> None:
        exp = getpreferredencoding() or getdefaultencoding()
        exp = exp.lower()
        val = get_encoding()
        msg = (
            f'\n\n'
            f'exp = {exp!r}\n\n'
            f'val = {val!r}\n\n'
        )
        self.assertEqual(val, exp, msg=msg)

    def test_name_int(self) -> None:
        exp = getpreferredencoding() or getdefaultencoding()
        exp = exp.lower()
        val = get_encoding(1)
        msg = (
            f'\n\n'
            f'exp = {exp!r}\n\n'
            f'val = {val!r}\n\n'
        )
        self.assertEqual(val, exp, msg=msg)

    def test_default_none(self) -> None:
        arg = getpreferredencoding() or getdefaultencoding()
        exp = arg.lower()
        val = get_encoding(arg, default=None)
        msg = (
            f'\n\n'
            f'exp = {exp!r}\n\n'
            f'val = {val!r}\n\n'
        )
        self.assertEqual(val, exp, msg=msg)

    def test_default_int(self) -> None:
        arg = getpreferredencoding() or getdefaultencoding()
        exp = arg.lower()
        val = get_encoding(arg, default=1)
        msg = (
            f'\n\n'
            f'exp = {exp!r}\n\n'
            f'val = {val!r}\n\n'
        )
        self.assertEqual(val, exp, msg=msg)

    def test_default_none_raises(self) -> None:
        with self.assertRaises(LookupError):
            get_encoding(default='blah')

    def test_name_none_raises(self) -> None:
        with self.assertRaises(LookupError):
            get_encoding(default='')
