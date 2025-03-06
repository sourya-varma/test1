import sys

def fullName(firstName, lastName):
    return f"My Full Name is {firstName} {lastName}"

if __name__ == "__main__":
    v = fullName(sys.argv[1], sys.argv[2])
    #b = fullName("ssd", "dfedf")
    print(v)

