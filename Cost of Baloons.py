def calculate_min_cost(green_cost, purple_cost, participants):
    total_cost1 = 0
    total_cost2 = 0
    
    for participant in participants:
        first_problem_solved, second_problem_solved = participant
        
        # Calculate cost for first configuration: green for problem 1, purple for problem 2
        total_cost1 += first_problem_solved * green_cost + second_problem_solved * purple_cost
        
        # Calculate cost for second configuration: purple for problem 1, green for problem 2
        total_cost2 += first_problem_solved * purple_cost + second_problem_solved * green_cost
    
    # Return the minimum cost between the two configurations
    return min(total_cost1, total_cost2)

# Read number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    # Read green and purple balloon costs
    green_cost, purple_cost = map(int, input().split())
    
    # Read number of participants
    n = int(input())
    
    participants = []
    
    # Read each participant's status
    for _ in range(n):
        status = list(map(int, input().split()))
        participants.append(status)
    
    # Calculate and print the minimum cost for the current test case
    min_cost = calculate_min_cost(green_cost, purple_cost, participants)
    print(min_cost)
