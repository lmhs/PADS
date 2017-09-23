from openedu_io import openedu_io

with openedu_io() as io:
  length = io.next_int()
  print(length)
  print(io.next_float())
  print(io.next_float())

# inputFile = open('input.txt','r')
# length = int(inputFile.readline())
# array = list(enumerate(inputFile.readline().split()))
# inputFile.close()

# for passnum in range(length-1,0,-1):
#   for i in range(passnum):
#     if float(array[i][1]) > float(array[i+1][1]):
#       temp = array[i]
#       array[i] = array[i+1]
#       array[i+1] = temp

# line = '' + str(array[0][0] + 1) + ' ' + str(array[-(-(length - 1)//2)][0] + 1) + ' ' + str(array[length - 1][0] + 1)

# outputFile = open('output.txt', 'w')
# outputFile.write(line)
# outputFile.close()
