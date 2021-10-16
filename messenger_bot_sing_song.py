from fbchat import Client
from fbchat.models import Message

sentence = 'Been working so hard I'm punching my card Eight hours, for what? Oh, tell me what I got I gotten this feeling That time's just holding me down I'll hit the ceiling Or else I'll tear up this town Tonight I gotta cut loose, footloose Kick off your Sunday shoes Please, Louise Pull me up off my knees Jack, get back C'mon, before we crack Lose your blues Everybody cut footloose You're playing so cool Obeying every rule Dig way down in your heart You're burning, yearning for some Somebody to tell you That life ain't passing you by I'm trying to tell you It will if you don't even try You can fly if you'd only cut loose, footloose Kick off your Sunday shoes Ooh-wee, Marie Shake it, shake it for me Whoa, Milo C'mon, c'mon let's go Lose your blues Everybody cut footloose'
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


    


