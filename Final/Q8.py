#Show the process how solve equation module will solve the following unsolved equations.
#[[['theory', '+', 'practical'], '=', 'total'], ['theory', '=', ['internal', '+', 'marks']], ['marks', '=', ['mid', '+', 'final']], ['internal', '=', ['quizzes', '+', 'assignments']], ['To-find', '=', ['total', '=', ['quizzes,', '=', ['assignments,', '=', ['mid,', '=', ['final', '=', 'practical']]]]]]]
#cost = ( admission + tuition )
#tuition = ( semester * total )
#total = 8
#semester = 45000
#admission = 12000
#To-find = cost
import sys
eqs = [
    ['cost', '=', ['admission', '+', 'tuition']],
    ['tuition', '=', ['semester', '*', 'total']],
    ['total', '=', '8'],
    ['semester', '=', '45000'],
    ['admission', '=', '12000'],
    ['to-find', '=', 'cost'],
]

sys.path = ['..', 'algos']

from student import solve_equations
solve_equations(eqs)
