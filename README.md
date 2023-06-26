This project was created to bridge VoiceAttack and Minecraft.

1. Set up your Minecraft server. In server.properties, set enable-rcon to true; set a password for rcon-password; ensure your firewall/ports are open.
2. Set up VoiceAttack (VA). VA recognises a verbalised command (trigger). Voice commands can have multiple words to trigger the same action by using this format: \*trigger\*;\*trigger\*
3. VA creates/writes to a text file (readfromme.txt) in this folder. The content it writes will be the (trigger)|(action). Do this by creating an action that writes `{CMD_WILDCARDKEY}|kill` to the file path of readfromme.txt in this folder. Do this for each VoiceAttack command. Check 'Overwrite file if it already exists'.
4. Create a config.py file in this folder using config_template.py and fill in the details.
5. Run `pip install -r requirements.txt` in the terminal.
6. Run txt-to-mcrcon.py
