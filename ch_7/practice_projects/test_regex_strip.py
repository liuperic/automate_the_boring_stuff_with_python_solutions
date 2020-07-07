# Pytest unit test for regex_strip

from regex_strip import regex_strip

def test_regex_strip():
    assert '-test-' == regex_strip('    -test-    ')
    assert '-test-' == regex_strip('    -test-    ')
    assert '-test-' == regex_strip('    -test-    ')

    assert '123abc123' == regex_strip('abc123abc123abc', 'abc')
    assert '123abc123' == regex_strip('abcabc123abc123abcabc', 'abc')
    assert ' is a test' == regex_strip('this is a test', 'this')