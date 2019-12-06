import os
import pypoll as p

path = r"C:\Users\Cathy\Desktop\UT_CourseWork\hw-2\python-challenge"
filename = os.path.join(path, "election_data.csv")
p.election(filename)