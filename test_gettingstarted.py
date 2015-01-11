import pytest

'''
Functions that have the prefix 'test_' will be run by pytest. 
The same prefix must be applied to the filename for pytest
to 'see' it.
'''

def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5

def f():
    raise SystemExit(1)

def test_mytest():
    #This is a way to assert exceptions are raised
    with pytest.raises(SystemExit):
        f()

'''
If grouping tests in classes, the class name must be prefixed by 'Test'
in order to be seen.
'''
class TestClass(object):

    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')

def test_needsfiles(tmpdir):
    '''
    Adding a parameter called 'tmpdir' makes py.test create temporary 
    directory which can be used in the test
    '''
    print(tmpdir)
    assert 0

