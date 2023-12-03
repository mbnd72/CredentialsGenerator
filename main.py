#Author Mounika Bandhamravuri 
import random
noOfUsers = int(input("Please Enter No of users: "))
mailingDomain = input("Enter Mailing Domain: ")
lengthOfPassword = int(input("Enter legth of passwords: "))
#Email Generation Logic
userList = []
for i in range(noOfUsers):
    userList.append(input("Enter User Name: "))
for j in range(len(userList)):
    userList[j] = userList[j]+"@"+mailingDomain
# Password Generation Logic
strPass = ''
string = 'abcdefghijklmnopqrstuvwxyz!@#%$&'
passwordList = []
strPassList = []
for i in string:
    passwordList.append(i)
for j in range(noOfUsers):
    generatedPassword = random.sample(passwordList,lengthOfPassword)
    strPassList.append(strPass.join(generatedPassword))
#Id Generation Logic
studentID = []
count = 11
for i in range(len(userList)):
    studentID.append(userList[i][slice(3)]+str(count))
    count += 1
for k in range(noOfUsers):
    print("\n")
    print("***********Generated Details*************")
    print("User ID: " + studentID[k] )
    print("Generated Email: " + userList[k])
    print("User Password: "+ strPassList[k])