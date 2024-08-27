hyttiluokka = input("Kerro hyttiluokkasi: ")
print()

if (hyttiluokka == "LUX") or (hyttiluokka == "lux"):
    print("LUX on parvekkeellinen hytti yläkannella.")
elif (hyttiluokka == "A") or (hyttiluokka == "a"):
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif (hyttiluokka == "B") or (hyttiluokka == "b"):
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif (hyttiluokka == "C") or (hyttiluokka == "c"):
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print('"Virheellinen hyttiluokka"')
