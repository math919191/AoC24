

from sympy import symbols, Eq, solve
from ortools.linear_solver import pywraplp

with open('input/day13_test.txt') as f: s = f.read()
systems = s.split('\n\n')

total = 0

for system in systems:
    button1, button2, prize = system.split('\n')
    button1split = button1.split("+")
    button1x = int(button1split[1][:button1split[1].index(',')])
    button1y = int(button1split[2])

    button2split = button2.split("+")
    button2x = int(button2split[1][:button2split[1].index(',')])
    button2y = int(button2split[2])

    prizesplit = prize.split("=")
    prizex = int(prizesplit[1][:prizesplit[1].index(',')])
    prizey = int(prizesplit[2])

    # input parsing finished
    print(button1x, button1y, button2x, button2y, prizex, prizey)
    # system of equations
    # button1x * (A) + button2x * (B) = prizex
    # button1y * (A) + button2y * (B) = prizey
    # Where: A, B <= 100
    # where min(A * 3 + 1 * B)

    # a, b = symbols('a b')
    # eq1 = Eq(button1x * a + button2x * b, prizex)
    # eq2 = Eq(button1y * a + button2y * b, prizey)
    # solution = solve((eq1, eq2), (a, b))

    # get solver
    solver = pywraplp.Solver.CreateSolver('SAT')

    # declare decision variables
    x1 = solver.IntVar(0.0, solver.infinity(), 'x1')
    x2 = solver.IntVar(0.0, solver.infinity(), 'x2')

    # declare objective
    solver.Minimize(3 * x1 + 1 * x2)

    # declare constraints
    solver.Add(x1 <= 100)
    solver.Add(x1 <= 100)
    solver.Add(x1 >= 0)
    solver.Add(x2 >= 0)
    solver.Add(button1x * x1 + button2x * x2 == prizex)
    solver.Add(button1y * x1 + button2y * x2 == prizey)

    # solve
    status = solver.Solve()
    # print results
    if status == pywraplp.Solver.OPTIMAL:
        print("Solution:")
        print(f"Objective value = {solver.Objective().Value():0.1f}")
        print(f"x = {x1.solution_value():0.1f}")
        print(f"y = {x2.solution_value():0.1f}")
        total += solver.Objective().Value()

    else:
        print("The problem does not have an optimal solution.")


    print()

print(total)