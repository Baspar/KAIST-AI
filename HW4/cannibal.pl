%Part b)
    %Left to right
        %L=(1m)=>R
            follows([ML1, CL, left, MR1, CR], [ML2, CL, right, MR2, CR]) :-
                ML2 is ML1-1,
                MR2 is MR1+1,
                admissible(ML2, CL, MR2, CR).
        %L=(2m)=>R
            follows([ML1, CL, left, MR1, CR], [ML2, CL, right, MR2, CR]) :-
                ML2 is ML1-2,
                MR2 is MR1+2,
                admissible(ML2, CL, MR2, CR).
        %L=(1M1c)=>R
            follows([ML1, CL1, left, MR1, CR1], [ML2, CL2, right, MR2, CR2]) :-
                CL2 is CL1-1,
                CR2 is CR1+1,
                ML2 is ML1-1,
                MR2 is MR1+1,
                admissible(ML2, CL2, MR2, CR2).
        %L=(2c)=>R
            follows([ML, CL1, left, MR, CR1], [ML, CL2, right, MR, CR2]) :-
                CL2 is CL1-2,
                CR2 is CR1+2,
                admissible(ML, CL2, MR, CR2).
        %L=(1c)=>R
            follows([ML, CL1, left, MR, CR1], [ML, CL2, right, MR, CR2]) :-
                CL2 is CL1-1,
                CR2 is CR1+1,
                admissible(ML, CL2, MR, CR2).

    %Right to Left
        %L<=(1m)=R
            follows([ML1, CL, right, MR1, CR], [ML2, CL, left, MR2, CR]) :-
                ML2 is ML1+1,
                MR2 is MR1-1,
                admissible(ML2, CL, MR2, CR).
        %L<=(2m)=R
            follows([ML1, CL, right, MR1, CR], [ML2, CL, left, MR2, CR]) :-
                ML2 is ML1+2,
                MR2 is MR1-2,
                admissible(ML2, CL, MR2, CR).
        %L<=(1M1c)=R
            follows([ML1, CL1, right, MR1, CR1], [ML2, CL2, left, MR2, CR2]) :-
                CL2 is CL1+1,
                CR2 is CR1-1,
                ML2 is ML1+1,
                MR2 is MR1-1,
                admissible(ML2, CL2, MR2, CR2).
        %L<=(2c)=R
            follows([ML, CL1, right, MR, CR1], [ML, CL2, left, MR, CR2]) :-
                CL2 is CL1+2,
                CR2 is CR1-2,
                admissible(ML, CL2, MR, CR2).
        %L<=(1c)=R
            follows([ML, CL1, right, MR, CR1], [ML, CL2, left, MR, CR2]) :-
                CL2 is CL1+1,
                CR2 is CR1-1,
                admissible(ML, CL2, MR, CR2).

%Part c)
    admissible(M1, C1, M2, C2) :-
        M1>=0,
        M2>=0,
        C1>=0,
        C2>=0,
        (M1>=C1; M1 is 0),
        (M2>=C2; M2 is 0).

%Part d)
    %Case we have to look for it
        plan(X,G,L):-
            follows(X, Z),
            not(member(Z, L)),
            plan(Z, G, [Z|L]).
    %Case we found a plan to the goal
        plan(G, G, L):-
            out(L),
            write('DONE'), nl.

% Print function
    out([]) :- true.
    out([A|G]) :-
        out(G),
        write(A), nl,
        write('  ||'), nl,
        write('  \\/'), nl.

%Final
    find:-
        plan([3, 3, left, 0, 0], [0, 0, right, 3, 3], [[3, 3, left, 0, 0]]).
