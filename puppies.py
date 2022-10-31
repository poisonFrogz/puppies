#puppies measured in pounds at 3 months
puppydict = {
    "labrador" : 10,
    "german shepard" : 15,
    "springer spaniel" : 22,
    "tibetan terrier" : 12

}

while True:
    print("<---Welcome To how much does this weigh in puppies--->")
    item = input("Please enter the name of an object: ")
    weight = int(input("Please enter this objects weight in pounds: "))
    puppy = input("Please enter the puppy you would like to know how many of them your object weighs: ")

    if puppy == "labrador":
        number = puppydict.get("labrador")
        answer = weight / number
        print("One " + item + " weighs " + str(answer) + " labradors!!")

    elif puppy == "german shepard":
        number = puppydict.get("german shepard")
        answer = weight / number
        print("One " + item + " weighs " + str(answer) + " german shepards!!")

    elif puppy == "springer spaniel":
        number = puppydict.get("springer spaniel")
        answer = weight / number
        print("One " + item + " weighs " + str(answer) + " springer spaniels!!")

    elif puppy == "tibetan terrier":
        number = puppydict.get("tibetan terrier")
        answer = weight / number
        print("One " + item + " weighs " + str(answer) + " tibetan terriers!!")

    else:
        print("I'm sorry, we don't posess that puppy knowledge!")




