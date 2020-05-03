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

    def create_request(self, province, benefit, case, number, location):
        
        self.reqiest = (self.host + self.endpoint + '/' + self.type + '?'
            + "case=" + str(case) + '&province=' + province
            + '&format=' + self.format)
        if number:
            self.reqiest = self.reqiest + '&limit=' + number
        if benefit:
            self.reqiest = self.reqiest + '&benefit=' + self.to_ascii_url(benefit)
        if location:
            self.reqiest = self.reqiest + '&locality=' + self.to_ascii_url(location)
        
        # print debug url
        # print("request: " + self.reqiest)

    def create_fav_request(self, id_nfz):
    
        self.reqiest = (self.host + self.endpoint + '/' + self.type + '/' + id_nfz)
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
                print(str(error))
                raise
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

    def to_ascii_url(self, text):
        # remove white spaces around 
        text = text.strip()
        #remove duplicated spaces
        text = " ".join(text.split())
        # replace spaces by '%20'
        text = text.replace(" ", "%20")
        # strip right non ascii characters
        # urllib cant send utf-8 characters and
        # host doesn't 'understand' encoded ones
        for c in range(len(text)):
            if ord(text[c]) >= 128:
                return text[:c]
        return text
    
# for testing purposes
if __name__ == "__main__":
    reqiest = Request()
    reqiest.create_request('01', 'poradnia', 1)
    reqiest.send_request()
    
    from jsonparser import JsonParser
    jp = JsonParser(reqiest.rec_response())
    jp.parse()
    