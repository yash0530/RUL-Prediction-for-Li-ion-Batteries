import numpy as np

locs = {
    "/home/yash/Documents/RUL/RESULTS_25_ITR(STD, AVG)/ARD Reg": "ARD Reg",
    "/home/yash/Documents/RUL/RESULTS_25_ITR(STD, AVG)/Decision Tree Reg": "Decision Tree Reg",
    "/home/yash/Documents/RUL/RESULTS_25_ITR(STD, AVG)/Linear Reg": "Linear Reg",
    "/home/yash/Documents/RUL/RESULTS_25_ITR(STD, AVG)/Naive Bayes Reg": "Naive Bayes Reg",
    "/home/yash/Documents/RUL/RESULTS_25_ITR(STD, AVG)/Random Forest Reg": "Random Forest Reg",
    "/home/yash/Documents/RUL/RESULTS_25_ITR(STD, AVG)/ELM Reg": "ELM Reg"
}

ranges = [
    "1-20", "21-50", "51-70", "71-90"
]

results = {}
results_stddev = {}

from pprint import pprint as pp

# extracting results from the files
for ran in ranges:
    curr_result_stddev = [["Battery"], ["B0005"], ["B0006"], ["B0007"], ["B0018"]] 
    curr_result = [["Battery"], ["B0005"], ["B0006"], ["B0007"], ["B0018"]]

    for loc in locs:
        
        curr_result_stddev[0].append(locs[loc])
        curr_result[0].append(locs[loc])

        location = f"{loc}/{ran}/result.txt"

        with open(location,'r') as f:
            lines = f.readlines()

            j = 1
            for i in range(402, 416, 4):
                battery = lines[i].split()[1]
                std_dev = lines[i].split()[3][:11]
                avg_rmse = lines[i + 1].split()[3][:11]
                mode_cycle_param = lines[i + 2].split()[3]

                curr_result[j].append(f"{avg_rmse} ({mode_cycle_param})")
                curr_result_stddev[j].append(f"{std_dev}")

                j += 1

    results[ran] = curr_result
    results_stddev[ran] = curr_result_stddev

# geting row wise min rmse
print("----------------------- RMSE -------------------\n\n")
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

with open(f"rmses.csv", "w") as f:
    f.write("\\renewcommand{\\arraystretch}{2}%\n")
    f.write("\\begin{center}\n")
    f.write("\\begin{table*}\n")
    f.write("\\begin{tabular}{ | l | l | l | l | l | l | l | }\n") 
    for ran in ranges:
        # f.write("\\renewcommand{\\arraystretch}{2}%\n")
        # f.write("\\begin{center}\n")
        # f.write("\\begin{table*}\n")
        # f.write("\\begin{tabular}{ | l | l | l | l | l | l | l | }\n") 
        f.write("\\hline\n")
        f.write("\multicolumn{7}{|c|}{\\textbf{RMSE, Merge Param Range:"+ f"{ran}" + "}} \\\\\n")
        f.write("\\hline\n")
        for x in results[ran]:
            for y in range(len(x)):
                val = x[y]
                if val[0] == '*' or (val[0] >= 'A' and val[0] <= 'Z'):
                    if val[0] == '*':
                        val = val[3:]
                    val = "\\textbf{" + val + "}"
                if y == 6:
                    f.write(f"{val} ")
                else:
                    f.write(f"{val} & ")
            f.write("\\\\\n")
            f.write("\\hline\n")
        # f.write("\\end{tabular}\n")
        # f.write("\\end{table*}\n")
        # f.write("\\end{center}\n")
        # f.write("\n")
    f.write("\\end{tabular}\n")
    f.write("\\end{table*}\n")
    f.write("\\end{center}\n")
    f.write("\n")

# # printing rmses
# from prettytable import PrettyTable
# for ran in ranges:
#     p = PrettyTable()
#     p.title = f"Merge Param Range: {ran}"
#     p.field_names = results[ran][0]
#     for row in results[ran][1:]:
#         p.add_row(row)
#     print(p)
#     print("\n")

