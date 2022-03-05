import json


class Files:
    def __init__(self):
        pass

    def get_json_data(self, file_path):
        with open(file_path, 'r',) as file:
            return json.load(file)

    def create_file(self, file_path):
        open(file_path, 'w').close()

    def create_json_file(self, file_path):
        with open(file_path, 'w') as f:
            json.dump({
                "results": []
            }, f, ensure_ascii = False, indent = 4)
    
    def append_url_to_file(self, url, file_path):
        with open(file_path, "a") as file:
            file.write(url + '\n')

    def append_url_to_json_file(self, url, file_path):
        with open(file_path,'r+') as file:
            file_data = json.load(file)
            file_data["results"].append({
                "url": url
            })
            file.seek(0)
            json.dump(file_data, file, indent = 4)

    def create_output_file(self, file_path):
        if file_path.endswith('.json'):
            self.create_json_file(file_path)
        else:
            self.create_file(file_path)

    def append_url_to_output_file(self, url, file_path):
        if file_path.endswith('.json'):
            self.append_url_to_json_file(url, file_path)
        else:
            self.append_url_to_file(url, file_path)
