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
#pragma once
#include <Python.h>
#include <iostream>

namespace ciostream {

class streambuf : public std::streambuf {
public:
    streambuf(PyObject *s);

    virtual ~streambuf();

    virtual std::streambuf::int_type underflow() override;

    virtual int overflow(int c) override;

private:
        PyObject                *m_stream_obj;
        PyObject                *m_str;
        char                    m_buf[4096];
        int                     m_count;
};

class _cistream : public std::istream {
public:
    _cistream(PyObject *);

    virtual ~_cistream();

private:
    streambuf                 m_buf;

};

class _costream : public std::ostream {
public:
    _costream(PyObject *);

    virtual ~_costream();

private:
    streambuf                 m_buf;

};

}
