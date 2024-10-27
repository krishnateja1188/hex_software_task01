import sys
import argparse
import default_values

#Takes in command line arguments. If values are not specified, default values
# from default_values are used. Returns a namespace object
def get_arguments():
    #Pull arguments from the command line
    parser = argparse.ArgumentParser(description="Basic import/export tool")
    parser.add_argument("-b", "--big_ratio",
                        dest = "big_ratio",
                        required = False,
                        action = "store",
                        type = float,
                        default = default_values.BIG_ROOM_FRAC,
                        help = "Percentage of the bigger room to the total bedroom space")
    parser.add_argument("-s", "--small_ratio",
                        dest = "small_ratio",
                        required = False,
                        action = "store",
                        type = float,
                        default = default_values.SMALL_ROOM_FRAC,
                        help = "Percentage of the smaller room to the total bedroom space")
    parser.add_argument("-bn", "--big_num",
                        dest = "big_num",
                        required = False,
                        action = "store",
                        type = int,
                        default = default_values.BIG_ROOM_PEOPLE,
                        help = "Number of people staying in the big room")
    parser.add_argument("-sn", "--small_num",
                        dest = "small_num",
                        required = False,
                        action = "store",
                        type = int,
                        default = default_values.SMALL_ROOM_PEOPLE,
                        help = "Number of people staying in the small room")
    parser.add_argument("-p", "--parking",
                        dest = "parking",
                        required = False,
                        action = "store",
                        type = int,
                        default = default_values.TOTAL_PARKING,
                        help = "Price (in dollars) of the total parking cost")
    parser.add_argument("-r", "--rent",
                        dest = "rent",
                        required = False,
                        action = "store",
                        type = int,
                        default = default_values.TOTAL_RENT,
                        help = "Price (in dollars) of the total rent cost")
    # Parse parameters
    args = parser.parse_args()
    return args

#Calculates and prints rent for each person
def calculate(cl_args):
    #Derive a few constants for easier reading
    rent_noparking = cl_args.rent - cl_args.parking
    total_people = cl_args.big_num + cl_args.small_num

    #Divide common areas
    common_area_fee = rent_noparking / 3 #How much of the common area should be the rent
    kitchen_fee = common_area_fee / total_people

    #Divide small room
    rent_small_room = ((rent_noparking - common_area_fee) * cl_args.small_ratio / cl_args.small_num) + kitchen_fee
    print("Each small room resident owes: $" + str(int(round(rent_small_room))))

    #Divide big room
    rent_big_room = ((rent_noparking - common_area_fee) * cl_args.big_ratio / cl_args.big_num) + kitchen_fee
    print("Each big room resident owes: $" + str(int(round(rent_big_room))))

    print("Reminder parking is $110 per spot.")
    return

def main():
    cl_args = get_arguments() #Sets cl_args to command line arguments
    calculate(cl_args) #Calculates and prints rent
    return 0

if __name__ == "__main__":
    main()