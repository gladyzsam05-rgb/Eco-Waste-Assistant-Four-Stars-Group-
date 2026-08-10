print("welcome to Eco-Waste Assistant!")
print("i can help you  make better waste management decision")
waste = input("what type of waste do you need help with?")
print("You entered:" , waste)
if "plastic" in waste.lower():
      print("This may be recyclable. Check your local recycling guideline.")
elif "babana peels" in waste.lower():
      print("Food waste can often be composted.")
elif "old phone" in waste.lower():
      print("old phone should be taken to a suitable collection point.")
else:
      print("please check local waste-management guidelines for this item.")



