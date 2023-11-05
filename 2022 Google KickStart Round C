# PROBLEM A: NEW PASSWORD

from string import ascii_lowercase, ascii_uppercase

def generate_new_password():
    password_length = int(input())
    current_password = list(input())
    updated_password = current_password[:]
    
    for character_set in (uppercase_letters, lowercase_letters, digits, special_characters):
        if not any(character in character_set for character in current_password):
            updated_password.append(next(iter(character_set)))
    
    updated_password.extend(uppercase_letters[0] * (minimum_length - len(updated_password)))
    return "".join(updated_password)

minimum_length = 7
uppercase_letters = set(ascii_uppercase)
lowercase_letters = set(ascii_lowercase)
digits = set(str(i) for i in range(10))
special_characters = set("#@*&")

number_of_cases = int(input())
for case_number in range(1, number_of_cases + 1):
    print(f'Case #{case_number}: {generate_new_password()}')





# PROBLEM B: RANGE PARTITION 

def find_range_partition():
    num_elements, sum_group_x, sum_group_y = map(int, input().split())
    total_sum = sum(range(1, num_elements + 1))
    quotient, remainder = divmod(total_sum, sum_group_x + sum_group_y)
    
    if remainder:
        return "IMPOSSIBLE"
    
    target_sum_x = quotient * sum_group_x
    selected_elements = []
    for element in reversed(range(1, num_elements + 1)):
        if element <= target_sum_x:
            target_sum_x -= element
            selected_elements.append(element)
    
    if target_sum_x == 0:
        return f"POSSIBLE\n{len(selected_elements)}\n{' '.join(map(str, selected_elements))}"
    else:
        return "IMPOSSIBLE"

number_of_cases = int(input())
for case_number in range(1, number_of_cases + 1):
    print(f'Case #{case_number}: {find_range_partition()}')





# PROBLEM C: ANTS ON A STICK 

from collections import deque

def compute_ants_fall_order():
    num_ants, stick_length = map(int, input().split())
    positions, directions = [], []

    for _ in range(num_ants):
        position, direction = map(int, input().split())
        positions.append(position)
        directions.append(direction)

    ant_indices = deque(sorted(range(num_ants), key=lambda index: positions[index]))

    fall_events = []
    for index in range(num_ants):
        time_to_fall = positions[index] if directions[index] == 0 else stick_length - positions[index]
        fall_events.append((time_to_fall, ant_indices.popleft() if directions[index] == 0 else ant_indices.pop(), directions[index]))

    fall_events.sort()
    fall_order = [str(event[1] + 1) for event in fall_events]

    return " ".join(fall_order)

number_of_cases = int(input())
for case_number in range(1, number_of_cases + 1):
    print(f'Case #{case_number}: {compute_ants_fall_order()}')





# PROBLEM D: PALINDROMIC DELETIONS 

def inverse_combinations(n, k, mod):
    while len(inverse_cache) <= n:
        factorial_cache.append(factorial_cache[-1] * len(inverse_cache) % mod)
        inverse_cache.append(inverse_cache[mod % len(inverse_cache)] * (mod - mod // len(inverse_cache)) % mod)
        inverse_factorial_cache.append(inverse_factorial_cache[-1] * inverse_cache[-1] % mod)
    return (inverse_factorial_cache[n] * factorial_cache[n - k] % mod) * factorial_cache[k] % mod

def count_palindromic_deletions():
    string_length = int(input())
    string = input()
    total_palindromic_sequences = 1
    dynamic_programming_cache = [[[0] * string_length for _ in range(string_length)] for _ in range(look_back_limit)]
    for current_length in range(1, string_length):
        for start in reversed(range(string_length)):
            dynamic_programming_cache[current_length % look_back_limit][start][start] = 1 if current_length == 1 else 0
            for end in range(start + 1, string_length):
                start_to_end = dynamic_programming_cache[current_length % look_back_limit][start][end - 1]
                start_after_to_end = dynamic_programming_cache[current_length % look_back_limit][start + 1][end]
                start_after_to_end_before = dynamic_programming_cache[current_length % look_back_limit][start + 1][end - 1]
                dynamic_programming_cache[current_length % look_back_limit][start][end] = (start_to_end + start_after_to_end - start_after_to_end_before) % mod_value
                if string[start] == string[end]:
                    dynamic_programming_cache[current_length % look_back_limit][start][end] = (
                        dynamic_programming_cache[current_length % look_back_limit][start][end] + 
                        (1 if current_length == 2 else dynamic_programming_cache[(current_length - 2) % look_back_limit][start + 1][end - 1])
                    ) % mod_value
        total_palindromic_sequences = (total_palindromic_sequences + dynamic_programming_cache[current_length % look_back_limit][0][string_length - 1] * inverse_combinations(string_length, current_length, mod_value)) % mod_value
    return total_palindromic_sequences

look_back_limit = 3
mod_value = 10**9 + 7
factorial_cache = [1, 1]
inverse_cache = [1, 1]
inverse_factorial_cache = [1, 1]
for case_number in range(int(input())):
    print(f'Case #{case_number + 1}: {count_palindromic_deletions()}')
