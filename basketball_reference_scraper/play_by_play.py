import numpy as np
import pandas as pd
from requests import get
from bs4 import BeautifulSoup

try:
    from constants import TEAM_TO_TEAM_ABBR
except:
    try:
        from basketball_reference_scraper.constants import TEAM_TO_TEAM_ABBR
    except:
        from basketball_reference_scraper.basketball_reference_scraper.constants import TEAM_TO_TEAM_ABBR


def get_play_by_play():
    r = get(f'https://widgets.sports-reference.com/wg.fcgi?css=1&site=bbr&url=%2Fleagues%2FNBA_2022_play-by-play.html&div=div_pbp_stats')
    if r.status_code==200:
        soup = BeautifulSoup(r.content, 'html.parser')
        table = soup.find('table')
        df = pd.read_html(str(table))[0]
        df.columns = [y if 'Unnamed:' in x or 'Position Estimate' in x or 'Misc.' in x else x+' '+y for x,y in df.columns]
        df = df.loc[df['Player'] != 'Player', :].copy()
        df.rename(columns={'Player': 'PLAYER', 'Tm': 'TEAM'}, inplace=True)
        df.loc[:, ['PG%', 'SG%', 'SF%', 'PF%', 'C%']] = df.loc[:, ['PG%', 'SG%', 'SF%', 'PF%', 'C%']].applymap(lambda x: float(x.replace('%',''))/100.0 if not pd.isna(x) else 0.0)
        # df['TEAM'] = df['TEAM'].apply(lambda x: TEAM_TO_TEAM_ABBR[x.upper()])
        return df
