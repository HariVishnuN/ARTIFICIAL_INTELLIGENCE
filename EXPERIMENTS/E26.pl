fruit_color(apple, red).
fruit_color(banana, yellow).
fruit_color(grape, green).
fruit_color(orange, orange).
fruit_color(cherry, red).
fruit_color(blackberry, black).
fruit_color(plum, purple).

find_by_color(Color) :-
    fruit_color(Fruit, Color),
    format('Found: ~w is ~w.~n', [Fruit, Color]),
    fail. % The 'fail' predicate forces Prolog to backtrack and find the next match.
find_by_color(_) :- 
    write('No more fruits found for this color.').

% List every fruit and its color entry one by one
list_all_fruits :-
    fruit_color(Fruit, Color),
    format('Fruit: ~w, Color: ~w~n', [Fruit, Color]),
    fail.
list_all_fruits :- 
    write('End of database.').