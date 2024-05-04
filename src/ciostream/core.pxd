#****************************************************************************
#* iostream.pyd
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

cdef extern from "<iostream>" namespace "std":
    cdef cppclass istream:
        pass
    cdef cppclass ostream:
        pass

cdef extern from 'ciostream_native.h' namespace "ciostream":
    cpdef cppclass _cistream(istream):
        _cistream(cpy_ref.PyObject *)
        
    cpdef cppclass _costream(ostream):
        _costream(cpy_ref.PyObject *)
        
cdef class cistream(object):
    cdef istream           *_hndl
    cdef istream *stream(self)
    
cdef class costream(object):
    cdef ostream           *_hndl
    cdef ostream *stream(self)

    

