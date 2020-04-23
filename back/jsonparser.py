import json
from institution import Institution


class JsonParser:
    def __init__(self, data):
        self.data = data
        self.parsed = None
        self.institutions = None
        self.response = None
        
    def parse(self):
        self.parsed = json.loads(self.data)
        # print formatted received json
        # print(json.dumps(self.parsed, indent=4, sort_keys=True))
        
        self.institutions = []
        for row in self.parsed["data"]:
            new_institution = Institution()
            new_institution.address = self.try_figure_out(row, "address")
            new_institution.benefit = self.try_figure_out(row, "benefit")
            new_institution.car_park = self.try_figure_out(row, "car-park")
            new_institution.locality = self.try_figure_out(row, "locality")
            new_institution.phone = self.try_figure_out(row, "phone")
            new_institution.place = self.try_figure_out(row, "place")
            new_institution.provider = self.try_figure_out(row, "provider")
            new_institution.regon = self.try_figure_out(row, "regon-provider")

            # new_institution.p_print()
            self.institutions.append(new_institution)
        self.create_response_dict()

    def try_figure_out(self, r, name):
        try:
            attr = r["attributes"][name]
            return attr
        except Exception:
            # value not found
            # will be None = N/A
            return None

    def create_response_dict(self):
        response_list = []
        for new_institution in self.institutions:
            new_dict = {}
            new_dict['address'] = new_institution.address
            new_dict['benefit'] = new_institution.benefit
            new_dict['car_park'] = new_institution.car_park
            new_dict['locality'] = new_institution.locality
            new_dict['phone'] = new_institution.phone
            new_dict['place'] = new_institution.place
            new_dict['provider'] = new_institution.provider
            new_dict['regon'] = new_institution.regon
            response_list.append(new_dict)
        self.response = response_list
