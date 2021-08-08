from hockeysim.models.division import Division
from hockeysim.models.conference import Conference
from hockeysim.models.team import Team
from faker import Faker


class TeamSeeder():
    def __init__(self) -> None:
        fake = Faker()
        self.cities = []
        self.names = []
        for _ in range(30):
            self.cities.append(fake.city())
        
        for _ in range(30):
            self.names.append(fake.company())
        super().__init__()

    def run(self):
        east_conference = Conference.query.filter_by(name='East').first()
        for index, city in enumerate(self.cities[0:15]):
            team = Team(name=self.names[index], city=city)
            team.division = Division.query.filter_by(conference_id=east_conference.id).all()[0 if index < 8 else 1]
            team.save()

        west_conference = Conference.query.filter_by(name='West').first()
        for index, city in enumerate(self.cities[16:30]):
            team = Team(name=self.names[index], city=city)
            team.division = Division.query.filter_by(conference_id=west_conference.id).all()[0 if index < 7 else 1]
            team.save()
