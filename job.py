def job_scheduling():
    n = 4
    profit = [4,5,6,7]
    deadlines = [2,3,4,3]
    maxDeadLines = 12
    jobs = [0] * maxDeadLines
    for i in range(n):
        for j in range(n - 1):
            if profit[j] < profit[j + 1]:
                profit[j], profit[j + 1] = profit[j + 1], profit[j]
                deadlines[j], deadlines[j + 1] = deadlines[j + 1], deadlines[j]
    for i in range(n):
        if jobs[deadlines[i] - 1] == 0:
            jobs[deadlines[i] - 1] = profit[i]
        else:
            for j in range(deadlines[i] - 1, -1, -1):
                if jobs[j] == 0:
                    jobs[j] = profit[i]
                    break
    max_profit = sum(jobs)
    print("The maximum profit:", max_profit)
job_scheduling()
