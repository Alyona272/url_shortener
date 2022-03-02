from storage.model import InputCreateUser


class BaseStorage(object):

    def save_user(self, user: InputCreateUser, id: str):
        pass

    def delete_user(self, id: str):
        pass

    def get_user(self, id: str):
        pass

    def save_short_url(self, origin: str, short: str):
        pass
