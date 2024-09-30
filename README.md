# Discord Bot - Astronomy Facts and Daily Questions

This Discord bot automates the sending of **astronomy facts** and **daily questions** to specific channels in a server. The bot allows server administrators to configure channels, set the frequency of messages, and manage content, including optional images for embeds.

## Features

- **Custom Channel Setup**: Administrators can assign specific channels for astronomy facts or daily questions.
- **Configurable Frequency**: Set how often the bot sends messages (e.g., every 24 hours, every 12 hours).
- **Facts and Questions Modals**: Add astronomy facts or daily questions using a modal (pop-up window), with the option to include images.
- **Automated Message Sending**: Messages are sent at the configured intervals in the designated channels.
- **Discord Embed Formatting**: Facts and questions are displayed as beautiful, readable embeds in Discord.

## Commands

### `/set_channel`
- **Usage**: `/set_channel <channel_id> <fact/daily_question> <guild_id>`
- **Description**: This command sets the channel where either astronomy facts or daily questions will be sent.
- **Parameters**:
  - `channel_id`: The ID of the channel where the bot will post.
  - `fact/daily_question`: Specify if the channel is for astronomy facts or daily questions.
  - `guild_id`: The unique server (guild) ID.

### `/set_frequency`
- **Usage**: `/set_frequency <fact/daily_question> <frequency_in_hours>`
- **Description**: Set the frequency (in hours) at which the bot will send messages.
- **Parameters**:
  - `fact/daily_question`: Specify whether to set the frequency for facts or daily questions.
  - `frequency_in_hours`: Time interval between messages.

### `/add_fact`
- **Usage**: Open a modal for adding a new astronomy fact.
- **Description**: Add a new astronomy fact to the bot's database via a modal. Optionally, include an image that will be displayed with the fact.
- **Parameters**: None. A modal will open to input the fact and upload an optional image.

### `/add_question`
- **Usage**: Open a modal for adding a new daily question.
- **Description**: Add a new daily question to the bot's database via a modal. Optionally, include an image that will be displayed with the question.
- **Parameters**: None. A modal will open to input the question and upload an optional image.

## Setup

### Prerequisites

- **Python** (version 3.8 or higher)
- **pip** (Python Package Installer)
- **Discord Bot Token**: You will need a bot token from the [Discord Developer Portal](https://discord.com/developers/applications).

### Installation

1. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

2. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/yourbotname.git
   cd yourbotname
   
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   
4. Create a .env file in the root directory and add your Discord bot token:
   ```env
   DISCORD_TOKEN=your_bot_token_here
  
5. Run the bot:
   ```bash
   python3 main.py
   
## Running the Bot
Once started, the bot will listen for the commands `/set_channel`, `/set_frequency`, `/add_fact`, and `/add_question` to configure and manage its functionality.

It will automatically send astronomy facts and daily questions at the intervals you define using the `/set_frequency` command.

## Customization
You can modify the bot's behavior by updating the command handling logic inside the `src/commands` folder. The structure of embeds, frequency timing, or any additional features can be customized by altering the existing command code.

## Contributions
Feel free to open an issue or submit a pull request if you find any bugs or have suggestions for improvement.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

