# Build Your Own wc Tool

This is my python solution to John Crickett's Coding Challenge: [Build Your Own wc Tool](https://codingchallenges.fyi/challenges/challenge-wc/)

## Description

This is a simple implementation of Unix command line tool wc written in Python.

It takes an input file and generates an output based on the chosen option.

There are four options supported:

- `-c`: displays the number of bytes in a file.
- `-l`: displays the number of lines in a file.
- `-w`: displays the number of words in a file.
- `-m`: displays the number of chars in a file.

If no option is provided, it displays all the data: number of bytes, lines, words and chars.

## Dependencies

Python, Click, Sys

## Usage

The tool tries to follow wc syntax, the usage is as follows:

`python main.py [option] filename`

## License

This project is licensed under the terms of the MIT license.
