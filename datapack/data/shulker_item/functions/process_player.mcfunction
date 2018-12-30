# hotbar
data remove block ~ ~ ~ Items
data modify block ~ ~ ~ Items append from entity @s Inventory[{Slot:0b}]
data modify block ~ ~ ~ Items append from entity @s Inventory[{Slot:1b}]
data modify block ~ ~ ~ Items append from entity @s Inventory[{Slot:2b}]
data modify block ~ ~ ~ Items append from entity @s Inventory[{Slot:3b}]
data modify block ~ ~ ~ Items append from entity @s Inventory[{Slot:4b}]
data modify block ~ ~ ~ Items append from entity @s Inventory[{Slot:5b}]
data modify block ~ ~ ~ Items append from entity @s Inventory[{Slot:6b}]
data modify block ~ ~ ~ Items append from entity @s Inventory[{Slot:7b}]
data modify block ~ ~ ~ Items append from entity @s Inventory[{Slot:8b}]

execute if data block ~ ~ ~ Items[{Slot:0b,id:"minecraft:shulker_box"}] unless data block ~ ~ ~ Items[{Slot:0b,tag:{shulker_processed:1b}}] run function shulker_item:process_box/0
execute if data block ~ ~ ~ Items[{Slot:1b,id:"minecraft:shulker_box"}] unless data block ~ ~ ~ Items[{Slot:1b,tag:{shulker_processed:1b}}] run function shulker_item:process_box/1
execute if data block ~ ~ ~ Items[{Slot:2b,id:"minecraft:shulker_box"}] unless data block ~ ~ ~ Items[{Slot:2b,tag:{shulker_processed:1b}}] run function shulker_item:process_box/2
execute if data block ~ ~ ~ Items[{Slot:3b,id:"minecraft:shulker_box"}] unless data block ~ ~ ~ Items[{Slot:3b,tag:{shulker_processed:1b}}] run function shulker_item:process_box/3
execute if data block ~ ~ ~ Items[{Slot:4b,id:"minecraft:shulker_box"}] unless data block ~ ~ ~ Items[{Slot:4b,tag:{shulker_processed:1b}}] run function shulker_item:process_box/4
execute if data block ~ ~ ~ Items[{Slot:5b,id:"minecraft:shulker_box"}] unless data block ~ ~ ~ Items[{Slot:5b,tag:{shulker_processed:1b}}] run function shulker_item:process_box/5
execute if data block ~ ~ ~ Items[{Slot:6b,id:"minecraft:shulker_box"}] unless data block ~ ~ ~ Items[{Slot:6b,tag:{shulker_processed:1b}}] run function shulker_item:process_box/6
execute if data block ~ ~ ~ Items[{Slot:7b,id:"minecraft:shulker_box"}] unless data block ~ ~ ~ Items[{Slot:7b,tag:{shulker_processed:1b}}] run function shulker_item:process_box/7
execute if data block ~ ~ ~ Items[{Slot:8b,id:"minecraft:shulker_box"}] unless data block ~ ~ ~ Items[{Slot:8b,tag:{shulker_processed:1b}}] run function shulker_item:process_box/8

loot replace entity @s hotbar.0 9 mine ~ ~ ~ golden_pickaxe{drop_contents:true}


