parking_state = [
  [1,1,1],
  [0,0,0],
  [1,1,2]
]

#Your code go here:
def get_parking_lot(parking):
    occupied_slots = 0
    available_slots = 0
    total_slots = 0
    state = {}
    for colum in parking:
        for item in colum:
           if item == 1:
               occupied_slots += 1
           elif item == 2:
               available_slots += 1

    total_slots = occupied_slots + available_slots
    state["total_slots"] = total_slots
    state["available_slots"] = available_slots
    state["occupied_slots"] = occupied_slots
    return state

print(get_parking_lot(parking_state))


