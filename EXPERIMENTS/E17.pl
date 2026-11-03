sum(0, 0).
sum(N, R) :- N > 0, N1 is N - 1, sum(N1, R1), R is R1 + N.
start :- write('Enter N (with a period): '), read(N), sum(N, Result), write('Sum is: '), write(Result), nl.