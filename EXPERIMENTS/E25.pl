
initial_state(at_door, on_floor, at_window, has_not).

move(state(at_door, on_floor, at_window, has_not),
     walk,
     state(at_window, on_floor, at_window, has_not)).

move(state(at_window, on_floor, at_window, has_not),
     push_box,
     state(at_middle, on_floor, at_middle, has_not)).

move(state(at_middle, on_floor, at_middle, has_not),
     climb,
     state(at_middle, on_box, at_middle, has_not)).

move(state(at_middle, on_box, at_middle, has_not),
     grasp,
     state(at_middle, on_box, at_middle, has)).

solve(State, []) :-
    State = state(_, _, _, has).

solve(State, [Action|Rest]) :-
    move(State, Action, NextState),
    solve(NextState, Rest).
