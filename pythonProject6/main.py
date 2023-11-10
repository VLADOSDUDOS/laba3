import json
from xml.etree import ElementTree

class PersonAgeException(Exception):
    def __init__(self, message):
        super().__init__(message)

class Person:
    def __init__(self, name: str, age: int):
        if age <= 100:
            self.__age = age
        else:
            raise PersonAgeException("Person's age must be less than 100")

        self.__name = name

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        if age <= 100:
            self.__age = age
        else:
            raise PersonAgeException("Person's age must be less than 100")

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def sleeping(self):
        print(self.__name + " sleeping...")

class Media:
    def __init__(self, title: str, year: int):
        self.title = title
        self.year = year
        self.media_type = "Unknown"  # Тип медиа

class Movie(Media):
    def __init__(self, title: str, year: int, duration: int, director: str):
        Media.__init__(self, title, year)
        self.duration = duration
        self.director = director
        self.media_type = "Movie"  # Устанавливаем тип медиа как фильм

    def to_dict(self):
        movie_dict = {
            "title": self.title,
            "year": self.year,
            "duration": self.duration,
            "director": self.director,
            "media_type": self.media_type
        }
        return movie_dict

    def to_xml(self):
        movie_element = ElementTree.Element("Movie")

        title_element = ElementTree.Element("Title")
        title_element.text = self.title
        movie_element.append(title_element)

        year_element = ElementTree.Element("Year")
        year_element.text = str(self.year)
        movie_element.append(year_element)

        duration_element = ElementTree.Element("Duration")
        duration_element.text = str(self.duration)
        movie_element.append(duration_element)

        director_element = ElementTree.Element("Director")
        director_element.text = self.director
        movie_element.append(director_element)

        media_type_element = ElementTree.Element("MediaType")
        media_type_element.text = self.media_type
        movie_element.append(media_type_element)

        xml_tree = ElementTree.ElementTree(movie_element)

        return ElementTree.tostring(xml_tree.getroot(), encoding="utf-8", method="xml")

    @classmethod
    def from_json(cls, json_data):
        movie_dict = json.loads(json_data)
        title = movie_dict["title"]
        year = movie_dict["year"]
        duration = movie_dict["duration"]
        director = movie_dict["director"]

        movie_json = cls(title, year, duration, director)
        return movie_json

    @classmethod
    def from_xml(cls, xml_data):
        xml_tree = ElementTree.ElementTree(ElementTree.fromstring(xml_data))
        movie_element = xml_tree.getroot()

        title = movie_element.find("Title").text
        year = int(movie_element.find("Year").text)
        duration = int(movie_element.find("Duration").text)
        director = movie_element.find("Director").text

        movie_xml = cls(title, year, duration, director)
        return movie_xml

class TVShow(Media):
    def __init__(self, title: str, year: int, num_episodes: int, creator: str):
        Media.__init__(self, title, year)
        self.num_episodes = num_episodes
        self.creator = creator
        self.media_type = "TV Show"  # Устанавливаем тип медиа как телесериал

    def to_dict(self):
        tvshow_dict = {
            "title": self.title,
            "year": self.year,
            "num_episodes": self.num_episodes,
            "creator": self.creator,
            "media_type": self.media_type
        }
        return tvshow_dict

    def to_xml(self):
        tvshow_element = ElementTree.Element("TVShow")

        title_element = ElementTree.Element("Title")
        title_element.text = self.title
        tvshow_element.append(title_element)

        year_element = ElementTree.Element("Year")
        year_element.text = str(self.year)
        tvshow_element.append(year_element)

        num_episodes_element = ElementTree.Element("NumEpisodes")
        num_episodes_element.text = str(self.num_episodes)
        tvshow_element.append(num_episodes_element)

        creator_element = ElementTree.Element("Creator")
        creator_element.text = self.creator
        tvshow_element.append(creator_element)

        media_type_element = ElementTree.Element("MediaType")
        media_type_element.text = self.media_type
        tvshow_element.append(media_type_element)

        xml_tree = ElementTree.ElementTree(tvshow_element)

        return ElementTree.tostring(xml_tree.getroot(), encoding="utf-8", method="xml")

    @classmethod
    def from_json(cls, json_data):
        tvshow_dict = json.loads(json_data)
        title = tvshow_dict["title"]
        year = tvshow_dict["year"]
        num_episodes = tvshow_dict["num_episodes"]
        creator = tvshow_dict["creator"]

        tvshow_json = cls(title, year, num_episodes, creator)
        return tvshow_json

    @classmethod
    def from_xml(cls, xml_data):
        xml_tree = ElementTree.ElementTree(ElementTree.fromstring(xml_data))
        tvshow_element = xml_tree.getroot()

        title = tvshow_element.find("Title").text
        year = int(tvshow_element.find("Year").text)
        num_episodes = int(tvshow_element.find("NumEpisodes").text)
        creator = tvshow_element.find("Creator").text

        tvshow_xml = cls(title, year, num_episodes, creator)
        return tvshow_xml

# Создаем объекты Movie и TVShow
movie = Movie(title="Inception", year=2010, duration=148, director="Christopher Nolan")
tv_show = TVShow(title="Breaking Bad", year=2008, num_episodes=62, creator="Vince Gilligan")

# Пример использования

