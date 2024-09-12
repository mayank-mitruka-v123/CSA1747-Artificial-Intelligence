% Base case: the sum of integers from 1 to 0 is 0.
sum_of_integers(0, 0).

% Recursive case: the sum of integers from 1 to N.
sum_of_integers(N, Sum) :-
    N > 0,
    Previous is N - 1,               % Decrement N to get the previous integer
    sum_of_integers(Previous, Rest), % Recursively calculate the sum of integers from 1 to N-1
    Sum is N + Rest.                 % Sum N and the recursive sum
