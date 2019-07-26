import vk
from vk import API

access_token = "token"
session = vk.Session(access_token=access_token)
vk_api: API = vk.API(session, v='5.101')


def getMembers(group_id='lanatsummerschool'):
    members = vk_api.groups.getMembers(group_id=group_id)
    return members['items']


def getIterests(user_ids):
    interests = vk_api.users.get(user_ids=user_ids, fields=["interests", "about"])
    interests = list(filter(lambda x: "about" in x and x["about"] != "", interests))
    return interests

if __name__ == '__main__':
    members = getMembers()
    interests = getIterests(members)
