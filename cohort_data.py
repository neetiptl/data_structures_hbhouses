def unique_houses(filename):
    """TODO: Create a set of student houses.

    Iterates over the cohort_data.txt file to look for all of the included house names
    and creates a set called 'houses' that holds those names.

        ex. houses = set([ "Hufflepuff",
                    "Slytherin",
                    "Ravenclaw",
                    "Gryffindor",
                    "Dumbledore's Army",
                    "Order of the Phoenix"
            ])

    """
    houses = set()
    cohort_info = open(filename)
    for line in cohort_info:
        cohort_data = line.split("|")
        house = cohort_data[2]
        if house != "":
            houses.add(house)
        
    # Code goes here

    print houses



def sort_by_cohort(filename):
    """TODO: Sort students by cohort.

    Iterates over the data to create a list for each cohort, ordering students
    alphabetically by first name and tas separately. Returns list of lists.

        ex. winter_15 = ["alice tsao", "amanda gilmore", "anne vetto", "..." ]
        ex. all_students = [winter_15, spring_15, summer_15, tas]

    """
    cohort_info = open(filename)
    tas = set()
    all_students = []
    winter_15 = []
    spring_15 = []
    summer_15 = []
    for line in cohort_info:
        stripped_line = line.strip()    
        cohort_data = stripped_line.split("|")  
        cohort_lady_name = cohort_data[0] + " " + cohort_data[1]
        all_students.append(cohort_lady_name)
        season = cohort_data[4]
        if season == 'Winter 2015':
            winter_15.append(cohort_lady_name)
        if season == 'Spring 2015':
            spring_15.append(cohort_lady_name)
        if season == "Summer 2015":
            summer_15.append(cohort_lady_name)
        tas.add(cohort_data[3])


    # Code goes here

def students_by_house(filename):
    """TODO: Sort students by house.

    Iterate over the data to create a list for each house, and sort students
    into their appropriate houses by last name. Sort TAs into a list called "tas".
    Return all lists in one list of lists.
        ex. hufflepuff = ["Gaikwad", "Le", "..." ]
        ex. tas = ["Bryant", "Lefevre", "..."]
        ex. houses_tas = [ hufflepuff,
                        gryffindor,
                        ravenclaw,
                        slytherin,
                        dumbledores_army,
                        order_of_the_phoenix,
                        tas
            ]
    """

    all_students = []
    gryffindor = []
    hufflepuff = []
    slytherin = []
    dumbledores_army = []
    order_of_the_phoenix = []
    ravenclaw = []
    tas = set()
    cohort_info = open(filename)
    for line in cohort_info:
        stripped_line = line.strip()    
        cohort_data = stripped_line.split("|")  
        cohort_lady_name = cohort_data[1]
        if cohort_data[3] != "":
            tas.add(cohort_data[3])
        if cohort_data[2] == "Gryffindor":
            gryffindor.append(cohort_lady_name)
        if cohort_data[2] == "Hufflepuff":
            hufflepuff.append(cohort_lady_name)
        if cohort_data[2] == "Slytherin":
            slytherin.append(cohort_lady_name)
        if cohort_data[2] == "Ravenclaw":
            ravenclaw.append(cohort_lady_name)
        if cohort_data[2] == "Dumbledore's Army":
            dumbledores_army.append(cohort_lady_name)
        if cohort_data[2] == "Order of the Phoenix":
            order_of_the_phoenix.append(cohort_lady_name)
    list_o_lists = [gryffindor, hufflepuff, ravenclaw, slytherin, order_of_the_phoenix, dumbledores_army, tas]        


    

    return list_o_lists

students_by_house("cohort_data.txt")

def all_students_tuple_list(filename):
    """TODO: Create a list of tuples of student data.

    Iterates over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)
        ex. all_people = [
                ("Alice Tsao", "Slytherin", "Kristen", "Winter 2015"),
                ("Amanda Gilmore", "Hufflepuff", "Meggie", "Winter 2015"),
                # ...
            ]
    """
    cohort_info = open(filename)
    student_tuple_list =[]
    for line in cohort_info:
        stripped_line = line.strip()
        student_data = stripped_line.split("|")
        student_tuple =(student_data[0],student_data[1], student_data[2], student_data[3], student_data[4])
        student_tuple_list.append(student_tuple)


    # Code goes here

    return student_tuple_list

all_students_tuple_list("cohort_data.txt")

def find_cohort_by_student_name(student_list):
    """TODO: Given full name, return student's cohort.

    Use the above list of tuples generated by the preceding function to make a small
    function that, given a first and last name, returns that student's cohort, or returns
    'Student not found.' when appropriate. """

    inputted_first_name = raw_input("Please insert student first name:")
    inputted_last_name = raw_input("Please insert student last name:")
    student_info = all_students_tuple_list("cohort_data.txt")
    for each_student in student_info:
        if (inputted_first_name == each_student[0]) and (inputted_last_name == each_student[1]):
            return each_student[4]

    return "Student not found."

find_cohort_by_student_name("cohort_data.txt")

##########################################################################################
# Further Study Questions


def find_name_duplicates(filename):
    """TODO: Using set operations, make a set of student first names that have duplicates.

    Iterates over the data to find any first names that exist across multiple cohorts.
    Uses set operations (set math) to create a set of these names.
    NOTE: Do not include staff -- or do, if you want a greater challenge.

       ex. duplicate_names = set(["Sarah"])

    """

    duplicate_names = set()

    # Code goes here

    return duplicate_names


def find_house_members_by_student_name(student_list):
    """TODO: Create a function that prompts the user for a name via the command line
    and returns everyone in their house that's in their cohort.

    Use the list of tuples generated by all_students_tuple_list to make a small function that,
    when given a student's first and last name, returns students that are in both that
    student's cohort and that student's house."""

    # Code goes here

    return


#########################################################################################

#Here is some useful code to run these functions!

# all_students_data = all_students_tuple_list("cohort_data.txt")
# print all_students_data
# print unique_houses("cohort_data.txt")
# print sort_by_cohort("cohort_data.txt")
# print students_by_house("cohort_data.txt")
# print find_name_duplicates("cohort_data.txt")
# find_house_members_by_student_name(all_students_data)
# find_cohort_by_student_name(all_students_data)
