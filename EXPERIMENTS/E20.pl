planet(mercury, rocky, 0).
planet(venus, rocky, 0).
planet(earth, rocky, 1).
planet(mars, rocky, 2).
planet(jupiter, gas, 79).
start :- write('Enter planet name (lowercase, with period): '), read(Planet), 
         (planet(Planet, Type, Moons) -> 
         write('Type: '), write(Type), write(', Moons: '), write(Moons) ; write('Not found')), nl.