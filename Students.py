students ={}
print("This is a Student management system")
print("Choose one option(What number) .")
try:
    while True:
        choice = int(input("1. add student 2. display student 3. Delete student 4. search student 5. "))
        if choice == 1:
            id = int(input("what is the student id"))
            eng = int(input("what is the student english score"))
            math = int(input("What is the student math score"))
            chem = int(input("what is the student chemistry score"))
            phy = int(input("what is the student physics score"))
            students[id] = {"english" : eng , "mathematics" : math , "chemistry" : chem, "physics" : phy}
            print("Entered successfully")
        elif choice == 2:
            for id, details in students.items():
                print(id, students.items())
        elif choice == 3:
            id = int(input("Enter students id"))
            if id not in students:
                print("not available")
                continue
            else:
                del students[id]
                print("Deleted")
        elif choice == 4:
             id = int(input("what is the students id"))
             if id not in students:
                 print("not available")
                 continue
             else:
                 print(students[id])
except ValueError:
    print("Only digits are allowed")
    
