import sys  # handle arguments from coommand line
from os import system, name  # attributes to update commandline display live
from random import randrange

# initialize global constants: size tuples for each resource type. put them in reverse so the calculation in TK is more robust.
metal_sizes = (1000, 800, 600, 400, 200, 100, 50)
ceramic_sizes = (800, 640, 480, 320, 160, 80, 40)
chiral_count = 0


# ------------------------------------------------------------------------------
# adds the smallest possible individual units for each road it is asked to calculate
# you might think folks would want to round up lower mats to higher denominations, but in this case the lack of that rounding is a feature
def loopForTotals(material_counter, material_dict, size_array):
    smallest = size_array[len(size_array) - 1]
    while material_counter > smallest:
        for x in range(len(size_array)):

            if (material_counter % size_array[x]) == material_counter:
                continue
            else:
                material_dict[size_array[x]] += 1
                material_counter -= size_array[x]
                break

        if material_counter <= smallest and material_counter > 0:
            material_dict[smallest] += 1
            material_counter -= smallest
            break
    return material_dict


def loopForSingleCheck(material_counter, size_array, mat_name):
    # have to create new dictionaries solely within the scope of this function
    # that way they'll be unloaded after use
    # we don't need to keep them around for individual road calculations, we're ultimately interested in the totals
    material_dict = createOrderReqDictionaries(size_array)

    # this variable represents the smallest denomination in the material's size array
    # this is important to fix an off-by-one error that meant the script was consistently undershooting rather than overshooting requirements by <=smallest
    # in death stranding it's more important to oversupply
    smallest = size_array[len(size_array) - 1]

    mat_total = material_counter  # use this so you have something to print for the total that isnt wrong
    while material_counter > smallest:
        for x in range(len(size_array)):

            if (material_counter % size_array[x]) == material_counter:
                continue
            else:
                material_dict[size_array[x]] += 1
                material_counter -= size_array[x]
                break

        if material_counter <= smallest and material_counter > 0:
            material_dict[smallest] += 1
            material_counter -= smallest
            break

    displayResults(material_dict, mat_total, mat_name, size_array)


# function to clear the output screen for visualization
def clear():
    # if windows, use cls
    if name == "nt":
        _ = system("cls")
    # if mac or linux, use clear
    # this is just for completeness
    else:
        _ = system("clear")


# pauses execution to let you read, then moves on + clears screen
def pause():
    system("pause")
    clear()


# programmatically create instanced, integer:integer dicts from global constants above
def createOrderReqDictionaries(constants_list):
    empty_dict = {}
    for x in range(len(constants_list)):
        empty_dict.update({constants_list[x]: 0})
    return empty_dict


# creates array of specified size,
def create2DArray(height, width):
    arr = [[0 for i in range(height)] for j in range(width)]
    return arr
    # creates 2D lists specifically
    # [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]] type shit
    # shamelessly stolen from https://www.geeksforgeeks.org/python/python-using-2d-arrays-lists-the-right-way/


# also shamelessly stolen, basically creating an alias for the join method to make it easier to call
# map returns an iterator object, and can also apply a function to this iterator: in this case, it re-types input to string
# and join uses that iterator and a list/similar ordered structure, stapling them together in the given order into one object
# and the star in *args means it can take any number of arguments -- map() will cast them to strings
# and the list() function constructs those arguments into a list for processing by the map and join methods
def concatenate(*args):
    return " ".join(map(str, list(args)))


# assign inputs from file to integers in 2D list (metals, ceramics)
# iterates through an array of width 2 and height roads
def getRequirementsFromFile(filename, roads):
    material_array = create2DArray(3, roads)
    with open(filename) as f:
        for x in range(roads):
            # eval() is a function that evaluates any legal math expression in the save file, if it's there (e.g. supplied - required materials)
            # it is also mad dangerous to use in an app cause anybody could put in whatever unsanitized input they liked
            # so this is just a fun little script for me
            # abs() takes absolute value so the eval's can be subtracted in any order
            material_array[x][0] = abs(int(eval(f.readline())))  # chiral crystals
            material_array[x][1] = abs(int(eval(f.readline())))  # metals
            material_array[x][2] = abs(int(eval(f.readline())))  # ceramics
    return material_array


# just a random number generator for some fun, hope this works
# update it does. neat
def randomRequirements(filename, roads):
    material_array = create2DArray(3, roads)
    for x in range(roads):
        material_array[x][0] = randrange(0, 2000)  # chiral crystals
        material_array[x][1] = randrange(0, 2000)  # metals
        material_array[x][2] = randrange(0, 2000)  # ceramics
    return material_array


