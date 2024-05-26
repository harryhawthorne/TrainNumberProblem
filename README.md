# Train Carriage Number Problem (Solver)

## Background
Train carriages in Sydney are four digit numbers, 0001 to 9999.
The aim of the game is to make 10 with the digits.

## Rules
1. Must use all the digits.
2. Must use the digits in order (brackets can be used).
3. Operations available: `['+', '-', '/', '*', '**']`.

## Instructions
Run `python solver.py <num>`.

If it is possible to solve the problem with the given operations, the steps of the first solution found will be printed.
If no solution is found `"No solution found"` will be printed.

## Optional arguments
`-m`: Try all possible combinations of merged digits, e.g. `[1, 2, 3, 4]` would include `[12, 3, 4]`, `[1, 23, 4]` etc.

In the future I want to add more optional arguments to increase the number of solvable problems, such as an out-of-order argument.

