% Partie 1

n(0).
n(1).
n(2).
n(3).
n(4).
n(5).
n(6).
n(7).
n(8).
n(9).

transformer(A, B, C, D, E, N) :- N is 10000*A + 1000*B + 100*C + 10*D + E.
transformer(A, B, C, D, E, F, N) :- N is A*100000 + B*10000 + C*1000 + D*100 + E*10 + F.
transformer(A, B, C, D, E, F, G, N) :- N is A*1000000 + B*100000 + C*10000 + D*1000 + E*100 + F*10 + G.

% Partie 2

generer(R, O, U, G, E, I, S, A) :-
    n(R),
    n(O), O \= R,
    n(U), U \= O, U \= R,
    n(G), G \= U, G \= O, G \= R,
    n(E), E \= G, E \= U, E \= O, E \= R,
    n(I), I \= E, I \= G, I \= U, I \= O, I \= R,
    n(S), S \= I, S \= E, S \= G, S \= U, S \= O, S \= R,
    n(A), A \= S, A \= I, A \= E, A \= G, A \= U, A \= O, A \= R,
    transformer(R, O, U, G, E, ROUGE),
    transformer(G, O, R, G, E, GORGE),
    transformer(O, I, S, E, A, U, OISEAU),
    OISEAU is ROUGE+GORGE.

% aggregate_all(count, generer(R, O, U, G, E, I, S, A), Count).
% 3 solutions sont possibles.

% time(generer(R, O, U, G, E, I, S, A)).
% 36 303 805, 467 948, 10 543 puis 14 552 026 inférences relevées.


generer_sans_zero(R, O, U, G, E, I, S, A) :-
    n(R), R \= 0,
    n(O), O \= R, O \= 0,
    n(U), U \= O, U \= R,
    n(G), G \= U, G \= O, G \= R,
    n(E), E \= G, E \= U, E \= O, E \= R,
    n(I), I \= E, I \= G, I \= U, I \= O, I \= R,
    n(S), S \= I, S \= E, S \= G, S \= U, S \= O, S \= R,
    n(A), A \= S, A \= I, A \= E, A \= G, A \= U, A \= O, A \= R,
    transformer(R, O, U, G, E, ROUGE),
    transformer(G, O, R, G, E, GORGE),
    transformer(O, I, S, E, A, U, OISEAU),
    OISEAU is ROUGE+GORGE.

% aggregate_all(count, generer_sans_zero(R, O, U, G, E, I, S, A),
% Count).
% 2 solutions sont possibles.

% time(generer_sans_zero(R, O, U, G, E, I, S, A)).
% 27 645 723, 10 543 puis 13 411 293 inférences relevées

% Partie 3

generer_between(F, R, E, S, O, U, B, A, T, N) :-
    between(0, 9, F),
    between(0, 9, R), R \= F,
    between(0, 9, E), E \= R, E \= F,
    between(0, 9, S), S \= E, S \= R, S \= F,
    between(0, 9, O), O \= S, O \= E, O \= R, O \= F,
    between(0, 9, U), U \= O, U \= S, U \= E, U \= R, U \= F,
    between(0, 9, B), B \= U, B \= O, B \= S, B \= R, B \= R, B \= F,
    between(0, 9, A), A \= B, A \= U, A \= O, A \= S, A \= E, A \= R, A \= F,
    between(0, 9, T), T \= A, T \= B, T \= U, T \= O, T \= S, T \= E, T \= R, T \= F,
    between(0, 9, N), N \= T, N \= A, N \= B, N \= U, N \= O, N \= S, N \= E, N \= R, N \= F,
    transformer(F, R, E, R, E, FRERE),
    transformer(S, O, E, U, R, SOEUR),
    transformer(B, A, S, T, O, N, BASTON),
    BASTON is FRERE+SOEUR.

% time(generer_sans_zero(R, O, U, G, E, I, S, A)).
% 82 583 128, 13 483 718, 59 080 377, etc. inférences relevées


% Partie 4

generer_menier(M, E, N, I, R, P, O, L, G, Q, U, A) :-
    between(0, 9, M),
    between(0, 9, E), E \= M,
    between(0, 9, N), N \= E, N \= M,
    between(0, 9, I), I \= N, I \= E, I \= M,
    between(0, 9, R), R \= I, R \= N, R \= E, R \= M,
    between(0, 9, P), P \= R, P \= I, P \= N, P \= E, P \= R,
    between(0, 9, O), O \= P, O \= R, O \= I, P \= N, P \= E, P \= M,
    between(0, 9, L), L \= O, L \= P, L \= R, L \= I, L \= N, L \= E, L \= M,
    between(0, 9, G), G \= L, G \= O, G \= P, G \= R, G \= I, G \= N, G \= E, G \= M,
    between(0, 9, Q), Q \= G, Q \= L, Q \= O, Q \= P, Q \= R, Q \= I, Q \= N, Q \= E, Q \= M,
    between(0, 9, U), U \= Q, U \= G, U \= L, U \= O, U \= P, U \= R, U \= I, U \= N, U \= E, U \= M,
    between(0, 9, A), A \= Q, A \= G, A \= L, A \= O, A \= P, A \= R, A \= I, A \= N, A \= E, A \= M, A \= U,
    transformer(M, E, N, I, E, R, MENIER),
    transformer(P, R, O, L, O, G, PROLOG),
    transformer(M, A, G, I, Q, U, E, MAGIQUE),
    MAGIQUE is MENIER+PROLOG.

% Constatons qu'en utilisant un nombre de lettres supérieur à 10, aucun
% prédicat ne pourra être vrai, chaque lettre ne pourrait s'associer à
% un chiffre unique.
