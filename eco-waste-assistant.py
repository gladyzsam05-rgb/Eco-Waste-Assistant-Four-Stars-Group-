print("welcome to Eco-Waste Assistant!")
print("i can help you  make better waste management decision")
waste = input("What type of waste do you need help with? ")

if "plastic" in waste:
    category = "Plastic waste"
    reuse = "Yes, if the container is clean and safe to reuse."
    recycling = "Yes, depending on the type of plastic and local facilities."
    action = "Check if it can be recycled."
    concern = "Plastic can contribute to pollution if it is not disposed of properly."

elif "banana" in waste:
    category = "Organic waste"
    reuse = "No, but it can be composted."
    recycling = "No, composting is more suitable."
    action = "Consider composting it."
    concern = "Organic waste can cause environmental problems if poorly managed."

elif "phone" in waste:
    category = "E-waste"
    reuse = "Yes, if it is still working or can be repaired."
    recycling = "Yes, through an appropriate e-waste facility."
    action = "Take it to an appropriate e-waste collection point."
    concern = "E-waste can contain materials that should not be released into the environment."

else:
    category = "Other waste"
    reuse = "Unknown."
    recycling = "Check local recycling options."
    action = "Check local waste-management guidelines."
    concern = "Improper disposal can contribute to environmental pollution."

print("Category:", category)
print("Reuse possibility:", reuse)
print("Recycling possibility:", recycling)
print("Action:", action)
print("Environmental concern:", concern)


