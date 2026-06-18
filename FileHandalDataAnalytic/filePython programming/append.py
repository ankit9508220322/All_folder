# append method work add the text end of write file
f = open("write.txt","a")
string='''
mai append ka used karke extra file add kiya hu write vale me
'''
f.write(string)
print(f)
f.close()