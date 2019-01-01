def include(file):
   if not file.endswith(".png"):
      return False
   if file == "clock_00.png":
      return True
   if file.startswith("clock_"):
      return False
   if file == "compass_00.png":
      return True
   if file.startswith("compass_"):
      return False
   if file.startswith("bow_pulling_"):
      return False
   if file == "crossbow_standby.png":
      return True
   if file.startswith("crossbow_"):
      return False
   if file.startswith("empty_armor_slot"):
      return False
   if "overlay" in file:
      return False
   if file == "fishing_rod_cast.png":
      return False
   if file == "tipped_arrow_head.png":
      return False
   if file == "broken_elytra.png":
      return False
   if file == "filled_map_markings.png":
      return False
   if file == "ruby.png":
      return False
   if file == "tipped_arrow_base.png":
      return False
   if file == "spawn_egg.png":
      return False
   return True

def item_name(file):
   if file == "clock_00.png":
      return "clock"
   if file == "compass_00.png":
      return "compass"
   if file == "crossbow_standby.png":
      return "crossbow"
   return os.path.splitext(file)[0]

items_path = "D:\\Minecraft\\Java Storage\\Game History\\jar\\assets\\minecraft\\textures\\item"
items_path2 = "..\\extra item images"
overlay_path = "..\\extra item images\\overlay"
blocks_path = "..\\block images"

def get_preferred_source(file):
   if file in os.listdir(items_path2):
      return os.path.join(items_path2, item)
   elif file in os.listdir(items_path):
      return os.path.join(items_path, item)
   elif file in os.listdir(overlay_path):
      return os.path.join(overlay_path, item)

def get_number_translation(number, row):
   digits = [int(d) for d in str(number)]
   if len(digits) == 1:
      return "\\uF807" +get_digit_char(digits[0],row)+ "\\uF806"
   return "\\uF808\\uF805" +get_digit_char(digits[0],row)+ "\\uF801" +get_digit_char(digits[1],row)+ "\\uF806"

def get_durability_translation(durability, row):
   val = 31
   val += (row*14)
   val += durability
   return "\\uF808\\uF808\\uE" +format(val,"03x").upper()+ "\\uF804"

def get_digit_char(digit, row):
   digit += 1
   digit += (row*10)
   return "\\uE" +format(digit,"03x").upper()

def minecraft_id_to_translation(mc_id):
   if mc_id == "minecraft:clock":
      return "shulker_item.item.clock"
   if mc_id == "minecraft:compass":
      return "shulker_item.item.compass"
   if mc_id == "minecraft:crossbow":
      return "shulker_item.item.crossbow"
   stripped = mc_id[len("minecraft:"):]
   if stripped+".png" in blocks:
      return "shulker_item.block." +stripped
   if stripped+".png" in items:
      return "shulker_item.item." +stripped

import os
import math
from PIL import Image

# get all item PNGs from minecraft files
items = []
blocks = []
overlays = []
all_items = []
for file in os.listdir(items_path):
    if include(file):
      items.append(file)
      all_items.append(file)
for file in os.listdir(items_path2):
    if include(file) and file not in items:
      items.append(file)
      all_items.append(file)
for file in os.listdir(blocks_path):
    if include(file):
      blocks.append(file)
      all_items.append(file)
for file in os.listdir(overlay_path):
   overlays.append(file)

# create spritesheets
item_sprites = items.copy()
for file in overlays:
   item_sprites.append(file)
size = 16*math.ceil(math.sqrt(len(item_sprites)))
itemgrid = []
itemrow = []
x = 0
y = 0
with Image.new("RGBA", (size, size-16)) as sheet:
   for item in item_sprites:
      image_path = get_preferred_source(item)
      with Image.open(image_path).convert("RGBA") as sprite:
         pixels = sprite.load()
         r,g,b,a = pixels[0,0]
         a = max(a,1)
         pixels[0,0] = (r,g,b,a)
         r,g,b,a = pixels[15,15]
         a = max(a,1)
         pixels[15,15] = (r,g,b,a)
         sheet.paste(sprite, (x, y, x+16, y+16))
      x += 16
      itemrow.append(item)
      if x >= size:
         x = 0
         y += 16
         itemgrid.append(itemrow.copy())
         itemrow = []
   while len(itemrow) < len(itemgrid[0]):
      itemrow.append("")
   itemgrid.append(itemrow.copy())
   sheet.save("resourcepack\\assets\\shulker_item\\textures\\item_sheet.png", "PNG")

