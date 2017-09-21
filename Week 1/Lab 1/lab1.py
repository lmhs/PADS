inputFile = open("input.txt","r")
numbers = inputFile.read().split();
a = int(numbers[0])
b = int(numbers[1])
outputFile = open("output.txt", "w")
outputFile.write(str(a + b))
outputFile.close()