

# Generated at 2022-06-14 17:48:34.674479
# Unit test for function parseOpts
def test_parseOpts():
    import sys
    import tempfile
    import shutil

    def create_config_file(config):
        with tempfile.NamedTemporaryFile(delete=False) as f:
            f.write(config.encode('utf-8'))
            return f.name

    def delete_config_file(path):
        os.unlink(path)

    # Test for all valid arguments

# Generated at 2022-06-14 17:48:43.597604
# Unit test for function parseOpts
def test_parseOpts():
    from tempfile import NamedTemporaryFile
    import os
    import codecs
    from datetime import datetime
    from xml.sax.saxutils import unescape

    with NamedTemporaryFile(delete=False) as outtmpl_file:
        outtmpl = outtmpl_file.name
    with NamedTemporaryFile(delete=False) as cookie_file:
        cookie_file.write(b'\n'.join((
            b'# HTTP cookie file',
            b'# http://curl.haxx.se/rfc/cookie_spec.html',
            b'# This file was generated by libcurl! Edit at your own risk.',
            b'.youtube.com\tFALSE\t/\tFALSE\t0\tPREF\tPREFID\t5441')))
        cookie_

# Generated at 2022-06-14 17:48:54.352740
# Unit test for function parseOpts
def test_parseOpts():
    assert parseOpts([
        '--format=22/17/18',
        '--',
        'http://www.youtube.com/watch?v=BaW_jenozKc'
    ]) == (None,
           ['http://www.youtube.com/watch?v=BaW_jenozKc'],
           ['22', '17', '18'])

# Generated at 2022-06-14 17:49:03.935353
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts(['-i', '-f', '37/22/18', 'testvalue'])
    assert(opts.getverbatim)
    assert(opts.format == ['37/22/18'])
    assert(len(args) == 1)
    assert(args[0] == 'testvalue')

    # Test with config file
    parser, opts, args = parseOpts(['--config-location=tests/youtube-dl.conf'])
    assert(opts.getverbatim)
    assert(opts.verbose)
    assert(opts.username == 'testuser')
    assert(opts.password == 'testpass')
    assert(opts.format == ['37/22/18'])
    assert(opts.ignoreerrors)

# Generated at 2022-06-14 17:49:15.233779
# Unit test for function parseOpts
def test_parseOpts():
    # pylint: disable=missing-docstring
    parser, opts, args = parseOpts(
        ['--dump-user-agent'])
    assert opts.dump_user_agent
    parser, opts, args = parseOpts(
        ['--list-extractors'])
    assert opts.list_extractors
    parser, opts, args = parseOpts(
        ['--extractor-descriptions'])
    assert opts.extractor_descriptions
    parser, opts, args = parseOpts(
        ['--default-search', 'gvsearch15'])
    assert opts.default_search == 'gvsearch15'
    parser, opts, args = parseOpts(['--no-warnings'])
    assert opts.no_warnings
    parser, opt

# Generated at 2022-06-14 17:49:26.927346
# Unit test for function parseOpts
def test_parseOpts():
    from collections import namedtuple
    import unittest

    class FakeOption(object):
        def __init__(self, value):
            self.dest = 'fake_option'
            self.value = value
        def __eq__(self, other):
            return other is self.value

    def make_fake_options():
        FakeOptions = namedtuple('FakeOptions', ['verbose', 'fake_option', 'username', 'password', 'noplaylist', 'usenetrc'])
        return FakeOptions(False, None, None, None, False, False)

    # class FakeUsernamePasswordAuth(object):
    #     def __init__(self, username, password):
    #         self.username = username
    #         self.password = password
    #     def __eq__(self, other):
    #         return

# Generated at 2022-06-14 17:49:32.054941
# Unit test for function parseOpts
def test_parseOpts():
    from youtube_dl.utils import read_batch_urls
    parser, opts, args = parseOpts(['--download-archive', 'archive', '--batch-file', '-', '--verbose'])
    assert opts.download_archive == 'archive'
    assert opts.batchfile == '-'
    assert opts.verbose == True
    assert opts.ignoreconfig == False
    args = read_batch_urls(opts.batchfile, opts.forceurl, opts.playlistreverse, opts.playliststart, opts.playlistend, opts.start_time, opts.end_time)
    assert args == []
    return True

