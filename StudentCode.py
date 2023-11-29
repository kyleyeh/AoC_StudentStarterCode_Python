def readIntsFromFile(fileName):
    with open(fileName) as inputFile:
        orig = inputFile.read().splitlines()
    nums = [int(num) for num in orig]
    return nums
    

def readStringsFromFile(fileName):
    with open(fileName) as inputFile:
        orig = inputFile.read().splitlines()
    return orig


def partA(nums):
    return nums
    
def partB(nums):
    return nums

nums = readIntsFromFile("inputs1.txt")

print(partA(nums))
print(partB(nums))