# creating accuracy results from rmses
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


with open(f"accuracies.csv", "w") as f:
    f.write("\\renewcommand{\\arraystretch}{2}%\n")
    f.write("\\begin{center}\n")
    f.write("\\begin{table*}\n")
    f.write("\\begin{tabular}{ | l | l | l | l | l | l | l | }\n") 
    for ran in ranges:
        # f.write("\\renewcommand{\\arraystretch}{2}%\n")
        # f.write("\\begin{center}\n")
        # f.write("\\begin{table*}\n")
        # f.write("\\begin{tabular}{ | l | l | l | l | l | l | l | }\n") 
        f.write("\\hline\n")
        f.write("\multicolumn{7}{|c|}{\\textbf{ACCURACY, Merge Param Range:"+ f"{ran}" + "}} \\\\\n")
        f.write("\\hline\n")
        for x in results_accuracy[ran]:
            for y in range(len(x)):
                val = x[y]
                if val[0] == '*' or (val[0] >= 'A' and val[0] <= 'Z'):
                    if val[0] == '*':
                        val = val[3:]
                    val = "\\textbf{" + val + "}"
                if y == 6:
                    f.write(f"{val} ")
                else:
                    f.write(f"{val} & ")
            f.write("\\\\\n")
            f.write("\\hline\n")
        # f.write("\\end{tabular}\n")
        # f.write("\\end{table*}\n")
        # f.write("\\end{center}\n")
        # f.write("\n")
    f.write("\\end{tabular}\n")
    f.write("\\end{table*}\n")
    f.write("\\end{center}\n")
    f.write("\n")

# # printing accuracy table
# print("----------------------- ACC -------------------\n\n")
# for ran in ranges:
#     p = PrettyTable()
#     p.title = f"Merge Param Range: {ran}"
#     p.field_names = results_accuracy[ran][0]
#     for row in results_accuracy[ran][1:]:
#         p.add_row(row)
#     print(p)
#     print("\n")

# # printing stddev table
# print("----------------------- STDDEV -------------------\n\n")
# for ran in ranges:
#     p = PrettyTable()
#     p.title = f"Merge Param Range: {ran}"
#     p.field_names = results_stddev[ran][0]
#     for row in results_stddev[ran][1:]:
#         p.add_row(row)
#     print(p)
#     print("\n")


with open(f"stddevies.csv", "w") as f:
    f.write("\\renewcommand{\\arraystretch}{2}%\n")
    f.write("\\begin{center}\n")
    f.write("\\begin{table*}\n")
    f.write("\\begin{tabular}{ | l | l | l | l | l | l | l | }\n") 
    for ran in ranges:
        # f.write("\\renewcommand{\\arraystretch}{2}%\n")
        # f.write("\\begin{center}\n")
        # f.write("\\begin{table*}\n")
        # f.write("\\begin{tabular}{ | l | l | l | l | l | l | l | }\n") 
        f.write("\\hline\n")
        f.write("\multicolumn{7}{|c|}{\\textbf{STD DEV, Merge Param Range:"+ f"{ran}" + "}} \\\\\n")
        f.write("\\hline\n")
        for x in results_stddev[ran]:
            for y in range(len(x)):
                val = x[y]
                if val[0] == '*' or (val[0] >= 'A' and val[0] <= 'Z'):
                    if val[0] == '*':
                        val = val[3:]
                    val = "\\textbf{" + val + "}"
                if y == 6:
                    f.write(f"{val} ")
                else:
                    f.write(f"{val} & ")
            f.write("\\\\\n")
            f.write("\\hline\n")
        # f.write("\\end{tabular}\n")
        # f.write("\\end{table*}\n")
        # f.write("\\end{center}\n")
        # f.write("\n")
    f.write("\\end{tabular}\n")
    f.write("\\end{table*}\n")
    f.write("\\end{center}\n")
    f.write("\n")