/*
 * StreamReader.h
 *
 *  Created on: Dec 15, 2021
 *      Author: mballance
 */

#pragma once
#include <iostream>
#include <string>

class StreamReader {
public:
	StreamReader(std::istream *in);

	virtual ~StreamReader();

	std::string read();

private:
	std::istream			*m_in;

};

