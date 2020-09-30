import change_guest_list
import guest_list

print ("\n"+"Add new guests!"+"\n")
guest_list.guests.insert(0, 'Bogman')
guest_list.guests.insert(2, 'Jeka')
guest_list.guests.append('Sasha')
i = 0
while i <= len(guest_list.guests)-1:
    (print guest_list.guests[i] + " go to the Party!!!")
    i=i+1

print( "\nMalo mest sory pacani.\n")
while len(guest_list.guests) != 2:
    deleted_guest = guest_list.guests.pop(0)
    print ("Sorry " + deleted_guest)
i = 0
print()
while i <= len(guest_list.guests)-1:
    print (guest_list.guests[i] + " go to the Party!!!")
    i=i+1
while len(guest_list.guests) != 0:
    del guest_list.guests[0]
print (guest_list.guests )
