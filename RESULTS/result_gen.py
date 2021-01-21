locs = {
    "/home/yash/Documents/RUL/RESULTS/ARD Reg": "ARD Reg",
    "/home/yash/Documents/RUL/RESULTS/Decision Tree Reg": "Decision Tree Reg",
    "/home/yash/Documents/RUL/RESULTS/Linear Reg": "Linear Reg",
    "/home/yash/Documents/RUL/RESULTS/Naive Bayes Reg": "Naive Bayes Reg",
    "/home/yash/Documents/RUL/RESULTS/Random Forest Reg": "Random Forest Reg",
    "/home/yash/Documents/RUL/RESULTS/ELM Reg": "ELM Reg",
    "/home/yash/Documents/RUL/RESULTS/ELM Reg (PSO)": "ELM Reg (PSO)"
}

ranges = [
    "1-20", "21-50", "51-70", "71-90"
]

results = {}

from pprint import pprint as pp

for ran in ranges:
    curr_result = [["Battery"], ["B0005"], ["B0006"], ["B0007"], ["B0018"]]

    for loc in locs:
        curr_result[0].append(locs[loc])
        location = f"{loc}/{ran}/result.txt"
        with open(location,'r') as f:
            lines = f.readlines()

            j = 1
            for i in range(0, len(lines), 4):
                battery = lines[i][:-1]
                test_minima = lines[i + 1].split()[2][:-12]
                test_param = lines[i + 1].split()[5]
                train_minima = lines[i + 2].split()[2][:-12]
                train_param = lines[i + 2].split()[5]
                curr_result[j].append(f"{test_minima} ({test_param})")
                j += 1
    results[ran] = curr_result

for ran in ranges:
    for i in range(1, 5):
        row = results[ran][i][1:]
        mn = 1000
        loc = -1
        for j in range(len(row)):
            if (mn > float(row[j].split()[0])):
                mn = float(row[j].split()[0])
                loc = j
        results[ran][i][loc + 1] = f"** {results[ran][i][loc + 1]}"

from prettytable import PrettyTable
for ran in ranges:
    p = PrettyTable()
    p.title = f"Merge Param Range: {ran}"
    p.field_names = results[ran][0]
    for row in results[ran][1:]:
        p.add_row(row)
    print(p)
    print("\n")


results_accuracy = results
for ran in ranges:
    for i in range(1, 5):
        for j in range(len(results[ran][i][1:])):
            if (results[ran][i][j + 1]):
                if (results[ran][i][j + 1][0] == '*'):
                    merge = results[ran][i][j + 1].split(' ')[2]
                    abc = results[ran][i][j + 1].split(' ')[1]
                    acc = (1 - float(abc)) * 100
                    results_accuracy[ran][i][j + 1] = f"** {round(acc, 5)} {merge}"
                else:
                    abc = results[ran][i][j + 1].split(' ')[0]
                    merge = results[ran][i][j + 1].split(' ')[1]
                    acc = (1 - float(abc)) * 100
                    results_accuracy[ran][i][j + 1] = f"{round(acc, 5)} {merge}"

for ran in ranges:
    p = PrettyTable()
    p.title = f"Merge Param Range: {ran}"
    p.field_names = results_accuracy[ran][0]
    for row in results_accuracy[ran][1:]:
        p.add_row(row)
    print(p)
    print("\n")