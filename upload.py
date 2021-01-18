import tornado.web
import tornado.ioloop
import os

class uploadImgHandler(tornado.web.RequestHandler):

    def post(self):

        # show all images
        directory = r'./upload'
        list_of_files = {}
        for filename in os.listdir(directory):
            if filename.endswith(".jpg") or filename.endswith(".png"):
                list_of_files[filename] = os.path.join(directory, filename)
                self.write(f"<img src='{os.path.join(directory, filename)}' alt = '{filename}' style='width:100px;'> <br>")

        files = self.request.files["fileImage"]

        for f in files:
            fh = open(f"upload/{f.filename}", "wb")
            fh.write(f.body)
            fh.close()
            self.write(f"/upload/{f.filename} <br>")
        self.write('''<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <meta http-equiv="X-UA-Compatible" content="ie=edge">
            <title>Image Repository</title>
        </head>
        <body>
        <form method = "post" action = "/" enctype="multipart/form-data" accept-charset="">
        <input type = 'file' name = 'fileImage' multiple>
        <input type = 'submit' value = 'upload'>
        </form>
        </body>
        </html>''')

    def get(self):
        self.render("index.html")

if (__name__ == "__main__"):
    app = tornado.web.Application([
        ("/", uploadImgHandler),
        (r"/upload/(.*)", tornado.web.StaticFileHandler, {'path': 'upload'})
    ])

    app.listen(8080)
    print("Listening on port 8080")
    tornado.ioloop.IOLoop.instance().start()