# displays prettified results in consistent text formatting PLUS padding! hence the use of the concatenate() function
# take the length of a concatenated string, subtract it by some value of spacing, and use that difference to add the right number
# of spaces to a line to make the results line up
# i am positive that the .format method has all this shit baked in and more efficient but i made this from scratch with my bare brain so shut up
def displayResults(material_dict, total_material, mat_name, mat_sizes):
    print("For a requirement of", total_material, mat_name + ", you will need:")
    for x in range(len(material_dict)):
        form_front = concatenate(mat_sizes[x], "units:")
        print(form_front, " " * (13 - len(form_front)), material_dict[mat_sizes[x]])


# -------------------------------------------------------------------


def main(filename, road_number, check):

    # clear screen, initialize totals for reading from file
    clear()
    # cast check to int, then to boolean for proper typecasting
    # otherwise it casts the string to bool, where any data at all is true and only an empty string "" is false
    # so we skip that by making check a number in the command line (0 for false, 1 for true), and cast it from int to bool
    # fixes the problem nicely
    # i could have done a string input where the user types true or false but idfc nobody is gonna use this shit
    check = bool(int(check))

    # initialize totaling variables
    total_chiral = 0
    total_metal = 0
    total_ceramic = 0

    # cast road number input from string to int
    road_number = int(road_number)

    # create requirement_array 2D list
    # includes a random function for testing and fun
    requirement_array = getRequirementsFromFile(filename, road_number)
    # requirement_array = randomRequirements(filename, road_number)

    # create dicts using size array globals that will provide the final print output and totals
    metal_dict = createOrderReqDictionaries(metal_sizes)
    ceramic_dict = createOrderReqDictionaries(ceramic_sizes)

    # iterate through each "road" (aka row) of the 2D array, extract the metal and ceramic requirements from each,
    # add those requirements to the total, and run each individual set of them through the modulo loop as well
    # also total up the results in the main dictionary for each material, which were created just above this loop
    for n in range(road_number):
        # sum together all chiral crystals (not necessary to apply dictionaries, since it is undenominated)
        # read in metal and ceramic requirements from each index in array
        total_chiral += int(requirement_array[n][0])
        metal_counter, ceramic_counter = int(requirement_array[n][1]), int(
            requirement_array[n][2]
        )

        # add data from the requirement array to totals on each loop
        total_metal += metal_counter
        total_ceramic += ceramic_counter

        # even though these functions return a dictionary, we don't have to assign it to an output
        # the return just means the main dicts--that get edited in the function loopForTotals--"moves back" to main scope
        # in that way, the function is now editing an existing object, not returning an entirely new result
        # it's that functionality that lets us use one dictionary for each material and have them remain "editable" by functions
        loopForTotals(metal_counter, metal_dict, metal_sizes)
        loopForTotals(ceramic_counter, ceramic_dict, ceramic_sizes)

        # if the command line argument is True (aka 1), that means the user wants a road-by-road breakdown of each
        # road's material costs. this is useful to ensure you're using the right material sizes for the right roads
        # also this print formatting is big ass but i couldnt think of an abstract way to do this that didnt feel super arbitrary
        # like i could have a switch case type beat for some sort of input to a function (i.e., "single", "total") so it would print the right format
        # but that feels like a vicious waste of time when this works just fine
        # (plus because the print commands are inside the for loop i get to use 'n' in my indexing and printing which is a nice bonus)
        if check == True:
            print("//// SINGLE ROAD REQUIREMENT DISPLAY ////")
            print("For autopaver A" + str(n + 1) + ": ", "\n")
            loopForSingleCheck(metal_counter, metal_sizes, "metal")
            print("")
            loopForSingleCheck(ceramic_counter, ceramic_sizes, "ceramic")
            print("")
            print(
                "You will need",
                requirement_array[n][0],
                "chiral crystals for this autopaver.",
                "\n",
            )
            pause()

    # perhaps look up .format for printing, could make things prettier if you figure it out
    print("cmd: DSRC.py", filename, road_number, check)
    print("Reading from", filename + ", evaluating", road_number, "roads...", "\n")
    displayResults(metal_dict, total_metal, "metal", metal_sizes)
    print("")
    displayResults(ceramic_dict, total_ceramic, "ceramic", ceramic_sizes)
    print("")
    print("You will need", total_chiral, "chiral crystals in total.")


# calls the main function and passes arguments so this can be executed from the command line
main(sys.argv[1], sys.argv[2], sys.argv[3])
