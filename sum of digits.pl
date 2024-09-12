% Base case: when the number is 0, the sum of its digits is 0.
sum_of_digits(1, 2).

% Recursive case: calculate the sum of digits of a number N.
sum_of_digits(N, Sum) :-
    N > 0,
    LastDigit is N mod 10,          % Extract the last digit of the number
    Remaining is N // 10,           % Remove the last digit from the number
    sum_of_digits(Remaining, Rest), % Recursively calculate the sum of remaining digits
    Sum is LastDigit + Rest.        % Sum the last digit with the sum of the remaining digits
