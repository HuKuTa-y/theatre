import requests

class TestTicketAPI:
    def test_create(self):
        #Arrange
        data_in = {
            "row":"13",
            "place":1000,
            "name_movie":"movie1",
            "price":700
        }
        data_expect = [{
            "row":"13",
            "place":1000,
            "name_movie":"5656",
            "price":700
        }]
        #Act
        response_post = requests.post("http://localhost:8080/tickets",data=data_in)
        response_get = requests.get('http://localhost:8080/tickets')
        #Assert
        assert data_expect==response_get.json()