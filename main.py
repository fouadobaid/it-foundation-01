from typing import List, Any

print("\n\nBus Ticket Booking System\n")
booked_seat = []
restart = ('')
seats= [{1},{2,3,4},{5,6,7,8},{9,10,11,12},{13,14,15,16},{17,18,19,20}]
seats2 = [{1},{2,3,4},{5,6,7,8},{9,10,11,12},{13,14,15,16},{17,18,19,20}]
while restart != ('N', 'NO', 'n', 'no'):
    print("1.Check Bus schedules and routes")
    print("2.Exit")
    option = int(input("\nEnter your option : "))

    if option == 1:
        print("\nBus schedules and routes:")
        print("1- The bus heading from Rafah to Gaza.\n 2- The bus heading from Gaza to Rafah.")
        optionn = int(input("\n Enter the bus you want to know the details of its route and seats:"))
        if optionn== 1:
            print("\nThe bus leaves from Rafah at 7 and is expected to arrive to Gaza at 7:45")
            print("All seats:\n",seats[0],"\n",seats[1],"\n",seats[2],"\n",seats[3],"\n",seats[4],"\n",seats[5],"\nbooked seats:",booked_seat)
            restart = str(input("\nDo you want to reserve a seat? y/n: "))
            if restart in ('y', 'YES', 'yes', 'Yes'):
                people = int(input("\nEnter no. of Ticket you want : "))
                name_l = []
                age_l = []
                sex_l = []
                seat_l= []

                for p in range(people):


                    name = str(input("\nName : "))
                    name_l.append(name)
                    age = int(input("\nAge  : "))
                    age_l.append(age)
                    sex = str(input("\nMale or Female : "))
                    sex_l.append(sex)
                    seat = str(input("\nseat : "))
                    seat_l.append(seat)


                restart = str(input("\nDid you forgot someone? y/n: "))
                if restart in ('y', 'YES', 'yes', 'Yes'):
                    restart = ('Y')
                else:

                    print("\nTotal Ticket : ", people)
                    for p in range(1, people + 1):
                        x = 0
                        print("Ticket : ", p, "\t", )
                        print("Name : ", name_l[x])
                        print("Age  : ", age_l[x])
                        print("Sex : ", sex_l[x])
                        print("Seat : ", seat_l[x])
                        x += 1

                    exit(0)

            else:
                exit(0)
        elif optionn==2:
            print("\nThe bus leaves from Gaza at 7 and is expected to arrive to Rafah at 7:45")
            print(" All seats:\n", seats2[0], "\n", seats2[1], "\n", seats2[2], "\n", seats2[3], "\n", seats2[4], "\n",
                  seats2[5],"\nbooked seats:",booked_seat)
            restart = str(input("\nDo you want to reserve a seat? y/n: "))
            if restart in ('y', 'YES', 'yes', 'Yes'):
                people = int(input("\nEnter no. of Ticket you want : "))
                name_l = []
                age_l = []
                sex_l = []
                seat_l = []

                for p in range(people):
                    name = str(input("\nName : "))
                    name_l.append(name)
                    age = int(input("\nAge  : "))
                    age_l.append(age)
                    sex = str(input("\nMale or Female : "))
                    sex_l.append(sex)
                    seat = str(input("\nseat : "))
                    seat_l.append(seat)
                    booked_seat.append(seat)

                restart = str(input("\nDid you forgot someone? y/n: "))
                if restart in ('y', 'YES', 'yes', 'Yes'):
                    restart = ('Y')
                else:

                    print("\nTotal Ticket : ", people)
                    for p in range(1, people + 1):
                        x = 0
                        print("Ticket : ", p, "\t", )
                        print("Name : ", name_l[x])
                        print("Age  : ", age_l[x])
                        print("Sex : ", sex_l[x])
                        print("Seat : ", seat_l[x])
                        x += 1

                    exit(0)

            else:
                exit(0)






    elif option == 2:
        exit(0)
