# Getting the fire cells in a list

fire_cells_list = str(input()).split('#')
water_amount = int(input())
water_to_use = 0
current_cell = []
effort = 0
tot_fire = 0
print('Cells:')
for i in fire_cells_list:
    current_cell = i.split(' = ')
    if (current_cell[0] == 'High' and 81 <= int(current_cell[1]) <= 125)\
            or (current_cell[0] == 'Medium' and 51 <= int(current_cell[1]) <= 80) \
            or (current_cell[0] == 'Low' and 1 <= int(current_cell[1]) <= 50):
        if int(current_cell[1]) > water_amount:
            continue
        #print(f'water_amount = {water_amount}')
        water_amount -= int(current_cell[1])
        effort += 0.25 * int(current_cell[1])
        tot_fire += int(current_cell[1])
        print(f' - {current_cell[1]}')
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {tot_fire}')
