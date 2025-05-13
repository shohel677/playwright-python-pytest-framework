import json
from api.base_api import BaseAPI


class PageAPI(BaseAPI):
    def __init__(self):
        super().__init__()

    def get_post(self, post_id):
        return self.get(f"/posts/{post_id}")

    def create_post(self):
        with open("data/post_payload.json", "r") as f:
            payload = json.load(f)
        return self.post("/posts", payload)

    def update_post(self, post_id):
        with open("data/update_payload.json", "r") as f:
            payload = json.load(f)
        return self.put(f"/posts/{post_id}", payload)

    def patch_post(self, post_id):
        with open("data/partial_update_payload.json", "r") as f:
            payload = json.load(f)
        return self.patch(f"/posts/{post_id}", payload)

    def delete_post(self, post_id):
        return self.delete(f"/posts/{post_id}")
