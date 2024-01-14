# ColorGreet Discord Bot

## Introduction

ColorGreet is a Discord bot designed to provide a vibrant and dynamic welcome experience for new members joining your server. The bot implements a dynamic LED effect using role colors, creating an eye-catching and lively welcome. ColorGreet also includes features to prevent misuse and repeated welcomes.

## Features

- **Dynamic LED Effect**: ColorGreet assigns a special "Welcome" role to new members, creating a dynamic LED effect by changing the role's color multiple times before removing it.

- **Preventing Misuse**: The bot keeps track of member IDs in a file (`join.txt`) to prevent users from abusing the welcome feature by joining multiple times.

- **Customizable Configuration**: Server-specific settings, including the guild ID, welcome channel ID, and rules channel ID, can be configured in the `config.json` file.

## Setup

1. **Token Configuration**: Replace `'Your token goes here'` in the last line of the code with your Discord bot token.

2. **Configuration File (`config.json`)**:
   - Customize server-specific settings such as the guild ID, welcome channel ID, and rules channel ID in the `config.json` file.

3. **Role Creation**:
   - If the "Welcome" role does not exist, ColorGreet will attempt to create it. Ensure the bot has the necessary permissions to create roles.

4. **Dependencies Installation**:
   - Install the required dependencies using the following command:
     ```bash
     pip install discord.py
     ```

5. **Run the Bot**:
   - Execute the script to run ColorGreet. Example:
     ```bash
     python colorgreet_bot.py
     ```

## Configuration File (`config.json`)

The `config.json` file contains server-specific configuration details. Customize this file according to your server's needs.

```json
{
  "guild": 123456789012345678,        // Your server's ID
  "welcome_channel": 123456789012345, // ID of the welcome channel
  "rules_channel": 123456789012345    // ID of the rules channel
}
```

## Important Notes

- Ensure the bot has the necessary permissions to read messages, send messages, manage roles, and manage channels.

- Customize the welcoming message, LED effect, and role names to match your server's theme and preferences.

## Enjoy Colorful Welcomes with ColorGreet!

ColorGreet is ready to bring lively welcomes to your server. Feel free to modify and enhance the bot to suit your unique Discord community. For additional guidance or feature requests, refer to the [Discord.py documentation](https://discordpy.readthedocs.io/).
