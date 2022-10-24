# To explain data types

string = "This is a String"             #str
character = 'x'                         #str
integer = 2                             #int
decimal = 11.2                          #float
x = True                                #bool
y = False                               #bool
list1 = [1, 2, 'l', "list"]             #list[]
tuple1 = (1, 2, 't', "tuple")           #tuple()
set1 = {1, 2, 's', "set"}               #set{}
dict1 = {"sub1" : 11, "sub2" : 22}      #dictionary

# Creating a List
List = []
print("Blank List: ")
print(List)

# Creating a List of numbers
List = [10, 20, 14]
print("\nList of numbers: ")
print(List)

# Creating a List of strings and accessing
# using index
List = ["Geeks", "For", "Geeks"]
print("\nList Items: ")
print(List[0])
print(List[2])

# Creating an empty Tuple
Tuple1 = ()
print("Initial empty Tuple: ")
print(Tuple1)

# Creating a Tuple
# with the use of string
Tuple1 = ("Geeks", "For")
print("\nTuple with the use of String: ")
print(Tuple1)

# Creating a Tuple with
# the use of list
list1 = [1, 2, 4, 5, 6]
print("\nTuple using List: ")
print(tuple(list1))

# Creating a Tuple
# with the use of built-in function
Tuple1 = tuple("Geeks")
print("\nTuple with the use of function: ")
print(Tuple1)

# Creating a Set
set1 = set()
print("Initial blank Set: ")
print(set1)

# Creating a Set with
# the use of a String
set1 = set("GeeksForGeeks")
print("\nSet with the use of String: ")
print(set1)

# Creating a Set with
# the use of Constructor
# (Using object to Store String)
String = "GeeksForGeeks"
set1 = set(String)
print("\nSet with the use of an Object: ")
print(set1)

# Creating a Set with
# the use of a List
set1 = set(["Geeks", "For", "Geeks"])
print("\nSet with the use of List: ")
print(set1)

# Creating a Dictionary
# with Integer Keys
Dict = {1: "Geeks", 2: "For", 3: "Geeks"}
print("\nDictionary with the use of Integer Keys: ")
print(Dict)

# Creating a Dictionary
# with Mixed keys
Dict = {"Name": "Geeks", 1: [1, 2, 3, 4]}
print("\nDictionary with the use of Mixed Keys: ")
print(Dict)