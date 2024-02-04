s1= input("Enter a String:\n")
s2= input("Enter a String:\n")

def areAnagram(s1,s2):
    if len(s1) != len(s2):
        return False
    count=[0]*256   #creating a list with the 256 ascii positions as zero
    for i in range(len(s1)):
        count[ord(s1[i])]+=1    #ORD() gives the ascii value
        count[ord(s2[i])]-=1
    for x in count:
        if x!=0:
            return False
    return True