# Unit test runner
if __name__ == '__main__':
    import os
    import sys
    tests = [test_parseOpts]

# Generated at 2022-06-14 17:49:36.559248
# Unit test for function parseOpts
def test_parseOpts():
    import subprocess
    import sys
    import os

    # Prepare a test environment
    def create_config(config_location, contents):
        assert not os.path.exists(config_location)
        assert not os.path.exists(os.path.dirname(config_location))
        os.makedirs(os.path.dirname(config_location))
        with open(config_location, 'wb') as outf:
            outf.write(contents.encode('utf-8'))

    config_location = os.path.join('/tmp', 'youtube-dl', 'config')
    create_config(config_location, '--ignore-config\n-v\n')


# Generated at 2022-06-14 17:49:41.127306
# Unit test for function parseOpts
def test_parseOpts():
    # Long options
    # https://github.com/ytdl-org/youtube-dl/issues/3260
    _, opts, args = parseOpts(['--max-downloads=10'])
    assert opts.max_downloads == '10'

# https://github.com/ytdl-org/youtube-dl/issues/2696

# Generated at 2022-06-14 17:49:47.920889
# Unit test for function parseOpts
def test_parseOpts():
    try:
        import pytest
    except ImportError:
        return
    import sys
    sys.argv = ['youtube-dl']

    def check(*args, **kwargs):
        desc, conf = args[0].split('\n')
        kwargs['verbose'] = True
        parser, opts, _ = parseOpts(*args, **kwargs)
        assert type(parser.description) == type(desc)
        for section in parser.option_groups:
            for option in section.option_list:
                if not option.help:
                    continue
                opt = option.get_opt_string()
                assert opt in conf
                assert type(option.help) == type(conf[opt][1])

# Generated at 2022-06-14 17:50:08.913089
# Unit test for function parseOpts
def test_parseOpts():
    test_string = " --username abc --password 123"
    parser, opts, args = parseOpts(None)
    parser, opts, args = parseOpts(test_string.split())
    assert opts.username == 'abc'
    assert opts.password == '123'
    #assert opts.quiet == True
    return True


# Generated at 2022-06-14 17:50:20.243326
# Unit test for function parseOpts
def test_parseOpts():
    import re
    import copy
    import sys
    import tempfile
    if sys.version_info < (3,):
        def compat_expanduser(path):
            return path.replace('~', os.path.expanduser('~'))
    else:
        compat_expanduser = os.path.expanduser


# Generated at 2022-06-14 17:50:32.739926
# Unit test for function parseOpts

# Generated at 2022-06-14 17:50:41.554658
# Unit test for function parseOpts
def test_parseOpts():
    # A valid and complete config file
    _writeConfig('/tmp/youtube-dl.conf.test', [
        '--username=foo',
        '--password=bar',
        '--proxy=http://1.2.3.4:3128',
    ])

    # A suboptimal config file
    _writeConfig('/tmp/youtube-dl.conf.invalid', [
        '--foo'
    ])

    # The initial command line and config
    overrideArguments = [
        '--config-location=/tmp/youtube-dl.conf.invalid',
        '-v',
        'https://www.youtube.com/watch?v=BaW_jenozKc',
    ]

    # Checking that invalid values are ignored
    # (i.e. --config-location and -v)
    parser, opts

# Generated at 2022-06-14 17:50:54.561484
# Unit test for function parseOpts
def test_parseOpts():
    from youtube_dl.utils import encodeArgument

    args = ['-v', '--username', 'foobar', '--password', 'hunter2', '--no-check-certificate', '--proxy', '1.2.3.4:3128', '--no-verbose']
    _, opts, _ = parseOpts(args)

# Generated at 2022-06-14 17:50:58.865107
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts([])
    assert opts is not None
    assert parser is not None
    opts_missing = []
    for a in ['-f', '--format', '-o', '--output']:
        if a not in opts:
            opts_missing.append(a)
    assert opts_missing == []

if __name__ == '__main__':
    test_parseOpts()

# vim: expandtab:sw=4:ts=4

# Generated at 2022-06-14 17:51:01.311270
# Unit test for function parseOpts
def test_parseOpts():
    print("test_parseOpts start")
    print("test_parseOpts finish")


