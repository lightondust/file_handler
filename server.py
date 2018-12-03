import responder
from service import get_file_list

api = responder.API()


@api.route("/file/")
def file_list(req, resp):
    file_res = get_file_list('')
    resp.media = file_res
    resp.headers['Access-Control-Allow-Origin'] = '*'


@api.route("/file/{path}")
def file_list(req, resp, *, path):
    file_res = get_file_list(path)
    resp.media = file_res
    resp.headers['Access-Control-Allow-Origin'] = '*'


api.run()
