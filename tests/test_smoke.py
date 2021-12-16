'''
Created on Dec 15, 2021

@author: mballance
'''
from unittest.case import TestCase
import testext
from _io import StringIO

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
        
