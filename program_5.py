#Programmer: Timothy Pickering
#Date Written: 3/19/2025
#Title: Course Info

def get_courses():
    courses = {} #Dictionary to store course ID and course name

    while True:
        #Prompt user for course ID
        course_id = input("Enter course ID (or type 'done' to stop): ").strip()
        #Check if the user wants to stop entering courses
        if course_id.lower() == 'done':
            break

        #Prompt user for course name
        course_name = input("Enter course name: ").strip()
        #Store the course ID and name in the dictionary
        courses[course_id] = course_name

    #Return the dictionary containing all entered courses
    return courses

def filter_courses_by_subject(courses, subject):
    print(f"\nCourses under the subject '{subject}':")
    found = False
    #Loop courses to check if the course starts with the given subject
    for course_id, course_name in courses.items():
        if course_id.startswith(subject):
            print(f"{course_id}: {course_name}")
            found = True
    #If no courses match the subject then inform the user
    if not found:
        print("No courses found with that subject.")

#Get courses from user
courses = get_courses()

#Get subject to filter
subject = input("\nEnter a subject prefix to filter: ").strip()

#Display matching courses
filter_courses_by_subject(courses, subject)
