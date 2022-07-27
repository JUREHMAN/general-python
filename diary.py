print("Welcome to the Daily Diary system:")
#file1 = open('file.txt','r')
#file1= open("file.txt","w+")
n = int(input("Please Enter\n0 for editing your diary\n1 for viewing your entries:\n"))
if n == 0:
    file1= open("file.txt","w+")
    str1 = str(input("Please Enter the Things which you want to write in your diary:\n"))
    file1.write(str1)
    file1.close()
elif n == 1:
    with open('file.txt') as f:
     lines = f.readlines()
    #file2 = open("file.txt",'r')
     print(lines)
else:
    print("Something went wrong")