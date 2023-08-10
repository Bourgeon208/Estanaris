class Location:
    def __init__(self, name, name_en, type, description, sub_locations, travel_location, parent_location):
        self.name = name
        self.name_en = name_en
        self.type = type
        self.description = description
        self.sub_locations = sub_locations
        self.travel_location = travel_location
        self.parent_location = parent_location