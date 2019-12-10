#!/usr/bin/python3

import sys

#call like:
#    $ python3 8.py image_width image_height image_data

def part_one(layers):
    min_count = None
    min_layer = None
    for i in range(len(layers)):
        layer = layers[i]
        zeroes = list("".join(layer)).count('0')
        if (min_count is None):
            min_count = zeroes
            min_layer = i
        elif (zeroes < min_count):
            min_count = zeroes
            min_layer = i
    #count 1, count 2, multiply and return
    layer = list("".join(layers[min_layer]))
    ones = layer.count('1')
    twos = layer.count('2')
    print("Parity check as answer to part 1: %d" % (ones*twos))

def part_two(layers, w, h):
    top_layer = [["2" for x in range(w)] for y in range(h)]
    for layer in layers[::-1]:
        for y in range(h):
            for x in range(w):
                if layer[y][x] == "1" or layer[y][x] == "0":
                    top_layer[y][x] = layer[y][x]
    for line in top_layer:
        print("".join(line).replace("0", " ").replace("1", "#"))


if __name__ == "__main__":
    img_w = int(sys.argv[-3])
    img_h = int(sys.argv[-2])
    with open(sys.argv[-1]) as f:
        layers = []
        layer = [f.read(img_w) for x in range(img_h)]
        layers.append(layer)
        while (layer[0] != ''):
            layer = [f.read(img_w) for x in range(img_h)]
            layers.append(layer)
        layers.pop() # delete the final layer is cheaper than doing a branch
        layers.pop() # ( we actually get two garbage layers at the end )
        # --- part 1 solution bits ---
        part_one(layers)
        # --- part 2 solution bits ---
        part_two(layers, img_w, img_h)
