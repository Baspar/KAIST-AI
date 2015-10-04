#----------------------------------------------------------------------------#
#
# [CS470] Introduction to Artificial Intelligence
# 2015 Fall
# Assignment2 Part2: Finding the length of the shaded square
#
#----------------------------------------------------------------------------#

from Numberjack import *

def model(top, n):
    # [Problem2: A and B]
    # formulates the problem into CSP model.
    # top represents the maximum possible length of the squares.
    # n represents the number of squares in total, indexed from 0 to n-1.
    # returns the Model()
    squares=VarArray(n, 1, top)
    model = Model(
        #All different constraint
        AllDiff(squares),

        #Order constraint - 2-B
        [squares[i]<squares[i+1] for i in range(n-1)],

        #Constraint on the first square
        squares[0]==1,

        #Contraints on length
        squares[0] + squares[2] == squares[3],
        squares[3] + squares[0] == squares[4],
        squares[3] + squares[4] == squares[6],
        squares[4] + squares[6] == squares[7],
        squares[2] + squares[3] + squares[6] == squares[8],
        squares[0] + squares[4] + squares[7] == squares[10],
        squares[1] + squares[11] == squares[13],
        squares[1] + squares[13] == squares[14],
        squares[1] + squares[14] == squares[15],
        squares[9] + squares[10] == squares[16],
        squares[6] + squares[7] + squares[8] == squares[17],
        squares[5] + squares[15] == squares[18],
        squares[5] + squares[18] == squares[19],
        squares[8] + squares[17] == squares[20],
        squares[9] + squares[16] == squares[21],
        squares[13] + squares[14] == squares[22],
        squares[12] + squares[19] == squares[23],
        squares[20] + squares[21] + squares[22] == squares[24],
        squares[17] + squares[20] + squares[23] == squares[24],
        squares[18] + squares[19] + squares[23] == squares[24],
        squares[14] + squares[15] + squares[18] + squares[22] == squares[24],

        #Constraint on area
        Sum([squares[i]*squares[i] for i in range(n-1)]) == squares[24]*squares[24]
    )
    return model

def solve(param):
    m = model(param['Top'], param['N'])
    solver = m.load(param['solver'])
    solver.solve()
    print 'Length of squares\n', solver.get_solution()
    print 'The length of the 17th square is {0}'.format(solver.get_solution()[16])
    print 'Time taken:', solver.getTime()

solve(input({'solver':'Mistral', 'Top':200, 'N':25}))
