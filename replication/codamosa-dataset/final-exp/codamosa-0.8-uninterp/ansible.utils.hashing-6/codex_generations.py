

# Generated at 2022-06-13 16:10:02.543250
# Unit test for function md5s
def test_md5s():
    data = "hello"
    print(md5s(data))

if __name__ == '__main__':
    test_md5s()

# Generated at 2022-06-13 16:10:06.953096
# Unit test for function checksum
def test_checksum():
    import os
    files = [ __file__, __file__ + "foo", "/bin/ls" ]
    for f in files:
        if os.path.exists(f):
            c = checksum(f)
            assert(c == checksum_s(open(f).read()))

# Generated at 2022-06-13 16:10:09.123268
# Unit test for function md5
def test_md5():
    if not _md5:
        print('MD5 not available.  Possibly running in FIPS mode')



# Generated at 2022-06-13 16:10:20.258013
# Unit test for function md5
def test_md5():
    class FauxFile(object):

        def __init__(self, content=None):
            self.content = content
            self.cursor = 0

        def read(self, size=-1):
            if size < 0:
                size = len(self.content)
            start = self.cursor
            end = min(self.cursor + size, len(self.content))
            if end == start:
                return ''
            self.cursor = end
            return self.content[start:end]

        def __iter__(self):
            return self

        def next(self):
            c = self.read()
            if not c:
                raise StopIteration
            return c

    class VirtualFile(object):

        def __init__(self, name, content=None):
            self.name = name

# Generated at 2022-06-13 16:10:31.222070
# Unit test for function md5
def test_md5():
    '''
    Ensure that the md5() function gives the expected results for a set of files.

    The expected results are found in 'files.sum' and are generated by running md5sum
    from a Linux command line.
    '''

    import os

    with open('files.sum', 'r') as fp:
        expected = fp.read().splitlines()

    bad = []

    for line in expected:
        md5sum, filename = line.split('  ', 1)
        filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)
        if not os.path.exists(filename):
            print('%s does not exist' % filename)
            bad.append((filename, None))

# Generated at 2022-06-13 16:10:42.805008
# Unit test for function md5s
def test_md5s():
    "this function tests the md5s function"
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec={})
    if _md5:
        ret = md5s("abc")
        module.exit_json(changed=False, md5="900150983cd24fb0d6963f7d28e17f72", md5s=ret)
    else:
        module.exit_json(changed=False, md5='not supported', md5s='not supported')

    def test_md5():
        "this function tests the md5 function"
        from ansible.module_utils.basic import AnsibleModule
        module = AnsibleModule(argument_spec={})
        if _md5:
            ret = md5(__file__)
            module.exit_json

# Generated at 2022-06-13 16:10:44.944888
# Unit test for function checksum
def test_checksum():
    ''' '''
    assert checksum("hello world") == checksum("hello world")
    assert checksum("hello world") != checksum("Hello world")


# Generated at 2022-06-13 16:10:49.412719
# Unit test for function md5
def test_md5():

    fd, fname = tempfile.mkstemp(text=True)

    try:
        with os.fdopen(fd, 'w') as f:
            f.write("content")
        chksum = md5(fname)
        assert chksum == '945e8c1327b5e5b065d810a8ca24a7fa'
    finally:
        os.remove(fname)

# Generated at 2022-06-13 16:10:56.566489
# Unit test for function checksum
def test_checksum():
    '''
    hash function test
    '''

# Generated at 2022-06-13 16:11:01.574770
# Unit test for function md5
def test_md5():
    '''
    hash_util.md5 tests
    Returns True if md5 produces the same output as python's hashlib.md5
    '''
    try:
        import hashlib
    except ImportError:
        return True

    from random import randrange

    for x in range(100):
        block_size = randrange(1, 1024)
        data = os.urandom(block_size)
        assert(md5s(data) == hashlib.md5(data).hexdigest())

    return True


