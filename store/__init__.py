from model import Actress
import json
import os


filename_of_actress = "store/store.json"


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


def router_to_dict(router):
    return {
        "charts": router.charts
    }
    
    
def actress_dict_to_object(dict):
    actress_list = []
    for elem in dict:
        actress_list.append(Actress(name=elem["name"], nation=elem["nation"], birthday=elem["birthday"], constellation=elem["constellation"], blood_type=elem["blood_type"], height=elem["height"], weight=elem["height"]))
    
    return actress_list
  

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
