from model import Actress, AudienceFormUint
import json
import os


filename_of_actress = "store/actress.json"
filename_of_actor = "store/actor.json"
filename_of_audience_form = "store/audience.json"


class custom_encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, bytes):
            return str(obj, encoding="utf-8")
        return json.JSONEncoder.default(self, obj)


def actress_to_dict(actress):
    return {
        "name": actress.name,
        "nation": actress.nation,
        "birthday": actress.birthday,
        "constellation": actress.constellation,
        "blood_type": actress.blood_type,
        "height": actress.height,
        "weight": actress.weight,
    }


def audience_form_unit_to_dict(audience_form_unit):
    return {
        "date": audience_form_unit.date,
        "rate1": audience_form_unit.rate1,
        "share1": audience_form_unit.share1,
        "rank1": audience_form_unit.rank1,
        "rate2": audience_form_unit.rate2,
        "share2": audience_form_unit.share2,
        "rank2": audience_form_unit.rank2,
    }


def router_to_dict(router):
    return {
        "charts": router.charts
    }
    
    
def actress_dict_to_object(dict):
    actress_list = []
    for elem in dict:
        actress_list.append(Actress(name=elem["name"], nation=elem["nation"], birthday=elem["birthday"], constellation=elem["constellation"], blood_type=elem["blood_type"], height=elem["height"], weight=elem["height"]))
    
    return actress_list
  

def audience_form_unit_dict_to_object(dict):
    audience_form = []
    for elem in dict:
        audience_form.append(AudienceFormUint(date=elem["date"], rate1=elem["rate1"], share1=elem["share1"], rank1=elem["rank1"], rate2=elem["rate2"], share2=elem["share2"], rank2=elem["rank2"]))
    
    return audience_form
    

def store_actress_as_json(object_series):
    if os.path.exists(filename_of_actress):
        os.remove(filename_of_actress)
        
    with open(filename_of_actress, "a+", encoding="utf-8") as file_pointer:
        json.dump(object_series, file_pointer, cls=custom_encoder, default=actress_to_dict, indent=4, ensure_ascii=False)
    file_pointer.close()


def get_actress_stat():
    actress_list = []
    if not os.path.exists(filename_of_actress):
        return actress_list
    
    with open(filename_of_actress, encoding="utf-8") as file_pointer:
        actress_list = json.load(file_pointer)
    return actress_dict_to_object(actress_list)


def register_router(router, router_path):
    with open(router_path, "w", encoding="utf-8") as file_pointer:
        json.dump(router, file_pointer, cls=custom_encoder, default=router_to_dict, indent=4, ensure_ascii=False)
    file_pointer.close()


def store_actor_as_json(object_series):
    if os.path.exists(filename_of_actor):
        os.remove(filename_of_actor)

    with open(filename_of_actor, "a+", encoding="utf-8") as file_pointer:
        json.dump(object_series, file_pointer, cls=custom_encoder,
                  default=actress_to_dict, indent=4, ensure_ascii=False)
    file_pointer.close()
    
    
def get_actor_stat():
    actor_list = []
    if not os.path.exists(filename_of_actor):
        return actor_list

    with open(filename_of_actor, encoding="utf-8") as file_pointer:
        actor_list = json.load(file_pointer)
    return actress_dict_to_object(actor_list)


def store_audience_form_as_json(object_series):
    if os.path.exists(filename_of_audience_form):
        os.remove(filename_of_audience_form)

    with open(filename_of_audience_form, "a+", encoding="utf-8") as file_pointer:
        json.dump(object_series, file_pointer, cls=custom_encoder,
                  default=audience_form_unit_to_dict, indent=4, ensure_ascii=False)
    file_pointer.close()
    
    
def get_audience_form():
    audience_form = []
    if not os.path.exists(filename_of_audience_form):
        return audience_form

    with open(filename_of_audience_form, encoding="utf-8") as file_pointer:
        audience_form = json.load(file_pointer)
    return audience_form_unit_dict_to_object(audience_form)