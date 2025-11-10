class StatisticsService:
    def __init__(self, reader):
        self._reader = reader

    def search(self, name):
        for player in self._reader.get_players():
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._reader.get_players()
        )

        return list(players_of_team)

    def top(self, how_many):
        # metodin käyttämä apufunktio voidaan määritellä näin
        def sort_by_points(player):
            return player.points

        sorted_players = sorted(
            self._reader.get_players(),
            reverse=True,
            key=sort_by_points
        )

        result = []
        i = 0
        while i <= how_many:
            result.append(sorted_players[i])
            i += 1

        return result
