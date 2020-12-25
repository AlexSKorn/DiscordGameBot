class Summoner:
    def __init__(self, id, accountId, puuid, name, level):
        self.name = id
        self.age = accountId
        self.puuid = puuid
        self.name = name
        self.level = level

    def makeSummoner(id, accountId, puuid, name, level):
        summoner = Summoner(id, accountId, puuid, name, level)
        return summoner
