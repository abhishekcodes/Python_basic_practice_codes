fw = open("x.txt", 'w')
fw.write('writing soemthing in the file \n')
fw.write('this is not cool')
fw.close()

fr = open("x.txt", 'r')
text = fr.read()
print(text)
fr.close()


    
