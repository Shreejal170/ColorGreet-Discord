# ColorGreet
ColorGreet is a Discord bot that welcomes new members with a dynamic LED effect. It requires some initial setup in the config.json file. The bot ensures a lively, colorful welcome while preventing misuse of the LED effect feature. Enjoy the vibrant welcomes with ColorGreet

Read this before using the bot.

----------------------------------------------------------->
Here are certain things that you need to configure

If you haven't install discord py module:
Go to terminal and execute this following command
pip install discord

---------------Then---------------->

1. Open config.json file then replace
   -> Replace your server id in guild
   -> Replace your welcome channel's id in welcome_channel
   -> Replace your rules channel's id in rules_channel

2. Make sure that the bot's role is above member and welcome role. It will throw an error saying missing permission if the bot's role is below.

3. Please don't remove join.txt file. It is important because it checks if the member is new or had already joined. It will prevent users from misusing the led effect feautre by rejoining again and again.

4. Don't forget to add your bot's token.

5. For preview please have a look at the .gif image.
