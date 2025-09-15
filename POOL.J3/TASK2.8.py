# TASK 2.8
# Complete the following code so that it prints "42 is the answer"contains 16 characters.
s1,s2,s3 = "42","is","the answer"

    # METHOD 01
# print ("\""+(f"{s1}"+" "+s2+" "+s3)+"\""+"contains",len((f"{s1}"+" "+s2+" "+s3)),"characters.")
# print ("\""+f"{s1}",f"{s2}",f"{s3}"+"\""+"contains",len((f"{s1}"+" "+s2+" "+s3)),"characters.")
print ("\""+s1,s2,s3+"\""+" contains",len((f"{s1}"+" "+s2+" "+s3)),"characters.")

    # METHOD 02
text = s1+" "+s2+" "+s3
lenght = len(text)

print("\""+f"{text}"+"\"","contains",lenght,"characters.")