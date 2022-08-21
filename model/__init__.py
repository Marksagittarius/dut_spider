class Actress:
    
    def __init__(self, name, nation, birthday, blood_type, constellation, height, weight):
        """ The data structure to describe the profile of an Actress.
        
        Args:
            @name (string):
            @nation (string):
            @birthday (string)):
            @blood_type (string):
            @constellation (string):
            @height (int):
            @weight (int):
        """
              
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
        """ The data-structure to describe the audience data of given show
        on certain date.
        
        Args:
            @date (string):
            @rate1 (double):
            @share1 (double):
            @rank1 (double):
            @rate2 (double):
            @share2 (double):
            @rank2 (double):
        """
        
        self.date = date
        self.rate1 = rate1
        self.share1 = share1
        self.rank1 = rank1
        self.rate2 = rate2
        self.share2 = share2
        self.rank2 = rank2
        
        
class EpidemicStatOfProvince():
    
    def __init__(self, province_name, current_confirmed_num, total_local_confirmed_cases, cumulative_death_toll, cumulative_cured_toll, suspected_num, high_danger_count, mid_danger_count):
        """ The data-structure to describe the epidemic data of each province in CHINA.
        
        Args:
            @province_name (string):
            @current_confirmed_num (int):
            @total_local_confirmed_cases (int):
            @cumulative_death_toll (int):
            @cumulative_cured_toll (int):
            @suspected_num (int):
            @high_danger_count (int):
            @mid_danger_count (int):
        """
              
        self.province_name = province_name
        self.current_confirmed_num = current_confirmed_num
        self.total_local_confirmed_cases = total_local_confirmed_cases
        self.cumulative_death_roll = cumulative_death_toll
        self.cumulative_cured_roll = cumulative_cured_toll
        self.suspected_num = suspected_num
        self.high_danger_count = high_danger_count
        self.mid_danger_count = mid_danger_count
