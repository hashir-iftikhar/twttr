
line = input("Enter the line ")
vowel = "aeiouAEIOU"
result ="" 

for i in range(len(line)):
    if line[i] not in vowel:
        result +=line[i]
print(f"The result is : {result}")


