/*
 * Copyright 2021 Matthew Ballance
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#include "ciostream_native.h"
#include "__init__.h"

namespace ciostream {

streambuf::streambuf(PyObject *s) {
    m_stream_obj = s;
    Py_XINCREF(m_stream_obj);
    m_str = 0;
    m_count = 0;
}

streambuf::~streambuf() {
    Py_XDECREF(m_stream_obj);
    Py_XDECREF(m_str);
}

std::streambuf::int_type streambuf::underflow() {
    Py_XDECREF(m_str);
    m_str = PyObject_CallMethod(m_stream_obj, "read", "L", 4096);
    Py_XINCREF(m_str);
    Py_ssize_t sz;
    char *str = 0;

    if (PyUnicode_Check(m_str)) {
        str = (char *)PyUnicode_AsUTF8AndSize(m_str, &sz);
    } else if (PyBytes_Check(m_str)) {
        PyBytes_AsStringAndSize(m_str, &str, &sz);
    } else {
        fprintf(stdout, "Unknown\n");
    }

    if (sz == 0) {
        return traits_type::eof();
    } else {
        setg(str, str, str+sz);
        return traits_type::to_int_type(str[0]);
    }
}

int streambuf::overflow(int c) {
	if (c != EOF) {
		costream_write(m_stream_obj, c);
	}
	return 0;
}


_cistream::_cistream(PyObject *stream) : std::istream(&m_buf), m_buf(stream) {

}

_cistream::~_cistream() {

}

_costream::_costream(PyObject *stream) : std::ostream(&m_buf), m_buf(stream) {

}

_costream::~_costream() {

}

}

