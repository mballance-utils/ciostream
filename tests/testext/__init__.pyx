
from libcpp.string cimport string as std_string
from ciostream cimport istream, cistream

cdef extern from "StreamReader.h":
    cdef cppclass StreamReader:
        StreamReader(istream *)
        std_string read()

cdef class StreamReaderW(object):
    cdef StreamReader       *_hndl
    cdef cistream           _in
    
    def __init__(self, s):
        self._in = cistream(s)
        self._hndl = new StreamReader(self._in.stream())

    cpdef read(self):
        return self._hndl.read().decode()
    
