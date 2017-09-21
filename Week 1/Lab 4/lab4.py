with open('input.txt') as inputFile:
  length = int(inputFile.readline())
  list1 = print(x) for x in enumerate(inputFile.readline().split())

  print(list)

  # for passnum in range(length-1,0,-1):
  #   for i in range(passnum):
  #     if array[i][0]>array[i+1][0]:
  #       temp = array[i]
  #       array[i] = array[i+1]
  #       array[i+1] = temp

  line = '' + str(array[0][1]) + ' ' + str(array[-(-(length - 1)//2)][1]) + ' ' + str(array[length - 1][1])

outputFile = open('output.txt', 'w')
outputFile.write(line)