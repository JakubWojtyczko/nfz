import urllib
import urllib.request
from socket import timeout


class Request:

    def __init__(self):
        self.host = "https://api.nfz.gov.pl/"
        self.endpoint = "app-itl-api"
        self.type = "queues"
        self.format = "json"
        self.request = None
        self.response = None

    def create_request(self, province, benefit, case):
        self.reqiest = (self.host + self.endpoint + '/' + self.type + '?'
            + "case=" + str(case) + '&province=' + province
            + '&benefit=' + benefit + '&format=' + self.format)
        # print debug url
        print("request: " + self.reqiest)

    def send_request(self):
        if self.reqiest is not None:
            try:
                self.response = contents = urllib.request.urlopen(self.reqiest, timeout=10).read()
            except timeout:
                # waiting for response too long
                print('Error: timout while waiting for response')
                raise 
            except urllib.error.HTTPError as error:
                # cannot connect to the server
                print('ERROR: ' + str(error))
                raise ConnectionRefusedError
            except Exception as e:
                note = """
                !! Note: `urllib` requires ssl module for handling HTTPS requests.     !!
                !! Otherwise `urlopen` can raise ValueError or an another exception.   !!
                !! Type `pip install ssl` if you don't have installed this module yet. !!
                """
                print(note)
                raise ConnectionRefusedError from e
            return
        raise ValueError("ERROR: Try to send an empty request")

    def rec_response(self):
        return self.response


# for testing purposes
if __name__ == "__main__":
    reqiest = Request()
    reqiest.create_request('01', 'poradnia', 1)
    reqiest.send_request()
    
    from jsonparser import JsonParser
    jp = JsonParser(reqiest.rec_response())
    jp.parse()
    