# main inventory
data merge block ~ ~ ~ {Items:[{id:tnt,Count:1b,tag:{shulker_placeholder:1b}}]}
data modify block ~ ~ ~ Items[0].tag.shulker_item set from entity @s Inventory[{Slot:35b}]
function shulker_item:shift_copy
data modify block ~ ~ ~ Items[0].tag.shulker_item set from entity @s Inventory[{Slot:34b}]
function shulker_item:shift_copy
data modify block ~ ~ ~ Items[0].tag.shulker_item set from entity @s Inventory[{Slot:33b}]
function shulker_item:shift_copy
data modify block ~ ~ ~ Items[0].tag.shulker_item set from entity @s Inventory[{Slot:32b}]
function shulker_item:shift_copy
data modify block ~ ~ ~ Items[0].tag.shulker_item set from entity @s Inventory[{Slot:31b}]
function shulker_item:shift_copy
data modify block ~ ~ ~ Items[0].tag.shulker_item set from entity @s Inventory[{Slot:30b}]
function shulker_item:shift_copy
data modify block ~ ~ ~ Items[0].tag.shulker_item set from entity @s Inventory[{Slot:29b}]
function shulker_item:shift_copy
data modify block ~ ~ ~ Items[0].tag.shulker_item set from entity @s Inventory[{Slot:28b}]
function shulker_item:shift_copy
data modify block ~ ~ ~ Items[0].tag.shulker_item set from entity @s Inventory[{Slot:27b}]
function shulker_item:shift_copy
data modify block ~ ~ ~ Items[0].tag.shulker_item set from entity @s Inventory[{Slot:26b}]
function shulker_item:shift_copy
data modify block ~ ~ ~ Items[0].tag.shulker_item set from entity @s Inventory[{Slot:25b}]
function shulker_item:shift_copy
data modify block ~ ~ ~ Items[0].tag.shulker_item set from entity @s Inventory[{Slot:24b}]
function shulker_item:shift_copy
data modify block ~ ~ ~ Items[0].tag.shulker_item set from entity @s Inventory[{Slot:23b}]
function shulker_item:shift_copy
data modify block ~ ~ ~ Items[0].tag.shulker_item set from entity @s Inventory[{Slot:22b}]
function shulker_item:shift_copy
data modify block ~ ~ ~ Items[0].tag.shulker_item set from entity @s Inventory[{Slot:21b}]
function shulker_item:shift_copy
data modify block ~ ~ ~ Items[0].tag.shulker_item set from entity @s Inventory[{Slot:20b}]
function shulker_item:shift_copy
data modify block ~ ~ ~ Items[0].tag.shulker_item set from entity @s Inventory[{Slot:19b}]
function shulker_item:shift_copy
data modify block ~ ~ ~ Items[0].tag.shulker_item set from entity @s Inventory[{Slot:18b}]
function shulker_item:shift_copy
data modify block ~ ~ ~ Items[0].tag.shulker_item set from entity @s Inventory[{Slot:17b}]
function shulker_item:shift_copy
data modify block ~ ~ ~ Items[0].tag.shulker_item set from entity @s Inventory[{Slot:16b}]
function shulker_item:shift_copy
data modify block ~ ~ ~ Items[0].tag.shulker_item set from entity @s Inventory[{Slot:15b}]
function shulker_item:shift_copy
data modify block ~ ~ ~ Items[0].tag.shulker_item set from entity @s Inventory[{Slot:14b}]
function shulker_item:shift_copy
data modify block ~ ~ ~ Items[0].tag.shulker_item set from entity @s Inventory[{Slot:13b}]
function shulker_item:shift_copy
data modify block ~ ~ ~ Items[0].tag.shulker_item set from entity @s Inventory[{Slot:12b}]
function shulker_item:shift_copy
data modify block ~ ~ ~ Items[0].tag.shulker_item set from entity @s Inventory[{Slot:11b}]
function shulker_item:shift_copy
data modify block ~ ~ ~ Items[0].tag.shulker_item set from entity @s Inventory[{Slot:10b}]
function shulker_item:shift_copy
data modify block ~ ~ ~ Items[0].tag.shulker_item set from entity @s Inventory[{Slot:9b}]
function shulker_item:shift_copy
data remove block ~ ~ ~ Items[{tag:{shulker_placeholder:1b}}]