size = 64*math.ceil(math.sqrt(len(blocks)))
blockgrid = []
blockrow = []
x = 0
y = 0
with Image.new("RGBA", (size, size-64)) as sheet:
   for block in blocks:
      image_path = os.path.join(blocks_path, block)
      with Image.open(image_path).convert("RGBA") as sprite:
         pixels = sprite.load()
         r,g,b,a = pixels[0,0]
         a = max(a,1)
         pixels[0,0] = (r,g,b,a)
         r,g,b,a = pixels[63,63]
         a = max(a,1)
         pixels[63,63] = (r,g,b,a)
         sheet.paste(sprite, (x, y, x+64, y+64))
      x += 64
      blockrow.append(block)
      if x >= size:
         x = 0
         y += 64
         blockgrid.append(blockrow.copy())
         blockrow = []
   while len(blockrow) < len(blockgrid[0]):
      blockrow.append("")
   blockgrid.append(blockrow.copy())
   sheet.save("resourcepack\\assets\\shulker_item\\textures\\block_sheet.png", "PNG")

# create font characters for each
with open("resourcepack\\assets\\minecraft\\font\\default.json", "w") as file:
   num = 73
   file.write("{\"providers\":[{\"type\":\"ttf\",\"file\":\"shulker_item:negative_spaces.ttf\",\"shift\":[0.0,0.0],\"size\":10.0,\"oversample\":1.0},{\"type\":\"bitmap\",\"file\":\"shulker_item:tooltip.png\",\"ascent\":23,\"height\":78,\"chars\":[\"\\uE000\"]},{\"type\":\"bitmap\",\"file\":\"shulker_item:numbers.png\",\"ascent\":-4,\"height\":8,\"chars\":[\"\\uE001\\uE002\\uE003\\uE004\\uE005\\uE006\\uE007\\uE008\\uE009\\uE00A\"]},{\"type\":\"bitmap\",\"file\":\"shulker_item:numbers.png\",\"ascent\":-22,\"height\":8,\"chars\":[\"\\uE00B\\uE00C\\uE00D\\uE00E\\uE00F\\uE010\\uE011\\uE012\\uE013\\uE014\"]},{\"type\":\"bitmap\",\"file\":\"shulker_item:numbers.png\",\"ascent\":-40,\"height\":8,\"chars\":[\"\\uE015\\uE016\\uE017\\uE018\\uE019\\uE01A\\uE01B\\uE01C\\uE01D\\uE01E\"]},{\"type\":\"bitmap\",\"file\":\"shulker_item:durability.png\",\"ascent\":-8,\"height\":2,\"chars\":[\"\\uE01F\\uE020\\uE021\\uE022\\uE023\",\"\\uE024\\uE025\\uE026\\uE027\\uE028\",\"\\uE029\\uE02A\\uE02B\\uE02C\\uE000\"]},{\"type\":\"bitmap\",\"file\":\"shulker_item:durability.png\",\"ascent\":-26,\"height\":2,\"chars\":[\"\\uE02D\\uE02E\\uE02F\\uE030\\uE031\",\"\\uE032\\uE033\\uE034\\uE035\\uE036\",\"\\uE037\\uE038\\uE039\\uE03A\\uE000\"]},{\"type\":\"bitmap\",\"file\":\"shulker_item:durability.png\",\"ascent\":-44,\"height\":2,\"chars\":[\"\\uE03B\\uE03C\\uE03D\\uE03E\\uE03F\",\"\\uE040\\uE041\\uE042\\uE043\\uE044\",\"\\uE045\\uE046\\uE047\\uE048\\uE000\"]},")
   for i in range(0, 3):
      for thing in ["item", "block"]:
         grid = itemgrid
         if thing == "block":
            grid = blockgrid
         ascent = 5-(18*i)
         file.write("{\"type\":\"bitmap\",\"file\":\"shulker_item:" +thing+ "_sheet.png\",   \"ascent\":" +str(ascent)+ ",\"height\":16,\"chars\":[")
         last = len(grid)
         current = 0
         for row in grid:
            current += 1
            file.write("\"")
            for item in row:
               if item == "":
                  file.write("\\u0000")
               else:
                  file.write("\\uE" +format(num,"03x").upper())
                  num += 1
            file.write("\"")
            if current < last:
               file.write(",")
         file.write("]}")
         if i<2 or thing == "item":
            file.write(",")
   file.write("]}")

