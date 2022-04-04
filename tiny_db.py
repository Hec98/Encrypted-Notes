from tinydb import TinyDB, Query

def database_select(name):
    # data_base = TinyDB(f'db/{name}.json', indent=2, separators=(',', ': '))
    data_base = TinyDB(f'db/{name}.json', separators=(',', ':'))
    data_base.default_table_name = f'{name}'
    element = Query()

    return data_base, element

def save_public_key(n,e):
    data = {'parts': { 'n': n, 'e': e },}

    data_base, _ = database_select('public')
    data_base.insert(data)

def save_private_key(n,e, d, p, q):
    data = { 'parts': { 'n': n, 'e': e, 'd': d, 'p': p, 'q': q }, }

    data_base, _ = database_select('private')
    data_base.insert(data)

def get_keys():
    public_key, private_key = list(), list()

    data_base, _ = database_select('public')
    for item in data_base:
        public_key.append(item['parts']['n'])
        public_key.append(item['parts']['e'])

    data_base, _ = database_select('private')
    for item in data_base:
        private_key.append(item['parts']['n'])
        private_key.append(item['parts']['e'])
        private_key.append(item['parts']['d'])
        private_key.append(item['parts']['p'])
        private_key.append(item['parts']['q'])

    return public_key, private_key