# Generated at 2022-06-13 16:11:13.002215
# Unit test for function checksum
def test_checksum():
    if not _md5:
        raise ValueError('MD5 not available.  Possibly running in FIPS mode')
    filename = ''
    if checksum(filename) != None:
        raise AssertionError('checksum(filename) should return None.')
    filename = './ansible/module_utils/basic.py'
    digest_before = checksum(filename)
    with open(filename, 'r') as myfile:
        data = myfile.read()
    with open(filename, 'w') as myfile:
        myfile.write(data)
    digest_after = checksum(filename)
    if digest_before != digest_after:
        raise AssertionError('checksum(filename) should return a unchanged checksum.')

# Generated at 2022-06-13 16:11:24.280547
# Unit test for function checksum
def test_checksum():
    '''
    ansible.utils.crypto.checksum tests
    '''
    from ansible.compat.tests import unittest
    from ansible.compat.tests.mock import patch

    try:
        from hashlib import sha1
    except ImportError:
        from sha import sha as sha1

    class TestChecksum(unittest.TestCase):

        def setUp(self):
            pass

        def tearDown(self):
            pass

        @patch('ansible.utils.crypto.open')
        @patch('ansible.utils.crypto.os.path.exists')
        def test_checksum_bad_file(self, mock_exists, mock_open):
            ''' Make sure bad file call is handled properly '''

            mock_exists.return_value

# Generated at 2022-06-13 16:11:30.291780
# Unit test for function md5s
def test_md5s():
    if not _md5:
        return True

    data = 'test'
    hashed_data = md5s(data)

    if hashed_data != '098f6bcd4621d373cade4e832627b4f6':
        return False

    return True


# Generated at 2022-06-13 16:11:34.653186
# Unit test for function checksum
def test_checksum():
    fake_file = os.path.join(os.path.dirname(__file__), 'fake_file')
    assert(checksum(fake_file) == 'ee1eca47ad6db7dddca243dd3cc76efa4649c1cf')

# Generated at 2022-06-13 16:11:42.491638
# Unit test for function md5
def test_md5():
    ''' md5 unit tests '''

    import tempfile
    f = tempfile.NamedTemporaryFile(delete=False)
    f.write(b"hello")
    f.close()
    val1 = md5(f.name)

    try:
        f = open(f.name, 'w')
        f.write("hi")
        f.close()
        val2 = md5(f.name)
    finally:
        os.unlink(f.name)

    assert(val1 != val2)

    val3 = md5s("hello")
    val4 = md5s("hi")

    assert(val3 != val4)

# Generated at 2022-06-13 16:11:46.700161
# Unit test for function md5
def test_md5():
    import tempfile

    f = tempfile.NamedTemporaryFile(delete=True)
    f.write(b"foobar")
    f.flush()

    assert md5(f.name) == '3858f62230ac3c915f300c664312c63f'

# Generated at 2022-06-13 16:11:52.662173
# Unit test for function md5
def test_md5():
    import random
    import string
    rand = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10000))
    m = md5s(rand)
    print(m)


if __name__ == '__main__':
    test_md5()

# Generated at 2022-06-13 16:12:02.927929
# Unit test for function md5s
def test_md5s():
    import unittest
    import tempfile
    import random
    import shutil

    class TestMd5s(unittest.TestCase):

        def setUp(self):
            # Create a temp file
            (fd, self.tmpfile) = tempfile.mkstemp()
            fp = os.fdopen(fd, 'wb')
            # Write a bunch of random data to the file
            for x in range(0,10):
                fp.write(bytearray(random.getrandbits(8) for i in range(0, 1024)))
            fp.close()

            # create a second temp file
            (fd, self.tmpfile2) = tempfile.mkstemp()
            fp = os.fdopen(fd, 'wb')
            for x in range(0,10):
                fp

# Generated at 2022-06-13 16:12:08.543638
# Unit test for function checksum
def test_checksum():
    ''' simple checksum test, pass in test filename '''
    fn = 'sha1sum.py'
    checksum1 = secure_hash(fn)
    checksum2 = secure_hash_s(open(fn).read())
    assert checksum1 == checksum2
    print("checksum test passed")

if __name__ == '__main__':
    test_checksum()

# Generated at 2022-06-13 16:12:16.430235
# Unit test for function checksum
def test_checksum():
    test_file = os.path.join(os.getcwd(), 'checksum_test_file')
    with open(test_file, 'w') as fh:
        fh.write("ansible")