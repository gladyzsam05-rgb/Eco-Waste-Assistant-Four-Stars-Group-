# ECO WASTE ASSISTANT

print("ECO WASTE ASSISTANT")
print("1.Analyze my waste")
print("2.Get a waste disposal action plan")
print("3.Exit")

choice = input("Choose an option: ")

if choice == "1":
    waste = input("what type of waste do you need help with? ")

# STAGE 1: WASTE ANALYSIS

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


print("\n--- STAGE 1: WASTE ANALYSIS ---")
print("Category:", category)
print("Reuse possibility:", reuse)
print("Recycling possibility:", recycling)
print("Initial action:", action)
print("Environmental concern:", concern)


# STAGE 2: ACTION PLAN

print("\n--- STAGE 2: ACTION PLAN ---")

if category == "Plastic waste":
    print("1. Keep the plastic separate from organic waste.")
    print("2. Reuse the container if it is clean and safe.")
    print("3. Check whether your local facility accepts this type of plastic.")
    print("4. Reduce the use of single-use plastic.")

elif category == "Organic waste":
    print("1. Separate the organic waste from other waste.")
    print("2. Compost it where possible.")
    print("3. Avoid mixing it with plastic or electronic waste.")

elif category == "E-waste":
    print("1. Keep the electronic item separate from normal waste.")
    print("2. Repair or reuse it if possible.")
    print("3. Take it to an appropriate e-waste collection point.")
    print("4. Do not dispose of electronic waste with ordinary household waste.")

else:
    print("1. Separate the waste from other materials.")
    print("2. Check your local waste-management guidelines.")
    print("3. Look for an appropriate reuse or recycling option.")
