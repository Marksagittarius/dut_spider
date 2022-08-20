class Actress:
    
    def __init__(self, name, nation, birthday, blood_type, constellation, height, weight):
        self.name = name
        self.nation = nation
        self.birthday = birthday
        self.blood_type = blood_type
        self.constellation = constellation
        self.height = height
        self.weight = weight
        
        
class Actor(Actress):
    
    def __init__(self, name, nation, birthday, blood_type, constellation, height, weight):
        super().__init__(name, nation, birthday, blood_type, constellation, height, weight)


class AudienceFormUint:
    
    def __init__(self, date, rate1, share1, rank1, rate2, share2, rank2):
        self.date = date
        self.rate1 = rate1
        self.share1 = share1
        self.rank1 = rank1
        self.rate2 = rate2
        self.share2 = share2
        self.rank2 = rank2