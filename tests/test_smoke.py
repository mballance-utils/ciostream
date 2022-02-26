'''
Created on Dec 15, 2021

@author: mballance
'''
from unittest.case import TestCase
import testext
from _io import StringIO
from ciostream import my_cls
import inspect

class TestSmoke(TestCase):
    
    def test_smoke(self):
        data = """
        Hello, World
        """

        for e in dir(testext):
            print("e: %s" % str(e))
        reader = testext.StreamReaderW(StringIO(data))
        
        result = reader.read()
        
        print("result: %s" % result)
        
        pass
    
    def test_write_smoke(self):
        data = """
        Hello, World
        """

        s = StringIO()        
        writer = testext.StreamWriterW(s)
        
        writer.write(data)
        print("s.data=%s" % s.getvalue())

    def test_my_cls(self):
        c = my_cls()
        print("file of c: %s" % inspect.getsourcefile(my_cls))
        pass

        
