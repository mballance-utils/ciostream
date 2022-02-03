/*
 * StreamWriter.cpp
 *
 *  Created on: Feb 3, 2022
 *      Author: mballance
 */

#include <stdio.h>
#include "StreamWriter.h"

StreamWriter::StreamWriter(std::ostream *out) : m_out(out) {
	// TODO Auto-generated constructor stub

}

StreamWriter::~StreamWriter() {
	// TODO Auto-generated destructor stub
}

void StreamWriter::write(const std::string &data) {
	for (uint32_t i=0; i<data.size(); i++) {
		(*m_out) << data.at(i);
	}
}

