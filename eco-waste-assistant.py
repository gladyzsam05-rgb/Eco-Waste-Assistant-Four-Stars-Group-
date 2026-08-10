print("welcome to Eco-Waste Assistant!")
print("i can help you  make better waste management decision")
waste = input("What type of waste do you need help with? ")

if "plastic" in waste:
    category = "Plastic waste"
    action = "Check if it can be recycled."
    concern = "Plastic can contribute to pollution if it is not disposed of properly."

elif "banana" in waste:
    category = "Organic waste"
    action = "Consider composting it."
    concern = "Organic waste can produce unpleasant effects if it is poorly managed."

elif "phone" in waste:
    category = "E-waste"
    action = "Take it to an appropriate e-waste collection point."
    concern = "E-waste can contain materials that should not be released into the environment."

else:
    category = "Other waste"
    action = "Check local waste-management guidelines."
    concern = "Improper disposal can contribute to environmental pollution."

print("Category:", category)
print("Action:", action)
print("Environmental concern:", concern)



