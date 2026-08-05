# The parade roll needs your full record across three lines. Implement muster_record(name, service_number) and return exactly three lines, each separated by a newline. Line one is RECRUIT: followed by the name. Line two is SERVICE NUMBER: followed by the service number. Line three is QUARTERS: followed by the same Room R, Bunk B you worked out in the bunk-assignment exercise, using the eight-bunks-per-room rule. You have already built both halves of this; the task now is to compose them into one record. The newline between lines is part of the task to research.
def muster_record(name, service_number):
    name = str(name)
    service_number = int(service_number)
    zero_num = service_number - 1
    room = (zero_num // 8) + 1
    bunk = (zero_num % 8) + 1
    return (
        f"RECRUIT: {name}\n"
        f"SERVICE NUMBER: {service_number}\n"
        f"QUARTERS: Room {room}, Bunk {bunk}"
        )