# Write a function in python named calculate-attendance. This function gets a single list containing name and total no of presence of students. Total number of classes held are 40. The job of this function is to print students having attendance less than 50 percent. 

# data format: [["name", marks]...]
def calculateAttendance(data):
  std, perc = [], []
  for d in data:
    std.append(d[0])
    perc.append(d[1] * (100/40))
  for i in range(len(data)):
    if (perc[i] < 50):
      print(std[i])