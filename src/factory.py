class Client:
    prefix = 'db_'
    dbs = {}


def make_client(raw_client, database):
    key = "%s%s" % (Client.prefix, database)
    if database not in Client.dbs:
        client = getattr(raw_client(), database)
        Client.dbs[key] = client
    return Client.dbs[key] 
