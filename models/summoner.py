class Summoner:
    def __init__(self, id, accountId, puuid, name, level):
        self.name = id
        self.age = accountId
        self.puuid = puuid
        self.name = name
        self.level = level

    def makeSummoner(self, id, accountId, puuid, name, level):
        summoner = Summoner(id, accountId, puuid, name, level)
        return summoner

    def printSummoner(self):
        print(self.id, self.accountId, self.puuid, self.name, self.level)
