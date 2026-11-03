
parent(john, mary).
parent(mary, david).

grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).

ancestor(X, Y) :-
    parent(X, Y).

ancestor(X, Y) :-
    parent(X, Z),
    ancestor(Z, Y).

can_travel(X) :-
    has_ticket(X),
    has_id(X).

has_ticket(john).
has_id(john).
