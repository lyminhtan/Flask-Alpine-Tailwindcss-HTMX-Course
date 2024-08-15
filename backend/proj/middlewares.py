from werkzeug.wrappers import Request, Response, ResponseStream


class Middleware:
    """
    Simple WSGI middleware
    """

    def __init__(self, app):
        self.app = app
        self.userName = "Tony"
        self.password = "IamIronMan"

    def __call__(self, environ, start_response):
        print("Middleware")
        request = Request(environ)
        if request.authorization:
            userName = request.authorization.get("username")
            password = request.authorization.get("password")

            # these are hardcoded for demonstration
            # verify the username and password from some database or env config variable
            if userName == self.userName and password == self.password:
                environ["user"] = {"name": "Tony"}
                return self.app(environ, start_response)

            res = Response("Authorization failed", mimetype="text/plain", status=401)
            return res(environ, start_response)
        else:
            return self.app(environ, start_response)

class AnotherMiddleware:
    """
    Simple WSGI middleware
    """

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        print("Another middleware")
        return self.app(environ, start_response)