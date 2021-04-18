url = 'https://staging.replit.com/graphql'
body = {'query': 'query UserData { userByUsername(username: "headiscoding") { id, username, bio, karma, posts{ items{ title, voteCount} } } }'}
headers = {'X-Requested-With': 'RayhanADev', 'Referrer': 'https://staging.replit.com/' }

def getuserbody(username):
    return {'query': f'query UserData {{ userByUsername(username: "{username}") {{ id, username, bio, karma, posts{{ items{{ title, voteCount, url, board {{ name }} }} }}, publicRepls{{ items {{ language, title, url }} }} }} }}'}

#res = requests.post(url, data=body, headers=headers)
#print(res.text)