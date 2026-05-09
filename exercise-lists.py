# Elias Mandeville
# Thursday, 10.9.25
# List practice


# --------------------------------------------
# MAIN FUNCTION
# --------------------------------------------
def main():

    # A variable storing a single string
    fun = "I love Python"

    # A list containing strings
    animals = ["dog", "bird", "cat"]

    # A list containing integers
    nums = [7, 2, 99]

    # Print the variables and lists
    print(fun)
    print(animals)
    print(nums)
    print()

    # --------------------------------------------
    # INDEXING
    # --------------------------------------------
    print(animals[0])   # dog
    print(animals[1])   # bird
    print(animals[2])   # cat
    print(nums[1])      # 2
    print()

    # Negative indexing (from the right)
    print(animals[-1])  # cat
    print(animals[-2])  # bird
    print()

    # --------------------------------------------
    # SLICING
    # --------------------------------------------
    print(animals[0:2])  # dog, bird
    print()
    print(animals[1:])   # bird, cat
    print()
    print(animals[:2])   # dog, bird
    print()
    print(animals[:])    # whole list
    print()

    # --------------------------------------------
    # LIST METHODS
    # --------------------------------------------
    print(animals)
    animals.append("fish")   # Add to end
    print(animals)
    print()

    animals.insert(0, "lizard")  # Insert at index 0
    print(animals)
    print()

    animals[0] = "rabbit"  # Replace item at index 0
    print(animals)
    print()

    print(animals.pop())   # Remove last item
    print(animals)
    print()

    print(animals.pop(0))  # Remove item at index 0
    print(animals)
    print()

    animals.remove("cat")  # Remove by value
    print(animals)
    print()

    del animals[1]         # Delete by index
    print(animals)
    print()

    # Add items back
    animals.append("bird")
    animals.append("cat")
    print(animals)

    animals.sort()         # Sort A–Z
    print(animals)
    print()

    animals.reverse()      # Reverse list
    print(animals)
    print()

    # --------------------------------------------
    # METHODS ON NUMBERS LIST
    # --------------------------------------------
    print(nums)
    nums.sort()
    print(nums)
    nums.reverse()
    print(nums)
    print()

    # --------------------------------------------
    # BUILT-IN FUNCTIONS
    # --------------------------------------------
    print(sorted(animals))  # Temporary sort
    print(animals)
    print()

    print(sorted(fun))      # Sorted characters of string
    print()

    print(len(animals))     # Number of items
    print(len(nums))
    print(len(fun))         # Number of characters
    print()

    print(sum(nums))        # Sum of numbers
    print(sum(nums) / len(nums))  # Average
    print()

    # --------------------------------------------
    # LOOPS
    # --------------------------------------------
    for i in animals:
        print(f"I love {i}s!")
    print()

    for n in nums:
        print(f"{n}\t{n**3}")   # Correct f-string
    print()

    for num in nums:
        if num % 2 == 0:
            print("Even")
        else:
            print("Odd")
# Call main
main()    


# --------------------------------------------
# FUNCTION 1 — INCORRECT VERSION (FIXED)
# --------------------------------------------
def getscores():
    # Declare and initialize an empty list
    scores = []

    print("Welcome to my number scoring program")

    # FIX: append instead of assigning to scores[i]
    for i in range(5):
        scores.append(int(input("Please enter a score: ")))

    print(scores)


# --------------------------------------------
# FUNCTION 2 — PRE-SIZED LIST
# --------------------------------------------
def getscores2():
    scores = [0] * 5  # Pre-filled list of 5 zeros

    print("Welcome to my number scoring program")

    for i in range(5):
        scores[i] = int(input("Please enter a score: "))

    print(scores)


# --------------------------------------------
# FUNCTION 3 — USER-DEFINED LIST SIZE
# --------------------------------------------
def getScores3():
    scores = []       # Empty list
    numScores = 0     # Number of scores to enter

    print("Welcome to my number scoring program")

    numScores = int(input("How many scores will you enter: "))

    for i in range(numScores):
        scores.append(int(input("Please enter a score: ")))

    print(scores)


# Call main
#main()

    


