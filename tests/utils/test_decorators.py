import unittest
from opendeep.utils.decorators import (inherit_docs, init_optimizer)


class TestDecorators(unittest.TestCase):
    def setUp(self):
        pass

    def testDocString(self):
        class Foo(object):
            """This is a Foo class"""
            def __init__(self):
                """Initializes Foo"""
                self.foo = 'foo'

            def bar1(self):
                """Let's call bar1"""
                self.foo = 'bar1'

            def bar2(self):
                """Let's call bar2"""
                self.foo = 'bar2'

        @inherit_docs
        class Bar(Foo):
            def __init__(self):
                super(Bar, self).__init__()

            def bar1(self):
                self.foo = 'foobar1'

            def bar2(self):
                """New docstring"""
                self.foo = 'foobar2'

        bar = Bar()
        self.assertEquals(bar.__init__.__doc__, "Initializes Foo")
        self.assertEquals(bar.bar1.__doc__, "Let's call bar1")
        self.assertEquals(bar.bar2.__doc__, "New docstring")

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
