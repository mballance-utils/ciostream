/*
 * StreamWriter.h
 *
 *  Created on: Feb 3, 2022
 *      Author: mballance
 */

#pragma once
#include <iostream>
#include <string>


class StreamWriter {
public:
	StreamWriter(std::ostream *out);

	virtual ~StreamWriter();

	void write(const std::string &data);

private:
	std::ostream				*m_out;

};

