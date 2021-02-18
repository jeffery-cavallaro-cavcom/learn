#ifndef PRIMER_CH01_INPUT_H_
#define PRIMER_CH01_INPUT_H_

// Methods to input data types.

#include <iostream>
#include <string>

// Converts the specified integer string to an integer value.
int string_integer(const std::string &in);

// Inputs an integer from the specified input stream.
int input_integer(std::istream &in);

// Prompts for an integer from the standard input.
int prompt_integer(const std::string &prompt);

#endif  // PRIMER_CH01_INPUT_H_
