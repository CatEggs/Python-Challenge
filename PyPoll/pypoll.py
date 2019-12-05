import csv
import os

path = r"C:\Users\Cathy\Desktop\UT_CourseWork\hw-2\python-challenge"
filename = os.path.join(path, "election_data.csv")
with open(filename, "r") as csv_data:
    reader = csv.DictReader(csv_data, delimiter = ',')
    count = 0
    votes_list = []
    for row in reader:
        if count ==0:
            pass
            count +=1
        votes_list.append(row["Candidate"])
    total = len(list(votes_list))
    print("Election Results\n-----------------")
    print("Total Votes: %d\n------------------" %(total))
    candidate_list = set(votes_list)
    for i in candidate_list:
        votes = votes_list.count(i)
        percent_votes = (votes/total) * 100
        print("%s: %.2f%% (%d)" %(i, percent_votes, votes))