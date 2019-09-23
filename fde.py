import time


def to_binary(value):
    return int("".join(str(x) for x in value), 2)


#def LOAD(location):
#    return [0, 0, 1].append(str(to_binary(location)))


# Based on 8 bits
# First three bits is instruction opcode, last 5 bits is value
memory = [
    [0, 0, 1, 0, 0, 1, 1, 0],  # Load Memory Location (7)
    #LOAD(6),
    [0, 1, 1, 0, 0, 1, 1, 1],  # Add Memory Location (6)
    [0, 1, 0, 0, 0, 1, 1, 0],  # Store New Number in Location (7)
    [1, 0, 0, 0, 0, 0, 0, 0],  # Jump to location (0)
    # End of Instructions
    # Begin Value Address Space
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],  # Used to Store Big Number being computed
    [0, 0, 0, 0, 0, 1, 0, 1],  # Memory Location (8) Used to Store Number being Added (5)
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]

# Loads initial address to PC, everything has maximum of 8-bits
ac, pc, mar, mdr, cir = ([0, 0, 0, 0, 0, 0, 0, 0] for i in range(5))

Halt = False
status_register = [0] * 8
print("\n")
print('Status Register:    ', status_register)
print('Program Counter:    ', pc)
print('Current Instruction:', cir, '\n', '\n')


# Simulate Native Process of fetching address value
def get_from_ram():
    try:
        location = to_binary(mar)
        return memory[location]
    except IndexError:
        print("\n", "Memory Address out of Range halting")
        halt = True


# Update Program Counter to given Binary value
def update_program_counter(value=False):
    if value:
        return value

    binary = to_binary(pc) + 1
    res2 = list(map(int, list(bin((1 << 8) + binary))[-8:]))

    return res2


# Bit shift value by 5 to get opcode
def decode_opcode(address_value):
    address_value_binary = to_binary(address_value) >> 5
    return list(map(int, list(bin((1 << 8) + address_value_binary))[-3:]))


def cycle():
    time.sleep(2)


def pure():
    print("---------------------------------")
    print("Instruction: None")


def jump():
    global pc
    mdr_binary = to_binary(mdr)
    new_address = (mdr_binary & 0b00111111)
    res2 = list(map(int, list(bin((1 << 8) + new_address))[-8:]))

    pc = res2
    print("---------------------------------")
    print("Instruction: Jump")


def load():
    global mar, mdr, ac
    mdr_binary = to_binary(mdr)
    new_address = (mdr_binary & 0b00011111)
    mar = list(map(int, list(bin((1 << 8) + new_address))[-8:]))
    mdr = get_from_ram()

    ac = mdr
    print("---------------------------------")
    print("Instruction: Load", int("".join(str(x) for x in ac), 2))


def store():
    global mar, mdr, ac, memory
    mdr_binary = to_binary(mdr)
    new_address = (mdr_binary & 0b00011111)
    mar = list(map(int, list(bin((1 << 8) + new_address))[-8:]))
    mdr = get_from_ram()

    memory[new_address] = ac

    print("---------------------------------")
    print("Instruction: Store", to_binary(ac))


def add():
    global mar, mdr, ac
    binary_ac = to_binary(ac)

    mdr_binary = int("".join(str(x) for x in mdr), 2)
    new_address = (mdr_binary & 0b00011111)
    mar = list(map(int, list(bin((1 << 8) + new_address))[-8:]))

    new_mdr_binary = int("".join(str(x) for x in get_from_ram()), 2)

    new_ac = binary_ac + new_mdr_binary
    ac = list(map(int, list(bin((1 << 8) + new_ac))[-8:]))

    print("---------------------------------")
    print("Instruction: Add", new_mdr_binary)


def fetch():
    global mar, pc, mdr
    mar = pc  # Load PC contents to MAR
    print("mar:", mar)
    pc = update_program_counter()  # Update program counter to next address
    mdr = get_from_ram()  # Load Data Required to MDR
    print("mdr:", mdr)


def decode():
    global cir
    cir = decode_opcode(mdr)  # Load Current Instruction into CIR
    print("---------------------------------")
    print("Opcode: ", cir)


def execute():
    opcode = int("".join(str(x) for x in cir), 2)
    instructions[opcode]()


# Opcode definitions
instructions = {
    0b000: pure,  # Pure Value
    0b001: load,  # Load
    0b010: store,  # Store
    0b011: add,  # Add
    0b100: jump  # Jump
}


while not Halt:  # While loop to simulate timing
    cycle()    # Cycle

    fetch()

    if mdr is None:
        break

    if to_binary(ac) > 32:
        print("Buffer overflow, Computed Highest Number", to_binary(ac))
        break

    decode()

    execute()  # Perform Execution

    print("---------------------------------")
    print("acc:", ac, "\n", "\n")
