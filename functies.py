def information_to_dict(api_paramaters):
    """"Takes the part of the URL after http://webservices.ns.nl/ and returns the information from the API to a dictionairy."""

    import requests
    import xmltodict

    response = requests.get('http://webservices.ns.nl/{}'.format(api_paramaters), auth=('tim.vandijk@student.hu.nl', 'Y8TYvZa6rVciUFEZsljW8PyQlmnmBcgZXMXreN67AwaLJarWcLHhvA'))
    response_XML = xmltodict.parse(response.text)

    return response_XML