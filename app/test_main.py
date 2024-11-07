from manager import NameListManager

name_list = NameListManager(
    {"Elizabeth", "Brian", "Bella", "Jacob", "Jillian", "Liam"},
    {("Elizabeth", "Brian"), ("Brian", "Elizabeth"), ("Bella", "Brian")}
)

print('original list:', name_list.get_names())
name_list.add_name("Ben")
print('after adding Ben:', name_list.get_names())
name_list.remove_name("Liam")
print('after removing Liam:', name_list.get_names())
print('original constraints:', name_list.constraints)
name_list.add_constraint("Brian", "Bella")
print('after adding Brian -> Bella:', name_list.constraints)
name_list.remove_constraint("Brian", "Elizabeth")
print('after removing Brian -> Elizabeth:', name_list.constraints)
print('random test 1:', name_list.generate_pairs())
print('random test 2:', name_list.generate_pairs())
print('random test 3:', name_list.generate_pairs())