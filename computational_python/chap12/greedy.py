class Item(object):

    def __init__(self, n, w, v):
        self.name = n
        self.weight = w
        self.value = v

    def getName(self):
        return self.name

    def getValue(self):
        return self.value

    def getWeight(self):
        return self.weight


def value(item):
     return item.getValue()

def weightInverse(item):
    return 1.0/item.getWeight()

def density(item):
    return item.getValue()/item.getWeight()

def greedy(items, maxWeight, keyFunction):
    itemsCopy = sorted(items, key=keyFunction, reverse=True)
    result = []
    totalValue, totalWeight = 0.0, 0.0
    for i in range(len(itemsCopy)):
        if (totalWeight + itemsCopy[i].getWeight()) <= maxWeight:
            result.append(itemsCopy[i])
            totalWeight += itemsCopy[i].getWeight()
            totalValue += itemsCopy[i].getValue()
    return result, totalValue

def buildItems():
    names = ['clock', 'painting', 'radio', 'vase', 'book', 'computer']
    values = [175, 90, 20, 50, 10, 200]
    weights = [10, 9, 4, 2, 1, 2]
    Items = []
    for i in range(len(values)):
        Items.append(Item(names[i], values[i], weights[i]))
    return Items

def testGreedy(items, maxWeight, keyFunction):
    taken, val = greedy(items,  maxWeight, keyFunction)
    print('Total value of items taken is', val)
    for item in taken:
        print(" ", item)

def testGreedys(maxWeight=20):
    items = buildItems()
    print("Use greedy by value to fill knapsack of size", maxWeight)
    testGreedy(items, maxWeight, value)
    print("\nUse greedy by weight to fill knapsack of size", maxWeight)
    testGreedy(items, maxWeight, weightInverse)
    print("\nUse greedy by density to fill knapsack of size", maxWeight)
    testGreedy(items, maxWeight, density)

if __name__ == "__main__":
    testGreedys()