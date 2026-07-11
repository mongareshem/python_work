def sandwiches(*items):
    """A function that returns all items requested in a sandwich"""
    print(items)

sandwiches("reuben")
sandwiches("pastrami", "tuna")
sandwiches("burrito", 'pastrami', 'tuna')
print("-----------------------------------------------------------")

def user_profile(firstname, lastname, **other_info):
    """Displaying the details about the user including
       excesses which are stored in their own dictionary
    """
    user_details = {
        'firstname': firstname,
        'lastname': lastname,
    }
    for k,v in other_info.items():
        user_details[k] = v

    print(user_details)
    print("********** USER DETAILS *********")
    for k,v in user_details.items():
        print(f"{k.title()}: {v.title()}")
    print("\n")

user_profile("shem", "mong'are", field="engineering",
             campus="jkuat", year='5')
user_profile("shem", "mong'are")
print("-----------------------------------------------------------------")


def cars(manufacturer, model_name, **other_details):
    """Storing the information of a car in a dictionary"""
    car_details = {'manufacturer': manufacturer, 'model name': model_name,}

    print("The following are additional details: ")
    for k,v in other_details.items():
        car_details[k] = v
        print(f"\t{k}: {v}")

    print("\n********** CAR DETAILS **************")
    for k,v in car_details.items():
        print(f"{k}: {v}")

cars('subaru', 'outback', color='blue', towpackage=True)
