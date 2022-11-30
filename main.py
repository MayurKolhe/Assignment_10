import contacts

c = contacts.Contacts()

while True:
    print("      *** TUFFY TITAN CONTACTS MAIN MENU")
    print()
    print("1. Set database name")
    print("2. Add contact")
    print("3. Modify contact")
    print("4. Add phone")
    print("5. Modify phone")
    print("6. Print contact phone list")
    print("9. Exit the program")
    print()
    choice = int(input("Enter menu choice: "))
    print()

    # set database name
    if choice == 1:
        database_name = input("Enter database name: ")
        c.set_database_name(database_name)
        print()

    # add contact
    elif choice == 2:
        database_name = c.get_database_name()
        if database_name == '':
            print('ERROR: Set database name')
            print()
        else:
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            c.add_contact(first_name, last_name)
            print()

    # modify contact
    elif choice == 3:
        database_name = c.get_database_name()
        if database_name == '':
            print('ERROR: Set database name')
            print()
        else:
            contact_id = input("Enter contact id: ")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            c.modify_contact(contact_id, first_name, last_name)
            print()

    # add phone
    elif choice == 4:
        database_name = c.get_database_name()
        if database_name == '':
            print('ERROR: Set database name')
            print()
        else:
            contact_id = input("Enter contact id: ")
            phone_type = input("Enter phone type: ")
            phone_number = input("Enter phone number: ")
            c.add_phone(contact_id, phone_type, phone_number)
            print()

    # modify phone
    elif choice == 5:
        database_name = c.get_database_name()
        if database_name == '':
            print('ERROR: Set database name')
            print()
        else:
            phone_id = input("Enter phone id: ")
            phone_type = input("Enter phone type: ")
            phone_number = input("Enter phone number: ")
            c.modify_phone(phone_id, phone_type, phone_number)
            print()

    # print report
    elif choice == 6:
        database_name = c.get_database_name()
        if database_name == '':
            print('ERROR: Set database name')
            print()
        else:
            list = c.get_contact_phone_list()
            print('=======================================================')
            print('(id) Contact             (id) Phone Numbers       ')
            print('=======================  ==============================')
            previous_id = 0
            for x in list:
                if x[0] == previous_id:
                    print(f'{"":5}{" ":20}{"("+str(x[3])+")":5}{x[5]+": "+x[6]:25}')
                else:
                    print(f'{"("+str(x[0])+")":5}{x[1]+" "+x[2]:20}{"("+str(x[3])+")":5}{x[5]+": "+x[6]:25}')
                previous_id = x[0]
            print('=======================================================')
            print()

    #EXIT
    elif choice == 9:
        break;
