# Discord Bot Project

## Description

This Discord bot is designed to read Enven checkout webhook embeds in a Discord channel and send it to [Pushover](https://pushover.net/), a popular notification service.  This project came about because I found I was constantly sharing screenshots of Enven checkouts with my wife manually.

## Framework

Python with **discord.py** for Discord bot, **http.client** for Pushover API.

## Project Structure

- **.env**: Configuration file for storing tokens and IDs.
- **.gitignore**: A file which chooses which files not to track within Git.
- **bot.py**: Main script to run the Discord bot.
- **LICENSE**: The project license.  A license tells others what they can and can't do with your code.
- **pushover.py**: Module to handle Pushover notifications.
- **README.md**: This file, which is a long description of the project.
- **requirements.txt**: Required Python packages.

## Features

- Automatically reads Enven checkout embeds and forwards them to Pushover.
- Caches the latest Embed received.
- Can recall the latest Embed received with the (`!showlast`) commands.
- Can manually read specific Embeds with the (`!readmessage [channel_id] [message_id>]`) command.

## Installation & Setup

To set up this Discord bot, follow these steps:

1. **Create a Discord Application**:

    - Go to the [Discord Developer Portal](https://discord.com/developers/applications)
    - Click **New Application**.
    - Create a name for your Bot.  
    - Check the box agreeing to Discords TOS and Developer Policy.
    - Click **Create**.

2. **Enable Privileged Gateway Intents**

    Discord has classified some intents as "privaleged" because they can potentially access sesnsitive or private user data.
    - Click **Bot** under the Settings menu.
    - Under Privileged Gateway Intents, toggle on **Message Content Intent**.

3. **Invite the Bot to your Discord server**

    - Click **OAuth2** under the Settings menu, and then click **General**.
    - Make sure **bot** and **applications.commands** are checkmarked under Scopes.
    - Make sure **Administrator** is checkmarked under Bot Permissions.
        - This is definitely not the best permission to use, but is the only one I have tested.
    - Click **URL Generator** under **OAuth2** in the Settings menu.
    - Make sure **bot** and **applications.commands** are checkmarked under Scopes.
    - Make sure **Administrator** is checkmarked under Bot Permissions.
    - Click the **Copy** button under Generated URL.
    - Open a web browser and paste the link and invite the bot to your server.
    - Go to your Discord server where your bot has been invited and give it permissions to read messages where your Enven webhooks are.

4. **Clone the Repository in Git**:

    ```text
    git clone [https://github.com/Solysh/Enven2Pushover.git]
    ```

5. **Install Dependencies**:

    - Ensure you have Python installed.
    - Install required packages:

    ```text
    pip install -r requirements.txt
    ```

6. **Environment Variables**:

    - Create a `.env` file in the root directory.
    - Add the following:

    ```text
    DISCORD_TOKEN=your_discord_token_here
    PUSHOVER_USER_KEY=your_pushover_user_key_here
    PUSHOVER_API_TOKEN=your_pushover_api_token_here
    ```

## Running the Bot

- Open your terminal or command prompt.
- Navigate to the directory where your **bot.py** file is located.
- Run the bot by executing **python bot.py**.
- If everything is set up correctly, you should see a message like "Logged in as [Bot Name]".

## Usage

(Explain how to use the bot, different commands, and functionalities.)

## Contributing

Contributions to the project are welcome! Here's how you can contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed until the GPL-3.0 License - see the LICENSE file for details.

## Contact

For support or queries, reach out to me at `me@solysh.com` or `solysh` on Discord.
