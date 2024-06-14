import json


class Media:
    def __init__(self, email, cv, likedin):
        self.email = email
        self.cv = cv
        self.likedin = likedin



class Info:
    def __init__(self, icon, title, subtitle, description, date="", certificate="", technologies=[], image="", url="", github="", list=[]):
        self.icon = icon
        self.title = title
        self.subtitle = subtitle
        self.description = description
        self.list = list
        self.date = date
        self.certificate = certificate
        self.image = image
        self.url = url
        self.github = github


class Extra:
    def __init__(self, image, title, description, url):
        self.image = image
        self.title = title
        self.description = description
        self.url = url


class Data:
    def __init__(
        self,
            title,
            description,
            image,
            avatar,
            name,
            skill,
            location,
            media,
            about,
            experience,
            projects,
            training,
            extras
    ):
        self.title = title
        self.description = description
        self.image = image
        self.avatar = avatar
        self.name = name
        self.skill = skill
        self.location = location
        self.media = Media(**media)
        self.about = about
        self.experience = [Info(**info) for info in experience]
        self.projects = [Info(**info) for info in projects]
        self.training = [Info(**info) for info in training]
        self.extras = [Extra(**info) for info in extras]


with open("assets/data/data.json", 'r', encoding='utf-8') as file:
    json_data = json.load(file)

data = Data(**json_data)