# create translations for each
with open("resourcepack\\assets\\minecraft\\lang\\en_us.json", "w") as file:
   num = 73
   file.write("{\"If you can see this, you still need to equip the resource pack!\":\"%s\",\"shulker_item.background\":\"\\uF820\\uF804\\uE000\\uF80C\\uF80A\\uF808\\uF801\\uF806\\uF800\",\"shulker_item.empty_slot\":\"\\uF820\\uF828\\uF824\\uF800\",\"shulker_item.row_end\":\"\\uF820\\uF80C\\uF80A\\uF806\\uF802\\uF800\",")
   for i in range(0, 3):
      for number in range(2, 65):
         file.write("\"shulker_item.number." +str(number)+ "." +str(i)+ "\":\"\\uF820" +get_number_translation(number, i)+ "\\uF800\",")
      for durability in range(0, 15):
         file.write("\"shulker_item.durability." +str(durability)+ "." +str(i)+ "\":\"\\uF820" +get_durability_translation(durability, i)+ "\\uF800\",")
      for item in items:
         file.write("\"shulker_item.item." +item_name(item)+ "." +str(i)+ "\":\"\\uF820\\uE" +format(num,"03x").upper()+ "\\uF805\\uF800\",")
         num += 1
      for overlay in overlays:
         file.write("\"shulker_item.overlay." +item_name(overlay)+ "." +str(i) +"\":\"\\uF820\\uF808\\uF808\\uF802\\uE" +format(num,"03x").upper()+ "\\uF805\\uF800\",")
         num += 1
      for block in blocks:
         file.write("\"shulker_item.block." +item_name(block)+ "." +str(i)+ "\":\"\\uF820\\uE" +format(num,"03x").upper()+ "\\uF805\\uF800\"")
         if i<2 or block != blocks[-1]:
            file.write(",")
         num += 1
   file.write("}")

