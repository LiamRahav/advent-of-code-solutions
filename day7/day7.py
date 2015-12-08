# Created on 12/7/15

"""
This year, Santa brought little Bobby Tables a set of wires and bitwise logic gates! Unfortunately, little Bobby is a little under the recommended age range, and he needs help assembling the circuit.

Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0 to 65535). A signal is provided to each wire by a gate, another wire, or some specific value. Each wire can only get a signal from one source, but can provide its signal to multiple destinations. A gate provides no signal until all of its inputs have a signal.

The included instructions booklet describe how to connect the parts together: x AND y -> z means to connect wires x and y to an AND gate, and then connect its output to wire z.

Other possible gates include OR (bitwise OR) and RSHIFT (right-shift). If, for some reason, you'd like to emulate the circuit instead, almost all programming languages (for example, C, JavaScript, or Python) provide operators for these gates.

In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire a?
"""

from termcolor import colored
from string import ascii_lowercase


def check_for_int(test_input):
    if not test_input.isdigit():
        return wires[test_input]
    else:
        return int(test_input)

if __name__ == '__main__':
    f_input = []
    with open("input.txt") as f:
        f_input = f.readlines()

    wires = {}

    for first_character in ascii_lowercase:
        wires[first_character] = int(0)
        for second_character in ascii_lowercase:
            wires[first_character + second_character] = int(0)

    for line in f_input:
        line = line.strip().split(" ")
        line.remove("->")

        if len(line) == 2:
            wires[line[1]] = check_for_int(line[0])

        elif len(line) == 3:
            wires[line[2]] = ~check_for_int(line[1])

        elif len(line) == 4:
            input_wire = line[0]
            modifying_wire = line[2]
            target_wire = line[3]

            if line[1] == "RSHIFT":
                wires[target_wire] = check_for_int(input_wire) >> check_for_int(modifying_wire)

            elif line[1] == "LSHIFT":
                wires[target_wire] = check_for_int(input_wire) << check_for_int(modifying_wire)

            elif line[1] == "AND":
                wires[target_wire] = check_for_int(input_wire) & check_for_int(modifying_wire)

            elif line[1] == "OR":
                wires[target_wire] = check_for_int(input_wire) | check_for_int(modifying_wire)

    print colored("A:", "yellow"),
    print(wires["a"])