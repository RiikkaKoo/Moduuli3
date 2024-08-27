kuhan_pituus = float(input("Anna kuhan pituus senttimetreinä: "))
print()
if kuhan_pituus <= 37:
    print("Kuha on alamittainen. Laske se takaisin järveen!")
    puuttuva_pituus = float(37-kuhan_pituus)
    print(f"Kuhan pitäisi olla {puuttuva_pituus:.0f} senttimetriä pidempi, \njotta se olisi pyyntimittainen.")

else:
    print("Kuha on pyyntimittainen.")
