with open('input.txt') as inputFile:
  n = int(inputFile.readline())
  array = [int(x) for x in inputFile.readline().split()]
  arrayLines = array[:]
  for j, v in enumerate(array):
    i = j - 1
    while i > -1 and v < array[i]:
      array[i+1] = array[i]
      i = i - 1
    array[i+1] = v

    arrayLines[j] = i + 2

outputFile = open('output.txt', 'w')
outputFile.write(' '.join(str(x) for x in arrayLines) + '\n')

outputFile.write(' '.join(str(x) for x in array))
outputFile.close()