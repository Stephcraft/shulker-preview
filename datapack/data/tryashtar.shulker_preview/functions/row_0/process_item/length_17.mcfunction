execute if data storage tryashtar:shulker_preview item{id:"minecraft:barrier"} run summon area_effect_cloud ~ ~ ~ {Tags:["tryashtar.shulker_preview"],CustomName:'{"translate":"tryashtar.shulker_preview.item.barrier.0"}'}
execute if data storage tryashtar:shulker_preview item{id:"minecraft:bedrock"} run summon area_effect_cloud ~ ~ ~ {Tags:["tryashtar.shulker_preview"],CustomName:'{"translate":"tryashtar.shulker_preview.block.bedrock.0"}'}
execute if data storage tryashtar:shulker_preview item{id:"minecraft:chicken"} run summon area_effect_cloud ~ ~ ~ {Tags:["tryashtar.shulker_preview"],CustomName:'{"translate":"tryashtar.shulker_preview.item.chicken.0"}'}
execute if data storage tryashtar:shulker_preview item{id:"minecraft:compass"} run summon area_effect_cloud ~ ~ ~ {Tags:["tryashtar.shulker_preview"],CustomName:'{"translate":"tryashtar.shulker_preview.item.compass.0"}'}
execute if data storage tryashtar:shulker_preview item{id:"minecraft:conduit"} run summon area_effect_cloud ~ ~ ~ {Tags:["tryashtar.shulker_preview"],CustomName:'{"translate":"tryashtar.shulker_preview.block.conduit.0"}'}
execute if data storage tryashtar:shulker_preview item{id:"minecraft:diamond"} run summon area_effect_cloud ~ ~ ~ {Tags:["tryashtar.shulker_preview"],CustomName:'{"translate":"tryashtar.shulker_preview.item.diamond.0"}'}
execute if data storage tryashtar:shulker_preview item{id:"minecraft:diorite"} run summon area_effect_cloud ~ ~ ~ {Tags:["tryashtar.shulker_preview"],CustomName:'{"translate":"tryashtar.shulker_preview.block.diorite.0"}'}
execute if data storage tryashtar:shulker_preview item{id:"minecraft:dropper"} run summon area_effect_cloud ~ ~ ~ {Tags:["tryashtar.shulker_preview"],CustomName:'{"translate":"tryashtar.shulker_preview.block.dropper.0"}'}
execute if data storage tryashtar:shulker_preview item{id:"minecraft:emerald"} run summon area_effect_cloud ~ ~ ~ {Tags:["tryashtar.shulker_preview"],CustomName:'{"translate":"tryashtar.shulker_preview.item.emerald.0"}'}
execute if data storage tryashtar:shulker_preview item{id:"minecraft:end_rod"} run summon area_effect_cloud ~ ~ ~ {Tags:["tryashtar.shulker_preview"],CustomName:'{"translate":"tryashtar.shulker_preview.block.end_rod.0"}'}
execute if data storage tryashtar:shulker_preview item{id:"minecraft:feather"} run summon area_effect_cloud ~ ~ ~ {Tags:["tryashtar.shulker_preview"],CustomName:'{"translate":"tryashtar.shulker_preview.item.feather.0"}'}
execute if data storage tryashtar:shulker_preview item{id:"minecraft:furnace"} run summon area_effect_cloud ~ ~ ~ {Tags:["tryashtar.shulker_preview"],CustomName:'{"translate":"tryashtar.shulker_preview.block.furnace.0"}'}
execute if data storage tryashtar:shulker_preview item{id:"minecraft:granite"} run summon area_effect_cloud ~ ~ ~ {Tags:["tryashtar.shulker_preview"],CustomName:'{"translate":"tryashtar.shulker_preview.block.granite.0"}'}
execute if data storage tryashtar:shulker_preview item{id:"minecraft:ink_sac"} run summon area_effect_cloud ~ ~ ~ {Tags:["tryashtar.shulker_preview"],CustomName:'{"translate":"tryashtar.shulker_preview.item.ink_sac.0"}'}
execute if data storage tryashtar:shulker_preview item{id:"minecraft:jukebox"} run summon area_effect_cloud ~ ~ ~ {Tags:["tryashtar.shulker_preview"],CustomName:'{"translate":"tryashtar.shulker_preview.block.jukebox.0"}'}
execute if data storage tryashtar:shulker_preview item{id:"minecraft:lantern"} run summon area_effect_cloud ~ ~ ~ {Tags:["tryashtar.shulker_preview"],CustomName:'{"translate":"tryashtar.shulker_preview.item.lantern.0"}'}
execute if data storage tryashtar:shulker_preview item{id:"minecraft:leather"} run summon area_effect_cloud ~ ~ ~ {Tags:["tryashtar.shulker_preview"],CustomName:'{"translate":"tryashtar.shulker_preview.item.leather.0"}'}
execute if data storage tryashtar:shulker_preview item{id:"minecraft:lectern"} run summon area_effect_cloud ~ ~ ~ {Tags:["tryashtar.shulker_preview"],CustomName:'{"translate":"tryashtar.shulker_preview.block.lectern.0"}'}
execute if data storage tryashtar:shulker_preview item{id:"minecraft:oak_log"} run summon area_effect_cloud ~ ~ ~ {Tags:["tryashtar.shulker_preview"],CustomName:'{"translate":"tryashtar.shulker_preview.block.oak_log.0"}'}
execute if data storage tryashtar:shulker_preview item{id:"minecraft:pumpkin"} run summon area_effect_cloud ~ ~ ~ {Tags:["tryashtar.shulker_preview"],CustomName:'{"translate":"tryashtar.shulker_preview.block.pumpkin.0"}'}
execute if data storage tryashtar:shulker_preview item{id:"minecraft:red_bed"} run summon area_effect_cloud ~ ~ ~ {Tags:["tryashtar.shulker_preview"],CustomName:'{"translate":"tryashtar.shulker_preview.block.red_bed.0"}'}
execute if data storage tryashtar:shulker_preview item{id:"minecraft:red_dye"} run summon area_effect_cloud ~ ~ ~ {Tags:["tryashtar.shulker_preview"],CustomName:'{"translate":"tryashtar.shulker_preview.item.red_dye.0"}'}
execute if data storage tryashtar:shulker_preview item{id:"minecraft:spawner"} run summon area_effect_cloud ~ ~ ~ {Tags:["tryashtar.shulker_preview"],CustomName:'{"translate":"tryashtar.shulker_preview.block.spawner.0"}'}
execute if data storage tryashtar:shulker_preview item{id:"minecraft:trident"} run summon area_effect_cloud ~ ~ ~ {Tags:["tryashtar.shulker_preview"],CustomName:'{"translate":"tryashtar.shulker_preview.item.trident.0"}'}
execute if data storage tryashtar:shulker_preview item{id:"minecraft:trident"} run scoreboard players set #max shulker_preview 250
execute store result score #durability shulker_preview run data get storage tryashtar:shulker_preview item.tag.Damage
execute if data storage tryashtar:shulker_preview item.tag.Damage run function tryashtar.shulker_preview:row_0/process_durability
