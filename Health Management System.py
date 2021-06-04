# Health Management System
# Total 6 Files, 3 For exercise and 3 For for diet
# 3 clients - Saurav, Gaurav and XYZ
# write a function that when executed takes as input client name
# one more function to retrieve exercise or food for any client

print("Health Management System\n")
a = int(input("Enter 1 for log the value and 0 for Retrieve: "))


def getdate():
    import datetime
    return datetime.datetime.now()


if a == 1:
    b = int(input("\nEnter 1 for Saurav, 2 for Gaurav and 3 for XYZ: "))
    if b == 1:
        c = int(input("\nEnter 1 for food, 2 for Exercise: "))
        d = input("Enter here:\n")
        if c == 1:
            with open("Saurav_Food.txt", "a") as f:
                f.write(str([str(getdate())]) + ":" + d + "\n")
                print("Successfully Written")
        elif c == 2:
            with open("Saurav_Exercise.txt", "a") as f:
                f.write(str(getdate()) + ":" + d + "\n")
                print("Successfully Written")
        else:
            print("Enter the valid input")
    elif b == 2:
        c = int(input("\nEnter 1 for food, 2 for Exercise: "))
        d = input("\nEnter here:\n")
        if c == 1:
            with open("Gaurav_Food.txt", "a")as f:
                f.write(str(getdate()) + ":" + d + "\n")
                print("Successfully Written")
        elif c == 2:
            with open("Gaurav_Exercise.txt", "a") as f:
                f.write(str(getdate()) + ":" + d + "\n")
                print("Successfully Written")
        else:
            print("Enter the valid input")
    elif b == 3:
        c = int(input("\nEnter 1 for food, 2 for Exercise: "))
        d = input("Enter here:\n")
        if c == 1:
            with open("XYZ_Food.txt", "a")as f:
                f.write(str(getdate()) + ":" + d + "\n")
                print("Successfully Written")
        elif c == 2:
            with open("XYZ_Exercise.txt", "a") as f:
                f.write(str(getdate()) + ":" + d + "\n")
                print("Successfully Written")
    else:
        print("Enter the valid input")

elif a == 0:
    b = int(input("\nEnter 1 for Saurav, 2 for Gaurav, 3 for XYZ: "))
    if b == 1:
        c = int(input("\nEnter 1 for food, 2 for Exercise: "))
        if c == 1:
            with open("Saurav_Food.txt") as f:
                for i in f:
                    print(i)
        elif c == 2:
            with open("Saurav_Exercise") as f:
                for i in f:
                    print(i)
        else:
            print("Enter the valid input: ")
    elif b == 2:
        c = int(input("\nEnter 1 for food, 2 for Exercise: "))
        if c == 1:
            with open("Gaurav_Food.txt") as f:
                for i in f:
                    print(i)
        elif c == 2:
            with open("Gaurav_Exercise.txt") as f:
                for i in f:
                    print(i)
        else:
            print("Enter the valid input")
    elif b == 3:
        c = int(input("Enter 1 for food, 2 for Exercise: "))
        if c == 1:
            with open("XYZ_Food.txt") as f:
                for i in f:
                    print(i)
        elif c == 2:
            with open("XYZ_Exercise") as f:
                for i in f:
                    print(i)
        else:
            print("Enter the valid input")
