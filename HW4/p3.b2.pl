:-dynamic(on/2).
/*Initialization*/
on(a,b).
on(b,c).
on(c,table).


/*Code definition*/
r_put_on(A,B) :-
    on(A,B).
r_put_on(A,B) :-
    not(on(A,B)),
    A \== table,
    A \== B,
    clear_off(A),        /* N.B. "action" used as precondition */
    clear_off(B),
    on(A,X),
    retract(on(A,X)),
    assert(on(A,B)),
    assert(move(A,X,B)).
clear_off(table).    /* Means there is room on table */
clear_off(A) :-      /* Means already clear */
    not(on(_X,A)).
clear_off(A) :-
    A \== table,
    on(X,A),
    clear_off(X),      /* N.B. recursion */
    retract(on(X,A)),
    assert(on(X,table)),
    assert(move(X,A,table)).
do(Glist) :-
    valid(Glist),
    do_all(Glist,Glist).
valid(_).                          /* Temporary. See Exercise 2.19.1 */
do_all([G|R],Allgoals) :-          /* already true now */
    call(G),
    do_all(R,Allgoals),!.         /* continue with rest of goals */
do_all([G|_],Allgoals) :-          /* must do work to achieve */
    achieve(G),
    do_all(Allgoals,Allgoals).    /* go back and check previous goals */
do_all([],_Allgoals).              /* finished */
achieve(on(A,B)) :-
    r_put_on(A,B).


/*Print results according to the goal*/
do([on(a,table),on(b,a),on(c,b)]), listing(on), listing(move).
