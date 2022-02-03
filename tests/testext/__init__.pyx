
from libcpp.string cimport string as std_string
from ciostream cimport istream, cistream, ostream, costream

cdef extern from "StreamReader.h":
    cdef cppclass StreamReader:
        StreamReader(istream *)
        std_string read()
        
cdef extern from "StreamWriter.h":
    cdef cppclass StreamWriter:
        StreamWriter(ostream *)
        void write(const std_string)

cdef class StreamReaderW(object):
    cdef StreamReader       *_hndl
    cdef cistream           _in
    
    def __init__(self, s):
        self._in = cistream(s)
        self._hndl = new StreamReader(self._in.stream())

    cpdef read(self):
        return self._hndl.read().decode()
    
cdef class StreamWriterW(object):
    cdef StreamWriter       *_hndl
    cdef costream           _out
    
    def __init__(self, s):
        self._out = costream(s)
        self._hndl = new StreamWriter(self._out.stream())
    
    cpdef write(self, s):
        return self._hndl.write(s.encode())
    
