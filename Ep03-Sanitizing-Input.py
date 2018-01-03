# clean = False

# while clean == False:
# 
#   phones = raw_input("How many phones have you broken? ")
#   laptops = raw_input("How many laptops have you dropped? ")
# 
#   if phones.isdigit() and laptops.isdigit(): #isdigit() only works for positive numbers
#     clean = True
# 
# print int(phones) + int(laptops)
# 
# raw_input("Press Enter to Exit")


clean = False

while clean == False:

  phones = input("How many phones have you broken? ")
  laptops = input("How many laptops have you dropped? ")

  try:
      int(phones)
      int(laptops)
  except ValueError:
      print ('Hey! You didn\'t give me numbers.')
      clean = False
  else:
      clean = True

print(int(phones) + int(laptops))

input("Press Enter to Exit")