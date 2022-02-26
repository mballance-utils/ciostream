#****************************************************************************
#* iostream.pyx
#*
#* Python I/O stream to C++ I/O stream bridge
#*
#* Copyright 2021 Matthew Ballance
#*
#* Licensed under the Apache License, Version 2.0 (the "License");
#* you may not use this file except in compliance with the License.
#* You may obtain a copy of the License at
#*
#*     http://www.apache.org/licenses/LICENSE-2.0
#*
#* Unless required by applicable law or agreed to in writing, software
#* distributed under the License is distributed on an "AS IS" BASIS,
#* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#* See the License for the specific language governing permissions and
#* limitations under the License.
#*
#****************************************************************************

# cython: language=c++

cimport cpython.ref as cpy_ref
#cimport iostream_decl

class my_cls(object):
    def __init__(self):
        import inspect
        frame = inspect.stack()[1]
        print("frame: %s" % str(frame))
        pass

cdef class cistream(object):

    def __init__(self, s):
        self._hndl = new _cistream(<cpy_ref.PyObject *>(s))
        
    def __dealloc__(self):
        del self._hndl
        
    cdef istream *stream(self):
        return self._hndl

cdef class costream(object):

    def __init__(self, s):
        self._hndl = new _costream(<cpy_ref.PyObject *>(s))
        
    def __dealloc__(self):
        del self._hndl

    cdef ostream *stream(self):
        return self._hndl
    
cdef public void costream_write(obj, int c) with gil:
    obj.write("%c" % c)
