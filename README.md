# ciostream

Provides a Cython wrapper around C++ iostream, allowing Python
extensions to use Python streams with C++ code that uses
C++ iostreams.

## Example

Let's say that we have a class that reads from a C++ istream.
The class definition is shown below:

```
class StreamReader {
public:
	StreamReader(std::istream *in);

	virtual ~StreamReader();

	std::string read();

private:
	std::istream			*m_in;

};
```

We would like to wrap this as a Cython class and pass a Python
stream to the constructor. Using the ciostream extension, 
our Cython extension class looks like this:

```
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
```

Note that the ciostream package provides a definition of the std::istream
object that we can use in declaring the signature of the StreamReader
C++ class.

The `__init__` method of the extension class (StreamReaderW) creates an
instance of the `cistream` class, passing in the Python stream (s). It
then passes the std::stream handle to the C++ StreamReader constructor.

The C++ code is provided a C++ istream pointer that it can use to read 
from any Python stream.

Here is a small test for this extension class:

```
    def test_smoke(self):
        data = """
        Hello, World
        """

        for e in dir(testext):
            print("e: %s" % str(e))
        reader = testext.StreamReaderW(StringIO(data))
        
        result = reader.read()
        
        print("result: %s" % result)
```



