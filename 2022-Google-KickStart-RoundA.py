# PROBLEM A: SPEED TYPING 

test_cases = int(input())
for case_number in range(1, test_cases + 1):
    target_string = input()
    given_string = input()

    match_position = 0
    for character in target_string:
        match_position = given_string.find(character, match_position) + 1
        if not match_position:
            operations_needed = "IMPOSSIBLE"
            break
    else:
        operations_needed = len(given_string) - len(target_string)

    print(f"Case #{case_number}: {operations_needed}", flush=True)






# PROBLEM B: CHALLENGE NINE

num_test_cases = int(input())
for case_number in range(1, num_test_cases + 1):

    original_number = int(input())
    
    temp_number = original_number
    sum_of_digits = 0
    position = 0
    position_of_last_occurrence = {}  # Stores the last position of each digit
    
    while temp_number:
        temp_number, last_digit = divmod(temp_number, 10)
        sum_of_digits += last_digit
        position += 1
        position_of_last_occurrence[last_digit] = position
    
    digit_to_insert = sum_of_digits % 9
    if digit_to_insert:
        digit_to_insert = 9 - digit_to_insert
        position = max(
            position_of_last_occurrence.get(digit, 0)
            for digit in range(digit_to_insert + 1, 10)
        )
    else:
        position -= 1  
  
    multiplier = 10 ** position
    number_before_position, number_after_position = divmod(original_number, multiplier)
    
    new_number = (
        number_before_position * multiplier * 10 +
        digit_to_insert * multiplier +
        number_after_position
    )
    
    print(f"Case #{case_number}: {new_number}", flush=True)






# PROBLEM C: PALINDROME FREE STRINGS 

    def is_palindrome(s):
    return s == s[::-1]

K = 5
MSK1 = (1 << K) - 1
MSK = (1 << (K + 1)) - 1
bad_masks_5bits = [is_palindrome(bin(i)[2:].zfill(K)) for i in range(1 << K)]
bad_masks_6bits = [is_palindrome(bin(i)[2:].zfill(K + 1)) for i in range(1 << (K + 1))]

def solve(case_num, n, s):
    if n <= 4:
        return "POSSIBLE"

    dp = [False] * (1 << (K + 1))
    dp[0] = True

    for i, char in enumerate(s):
        ndp = [False] * (1 << (K + 1))
        for j in range(MSK + 1):
            if not dp[j]:
                continue
            for bit in (0, 1) if char == '?' else (int(char),):
                next_mask = ((j << 1) | bit) & MSK
                if (i >= 4 and not bad_masks_5bits[next_mask & MSK1]) and \
                   (i >= 5 and not bad_masks_6bits[next_mask]):
                    ndp[next_mask] = True
        dp = ndp

    return "POSSIBLE" if any(dp[:MSK]) else "IMPOSSIBLE"


t = int(input())
for case_number in range(1, t + 1):
    n, s = input().split()
    print(f"Case #{case_number}: {solve(case_number, int(n), s)}")







# PROBLEM D: INTERESTING INTEGERS 

from math import gcd

# Precompute GCD for all possible digit sums and single digits combinations.
gcd_precomputed = [[gcd(i, j) for j in range(120)] for i in range(1200)]

def read_int():
    """Read an integer from input."""
    return int(input())

def calculate_ways_to_digit_sum(num):
    """Calculate the number of ways to get a digit sum equal to the number itself,
    without forming a number with a leading zero and without forming palindromes."""
    if num == 0:
        return 0
    
    num_str = str(num)
    num_length = len(num_str)
    max_digit_sum = 9 * num_length
    total_ways = 0
    
    for target_sum in range(1, max_digit_sum + 1):
        ways_current = [[0, 0] for _ in range(target_sum + 1)]
        ways_current[0][1] = 1

        for idx, digit_char in enumerate(num_str):
            digit_int = int(digit_char)
            ways_next = [[0, 0] for _ in range(target_sum + 1)]
            
            for prev_sum in range(target_sum + 1):
                if prev_sum != 0 and target_sum % prev_sum != 0:
                    continue
                for cur_sum in range(min(target_sum, idx * 9) + 1):
                    for is_nonzero in range(2):
                        for is_same_prefix in range(2):
                            ways_count = ways_current[prev_sum][is_same_prefix]
                            if ways_count == 0:
                                continue
                            for next_digit in range(10):
                                if cur_sum + next_digit > target_sum:
                                    continue
                                next_sum = gcd_precomputed[max(prev_sum, 1) * next_digit][target_sum]
                                ways_next[next_sum][is_nonzero or next_digit][is_same_prefix and next_digit == digit_int] += ways_count
            ways_current = ways_next
        
        for sum_gcd in range(1, target_sum + 1):
            total_ways += ways_current[sum_gcd][1]

    return total_ways

def solve_case(case_idx):
    """Solve a single case of the problem."""
    num_start = read_int()
    num_end = read_int()
    result = calculate_ways_to_digit_sum(num_end) - calculate_ways_to_digit_sum(num_start - 1)
    print(f"Case #{case_idx}: {result}")

total_cases = read_int()
for case_number in range(1, total_cases + 1):
    solve_case(case_number)



    
