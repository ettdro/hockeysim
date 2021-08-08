from hockeysim.models.division import Division
from hockeysim.models.conference import Conference


class DivisionSeeder():
    def __init__(self) -> None:
        self.east_names = ['Atlantic', 'Metropolitan']
        self.west_names = ['Pacific', 'Central']
        super().__init__()

    def run(self):
        east_conference = Conference.query.filter_by(name='East').first()
        west_conference = Conference.query.filter_by(name='West').first()
        if (east_conference is not None):
            self.seed_divisions(east_conference, self.east_names)

        if (west_conference is not None):
            self.seed_divisions(west_conference, self.west_names)

    def seed_divisions(self, conference, names):
        for name in names:
            division = Division(name)
            division.conference = conference
            division.save()
