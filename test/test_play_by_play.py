import unittest
from basketball_reference_scraper.play_by_play import get_play_by_play

class TestPlayByPlay(unittest.TestCase):
    def test_play_by_play(self):
        df = get_play_by_play()
        req_columns = ['PLAYER', 'TEAM', 'Pos', 'PG%', 'SG%', 'SF%', 'PF%', 'C%']
        self.assertTrue(all([x in df.columns for x in req_columns]))

if __name__ == '__main__':
    unittest.main()
