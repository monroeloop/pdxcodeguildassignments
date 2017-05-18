# class Vehicle:
#     def __init__(self, model, color):
#         self.model = model
#         self.color = color
#
#     def __str__(self):
#         return '{}, {}, {}, {}'.format(self.color,
#                                         self.model)
#
#     def __repr__(self):
#         return '{} {}'.format(self.color,
#                                self.model)
#
# class ParkingLot:
#     def __init__(self, spaces):
#         self.spaces = spaces
#         self.spaces_left = spaces
#         self.parked_vehicles = []
#
def create_space_numbers ():
    parking_lot = {'Space 1': None, 'Space 2': None, 'Space 3': None, 'Space 4': None, 'Space 5': None}
    for k, v in parking_lot.items():
        if v == None:
            print('{} is available.'.format(k))

create_space_numbers()
#
#     def park(self, obj):
#         if self.spaces_left > 0:
#             self.spaces_left -= 1
#             self.parked_vehicles.append(obj)
#             print('There are {} spaces left'.format(self.spaces_left))
#         else:
#             print('Parking Lot is full.')
#
#     def remove(self):
#         car_list = enumerate(self.parked_vehicles)
#         for i, v in car_list:
#             print('{} is in spot {}.'.format(v, i))
#         removing = True
#         while removing:
#             q = input('Which car would you like to remove?  ')
#             if q.lower() == 'cancel' or q.lower() == 'c':
#                 break
#             else:
#                 try:
#                     veh = self.parked_vehicles.pop(int(q))
#                     self.spaces_left += 1
#                     print('{} has left the parking lot.'.format(veh.model))
#                     print('There are {} spaces left'.format(self.spaces_left))
#                     removing = False
#                 except IndexError:
#                     print('That space is already empty.')
#                 except ValueError:
#                     print('Please enter a space number.')
#
# plot = ParkingLot(5)
#
# car1 = Vehicle('Charger','Black')
# car2 = Vehicle('Focus', 'Yellow')
# car3 = Vehicle('M3', 'Orange')
#
# plot.park(car1)
# plot.park(car2)
# plot.park(car3)
# # print(plot.parked_vehicles)
# plot.remove()
