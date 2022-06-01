import os, json

class ShutterstockImg:
    'Saves images into Image objects to be sent to Discord'
    def __init__(self, query, num):
        self.img_url_list = []
        data = os.popen(f"shutterstock images search-images --query \"{query}\" --image-type photo --sort random --page 1 --per-page {num}").read()
        for i in range(num):
            json_data = json.loads(data)
            url = json_data["data"][i]["assets"]["preview_1500"]["url"]
            self.img_url_list.append(url)
    
    def get_url_list(self):
        return self.img_url_list