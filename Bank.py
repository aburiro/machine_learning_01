def check_state(num_processes, num_resources, available, allocated, request):
    work = available[:]
    finish = [False] * num_processes
    safe_sequence = []
    need = []
    for i in range(num_processes):
        need.append([request[i][j] - allocated[i][j] for j in range(num_resources)])
    while True:
        found = False
        for i in range(num_processes):
            if not finish[i] and all(need[i][j] <= work[j] for j in range(num_resources)):
                
                work = [work[j] + allocated[i][j] for j in range(num_resources)]
                finish[i] = True
                safe_sequence.append(i)
                found = True
        if not found:
            if all(finish):
                
                return "Safe", safe_sequence
            else:
                return "Unsafe", []
num_processes = 2
num_resources = 3
available = [0, 0, 1]
allocated = [
    [8, 1, 0],
    [9, 0, 0],
    [9, 0, 2],
    [9, 1, 1],
    [9, 7, 2]
]
request = [
    [9, 0, 0],
    [9, 0, 2],
    [9, 0, 0],
    [9, 0, 0],
    [9, 0, 2]
]
state, sequence = check_state(num_processes, num_resources, available, allocated, request)
print("System state:", state)
if state == "Safe":
    print("Safe sequence:", sequence)
