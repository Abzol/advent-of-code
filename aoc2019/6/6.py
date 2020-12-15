#!/usr/bin/python3

import sys

def traceBack(tree, node):
    if tree[node] == None:
        return 0
    else:
        return (traceBack(tree, tree[node]) + 1)

def countOrbits(tree):
    total = 0
    for key in tree:
        total += traceBack(tree, key)
    return total

def routeBack(tree, node):
    if tree[node] == None:
        return node
    else:
        return routeBack(tree, tree[node]) + ',' + node

if __name__ == "__main__":
    tree = {}
    with open(sys.argv[-1]) as f:
        for line in f:
            base, orbiter = line.rstrip().split(')')
            if base not in tree:
                tree[base] = None
            tree[orbiter] = base
        print("Total number of orbits: %d" % countOrbits(tree))
        santaRoute = routeBack(tree, "SAN").split(',')[::-1]
        youRoute = routeBack(tree, "YOU").split(',')[::-1]
        for i in youRoute:
            if i in santaRoute:
                print("Transfers to find santa: %d" % int(youRoute.index(i) + santaRoute.index(i) - 2))
                break
