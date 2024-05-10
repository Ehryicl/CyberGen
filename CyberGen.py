try:
    import os, json, random, asyncio, aiofiles, maskpass, aiohttp
except ModuleNotFoundError:
    [os.system(f'pip install {package}') for package in ['aiofiles', 'maskpass', 'aiohttp', 'brotlipy']]
config = json.load(open('cache/configuration/config.json'))
api_endpoints, success_codes = ['https://canary.discordapp.com', 'https://ptb.discordapp.com'], (200, 201, 202, 203, 204, 205, 206, 207, 208, 226)
pick_url = random.choice(api_endpoints)

class CyberGen:
    
    def __init__(self):
        self.__version__ = 1.3
        
    @staticmethod
    def Restart():
        exit = os.system('pause')
        os.system('cls')
        exit = CyberGen.Start()
        
    class Extensions:

        @staticmethod
        async def gen():
            global botid
            async with aiohttp.ClientSession() as session:
                async with session.post(f'{pick_url}/api/v9/applications',
                                headers={'method': 'POST', 'path': '/api/v9/applications',
                                        'scheme': 'https', 'accept': '*/*', 'accept-encoding': 'gzip, deflate, br',
                                        'accept-language': 'en-US,en;q=0.9',
                                        'authorization': token,
                                        'content-type': 'application/json',
                                        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
                                        'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"',
                                        'sec-fetch-dest': 'empty', 'sec-fetch-cors': 'cors',
                                        'sec-fetch-site': 'same-origin',
                                        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36'},
                                json={'name': config['bot_name']}) as resp:
                    text = await resp.text()
                    if 'retry_after' in text:
                        js = await resp.json()
                        print(f'Retrying in: {js["retry_after"]}')
                        await asyncio.sleep(js['retry_after'])
                    if resp.status in success_codes:
                        js2 = await resp.json()
                        botid = js2['id']
                        print(f'Successfully Made Bot: {botid}')
                        tokens = await aiofiles.open('cache/data/botids.txt', 'a+')
                        await tokens.write(f'{botid}\n')
                    else:
                        print(f'Error: Bot Maker: {resp.status}')
                        
        @staticmethod
        async def verify():
            async with aiohttp.ClientSession() as session:
                async with session.get(f'{pick_url}/api/v9/applications?with_team_applications=true',
                                headers={'method': 'GET',
                                        'path': f'/api/v9/applications?with_team_applications=true', 'scheme': 'https',
                                        'accept': '*/*',
                                        'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9',
                                        'authorization': token,
                                        'content-type': 'application/json',
                                        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
                                        'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"',
                                        'sec-fetch-dest': 'empty', 'sec-fetch-cors': 'cors',
                                        'sec-fetch-site': 'same-origin',
                                        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36'}) as resp:
                    data = await resp.json()
            for datapacket in data:
                id1 = datapacket['id']
                mapbotids.append(id1)
                    
        @staticmethod
        async def verified(botter: str):
            async with aiohttp.ClientSession() as session:
                async with session.post(f'{pick_url}/api/v9/applications/{botter}/bot',
                            headers={'method': 'POST',
                                    'path': f'/api/v9/applications/{botter}/bot', 'scheme': 'https', 'accept': '*/*',
                                    'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9',
                                    'authorization': token,
                                    'content-type': 'application/json',
                                    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
                                    'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"',
                                    'sec-fetch-dest': 'empty', 'sec-fetch-cors': 'cors',
                                    'sec-fetch-site': 'same-origin',
                                    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36'},
                            json={}) as resp:
                    if resp.status in success_codes:
                        print(f'Successfully Verified Bot: {botter}')
                    else:
                        print(await resp.text())
                        
        @staticmethod
        async def tokengen(botter: str):
            async with aiohttp.ClientSession() as session:
                async with session.post(f'{pick_url}/api/v9/applications/{botter}/bot/reset',
                                headers={'method': 'POST',
                                        'path': f'/api/v9/applications/{botter}/bot/reset', 'scheme': 'https',
                                        'accept': '*/*',
                                        'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9',
                                        'authorization': token,
                                        'content-type': 'application/json',
                                        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
                                        'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"',
                                        'sec-fetch-dest': 'empty', 'sec-fetch-cors': 'cors',
                                        'sec-fetch-site': 'same-origin',
                                        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36'}) as resp:
                    js = await resp.json()
                    bottoken = js['token']
                    if resp.status in success_codes:
                        print(f'Successfully Generated Bot Token: {bottoken} | For: {botter}')
                        tokens = await aiofiles.open('cache/data/tokens.txt', 'a+')
                        await tokens.write(f'{bottoken}\n')
                    text = await resp.text()
                    if 'retry_after' in text:
                        js = await resp.json()
                        print(f'Retrying in: {js["retry_after"]}')
                        await asyncio.sleep(js['retry_after'])

        @staticmethod
        async def botinvites():
            async with aiohttp.ClientSession() as session:
                async with session.get(f'{pick_url}/api/v9/applications?with_team_applications=true',
                                headers={'method': 'GET',
                                        'path': f'/api/v9/applications?with_team_applications=true', 'scheme': 'https',
                                        'accept': '*/*',
                                        'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9',
                                        'authorization': token,
                                        'content-type': 'application/json',
                                        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
                                        'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"',
                                        'sec-fetch-dest': 'empty', 'sec-fetch-cors': 'cors',
                                        'sec-fetch-site': 'same-origin',
                                        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36'}) as resp:
                    data = await resp.json()
                    for datapacket in data:
                        id1 = datapacket['id']
                        mapbotids.append(id1)
                        mapbotids4.write(f'https://discord.com/api/oauth2/authorize?client_id={id1}&permissions=8&scope=bot\n')
                    for botter in mapbotids:
                        print(f'Generated Invite For Bot: {botter}: https://discord.com/api/oauth2/authorize?client_id={botter}&permissions=8&scope=bot')
        
        @staticmethod
        async def getalltokens():
            global reset
            async with aiohttp.ClientSession() as session:
                async with session.get(f'{pick_url}/api/v9/applications?with_team_applications=true',
                                headers={'method': 'GET',
                                        'path': f'/api/v9/applications?with_team_applications=true', 'scheme': 'https',
                                        'accept': '*/*',
                                        'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9',
                                        'authorization': token,
                                        'content-type': 'application/json',
                                        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
                                        'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"',
                                        'sec-fetch-dest': 'empty', 'sec-fetch-cors': 'cors',
                                        'sec-fetch-site': 'same-origin',
                                        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36'}) as resp:        
                    data = await resp.json()
                    for datapacket in data:
                        id1 = datapacket['id']
                        ids.append(id1)
                        mapbotinvitetxt = await aiofiles.open('cache/data/botinvites.txt', 'a+')
                        mapbotinvitetxt.write(f'https://discord.com/api/oauth2/authorize?client_id={id1}&permissions=8&scope=bot\n')
                        async def reset(botter: str):
                            async with aiohttp.ClientSession() as session:
                                async with session.post(f'{pick_url}/api/v9/applications/{botter}/bot/reset',
                                            headers={'method': 'POST',
                                                'path': f'/api/v9/applications/{botter}/bot/reset', 'scheme': 'https',
                                                'accept': '*/*',
                                                'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9',
                                                'authorization': token,
                                                'content-type': 'application/json',
                                                'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
                                                'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"',
                                                'sec-fetch-dest': 'empty', 'sec-fetch-cors': 'cors',
                                                'sec-fetch-site': 'same-origin',
                                                'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36'}) as resp:
                                    if resp.status in success_codes:
                                        js = await resp.json()
                                        bottoken2 = js['token']
                                        print(f'Successfully Generated Bot Token: {bottoken2} | For: {id1}')
                                        print(f'Bot Invite: https://discord.com/api/oauth2/authorize?client_id={botter}&permissions=8&scope=bot')
                                        tokens = await aiofiles.open('cache/data/tokens.txt', 'a+')
                                        await tokens.write(f'{bottoken2}\n')
                                    text = await resp.text()
                                    if 'retry_after' in text:
                                        js = await resp.json()
                                        print(f'Retrying in: {js["retry_after"]}')
                                        await asyncio.sleep(js['retry_after'])
                                    else:
                                        print(f'Error: {resp.status}')
        @staticmethod
        async def enableintents():
            global flagger
            async with aiohttp.ClientSession() as session:
                async with session.get(f'{pick_url}/api/v9/applications?with_team_applications=true',
                                headers={'method': 'GET',
                                        'path': f'/api/v9/applications?with_team_applications=true', 'scheme': 'https',
                                        'accept': '*/*',
                                        'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9',
                                        'authorization': token,
                                        'content-type': 'application/json',
                                        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
                                        'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"',
                                        'sec-fetch-dest': 'empty', 'sec-fetch-cors': 'cors',
                                        'sec-fetch-site': 'same-origin',
                                        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36'}) as resp:
                    print(resp.status)
                    data = await resp.json()
                    for datapacket in data:
                        id1 = datapacket['id']
                        ids.append(id1)
                        
            async def flagger(botter: str):
                async with aiohttp.ClientSession() as session2:
                    async with session2.patch(f'{pick_url}/api/v9/applications/{botter}',
                                headers={'method': 'PATCH',
                                        'path': f'/api/v9/applications/{botter}', 'scheme': 'https',
                                        'accept': '*/*',
                                        'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9',
                                        'authorization': token,
                                        'content-type': 'application/json',
                                        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
                                        'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"',
                                        'sec-fetch-dest': 'empty', 'sec-fetch-cors': 'cors',
                                        'sec-fetch-site': 'same-origin',
                                        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36'},
                                json={'bot_public': True, 'bot_require_code_grant': False, 'flags': '565248'}) as resp:
                        if resp.status in success_codes:
                            print(f'Successfully Changed Bot Intents For: {botter} To Flags: 565248')
                        text = await resp.text()
                        if 'retry_after' in text:
                            js = await resp.json()
                            print(f'Retrying in: {js["retry_after"]}')
                            await asyncio.sleep(js['retry_after'])

        @staticmethod
        async def verification():
            global verifybots
            async with aiohttp.ClientSession() as session:
                async with session.get(f'{pick_url}/api/v9/applications?with_team_applications=true',
                                headers={'method': 'GET',
                                        'path': f'/api/v9/applications?with_team_applications=true', 'scheme': 'https',
                                        'accept': '*/*',
                                        'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9',
                                        'authorization': token,
                                        'content-type': 'application/json',
                                        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
                                        'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"',
                                        'sec-fetch-dest': 'empty', 'sec-fetch-cors': 'cors',
                                        'sec-fetch-site': 'same-origin',
                                        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36'}) as resp:
                    data = await resp.json()
                    for datapacket in data:
                        izo2 = datapacket['id']
                        mapped.append(izo2)     
            async def verifybots(botter: str):
                async with aiohttp.ClientSession() as session:
                    async with session.post(f'{pick_url}/api/v9/applications/{botter}/bot',
                                headers={'method': 'POST',
                                        'path': f'/api/v9/applications/{botter}/bot', 'scheme': 'https', 'accept': '*/*',
                                        'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9',
                                        'authorization': token,
                                        'content-type': 'application/json',
                                        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
                                        'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"',
                                        'sec-fetch-dest': 'empty', 'sec-fetch-cors': 'cors',
                                        'sec-fetch-site': 'same-origin',
                                        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36'},
                                json={}) as resp:
                        text = await resp.text()
                        if'retry_after' in text:
                            js = await resp.json()
                            print(f'Retrying in: {js["retry_after"]}')
                            await asyncio.sleep(js['retry_after'])
                        if resp.status in success_codes:
                            print(f'Successfully Verified Bot: {botter}')
                        else:
                            print(f'Error: Status Codes: {resp.status}')
    
    @staticmethod
    async def Start():
        print('''
Choice 1: Create, Verify, Gen Tokens For Bots, 
Choice 2: Check If All Tokens In tokens.txt Is Valid, 
Choice 3: Get All Bot Invites
Choice 4: Get All Tokens Of Bots In Applications
Choice 5: Enable Intents On All Bots
Choice 6: Verify All Bots
Credits: Made by Ellisians\n''')
        choice = input(f'Choice: ')

        if choice == "1":
            global mapbotids, token, amount
            mapbotids = []
            token = maskpass.askpass(prompt='token: ', mask='•')
            amount = int(input(f'amount: '))
            await asyncio.gather(*(CyberGen.Extensions.gen() for _ in range(amount)))
            await CyberGen.Extensions.verify()
            await asyncio.gather(*(CyberGen.Extensions.verified(botter) for botter in mapbotids))
            await asyncio.gather(*(CyberGen.Extensions.tokengen(botter) for botter in mapbotids))
            input(f'Finished Press any button to Restart the Program...')
            CyberGen.Restart()
            
        if choice == "2":
            tokens = open('cache/data/tokens.txt').read().splitlines()
            async def check(token):
                async with aiohttp.ClientSession() as session:
                    async with session.get(f'{pick_url}/api/v9/users/@me',
                                        headers={'Authorization': f'Bot {token}'}) as check:
                        if check.status == 200:
                            print(f'{token} - VALID - {check.status} | Type: BOT\n')
                        if check.status == 401:
                            print(f'{token} - INVALID - {check.status}\n')
            await asyncio.gather(*(check(token) for token in tokens))
            CyberGen.Restart()

        if choice == "3":
            global mapbotids4
            token = maskpass.askpass(prompt='token: ', mask='•')
            mapbotids = []
            mapbotids4 = open('cache/data/botinvites.txt', 'a+')
            await CyberGen.Extensions.botinvites()
            CyberGen.Restart()

        if choice == "4":
            global ids
            ids = []
            token = maskpass.askpass(prompt='token: ', mask='•')
            await CyberGen.Extensions.getalltokens()
            await asyncio.gather(*(reset(botter) for botter in ids))
            CyberGen.Restart()

        if choice == "5":
            token = maskpass.askpass(prompt='token: ', mask='•')
            ids = []
            await CyberGen.Extensions.enableintents()
            await asyncio.gather(*(flagger(botter) for botter in ids))
            CyberGen.Restart()

        if choice == "6":
            global mapped
            mapped = []
            token = maskpass.askpass(prompt='token: ', mask='•')
            await CyberGen.Extensions.verification()
            await asyncio.gather(*(verifybots(botter) for botter in mapped))
            CyberGen.Restart()

if __name__ == '__main__':
    asyncio.run(CyberGen.Start())
