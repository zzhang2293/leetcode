def getMaxSubarrayLen(team_a, team_b):
    # Write your code here
    res = [[0, 0] for _ in range(len(team_a) + 1)]
    team_a.append(float("inf"))
    team_b.append(float("inf"))
    res_val = 0
    for i in range(len(team_a) - 2, -1, -1):
        team_a_val = team_a[i]
        team_b_val = team_b[i]
        if team_a[i + 1] >= team_a_val:
            res[i][0] = max(res[i][0], res[i + 1][0] + 1)
        if team_b[i + 1] >= team_a_val:
            res[i][0] = max(res[i][0], res[i + 1][1] + 1)
        if team_a[i + 1] < team_a_val and team_b[i + 1] < team_a_val:
            res[i][0] = 1
        if team_a[i + 1] >= team_b_val:
            res[i][1] = max(res[i][1], res[i + 1][0] + 1)
        if team_b[i + 1] >= team_b_val:
            res[i][1] = max(res[i][1], res[i + 1][1] + 1)
        if team_a[i + 1] < team_b_val and team_b[i + 1] < team_b_val:
            res[i][1] = 1
        res_val = max(res_val, res[i][0], res[i][1])
    return res_val

print(getMaxSubarrayLen([2, 7, 3], [4, 2, 6]))
         

            
    