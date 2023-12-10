const { Client } = require('discord.js');
const fetch = require('node-fetch');

// Discord bot token
const TOKEN = 'YOUR_DISCORD_BOT_TOKEN';

// Discord channel ID where you want to send messages
const CHANNEL_ID = 'YOUR_CHANNEL_ID'; // Replace with your channel ID

// Function to send a message to a Discord channel
async function sendDiscordMessage(message) {
  const channel = client.channels.cache.get(CHANNEL_ID);
  if (channel) {
    await channel.send(message);
  }
}

// Function to perform AUM monitoring and send a Discord message if the limit is exceeded
async function monitorAUM() {
  const client = new Client();

  client.on('ready', () => {
    console.log(`Logged in as ${client.user.tag}`);
  });

  client.login(TOKEN);

  while (true) {
    try {
      const response = await fetch('https://jup.ag/perps-earn/buy/SOL');
      const html = await response.text();

      // Use a method like cheerio to parse HTML and find AUM data
      // Replace this logic with your scraping method

      const aumLimitReached = false; // Replace this with your AUM checking logic

      if (aumLimitReached) {
        await sendDiscordMessage('AUM limit reached! New funds not accepted.');
        break;
      } else {
        console.log('AUM limit not reached. Checking again in 10 minutes...');
        await new Promise(resolve => setTimeout(resolve, 600000)); // Wait for 10 minutes
      }
    } catch (error) {
      console.error('Error:', error);
      await new Promise(resolve => setTimeout(resolve, 600000)); // Wait for 10 minutes in case of error
    }
  }
}

monitorAUM();