# -- Result objects
# ----------------------------------------------------------------------


# Generated at 2022-06-14 17:51:14.258897
# Unit test for function parseOpts
def test_parseOpts():
    # This function is just a unit test for parseOpts().
    # It doesn't do anything useful by itself.
    from youtube_dl.utils import DateRange
    from youtube_dl.extractor import gen_extractors, list_extractors

    def _print(s):
        print(s)

    def _do_test(argv):
        _print('Testing with %s' % repr(' '.join(argv)))
        parser, opts, args = parseOpts(argv)
        _print('Options:')
        for opt in parser.option_list:
            if opt.dest is None:
                continue
            if opt.dest == 'help':
                continue
            _print('  %-32s: %s' % (opt.get_opt_string(), getattr(opts, opt.dest)))

# Generated at 2022-06-14 17:51:18.778730
# Unit test for function parseOpts
def test_parseOpts():
    try:
        import unit_test
        unit_test.parse_opts_tester()
    except ImportError:
        print('To test parseOpts(), you need to run the test from the YoutubeDL source directory.')



# Generated at 2022-06-14 17:51:22.166221
# Unit test for function parseOpts
def test_parseOpts():
    import doctest
    doctest.run_docstring_examples(parseOpts, globals(), name='parseOpts')
# check for updates, returns a message if a new version is available

