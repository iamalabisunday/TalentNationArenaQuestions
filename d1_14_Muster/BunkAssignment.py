# Quarters are assigned by service number. Each room holds eight bunks. Rooms and bunks are both counted from one: service numbers 1 to 8 fill Room 1 (Bunk 1 to Bunk 8), service numbers 9 to 16 fill Room 2, and so on. Implement bunk_assignment(service_number) and return the line Room R, Bunk B with the correct numbers. For service number 9 the answer is Room 2, Bunk 1. Work the room and the bunk out with the floor-division and modulo operators. Do not use divmod.
def bunk_assignment(service_number):
    zero_based = service_number - 1
    room = (zero_based // 8) + 1
    bunk = (zero_based % 8) + 1
    return f"Room {room}, Bunk {bunk}"