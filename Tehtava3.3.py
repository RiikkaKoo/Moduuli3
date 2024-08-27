sukupuoli = input("Kerro biologinen sukupuolesi (mies tai nainen): ")
hemoglobiini = float(input("Kerro myös hemoglobiiniarvosi (g/l): "))

print()

if sukupuoli == "Mies" or sukupuoli == "mies":
    if 134 <= hemoglobiini <= 195:
        print("Hemoglobiiniarvosi on normaali.")
    elif hemoglobiini < 134:
        print("Hemoglobiiniarvosi on alhainen.")
    elif hemoglobiini > 195:
        print("Hemoglobiiniarvosi on korkea.")

if sukupuoli == "Nainen" or sukupuoli == "nainen":
    if 117 <= hemoglobiini <= 175:
        print("Hemoglobiiniarvosi on normaali.")
    elif hemoglobiini < 117:
        print("Hemoglobiiniarvosi on alhainen.")
    elif hemoglobiini > 175:
        print("Hemoglobiiniarvosi on korkea.")