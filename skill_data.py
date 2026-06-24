import json

skill_data = open("skill_data.json","w")

output_list = []

def reload_skill():
    output_dict = {}
    base_name = "l"
    output_dict["name"] = "fast_reload"
    for i in range(1,25+1):
        level_name = base_name + str(i)
        output_dict[level_name] = 1-0.965**i
    output_list.append(output_dict)
    print(output_dict)
    output_dict = {}

def crit_skill():
    output_dict = {}
    base_name = "l"
    output_dict["name"] = "critical_shot"
    for i in range(1,25+1):
        level_name = base_name + str(i) + "chance"
        if i == 1:
            output_dict[level_name] = 0.04
        else:
            output_dict[level_name] = 0.04 + (0.005*(i-1))
    for i in range(1,25+1):
        level_name = base_name + str(i) + "damage"
        if i == 1:
            output_dict[level_name] = 0.05
        else:
            output_dict[level_name] = 0.05 + (0.04*(i-1))
    output_list.append(output_dict)
    print(output_dict)
    output_dict = {}

def adrenaline():
    output_dict = {}
    base_name = "l"
    output_dict["name"] = "adrenaline"
    for i in range(1,25+1):
        level_name = base_name + str(i)
        output_dict[level_name] = 1-0.75*0.98**(i-1)
    output_list.append(output_dict)
    print(output_dict)
    output_dict = {}

def killing_spree():
    output_dict = {}
    base_name = "l"
    output_dict["name"] = "killing_spree"
    for i in range(1,25+1):
        level_name = base_name + str(i)
        output_dict[level_name] = 0.3 + 0.05*(i-1)
    output_list.append(output_dict)
    print(output_dict)
    output_dict = {}
    
def deadly_force():
    output_dict = {}
    base_name = "l"
    output_dict["name"] = "deadly_force"
    for i in range(1,25+1):
        level_name = base_name + str(i)
        output_dict[level_name] = 0.01*(i)
    output_list.append(output_dict)
    print(output_dict)
    output_dict = {}

def htl():
    output_dict = {}
    base_name = "l"
    output_dict["name"] = "hold_the_line"
    for i in range(1,25+1):
        level_name = base_name + str(i)
        output_dict[level_name] = 0.3 + 0.04*(i-1)
    output_list.append(output_dict)
    print(output_dict)
    output_dict = {}

def heavy_gear():
    output_dict = {}
    base_name = "l"
    output_dict["name"] = "heavy_gear"
    for i in range(1,25+1):
        level_name = base_name + str(i)
        output_dict[level_name] = 0.1 + 0.0375*(i-1)
    output_list.append(output_dict)
    print(output_dict)
    output_dict = {}

def bcb():
    output_dict = {}
    base_name = "l"
    output_dict["name"] = "biocleanse_bomb"
    for i in range(1,25+1):
        level_name = base_name + str(i)
        output_dict[level_name] = 0.5
    output_list.append(output_dict)
    print(output_dict)
    output_dict = {}

reload_skill()
crit_skill()
adrenaline()
killing_spree()
deadly_force()
htl()
heavy_gear()
bcb()

print(output_list)

json.dump(output_list,skill_data,indent=4)