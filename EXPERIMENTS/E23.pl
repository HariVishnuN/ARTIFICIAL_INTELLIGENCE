
male(john).
male(peter).
male(david).
female(mary).
female(lisa).
female(susan).

parent(john, peter).
parent(mary, peter).
parent(john, lisa).
parent(mary, lisa).
parent(peter, david).
parent(lisa, susan).

father(X, Y) :-
    male(X),
    parent(X, Y).

mother(X, Y) :-
    female(X),
    parent(X, Y).

sibling(X, Y) :-
    parent(Z, X),
    parent(Z, Y),
    X \= Y.

grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).
