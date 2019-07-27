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
