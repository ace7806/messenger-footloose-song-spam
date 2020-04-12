from fbchat import Client
from fbchat.models import Message

sentence = "This is for Rachel you big fat white nasty smelling fat bitch why you took me off the motherfuckin schedule with your trifflin dirty white racist ass you big fat bitch oompa loompa body ass bitch I'm coming up there and I'm gonna beat the f*ck out of you bitch and don't even call the police today cause I'm gonna come up there unexpected and wait on your motherfuckin ass bitch im coming to beat the f*ck out of you bitch cause you did that on purpose with your aundry racist white ass thin haired bitch watch I'm coming up there to f*ck you up bitch I'm telling you watch I know what kind of car you drive I'm gonna wait on you and I'm gonna beat your ass bitch cause Imma show you not to play with Jasmine Collin's money bitch thats the first thing you did and you got me fucked up cause bitch I told you what the f*ck was going on you white mother fuckers hate to see black people doing good or doing good or doing anything for them motherfuckin selves ugly fat white bitch watch I'm telling you I'm coming up there to beat your mother fucking ass thin haired smelling white dog smelling ass bitch watch I'm coming to f*ck you up cause you got me fucked up gonna sit up there and try to do that little aundry was shit bitch you aundry since the first day I came up there talking about a bitch that had on pajamas but you walking around here in some ten dollar ass jeans on dirty dusty white bitch sit up there behind that counter smelling like cheese bitch stinky fat white ass bitch and you gonna try to not answer this phone I'm coming to f*ck you up I'm telling you you better remember who I am cause bitch you gonna run when you see me cause I'm coming to f*ck you up bitch wanna sit up and play me about my motherfuckin money wanna play about my motherfuckin money bitch you gonna sit up there and try to do that bitch little do you know little do you know I know enough people watch I'm coming to f*ck you up I'm promise you that i promise you I'm coming to f*ck you up you fat stinky white bitch thin haired yellow yuck mouth nasty mouth ass bitch you stink you smell like fucking cheese and you got that trifflin ass attitude Imma beat that attitude up out you bitch watch you treat everybody like that all these old black people that you do like that you in the wrong position you trifflin ass racist ass white bitch thats why don't nobody f*ck with you cause you trifflin and you racist bitch sit up there and did all this shit and I told you what the f*ck was going on gonna tell me that I worked at that motherfuckin job when I'm telling you the f*ck I didn't bitch why the f*ck would I lie about some shit like that watch I finna come there and beat your motherfuckin ass you better not get out that car bitch I'm telling you fucking-﻿"
sentence = sentence.split(' ')

username = "facebook account"
password = "password"
# login
client = Client(username, password)
personToSpam = 'friendsName'
#just making sure
if not client.isLoggedIn():
    client.login(username, password)


print('fetching most recent users u talked too...')
users = client.fetchThreadList()
detailed_users = [ list(client.fetchThreadInfo(user.uid).values())[0] for user in users ]

#sorting them by message count
sorted_detailed_users = sorted(detailed_users, key=lambda u: u.message_count, reverse=True)

print('looking for',personToSpam)
for friend in sorted_detailed_users:
    if personToSpam in friend.name :
        personToSpam = friend
        break

print('sending aannoying spam to:',personToSpam.name)
for word in sentence:
    client.send(Message(text=word),thread_id=personToSpam.uid)


    


