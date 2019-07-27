import os
import re

import gensim as gensim
import requests
import vk
import wget as wget
from vk import API

access_token = "9128341691283416912834169e9143eb9c9912891283416cc1048fcb23dd80ee12ec85a"
session = vk.Session(access_token=access_token)
vk_api: API = vk.API(session, v='5.101')


def getMembers(group_id='lanatsummerschool'):
    members = vk_api.groups.getMembers(group_id=group_id)
    return members['items']


def getIterests(user_ids):
    interests = vk_api.users.get(user_ids=user_ids, fields=["interests", "about"])
    interests = list(filter(lambda x: "about" in x and x["about"] != "", interests))
    return interests


def api_neighbor(m, w, f):
    neighbors = {}
    url = '/'.join(['http://rusvectores.org', m, w, 'api', f]) + '/'
    r = requests.get(url=url, stream=True)
    for line in r.text.split('\n'):
        try:  # первые две строки в файле -- служебные, их мы пропустим
            word, sim = re.split('\s+', line)  # разбиваем строку по одному или более пробелам
            neighbors[word] = sim
        except:
            continue
    print(neighbors)
    return neighbors


def api_similarity(w1, w2, m='ruwikiruscorpora_upos_skipgram_300_2_2019'):
    url = '/'.join(['https://rusvectores.org', m, w1 + '__' + w2, 'api', 'similarity/'])
    r = requests.get(url, stream=True)
    return r.text.split('\t')[0]


with open("Analysis of VK group/model.bin", "rb") as stream:
    # stream = stream.read()
    model = gensim.models.KeyedVectors.load_word2vec_format(stream, binary=True)
    # print(model.vocab)



hobbylist = open("Analysis of VK group/hobbylist.txt", "rt").read().split("\n")
hobbylist = list(map(lambda x: x.lower() + "_NOUN", hobbylist))
hobbylist = list(filter(lambda x: x in model, hobbylist))
print(hobbylist)

if __name__ == '__main__':
    members = getMembers()
    interests = []
    for n in range(0, len(members), 50):
        new_interests = getIterests(members[n:n + 50])
        interests.extend(new_interests)
        print(len(new_interests), len(interests))
    w_interests = []
    w1_interests = []
    for i in interests:
        w_interests.append(i['interests'])
    for i in w_interests:
        w1_interests.append(
            re.sub('[!@#$%&^*()+=\n.\'":_1234567890/AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz]', '', i))
    w_interests = ' '.join(w1_interests)
    w_interests = w_interests.split(", ")
    w1_interests = []
    for i in w_interests:
        w1_interests += i.split(" ")
    w1_interests = list(filter(lambda x: x not in ['', '-'], w1_interests))
    for i in range(len(w1_interests)):
        w1_interests[i] = w1_interests[i].lower()
    # new_w = set(w1_interests)
    new_w = w1_interests
    print(new_w)

    new_w = list(map(lambda x: x.lower() + "_NOUN", new_w))

    word_hobbies = {}
    threshold = 0.5

    for interestword in new_w:
        nearest_word = ""
        max_similarity = 0
        if interestword not in model:
            # word_hobbies[interestword] = ""
            continue

        for hobby in hobbylist:
            sim = model.similarity(interestword, hobby)
            sim = float(sim)
            if sim > max_similarity:
                nearest_word = hobby
                max_similarity = sim
        if max_similarity < threshold:
            pass
            # word_hobbies[interestword] = ""
        else:
            if interestword in word_hobbies:
                word_hobbies[nearest_word] += interestword + ", "
            else:
                word_hobbies[nearest_word] = interestword + ", "


    print(word_hobbies)

    # interests = []
    # model = 'ruwikiruscorpora_upos_skipgram_300_2_2019'
    # rez = api_neighbor(model, 'фотография', 'csv')
