
fact(rain).
fact(cold).

rule(wet_ground) :-
    fact(rain).

rule(carry_umbrella) :-
    fact(rain).

rule(wear_jacket) :-
    fact(cold).

derive(wet_ground) :-
    rule(wet_ground).

derive(carry_umbrella) :-
    rule(carry_umbrella).

derive(wear_jacket) :-
    rule(wear_jacket).
