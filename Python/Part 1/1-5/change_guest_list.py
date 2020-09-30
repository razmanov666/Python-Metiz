import guest_list

print ("\n"+guest_list.guests[0] + " can't visiting me today.")
guest_list.guests.insert(0, 'Slavchik')
del guest_list.guests[1]
#print guest_list.guests
print ("\n"+guest_list.guests[0] + ', go to the party.')
print (guest_list.guests[1] + ', go to the party.')
print (guest_list.guests[2] + ', go to the party.')
