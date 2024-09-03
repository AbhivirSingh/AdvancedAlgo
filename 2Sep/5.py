def job_sequencing(jobs, deadlines):
    jobs_sorted = sorted(jobs, key=lambda x: x[1], reverse=True)

    n = max(deadlines)
    slots = [-1] * n 

    max_profit = 0

    for i in range(len(jobs_sorted)):
        for j in range(min(n, deadlines[i]) - 1, -1, -1):
            if slots[j] == -1:
                slots[j] = i
                max_profit += jobs_sorted[i][1]
                break

    selected_jobs = [jobs_sorted[i][0] for i in slots if i != -1]
    return selected_jobs, max_profit

jobs = [("Job1", 100), ("Job2", 50), ("Job3", 200)]
deadlines = [2, 1, 2]

selected_jobs, max_profit = job_sequencing(jobs, deadlines)
print(f"Selected jobs: {selected_jobs}, Maximum profit: {max_profit}")
