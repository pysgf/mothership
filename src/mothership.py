#!/usr/bin/env python
import json
import web

urls = ("/users/(\w+).*", "Users",
        "/events/(\w+).*", "Events",
        "/calendars/(\w+).*", "Calendars")
app = web.application(urls, globals())


class BaseResponse(object):
    def __init__(self):
        self.get_methods = ['retrieve']
        self.post_methods = ['create', 'update', 'delete']

    def create(self):
        raise NotImplementedError("Must override in child classes")

    def retrieve(self):
        raise NotImplementedError("Must override in child classes")

    def update(self):
        raise NotImplementedError("Must override in child classes")

    def delete(self):
        raise NotImplementedError("Must override in child classes")

    def require_authentication(self):
        pass

    def get_post_data(self):
        try:
            return json.loads(web.data())
        except ValueError:
            return {}


class Users(BaseResponse):
    def GET(self, method):
        if method not in self.get_methods:
            return web.Forbidden()

    def POST(self, method):
        if method not in self.post_methods:
            return web.Forbidden()

        self.require_authentication()
        post_data = self.get_post_data()
        getattr(self, method)(post_data)

    def create(self, obj):
        pass

    def retrieve(self):
        pass

    def update(self, obj):
        pass

    def delete(self, obj):
        pass


class Events(BaseResponse):
    def GET(self, method):
        if method not in self.get_methods:
            return web.Forbidden()

    def POST(self, method):
        if method not in self.post_methods:
            return web.Forbidden()

        self.require_authentication()
        post_data = self.get_post_data()
        getattr(self, method)(post_data)

    def create(self, obj):
        pass

    def retrieve(self):
        pass

    def update(self, obj):
        pass

    def delete(self, obj):
        pass


class Calendars(BaseResponse):
    def GET(self, method):
        if method not in self.get_methods:
            return web.Forbidden()

    def POST(self, method):
        if method not in self.post_methods:
            return web.Forbidden()

        self.require_authentication()
        post_data = self.get_post_data()
        getattr(self, method)(post_data)

    def create(self, obj):
        pass

    def retrieve(self):
        pass

    def update(self, obj):
        pass

    def delete(self, obj):
        pass


if __name__ == "__main__":
    web.config.debug = True
    app.run()
