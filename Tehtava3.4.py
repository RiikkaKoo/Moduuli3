vuosi = float(input("Anna vuosiluku: "))
print()
vuosi_jaettuna = vuosi/4
vuosi_sata = vuosi-(vuosi % 100)
vuosi_tuhat = vuosi-(vuosi % 100)

if vuosi < 100:
    if vuosi/4 == int(vuosi_jaettuna):
        print("Tämä vuosi on karkausvuosi.")
    else:
        print("Tämä vuosi ei ole karkausvuosi.")

if 100 <= vuosi < 1000:
    if vuosi == vuosi_sata:
        if vuosi_sata >= 400:
            vuosisata_jaettuna = vuosi_sata/400
            if vuosisata_jaettuna >= 1 and vuosisata_jaettuna == int(vuosisata_jaettuna):
                print("Tämä vuosi on karkausvuosi.")
        else:
            print("Tämä vuosi ei ole karkausvuosi.")
    elif vuosi/4 == int(vuosi/4):
        print("Tämä vuosi on karkausvuosi.")
    else:
        print("Tämä vuosi ei ole karkausvuosi.")

if vuosi >= 1000:
    if vuosi == vuosi_tuhat:
        vuosituhat_jaettuna = vuosi_tuhat/400
        if vuosituhat_jaettuna >= 1 and vuosituhat_jaettuna == int(vuosituhat_jaettuna):
                print("Tämä vuosi on karkausvuosi.")
        else:
            print("Tämä vuosi ei ole karkausvuosi.")
    elif vuosi/4 == int(vuosi/4):
        print("Tämä vuosi on karkausvuosi.")
    else:
        print("Tämä vuosi ei ole karkausvuosi.")