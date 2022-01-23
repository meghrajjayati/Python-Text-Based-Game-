import json
from types import SimpleNamespace

class player():
    def __init__(self):
        self.name = ""
        self.gender = ""
        self.age = 0
        self.partner_gender = ""
        self.preferred_partner_types = []
        self.score = 0

class partner():
    def __init__(self):
        self.name = ""
        self.gender = ""
        self.age = 0
        self.occupation = ""
        self.personality_types = []


class JsonConvert(object):
    mappings = {}
     
    @classmethod
    def class_mapper(clsself, d):
        for keys, cls in clsself.mappings.items():
            if keys.issuperset(d.keys()):   # are all required arguments present?
                return cls(**d)
        else:
            # Raise exception instead of silently returning None
            raise ValueError('Unable to find a matching class for object: {!s}'.format(d))
     
    @classmethod
    def complex_handler(clsself, Obj):
        if hasattr(Obj, '__dict__'):
            return Obj.__dict__
        else:
            raise TypeError('Object of type %s with value of %s is not JSON serializable' % (type(Obj), repr(Obj)))
 
    @classmethod
    def register(clsself, cls):
        clsself.mappings[frozenset(tuple([attr for attr,val in cls().__dict__.items()]))] = cls
        return cls
 
    @classmethod
    def ToJSON(clsself, obj):
        return json.dumps(obj.__dict__, default=clsself.complex_handler, indent=4)
 
    @classmethod
    def FromJSON(clsself, json_str):
        return json.loads(json_str, object_hook=clsself.class_mapper)
     
    @classmethod
    def ToFile(clsself, obj, path):
        with open(path, 'w') as jfile:
            jfile.writelines([clsself.ToJSON(obj)])
        return path
 
    @classmethod
    def FromFile(clsself, filepath):
        result = None
        with open(filepath, 'r') as jfile:
            result = clsself.FromJSON(jfile.read())
        return result

@JsonConvert.register
class option(object):
    def __init__(self, id:int=None, option:str="", personality_type:str="", response_positive:str="", response_negative:str="", jump_to_mcq_id:int=None, jump_to_scenario_id:int=None, jump_to_scenario_path:str=""):
        self.id = id
        self.option = option
        self.personality_type = personality_type
        self.response_positive = response_positive
        self.response_negative = response_negative
        self.jump_to_mcq_id = jump_to_mcq_id
        self.jump_to_scenario_id = jump_to_scenario_id
        self.jump_to_scenario_path = jump_to_scenario_path
        return

@JsonConvert.register
class mcq(object):
    def __init__(self, id:int=None, question:str="", options:[option]=None):
        self.id = id
        self.question = question
        self.options = [] if options is None else options
        return
 
@JsonConvert.register
class scenario(object):
    def __init__(self, id:int=None, title:str="", path:str="", mcqs:[mcq]=None):
        self.id = id
        self.title = title
        self.path = path
        self.mcqs = [] if mcqs is None else mcqs
        return

@JsonConvert.register
class story(object):
    def __init__(self, scenarios:[scenario]=None):
        self.scenarios = [] if scenarios is None else scenarios
        return
