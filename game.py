def removeMaxPossible(inNumber):
    """
    This method removes the maximun number satisfying the n-2^k constraint

    @return int The number after remove the max number as an integer
    @return bool False if is not possible to remove any number
    """
    # Get the number in binary and remove the "0b" prefix
    binNumber = bin(inNumber)[2:]
    # The first zero will determinate the first max number than can be removed keeping the same number of '1'
    # and complaining with the n-2^k constraint
    firstZeroPos = binNumber.find('0')

    # If we don't have zeros, we can remove anything keeping the same number of '1' 
    if firstZeroPos == -1:
        return False
    return inNumber - int("1%s" % ('0' * (len(binNumber) - firstZeroPos - 1)), 2)

def resolve(num):
    """
    @return str The player who will win the game
    """
    firstWin = False
    # Substract numbers until have a number that can't be reduced (withouth any zero on it)
    n = removeMaxPossible(num)
    while n != False:
        firstWin = not firstWin
        n = removeMaxPossible(n)

    if firstWin:
        return "First Player"
    return "Second Player"


t = int(input())
while t>0:
    n = int(input())
    print(solve(n))
    t -= 1
