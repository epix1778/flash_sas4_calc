import json

weapons = open("weapons.json","r")
weapons_data = json.load(weapons)
ammo = open("ammos.json","r")
ammo_data = json.load(ammo)
names = open("weapon_name_desc.csv","r",encoding="utf-8")

weapon_output_list = []
weapons_important_items=["name","category","range","rps","clipSize","reloadSpeed","movementReduction","ammoID","weaponVersion","burstSpeed","burstCount"]
ammos_important_items = ["projectileCount","damage","damageType","radius","pierce","dot","dotLength"]

for dyct in weapons_data:
    output_dict = {}
    for key in dyct.keys():
        if key in weapons_important_items:
            if key == "name":
                for line in names.readlines():
                    line_data = line.split(",")
                    if int(line_data[0]) == dyct[key]:
                        output_dict[key] = line_data[2].strip().strip('"').strip(" ")
                names.seek(0)
            elif key == "ammoID":
                for dyct2 in ammo_data:
                    for key2 in dyct2.keys():
                        if key2 == "id":
                            if dyct2[key2] == dyct[key]:
                                for key2 in dyct2.keys():
                                    if key2 in ammos_important_items:
                                        output_dict[key2] = dyct2[key2]
            else:
                output_dict[key] = dyct[key]
    weapon_output_list.append(output_dict)

with open("full_weapon_data.json","w") as file:
    json.dump(weapon_output_list,file,indent=4)