execute if data block ~ ~ ~ Items[{Slot:9b,id:"minecraft:shulker_box"}] unless data block ~ ~ ~ Items[{Slot:9b,tag:{shulker_processed:1b}}] run function shulker_item:process_box/9
execute if data block ~ ~ ~ Items[{Slot:10b,id:"minecraft:shulker_box"}] unless data block ~ ~ ~ Items[{Slot:10b,tag:{shulker_processed:1b}}] run function shulker_item:process_box/10
execute if data block ~ ~ ~ Items[{Slot:11b,id:"minecraft:shulker_box"}] unless data block ~ ~ ~ Items[{Slot:11b,tag:{shulker_processed:1b}}] run function shulker_item:process_box/11
execute if data block ~ ~ ~ Items[{Slot:12b,id:"minecraft:shulker_box"}] unless data block ~ ~ ~ Items[{Slot:12b,tag:{shulker_processed:1b}}] run function shulker_item:process_box/12
execute if data block ~ ~ ~ Items[{Slot:13b,id:"minecraft:shulker_box"}] unless data block ~ ~ ~ Items[{Slot:13b,tag:{shulker_processed:1b}}] run function shulker_item:process_box/13
execute if data block ~ ~ ~ Items[{Slot:14b,id:"minecraft:shulker_box"}] unless data block ~ ~ ~ Items[{Slot:14b,tag:{shulker_processed:1b}}] run function shulker_item:process_box/14
execute if data block ~ ~ ~ Items[{Slot:15b,id:"minecraft:shulker_box"}] unless data block ~ ~ ~ Items[{Slot:15b,tag:{shulker_processed:1b}}] run function shulker_item:process_box/15
execute if data block ~ ~ ~ Items[{Slot:16b,id:"minecraft:shulker_box"}] unless data block ~ ~ ~ Items[{Slot:16b,tag:{shulker_processed:1b}}] run function shulker_item:process_box/16
execute if data block ~ ~ ~ Items[{Slot:17b,id:"minecraft:shulker_box"}] unless data block ~ ~ ~ Items[{Slot:17b,tag:{shulker_processed:1b}}] run function shulker_item:process_box/17
execute if data block ~ ~ ~ Items[{Slot:18b,id:"minecraft:shulker_box"}] unless data block ~ ~ ~ Items[{Slot:18b,tag:{shulker_processed:1b}}] run function shulker_item:process_box/18
execute if data block ~ ~ ~ Items[{Slot:19b,id:"minecraft:shulker_box"}] unless data block ~ ~ ~ Items[{Slot:19b,tag:{shulker_processed:1b}}] run function shulker_item:process_box/19
execute if data block ~ ~ ~ Items[{Slot:20b,id:"minecraft:shulker_box"}] unless data block ~ ~ ~ Items[{Slot:20b,tag:{shulker_processed:1b}}] run function shulker_item:process_box/20
execute if data block ~ ~ ~ Items[{Slot:21b,id:"minecraft:shulker_box"}] unless data block ~ ~ ~ Items[{Slot:21b,tag:{shulker_processed:1b}}] run function shulker_item:process_box/21
execute if data block ~ ~ ~ Items[{Slot:22b,id:"minecraft:shulker_box"}] unless data block ~ ~ ~ Items[{Slot:22b,tag:{shulker_processed:1b}}] run function shulker_item:process_box/22
execute if data block ~ ~ ~ Items[{Slot:23b,id:"minecraft:shulker_box"}] unless data block ~ ~ ~ Items[{Slot:23b,tag:{shulker_processed:1b}}] run function shulker_item:process_box/23
execute if data block ~ ~ ~ Items[{Slot:24b,id:"minecraft:shulker_box"}] unless data block ~ ~ ~ Items[{Slot:24b,tag:{shulker_processed:1b}}] run function shulker_item:process_box/24
execute if data block ~ ~ ~ Items[{Slot:25b,id:"minecraft:shulker_box"}] unless data block ~ ~ ~ Items[{Slot:25b,tag:{shulker_processed:1b}}] run function shulker_item:process_box/25
execute if data block ~ ~ ~ Items[{Slot:26b,id:"minecraft:shulker_box"}] unless data block ~ ~ ~ Items[{Slot:26b,tag:{shulker_processed:1b}}] run function shulker_item:process_box/26
execute if data block ~ ~ ~ Items[{Slot:27b,id:"minecraft:shulker_box"}] unless data block ~ ~ ~ Items[{Slot:27b,tag:{shulker_processed:1b}}] run function shulker_item:process_box/27
execute if data block ~ ~ ~ Items[{Slot:28b,id:"minecraft:shulker_box"}] unless data block ~ ~ ~ Items[{Slot:28b,tag:{shulker_processed:1b}}] run function shulker_item:process_box/28
execute if data block ~ ~ ~ Items[{Slot:29b,id:"minecraft:shulker_box"}] unless data block ~ ~ ~ Items[{Slot:29b,tag:{shulker_processed:1b}}] run function shulker_item:process_box/29
execute if data block ~ ~ ~ Items[{Slot:30b,id:"minecraft:shulker_box"}] unless data block ~ ~ ~ Items[{Slot:30b,tag:{shulker_processed:1b}}] run function shulker_item:process_box/30
execute if data block ~ ~ ~ Items[{Slot:31b,id:"minecraft:shulker_box"}] unless data block ~ ~ ~ Items[{Slot:31b,tag:{shulker_processed:1b}}] run function shulker_item:process_box/31
execute if data block ~ ~ ~ Items[{Slot:32b,id:"minecraft:shulker_box"}] unless data block ~ ~ ~ Items[{Slot:32b,tag:{shulker_processed:1b}}] run function shulker_item:process_box/32
execute if data block ~ ~ ~ Items[{Slot:33b,id:"minecraft:shulker_box"}] unless data block ~ ~ ~ Items[{Slot:33b,tag:{shulker_processed:1b}}] run function shulker_item:process_box/33
execute if data block ~ ~ ~ Items[{Slot:34b,id:"minecraft:shulker_box"}] unless data block ~ ~ ~ Items[{Slot:34b,tag:{shulker_processed:1b}}] run function shulker_item:process_box/34
execute if data block ~ ~ ~ Items[{Slot:35b,id:"minecraft:shulker_box"}] unless data block ~ ~ ~ Items[{Slot:35b,tag:{shulker_processed:1b}}] run function shulker_item:process_box/35

loot replace entity @s inventory.0 27 mine ~ ~ ~ golden_pickaxe{drop_contents:true}
