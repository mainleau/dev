list_max([A], A) :- !.
list_max([A | B], C) :- list_max(B, D), (A > D -> C = A ; C = D).
