# advent-of-code
advent of code repo; sorted by year and then day

calling convention for 2020 is
`python3 aoc.py <day> <task>`
the code itself is stored in separate folders which are loaded with the same script, to minimize the ammount of copy pasted code and simplify changing it.
each day folder contains an `__init__.py` and an `input` file, where `__init__.py` contains two functions called `ver_one()` and `ver_two()`, that each take the `input` file as input and returns the correct answer for a given day. All solutions are written to be generic and should work regardless of input file given. (In other words, problems like day 8, task 2, for which editing part of the input file was a task part, are done entirely in memory.
