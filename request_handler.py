from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from views.actor_request import create_actor, get_all_actors, get_single_actor

from views.movie_request import create_movie, get_all_movies, get_single_movie


class HandleRequests(BaseHTTPRequestHandler):
    """Handles the requests to this server"""

    def parse_url(self):
        """Parse the url into the resource and id"""
        split_path = self.path.split('/')
        resource = split_path[1]
        if '?' in resource:
            param = resource.split('?')[1]
            resource = resource.split('?')[0]
            pair = param.split('=')
            key = pair[0]
            value = pair[1]
            return (resource, key, value)
        
        id = None
        try:
            id = int(split_path[2])
        except (IndexError, ValueError):
            pass
        return (resource, id)

    def _set_headers(self, status):
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        """Sets the options headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                         'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                         'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    def do_GET(self):
        """Handle Get requests to the server"""
        (resource, id) = self.parse_url()
        self._set_headers(200)
        response = None
        if resource == 'movies':
            if id is not None:
                response = get_single_movie(id)
            else:
                response = get_all_movies()
        if resource == 'actors':
            if id is not None:
                response = get_single_actor(id)
            else:
                response = get_all_actors()
        
        self.wfile.write(response.encode())

    def do_POST(self):
        """Make a post request to the server"""
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        resource, _ = self.parse_url()
        response = None
        if resource == 'movies':
            response = create_movie(post_body)
        if resource == 'actors':
            response = create_actor(post_body)

        self.wfile.write(response.encode())



    def do_PUT(self):
        """Handles PUT requests to the server"""
        pass

    def do_DELETE(self):
        """Handle DELETE Requests"""
        pass


def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
