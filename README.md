### Download

|Version|Links|
|---|---|
|Minecraft 1.16|[Data Pack](https://github.com/tryashtar/shulker-preview/raw/1.16/Shulker%20Preview%20Data%20Pack%20(1.16).zip)<br>[Resource Pack](https://github.com/tryashtar/shulker-preview/raw/1.16/Shulker%20Preview%20Resource%20Pack%20(1.16).zip)|
|Minecraft 1.15|[Data Pack](https://github.com/tryashtar/shulker-preview/raw/1.15/Shulker%20Preview%20Data%20Pack%20(1.15).zip)<br>[Resource Pack](https://github.com/tryashtar/shulker-preview/raw/1.15/Shulker%20Preview%20Resource%20Pack%20(1.15).zip)|
|Minecraft 1.14.3|[Data Pack](https://github.com/tryashtar/shulker-preview/raw/1.14/Shulker%20Preview%20Data%20Pack%20(1.14).zip)<br>[Resource Pack](https://github.com/tryashtar/shulker-preview/raw/1.14/Shulker%20Preview%20Resource%20Pack%20(1.14).zip)|

There is also a [Faithful x32 version of the resource pack](https://github.com/FaithfulTeam/Shulker-Preview), thanks to Faithful creator [xMrVizzy](https://github.com/xMrVizzy)!

### How to use
1. Download the data pack and resource pack for your Minecraft version.
2. Select your world in-game and click `Edit`, then `Open World Folder`.
3. Drag the datapack zip from your `Downloads` folder to the `datapacks` folder in your world.
4. Go to the resource packs menu and click `Open Resource Pack Folder`.
5. Drag the resource pack zip from your `Downloads` folder to the resource packs folder.
6. Equip the resource pack.
7. Enter your world and enjoy!

### FAQ
* Does this work with Spigot/Bukkit/Paper?
   * No. These server softwares break a vanilla command behavior this pack relies on, which I cannot work around. It causes all tooltips to be blank.
* Does this work with Optifine?
   * Yes.
* Does this work with other resource packs?
   * In 1.16 and later, items in the preview will look as they do in your personal resource pack, but blocks will appear with vanilla textures.
   * In 1.15 and earlier, both items and blocks will use vanilla textures. Also, the pack may conflict with other packs that override private use characters.
* What happens if players don't have the resource pack?
   * They will see the vanilla shulker box tooltip, though it may contain a few blank lines.
* How do I disable/enable ender chest previews?
   * Disable: `/function tryashtar.shulker_preview:.meta/disable_ender`
   * Enable: `/function tryashtar.shulker_preview:.meta/enable_ender`
* It's not working for me!
   * First, please [follow these instructions](https://imgur.com/a/rBukto5) to diagnose and solve some very common issues.
   * If that didn't fix your problem, feel free to message me on twitter ([@tryashtar](https://twitter.com/tryashtar)) or discord (@tryashtar#7885) and I will be happy to help.

### Changelog
```diff
Current 1.16 version
+ All 1.16 items
+ Now uses custom font, preventing potential private use conflicts
+ Item textures use the player's current resource pack
+ Custom colored armor, potions, etc. show approximate colors
+ When ender chest previews are enabled, ender chests showing the same preview can stack

Current 1.15 version
+ All 1.15 items

Current 1.14 version
+ All 1.14 items
+ Option to preview ender chests
+ Optifine compatibility
+ Show custom item name in tooltip
+ More accurate durability bars
+ Data pack no longer requires clicking forceload text
+ Default Minecraft tooltip appears for players without the pack

Video release
+ Dropped shulker box items are processed

Initial release (reddit)
```