# create tons of commands
durability_dict = {
   "minecraft:leather_helmet": 55,
   "minecraft:leather_chestplate": 80,
   "minecraft:leather_leggings": 75,
   "minecraft:leather_boots": 65,
   "minecraft:golden_helmet": 77,
   "minecraft:golden_chestplate": 112,
   "minecraft:golden_leggings": 105,
   "minecraft:golden_boots": 91,
   "minecraft:chainmail_helmet": 165,
   "minecraft:chainmail_chestplate": 240,
   "minecraft:chainmail_leggings": 225,
   "minecraft:chainmail_boots": 195,
   "minecraft:iron_helmet": 165,
   "minecraft:iron_chestplate": 240,
   "minecraft:iron_leggings": 225,
   "minecraft:iron_boots": 195,
   "minecraft:diamond_helmet": 363,
   "minecraft:diamond_chestplate": 528,
   "minecraft:diamond_leggings": 495,
   "minecraft:diamond_boots": 429,
   "minecraft:golden_axe": 32,
   "minecraft:golden_pickaxe": 32,
   "minecraft:golden_shovel": 32,
   "minecraft:golden_hoe": 32,
   "minecraft:golden_sword": 32,
   "minecraft:wooden_axe": 59,
   "minecraft:wooden_pickaxe": 59,
   "minecraft:wooden_shovel": 59,
   "minecraft:wooden_hoe": 59,
   "minecraft:wooden_sword": 59,
   "minecraft:stone_axe": 131,
   "minecraft:stone_pickaxe": 131,
   "minecraft:stone_shovel": 131,
   "minecraft:stone_hoe": 131,
   "minecraft:stone_sword": 131,
   "minecraft:iron_axe": 250,
   "minecraft:iron_pickaxe": 250,
   "minecraft:iron_shovel": 250,
   "minecraft:iron_hoe": 250,
   "minecraft:iron_sword": 250,
   "minecraft:diamond_axe": 1561,
   "minecraft:diamond_pickaxe": 1561,
   "minecraft:diamond_shovel": 1561,
   "minecraft:diamond_hoe": 1561,
   "minecraft:diamond_sword": 1561,
   "minecraft:fishing_rod": 64,
   "minecraft:flint_and_steel": 64,
   "minecraft:carrot_on_a_stick": 25,
   "minecraft:shears": 238,
   "minecraft:shield": 336,
   "minecraft:bow": 384,
   "minecraft:trident": 250,
   "minecraft:elytra": 432,
   "minecraft:crossbow": 326
}
potion_dict = {
   "minecraft:night_vision": "shulker_item.overlay.potion_liquid.night_vision",
   "minecraft:long_night_vision": "shulker_item.overlay.potion_liquid.night_vision",
   "minecraft:invisibility": "shulker_item.overlay.potion_liquid.invisibility",
   "minecraft:long_invisibility": "shulker_item.overlay.potion_liquid.invisibility",
   "minecraft:leaping": "shulker_item.overlay.potion_liquid.leaping",
   "minecraft:strong_leaping": "shulker_item.overlay.potion_liquid.leaping",
   "minecraft:long_leaping": "shulker_item.overlay.potion_liquid.leaping",
   "minecraft:fire_resistance": "shulker_item.overlay.potion_liquid.fire_resistance",
   "minecraft:long_fire_resistance": "shulker_item.overlay.potion_liquid.fire_resistance",
   "minecraft:swiftness": "shulker_item.overlay.potion_liquid.swiftness",
   "minecraft:strong_swiftness": "shulker_item.overlay.potion_liquid.swiftness",
   "minecraft:long_swiftness": "shulker_item.overlay.potion_liquid.swiftness",
   "minecraft:water_breathing": "shulker_item.overlay.potion_liquid.water_breathing",
   "minecraft:long_water_breathing": "shulker_item.overlay.potion_liquid.water_breathing",
   "minecraft:healing": "shulker_item.overlay.potion_liquid.healing",
   "minecraft:strong_healing": "shulker_item.overlay.potion_liquid.healing",
   "minecraft:harming": "shulker_item.overlay.potion_liquid.harming",
   "minecraft:strong_harming": "shulker_item.overlay.potion_liquid.harming",
   "minecraft:poison": "shulker_item.overlay.potion_liquid.poison",
   "minecraft:strong_poison": "shulker_item.overlay.potion_liquid.poison",
   "minecraft:long_poison": "shulker_item.overlay.potion_liquid.poison",
   "minecraft:regeneration": "shulker_item.overlay.potion_liquid.regeneration",
   "minecraft:strong_regeneration": "shulker_item.overlay.potion_liquid.regeneration",
   "minecraft:long_regeneration": "shulker_item.overlay.potion_liquid.regeneration",
   "minecraft:strength": "shulker_item.overlay.potion_liquid.strength",
   "minecraft:strong_strength": "shulker_item.overlay.potion_liquid.strength",
   "minecraft:long_strength": "shulker_item.overlay.potion_liquid.strength",
   "minecraft:weakness": "shulker_item.overlay.potion_liquid.weakness",
   "minecraft:long_weakness": "shulker_item.overlay.potion_liquid.weakness",
   "minecraft:luck": "shulker_item.overlay.potion_liquid.luck",
   "minecraft:turtle_master": "shulker_item.overlay.potion_liquid.turtle_master",
   "minecraft:strong_turtle_master": "shulker_item.overlay.potion_liquid.turtle_master",
   "minecraft:long_turtle_master": "shulker_item.overlay.potion_liquid.turtle_master",
   "minecraft:slow_falling": "shulker_item.overlay.potion_liquid.slow_falling",
   "minecraft:long_slow_falling": "shulker_item.overlay.potion_liquid.slow_falling",
}
length_dict = {}
for item in all_items:
   name = "minecraft:" +item_name(item)
   if len(name) in length_dict:
      length_dict[len(name)].append(name)
   else:
      length_dict[len(name)] = [name]

