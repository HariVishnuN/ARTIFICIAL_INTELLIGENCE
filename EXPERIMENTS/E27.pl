edge(a, b).
edge(a, c).
edge(b, d).
edge(b, e).
edge(c, f).
edge(c, g).

h(a, 3).
h(b, 4).
h(c, 2).
h(d, 5).
h(e, 6).
h(f, 1).
h(g, 0).

best_first(Start, Goal, Path) :-
    h(Start, H),
    bfs([[H, [Start]]], Goal, RevPath),
    reverse(RevPath, Path).

bfs([[_, [Goal | Path] | _] | _], Goal, [Goal | Path]).

bfs([[_, [Current | Path] | Queue] | RestQueue], Goal, FinalPath) :-
    findall([H_Next, [Next, Current | Path]],
            (edge(Current, Next),
             \+ member(Next, [Current | Path]),
             h(Next, H_Next)),
            Successors),
    append(Queue, Successors, CombinedQueue),
    sort(CombinedQueue, SortedQueue),
    bfs(SortedQueue, Goal, FinalPath).