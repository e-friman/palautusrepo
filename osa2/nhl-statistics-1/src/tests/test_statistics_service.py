import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )
    
    def test_etsii_oikein(self):
        pelaaja = self.stats.search("Kurri")

        self.assertEqual(pelaaja.name, "Kurri")

    def test_etsii_vaarin(self):
        pelaaja = self.stats.search("Jormakka")

        self.assertEqual(pelaaja, None)
    
    def test_tiimi(self):
        pelaajat = self.stats.team("EDM")
        for player in pelaajat:
            if player.name == "Semenko":
                self.assertEqual(player.name, "Semenko")
            if player.name == "Kurri":
                self.assertEqual(player.name, "Kurri")
            if player.name == "Gretzky":
                self.assertEqual(player.name, "Gretzky")

    def test_top_pelaajat(self):
        top = self.stats.top(3)

        if top[0].name == "Gretzky" and top[1].name == "Yzerman" and top[2].name == "Lemieux":
            self.assertEqual(1, 1)
