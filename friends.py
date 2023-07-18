def can_distribute_chocolates(A, B):
    if (A + B) % 2 == 0 and abs(A - B) % 2 == 0:
        return "YES"
    else:
        return "NO"

# Read the number of test cases
T = int(input())

for _ in range(T):
    # Read A and B for each test case
    A, B = map(int, input().split())
    
    # Check if chocolates can be distributed equally
    result = can_distribute_chocolates(A, B)
    
    # Print the result
    print(result)
