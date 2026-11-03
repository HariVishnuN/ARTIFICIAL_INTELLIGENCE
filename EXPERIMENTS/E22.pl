
bird(sparrow).
bird(parrot).
bird(pigeon).
bird(eagle).
bird(ostrich).
bird(penguin).

can_fly(sparrow).
can_fly(parrot).
can_fly(pigeon).
can_fly(eagle).

cannot_fly(ostrich).
cannot_fly(penguin).

check_flying(Bird) :-
    can_fly(Bird),
    write(Bird),
    write(' can fly.').

check_flying(Bird) :-
    cannot_fly(Bird),
    write(Bird),
    write(' cannot fly.').

check_flying(Bird) :-
    \+ bird(Bird),
    write('Unknown bird.').
