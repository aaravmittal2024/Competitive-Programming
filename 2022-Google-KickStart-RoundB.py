# PROBLEM A: INFINITY AREA 

from math import pi
test_cases = int(input())

for case_number in range(1, test_cases + 1):
    initial_radius, multiplier_a, divider_b = map(int, input().split())

    total_area = initial_radius * initial_radius
    current_radius = initial_radius

    while current_radius:
        current_radius *= multiplier_a
        total_area += current_radius * current_radius
        current_radius //= divider_b
        total_area += current_radius * current_radius
    
    total_area *= pi
    print(f"Case #{case_number}: {total_area}", flush=True)





# PROBLEM B: PALINDROMIC FACTORS

import math

def check_palindrome(s):
    return int(s == s[::-1])

def main():
    ans = 0
    A = int(input().strip())

    goal = int(math.sqrt(A))

    for i in range(1, goal + 1):
        if A % i == 0:
            B = A // i
            ans += check_palindrome(str(i))
            if i != B:
                ans += check_palindrome(str(B))

    print(ans)

if __name__ == "__main__":
    main()





# PROBLEM C: UNLOCK THE PADDLE 

def unlock_the_padlock():
    def get_rotation_cost(from_digit, to_digit):
        difference = abs(from_digit - to_digit)
        return min(difference, D - difference)

    def find_minimum_cost(N, D, digits):
        cost_table = [[0] * N for _ in range(N)]

        for length in range(2, N + 1):  # The chain length from 2 to N
            for start in range(N - length + 1):
                end = start + length - 1
                cost_table[start][end] = float('inf')
                for x in [digits[start], digits[end]]:
                    cost_start = get_rotation_cost(digits[start], x) + cost_table[start + 1][end]
                    cost_end = get_rotation_cost(digits[end], x) + cost_table[start][end - 1]
                    current_cost = min(cost_start, cost_end)
                    if current_cost < cost_table[start][end]:
                        cost_table[start][end] = current_cost
        return cost_table[0][N - 1]

    num_digits, digit_limit = map(int, input().split())
    padlock_digits = list(map(int, input().split()))
    return find_minimum_cost(num_digits, digit_limit, padlock_digits)

num_cases = int(input())
for case_number in range(1, num_cases + 1):
    min_cost = unlock_the_padlock()
    print(f'Case #{case_number}: {min_cost}')





# PROBLEM D: HAMILTONIAN TOUR 

def determine_direction(node_from, node_to, column_count):
    row_from, col_from = divmod(node_from, column_count)
    row_to, col_to = divmod(node_to, column_count)
    if row_to - row_from == 1: return 'S'
    if col_to - col_from == 1: return 'E'
    if row_to - row_from == -1: return 'N'
    if col_to - col_from == -1: return 'W'

def setup_initial_node(grid_columns, node, next_nodes):
    row, col = node
    row, col = 2 * row, 2 * col
    if next_nodes[row * grid_columns + col] != -1:
        return False
    for delta_row, delta_col in MOVES:
        next_nodes[row * grid_columns + col] = (row + delta_row) * grid_columns + (col + delta_col)
        row, col = row + delta_row, col + delta_col
    return True

def link_nodes(grid_columns, node, parent_node, next_nodes):
    if node < parent_node:
        node, parent_node = parent_node, node
    row, col = node
    parent_row, parent_col = parent_node
    if row - parent_row:
        next_nodes[(2 * row) * grid_columns + (2 * col)] = (2 * parent_row + 1) * grid_columns + (2 * col)
        next_nodes[(2 * parent_row + 1) * grid_columns + (2 * parent_col + 1)] = (2 * row) * grid_columns + (2 * col + 1)
    else:
        next_nodes[(2 * row + 1) * grid_columns + (2 * col)] = (2 * parent_row + 1) * grid_columns + (2 * parent_col + 1)
        next_nodes[(2 * parent_row) * grid_columns + (2 * parent_col + 1)] = (2 * row) * grid_columns + (2 * col)

def perform_dfs(grid_rows, grid_columns, board):
    next_nodes = [-1] * ((2 * grid_rows) * (2 * grid_columns))
    setup_initial_node(grid_columns, (0, 0), next_nodes)
    stack = [(1, ((0, 0), None))]
    while stack:
        step, args = stack.pop()
        if step == 1:
            current_node, parent_node = args
            if parent_node:
                link_nodes(grid_columns, current_node, parent_node, next_nodes)
            stack.append((2, (current_node, 0)))
        elif step == 2:
            current_node, move_index = args
            next_row, next_col = current_node[0] + MOVES[move_index][0], current_node[1] + MOVES[move_index][1]
            if move_index + 1 < len(MOVES):
                stack.append((2, (current_node, move_index + 1)))
            if not (0 <= next_row < grid_rows and 0 <= next_col < grid_columns and board[next_row][next_col] == '*' and setup_initial_node(grid_columns, (next_row, next_col), next_nodes)):
                continue
            stack.append((1, ((next_row, next_col), current_node)))
    return next_nodes

def hamiltonian_tour():
    grid_rows, grid_columns = map(int, input().strip().split())
    board = [input().strip() for _ in range(grid_rows)]
    next_nodes = perform_dfs(grid_rows, grid_columns, board)
    if next_nodes.count(-1) != 4 * sum(row.count('#') for row in board):
        return "IMPOSSIBLE"
    tour = []
    current = 0
    while not (tour and current == 0):
        tour.append(determine_direction(current, next_nodes[current], 2 * grid_columns))
        current = next_nodes[current]
    return "".join(tour)

MOVES = [(0, 1), (1, 0), (0, -1), (-1, 0)]
num_cases = int(input().strip())
for case_number in range(1, num_cases + 1):
    print(f'Case #{case_number}: {hamiltonian_tour()}')

