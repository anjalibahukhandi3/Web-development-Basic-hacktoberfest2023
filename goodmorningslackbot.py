import os
from slack import WebClient

# Set your Slack API token
slack_token = os.environ['SLACK_API_TOKEN']  # Make sure to set this environment variable

# Initialize the Slack client
client = WebClient(token=slack_token)

# The channel where you want to send the "Good morning" message
channel = "#general"  # Change this to the desired channel

# The "Good morning" message
message = "Good morning, everyone! :sunrise:"

# Send the message to the channel
client.chat_postMessage(channel=channel, text=message)
