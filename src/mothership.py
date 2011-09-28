import web

urls = ("/.*", "hello")
app = web.application(urls, globals())

class hello:
    def GET(self):
        return 'Hello, Mothership!'

if __name__ == "__main__":
    web.config.debug = True
    app.run()