# Generated at 2022-06-14 17:52:03.319989
# Unit test for function parseOpts
def test_parseOpts():
    # Copy YoutubeDL default params
    params = YoutubeDL.params.copy()
    # Set option '--yes-playlist'
    params['yesplaylist'] = True
    # Set option '--write-info-json'
    params['writeinfojson'] = True
    # Set option '-f'
    params['format'] = 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4'

    # Create parser
    parser, opts, _ = parseOpts(['-f', 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4', '--yes-playlist', '--write-info-json'])

    # Check if parser options match default YoutubeDL params
    assert params == vars(opts)


# Generated at 2022-06-14 17:52:12.883701
# Unit test for function parseOpts
def test_parseOpts():
    def check_opts(opts):
        assert opts.usenetrc is True
        assert opts.username == 'charlie'
        assert opts.password == 'burger'
        assert opts.verbose is True
        assert opts.quiet is True
        assert opts.simulate is True
        assert opts.geturl is True
        assert opts.gettitle is True
        assert opts.getid is True
        assert opts.getthumburl is True
        assert opts.get_duration is True
        assert opts.get_filename is True
        assert opts.get_format is True
        assert opts.proxy is None
        assert opts.ratelimit == '1k'
        assert opts.nooverwrites is True
        assert opts.playliststart == 1
       

# Generated at 2022-06-14 17:52:14.203946
# Unit test for function parseOpts
def test_parseOpts():
    opts = parseOpts()
    return 0

# Generated at 2022-06-14 17:52:26.770423
# Unit test for function parseOpts
def test_parseOpts():
    import os
    os.getcwd()
    opts = parseOpts()[1]
    isinstance(opts.config_location, str)
    isinstance(opts.ignoreconfig, bool)
    isinstance(opts.verbose, int)
    isinstance(opts.writeinfojson, bool)
    isinstance(opts.writemeta, bool)
    isinstance(opts.writeannotations, bool)
    isinstance(opts.writeautomaticsub, bool)
    isinstance(opts.allsubtitles, bool)
    isinstance(opts.writethumbnail, bool)
    isinstance(opts.outtmpl, str)
    isinstance(opts.usetitle, bool)
    isinstance(opts.usename, bool)

# Generated at 2022-06-14 17:52:36.619966
# Unit test for function parseOpts
def test_parseOpts():
    if not isinstance(argv, list):
        argv = sys.argv[1:]
    if '-h' not in argv and '--help' not in argv and '-U' not in argv and '--update' not in argv:
        parser, opts, args = parseOpts(['-h'])
        sys.exit(0)
    # Test update
    if '-U' in argv or '--update' in argv:
        update()
        sys.exit(0)

# Generated at 2022-06-14 17:52:41.630730
# Unit test for function parseOpts
def test_parseOpts():
    # Parse command line arguments
    parser, opts, dummy_args = parseOpts(['-f', '22/18/17/best',
        'http://www.youtube.com/watch?v=BaW_jenozKc'])

    assert opts.format == ['22/18/17/best']


# Generated at 2022-06-14 17:52:48.543450
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts_, args_ = parseOpts(['--username', 'foo', '--password', 'bar', '--verbose', '--output', '%(id)s', 'foobar'])
    assert opts_.username == 'foo'
    assert opts_.password == 'bar'
    assert opts_.output == '%(id)s'
    assert opts_.verbose == True
    assert args_ == ['foobar']


# Generated at 2022-06-14 17:53:01.005930
# Unit test for function parseOpts
def test_parseOpts():
    from xml.dom.minidom import parseString
    parser, opts, args = parseOpts([
        '--output', 'TEST',
        '--get-id',
        'https://www.youtube.com/watch?v=BaW_jenozKc',
        'https://www.youtube.com/watch?v=fJ9rUzIMcZQ'])
    assert(opts.outtmpl == 'TEST')
    assert(opts.getid == True)
    assert(opts.ignoreerrors == True)
    assert(opts.verbose == False)
    assert(opts.usenetrc == False)
    assert(opts.ratelimit == '0')
    assert(opts.retries == 10)
    assert(opts.buffersize == '1024')
   

# Generated at 2022-06-14 17:53:06.014251
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts([])
    # assert parser
    assert opts
    assert args
    # assert opts.write_all_thumbnails
    # assert not opts.writethumbnail


# Generated at 2022-06-14 17:53:15.591269
# Unit test for function parseOpts
def test_parseOpts():
    _, opts, args = parseOpts(['-s', '-v'])
    assert(opts.simulate is True)
    assert(opts.verbose is True)
    assert(args == [])

    parser, opts, args = parseOpts(['-m', 'https://www.youtube.com/watch?v=BaW_jenozKc'])
    assert(opts.playliststart == 1)
    assert(opts.playlistend == 1)
    assert(args == [])

    parser, opts, args = parseOpts(['--max-downloads', '10'])
    assert(opts.max_downloads == 10)
    assert(args == [])

    parser, opts, args = parseOpts(['--max-filesize', '1024'])

# Generated at 2022-06-14 17:54:24.499433
# Unit test for function parseOpts
def test_parseOpts():
    def _test_parseOpts(args, expected):
        parser, opts, args = parseOpts(args)
        observed = dict((o.dest, getattr(opts, o.dest))
                        for o in parser.option_list
                        if o.dest is not None)
        assert observed == expected


# Generated at 2022-06-14 17:54:36.784157
# Unit test for function parseOpts
def test_parseOpts():
    def _test_parseOpts(args, expected_opts, expected_args):
        parser, opts, args = parseOpts(args)
        assert opts.__dict__ == expected_opts
        assert args == expected_args
        return parser

    parser = _test_parseOpts(
        ['--restrict-filenames'],
        {'restrictfilenames': True}, [])

    parser = _test_parseOpts(
        ['--no-mtime'],
        {'updatetime': False}, [])

    parser = _test_parseOpts(
        ['--extract-audio'],
        {'extractaudio': True}, [])


# Generated at 2022-06-14 17:54:50.906844
# Unit test for function parseOpts
def test_parseOpts():
    import re
    import unittest
    class TestParseOpts(unittest.TestCase):
        parser, opts, args = parseOpts(['-v'])
        self.assertEqual(opts.verbose, True)
        self.assertEqual(len(args),0)
        parser, opts, args = parseOpts(['-v', 'http://www.youtube.com/watch?v=BaW_jenozKc'])
        self.assertEqual(opts.verbose, True)
        self.assertEqual(args[0],'http://www.youtube.com/watch?v=BaW_jenozKc')

        self.assertNotEqual(opts.username, None)
        self.assertNotEqual(opts.password, None)
        self.assertE

# Generated at 2022-06-14 17:55:01.932118
# Unit test for function parseOpts
def test_parseOpts():
    try:
        parseOpts([])
    except SystemExit as e:
        if e.code != 2:
            raise Exception('Expected error code 2')
    else:
        raise Exception('Expected to exit with error code 2')
    return True


# Parse options
parser, opts, args = parseOpts()

# Do not ignore config files if an explicit config file is given as argument
if opts.config_location is not None:
    opts.ignoreconfig = False

# Do not ignore config files if --ignore-config was not given as argument
# (it has to be specified explicitly to be effective)
if '--ignore-config' not in sys.argv[1:] and '--ignore-config' not in sys.argv[1:]:
    opts.ignoreconfig = False


# Generated at 2022-06-14 17:55:12.842484
# Unit test for function parseOpts
def test_parseOpts():
    # Generate a YouTube age restricted video URL
    from youtube_dl.utils import age_restricted
    url = age_restricted('https://www.youtube.com/watch?v=9bZkp7q19f0')

    # Test download of age restricted video with default arguments
    _, opts, _ = parseOpts([url])
    assert opts.age_limit == None

    # Test the download of the age restricted video by providing the age
    # i.e. the video is downloaded successfully.
    _, opts, _ = parseOpts([url, '--age-limit', '18'])
    assert opts.age_limit == 18
    assert opts.download == True

    # Test the age restriction check logic for 18+ video

# Generated at 2022-06-14 17:55:18.595321
# Unit test for function parseOpts
def test_parseOpts():
    # Create options that don't need to be tested here
    class Namespace(object):
        pass

    class Option(object):
        def __init__(self, *args, **kargs):
            self.__dict__.update(kargs)
            self.dest = self.dest.replace('-', '_')

    opts = Namespace()
    opts.password = None
    opts.outtmpl = None
    opts.username = None
    opts.usenetrc = False
    opts.verbose = False
    opts.quiet = False
    opts.no_warnings = False
    opts.hls_prefer_ffmpeg = False
    opts.hls_prefer_native = False

    # Construct a parser

# Generated at 2022-06-14 17:55:28.717921
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts(['-v', '--output', '%(uploader)s/%(upload_date)s-%(title)s-%(id)s.%(ext)s', '--ignore-config', 'plugin://plugin.video.youtube/play/?video_id=BaW_jenozKc', '--youtube-skip-dash-manifest', '--max-filesize', '10485760', '--write-description', '--write-info-json', '--write-annotations', '--load-info-json', 'description.json', '--embed-subs', '--add-metadata', '--convert-subs', 'srt', '--xattrs', '--embed-thumbnail', '--prefer-ffmpeg'])
    assert opts.verbose

# Generated at 2022-06-14 17:55:33.578930
# Unit test for function parseOpts
def test_parseOpts():
    argv = ['--verbose']
    parser, opts, args = parseOpts(overrideArguments=argv)
    assert opts.verbose == True



# Generated at 2022-06-14 17:55:42.855183
# Unit test for function parseOpts
def test_parseOpts():

    opts = {
        # Intentionally using non-ASCII characters
        'username': 'user\u00e9', 'password': 'passwd\u00e9',
        'usenetrc': True, 'verbose': True,
        'format': 'best', 'format_limit': None,
        'playliststart': 1, 'playlistend': 10,
        'matchtitle': 'regex', 'rejecttitle': 'regex',
        'max_downloads': 10,
        'prefer_free_formats': True, 'verbose': True,
        'prefer_insecure': True,
        'listformats': True, 'list_thumbnails': True,
        'simulate': True,
        'skip_download': True,
        'outtmpl': 'test',
    }

# Generated at 2022-06-14 17:55:51.452667
# Unit test for function parseOpts
def test_parseOpts():
    # Test --version
    opts, args = parseOpts([])
    assert opts.version == False

    opts, args = parseOpts(['--version'])
    assert opts.version == True

    # Test --default-search
    opts, args = parseOpts([])
    assert opts.default_search == 'auto'

    opts, args = parseOpts(['--default-search', 'auto'])
    assert opts.default_search == 'auto'

    opts, args = parseOpts(['--default-search', 'ytsearch'])
    assert opts.default_search == 'ytsearch'

    opts, args = parseOpts(['--default-search', 'ytsearch5'])
    assert opts.default_search == 'ytsearch5'


# Generated at 2022-06-14 17:58:02.309299
# Unit test for function parseOpts
def test_parseOpts():
    from .utils import encodeArgument