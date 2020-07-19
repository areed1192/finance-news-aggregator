from configparser import ConfigParser

# Initialize the Parser.
config = ConfigParser()

# Add the Section.
config.add_section('main')

# Set the Values.
config.set('main', 'API_KEY', '')
config.set('main', 'CHANNEL_ID', '')
config.set('main', 'PLAYLIST_ID', '')

# Write the file.
with open('configs/config.ini', 'w+') as f:
    config.write(f)
