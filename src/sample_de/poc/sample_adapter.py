import json

# 1. Target: main class which require json dataset
class DataProcessor:
    def process_json_data(self, json_string):
        data = json.loads(json_string)
        print(f"[Processor] Processing data for user: {data['name']}")
        print(f"[Processor] Role: {data['role']}")
        print(f"[Processor] Objective: {data['objective']}")


# 2. Adaptee: Previous srrvice which gives xml data
class OldXMLService:
    def get_xml_data(self):
        # sample old xml data
        return "<user><name>Ashok Jha</name><role>Traveller</role></user><objective>SKY is Limit</objective>"


# 3. Adapter: जो XML को JSON में बदलकर Target के अनुकूल बनाता है
class XMLToJSONAdapter:
    def __init__(self, xml_service: OldXMLService):
        self.xml_service = xml_service

    def get_data_as_json(self):
        # get xml data
        xml_data = self.xml_service.get_xml_data()
        
        # easy way to extract XML  (in project use xml.etree)
        # usiubg simple setting
        name = xml_data.split("<name>")[1].split("</name>")[0]
        role = xml_data.split("<role>")[1].split("</role>")[0]
        objective = xml_data.split("<objective>")[1].split("</objective>")[0]
        
        # convert data into JSON format
        dictionary = {"name": name, "role": role, "objective": objective}
        return json.dumps(dictionary)


# 4. Client Code: run both service
if __name__ == "__main__":
    # old service and start adapter service
    old_service = OldXMLService()
    adapter = XMLToJSONAdapter(old_service)
    
    # main data processor
    processor = DataProcessor()

    # convert old data in xml format to  data in json format
    compatible_json_data = adapter.get_data_as_json()
    
    print("--- Adapter Pattern Output ---")
    processor.process_json_data(compatible_json_data)
