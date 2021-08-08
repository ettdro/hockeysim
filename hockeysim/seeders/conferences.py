from hockeysim.models.conference import Conference


class ConferenceSeeder():
    def __init__(self) -> None:
        self.names = ['East', 'West']
        super().__init__()

    def run(self):
        for name in self.names:
            conference = Conference(name)
            conference.save()