for row in range(0, 3):
   with open("datapack\\data\\shulker_item\\functions\\row_" +str(row)+ "\\process_item.mcfunction", "w") as file:
      file.write("# get the length of this item and call the appropriate function\nexecute store result score #length shulker_item run data get block ~2 1 ~ RecordItem.id\n")
      dictsort = list(length_dict.keys())
      dictsort.sort()
      for length in dictsort:
         file.write("execute if score #length shulker_item matches " +str(length)+ " run function shulker_item:row_" +str(row)+ "/process_item/length_" +str(length)+ "\n")
         with open("datapack\\data\\shulker_item\\functions\\row_" +str(row)+ "\\process_item\\length_" +str(length)+ ".mcfunction", "w") as lengthfile:
            needspot = False
            needsdur = False
            for item in length_dict[length]:
               lengthfile.write("execute if block ~2 1 ~ jukebox{RecordItem:{id:\"" +item+ "\"}} run summon area_effect_cloud ~ ~ ~ {Tags:[\"shulker_item\"],CustomName:\"{\\\"translate\\\":\\\"" +minecraft_id_to_translation(item)+ "." +str(row)+ "\\\"}\"}\n")
               if item in ("minecraft:potion", "minecraft:splash_potion", "minecraft:lingering_potion"):
                  needspot = True
               if item in durability_dict:
                  lengthfile.write("execute if block ~2 1 ~ jukebox{RecordItem:{id:\"" +item+ "\"}} run scoreboard players set #max shulker_item " +str(durability_dict[item])+ "\n")
                  needsdur = True
            if needspot:
               lengthfile.write("execute if data block ~2 1 ~ RecordItem.tag.Potion run function shulker_item:row_" +str(row)+ "/process_potion\n")
            if needsdur:
               lengthfile.write("execute store result score #durability shulker_item run data get block ~2 1 ~ RecordItem.tag.Damage\nexecute if data block ~2 1 ~ RecordItem.tag.Damage run function shulker_item:row_" +str(row)+ "/process_durability\n")
      file.write("\n# summon in count entity\nexecute store result score #count shulker_item run data get block ~2 1 ~ RecordItem.Count\nexecute if score #count shulker_item matches 2.. run function shulker_item:row_" +str(row)+ "/process_count\n")
   with open("datapack\\data\\shulker_item\\functions\\row_" +str(row)+ "\\process_count.mcfunction", "w") as file:
      file.write("# create an entity that draws item counts\n")
      for i in range(2, 65):
         file.write("execute if score #count shulker_item matches " +str(i)+ " run summon area_effect_cloud ~ ~0.1 ~ {Tags:[\"shulker_item\"],CustomName:\"{\\\"translate\\\":\\\"shulker_item.number." +str(i)+ "." +str(row)+ "\\\"}\"}\n")
   with open("datapack\\data\\shulker_item\\functions\\row_" +str(row)+ "\\process_durability.mcfunction", "w") as file:
      file.write("# create an entity that draws a durability bar\nscoreboard players operation #durability shulker_item *= #14 shulker_item\nscoreboard players operation #durability shulker_item /= #max shulker_item\n")
      for i in range(0, 14):
         file.write("execute if score #durability shulker_item matches ")
         if i == 13:
            file.write("13..")
         else:
            file.write(str(i))
         file.write(" run summon area_effect_cloud ~ ~ ~ {Tags:[\"shulker_item\"],CustomName:\"{\\\"translate\\\":\\\"shulker_item.durability." +str(i)+ "." +str(row)+ "\\\"}\"}\n")
   with open("datapack\\data\\shulker_item\\functions\\row_" +str(row)+ "\\process_potion.mcfunction", "w") as file:
      file.write("# create an entity that draws the proper potion overlay color\n")
      for potionname, translation in potion_dict.items():
         file.write("execute if block ~2 1 ~ jukebox{RecordItem:{tag:{Potion:\"" +potionname+ "\"}}} run summon area_effect_cloud ~ ~0.1 ~ {Tags:[\"shulker_item\"],CustomName:\"{\\\"translate\\\":\\\"" +translation+ "." +str(row)+ "\\\"}\"}\n")

# copy status of process_box/0
with open("datapack\\data\\shulker_item\\functions\\process_box\\0.mcfunction", "r") as file:
   text = file.read()
   for i in range(1, 27):
      with open("datapack\\data\\shulker_item\\functions\\process_box\\" +str(i)+ ".mcfunction", "w") as file2:
         file2.write(text.replace("0", str(i)))

# test all items!
import json
with open("D:\\Minecraft\\Java Storage\\Game History\\reports\\registries.json") as file:
   register = json.loads(file.read())
   mc_items = list(register["minecraft:item"]["entries"].keys())

   all_items2 = []
   for i in all_items:
      all_items2.append(item_name(i))
   mc_items2 = []
   for i in mc_items:
      mc_items2.append(i[len("minecraft:"):])
   unsupported = list(set(mc_items2) - set(all_items2))
   extra = list(set(all_items2) - set(mc_items2))
   print("Unsupported Minecraft items:")
   print(unsupported)
   print("Extra items?")
   print(extra)

   index = 0
   while index < len(mc_items):
      boxes = 0
      boxslot = 0
      command = "setblock ~ ~1 ~ chest{Items:["
      while index < len(mc_items) and len(command) < 32000:
         item = mc_items[index]
         if boxslot == 0:
            command += "{id:shulker_box,Count:1b,Slot:" +str(boxes)+ "b,tag:{BlockEntityTag:{Items:["
            boxes += 1
         command += "{id:\"" +item+ "\",Count:1b,Slot:" +str(boxslot)+ "b},"
         index += 1
         boxslot +=1
         if boxslot >= 27:
            boxslot = 0
         if boxslot == 0:
            command += "]}}},"
            if boxes >= 27:
               break
      if boxslot != 0:
         command += "]}}},"
      command += "]}"
      print(command)
