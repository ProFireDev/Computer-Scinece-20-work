 

#/bin/python3.8
'''
Dislog.py
Script to log all discord messages the user(s) have access to.
'''
import discord
import asyncio
import time
from datetime import datetime
from videoAscii import video2ascii, progress_bar

CHANNEL_ID = 204621105720328193
VIDEO_PATH = 'BadApple.mp4'

TOKENS = [
    
]

class discordPlayer:
    def __init__(self, accounts):
        self.accounts = accounts
        self.frame_rate = len(accounts)#one message per account per second
        print(f'Using framerate {self.frame_rate}.')
        print('-Loading video frames as ascii.')
        self.ascii_frames = video2ascii(VIDEO_PATH, frame_size=[57,32], frame_rate=self.frame_rate, ascii_chars=['⬜', '🔲', '⚫', '⬛'])
        print('Done')
    async def run(self):
        def check_ready(accounts):
            for acc in accounts:
                if not acc.ready:
                    return False
            return True
        while True:
            if check_ready(self.accounts):
                break
            else:
                await asyncio.sleep(1)
        await self.play()
    
    async def play(self):
        frame_count = len(self.ascii_frames)
        delay = 1/self.frame_rate
        frame_index = 0
        last_frame = time.time()
        while frame_index < frame_count:
            for acc in self.accounts:
                if frame_index >= len(self.ascii_frames):
                    break

                await acc.send_frame(self.ascii_frames[frame_index])

                progress_bar(frame_index+1, frame_count)

                frame_index += 1
                t = last_frame
                last_frame = time.time()

                #print(f'waiting {delay-(last_frame-t)} seconds')
                await asyncio.sleep(delay-(last_frame-t))
                

class DiscordUser:
    '''
    A new instance of this class is created for every token.
    '''
    def __init__(self, token):
        self.ready = False
        intents=discord.Intents.default()
        #intents.members = True
        self.client = discord.Client(intents=intents)
        self.token = token
        self.client.on_ready = self.client.event(self.on_ready)

    async def run(self):
        try:
            await self.client.start(self.token, bot=False)
        except discord.errors.LoginFailure:
            print(f"Account with token:\n{self.token}\n is unable to login.")
            exit()

    async def on_ready(self):
        self.channel = self.client.get_channel(CHANNEL_ID)
        self.ready = True
        print(f'Logged in as bot {self.client.user.name}')
        return
    
    async def send_frame(self, frame):
        try:
            await self.channel.send(f'```{frame}```')
        except Exception:
            pass
        return
        

#start
print("Starting:")
loop = asyncio.get_event_loop()

tasks = []
accounts = []

#login accounts
for token in TOKENS:
    user = DiscordUser(token)
    tasks.append(loop.create_task(user.run()))
    accounts.append(user)
#run discordPlayer
player = discordPlayer(accounts)
tasks.append(loop.create_task(player.run()))

print("-Running threads")
gathered = asyncio.gather(*tasks, loop=loop)
loop.run_until_complete(gathered)
