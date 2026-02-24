# Hockey Efficiency Ratings


# Introduction

Hello and welcome to my final project for Unstructured Data! In this
project, I plan to analyze stats of Hall of Fame Goalie, Martin Brodeur.
I plan to scrape data from Hockey Reference in order to get his lifetime
career playoff & regular season statistics. I plan on using this
information to then create an efficiency score to observe when Brodeur
was the most efficient in his career. Additionally, I hope to view the
teams that he was most efficient against across his career.

``` python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from bs4 import BeautifulSoup
import requests
import time
```

# Data Collection

``` python
brod_playoff_url = "https://www.hockey-reference.com/players/b/brodema01/gamelog/playoffs"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}
hockey_request = requests.get(brod_playoff_url, headers = headers)
hockey_soup = BeautifulSoup(hockey_request.content, "html.parser")
```

``` python
hockey_request 
clean_html = hockey_request.text.replace('', '')

playoff_stats_table = hockey_soup.find('table', id='gamelog_playoffs')

if playoff_stats_table:

    playoff_tables = pd.read_html(str(playoff_stats_table))
    
    brodeur_playoffs_df = playoff_tables[0]
    
    brodeur_playoffs_df.columns = brodeur_playoffs_df.columns.droplevel()
  
    print(brodeur_playoffs_df.head())
    
else:
    print("Table not found.")
```

       Rk  Gcar  Gtm        Date  Team Unnamed: 5_level_1  Opp  Result    DEC  \
    0   1     1    5  1992-04-27   NJD                  @  NYR   L 5-8  0-1-0   
    1  Rk  Gcar  Gtm        Date  Team                NaN  Opp  Result    DEC   
    2   2     2    1  1994-04-17   NJD                NaN  BUF   L 0-2  0-1-0   
    3   3     3    2  1994-04-19   NJD                NaN  BUF   W 2-1  1-0-0   
    4   4     4    3  1994-04-21   NJD                  @  BUF   W 2-1  1-0-0   

         MIN  GA  SV  Shots   SV%  PIM  G  A  PTS  
    0  32:04   3  12     15  .800    0  0  0    0  
    1    MIN  GA  SV  Shots   SV%  PIM  G  A  PTS  
    2  59:43   1  21     22  .955    0  0  0    0  
    3  59:55   1  23     24  .958    0  0  0    0  
    4  60:00   1  29     30  .967    0  0  0    0  

    /var/folders/vy/pldbp8tx5bzcr752wcc7m57h0000gn/T/ipykernel_4327/194281229.py:8: FutureWarning:

    Passing literal html to 'read_html' is deprecated and will be removed in a future version. To read from a literal string, wrap it in a 'StringIO' object.

``` python
brodeur_playoffs_df = brodeur_playoffs_df.rename(columns={
    'Rk': 'Rank',
    'Gcar': 'Games Career',
    'Gtm': 'Games Team',
    'Date': 'Date',
    'Age': 'Age',
    'Tm': 'Team',
    'Lg': 'League',
    'G': 'Games Played',
    'GS': 'Games Started',
    'W': 'Wins',
    'L': 'Losses',
    'T': 'Ties',
    'OTL': 'Overtime Losses',
    'GA': 'Goals Against',
    'SA': 'Shots Against',
    'SV': 'Saves',
    'SV%': 'Save Percentage',
    'GAA': 'Goals Against Average'
})
print(brodeur_playoffs_df.head())
```

      Rank Games Career Games Team        Date  Team Unnamed: 5_level_1  Opp  \
    0    1            1          5  1992-04-27   NJD                  @  NYR   
    1   Rk         Gcar        Gtm        Date  Team                NaN  Opp   
    2    2            2          1  1994-04-17   NJD                NaN  BUF   
    3    3            3          2  1994-04-19   NJD                NaN  BUF   
    4    4            4          3  1994-04-21   NJD                  @  BUF   

       Result    DEC    MIN Goals Against Saves  Shots Save Percentage  PIM  \
    0   L 5-8  0-1-0  32:04             3    12     15            .800    0   
    1  Result    DEC    MIN            GA    SV  Shots             SV%  PIM   
    2   L 0-2  0-1-0  59:43             1    21     22            .955    0   
    3   W 2-1  1-0-0  59:55             1    23     24            .958    0   
    4   W 2-1  1-0-0  60:00             1    29     30            .967    0   

      Games Played  A  PTS  
    0            0  0    0  
    1            G  A  PTS  
    2            0  0    0  
    3            0  0    0  
    4            0  0    0  

``` python
brod_career_url = "https://www.hockey-reference.com/players/b/brodema01/splits/"

brodeur_career_request = requests.get(brod_career_url, headers = headers)
brodeur_soup = BeautifulSoup(brodeur_career_request.content, "html.parser")

career_stats_table = brodeur_soup.find('table', id='splits')

if career_stats_table:

    career_tables = pd.read_html(str(career_stats_table))
    
    brodeur_career_df = career_tables[0]
    
    brodeur_career_df = brodeur_career_df.rename(columns={
        'Rk': 'Rank',
        'Gcar': 'Games Career',
        'Gtm': 'Games Team',
        'Date': 'Date',
        'Age': 'Age',
        'Tm': 'Team',
        'Lg': 'League',
        'G': 'Games Played',
        'GS': 'Games Started',
        'W': 'Wins',
        'L': 'Losses',
        'T/O': 'Ties/Overtime Losses',
        'GA': 'Goals Against',
        'SA': 'Shots Against',
        'SV': 'Saves',
        'SV%': 'Save Percentage',
        'GAA': 'Goals Against Average',
        'SO': 'Shutouts',
        'EV GA': 'Even Strength Goals Against',
        'PP GA': 'Power Play Goals Against',
        'SH GA': 'Short Handed Goals Against',
    })
  
    print(brodeur_career_df.head())
    
else:
    print("Table not found.")
```

       Split  Value    GP Wins Losses Ties/Overtime Losses Goals Against  \
    0    NaN  Total  1266  691    397                  154          2781   
    1  Split  Value    GP    W      L                  T/O            GA   
    2  Place   Home   642  380    183                   69          1371   
    3    NaN   Road   624  311    214                   85          1410   
    4  Split  Value    GP    W      L                  T/O            GA   

      Shots Against  Saves Save Percentage Goals Against Average Shutouts  PIM  \
    0         31709  28928            .912                  2.24      125  122   
    1            SA     SV             SV%                   GAA       SO  PIM   
    2         15336  13965            .911                  2.17       66   52   
    3         16373  14963            .914                  2.32       59   70   
    4            SA     SV             SV%                   GAA       SO  PIM   

            TOI Even Strength Goals Against Power Play Goals Against  \
    0  74438:20                        1576                      503   
    1       TOI                       EV GA                    PP GA   
    2  37941:36                         777                      246   
    3  36496:44                         799                      257   
    4       TOI                       EV GA                    PP GA   

      Short Handed Goals Against  
    0                         73  
    1                      SH GA  
    2                         39  
    3                         34  
    4                      SH GA  

    /var/folders/vy/pldbp8tx5bzcr752wcc7m57h0000gn/T/ipykernel_4327/3947445957.py:10: FutureWarning:

    Passing literal html to 'read_html' is deprecated and will be removed in a future version. To read from a literal string, wrap it in a 'StringIO' object.

``` python
brodeur_career_df
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
&#10;    .dataframe tbody tr th {
        vertical-align: top;
    }
&#10;    .dataframe thead th {
        text-align: right;
    }
</style>

|  | Split | Value | GP | Wins | Losses | Ties/Overtime Losses | Goals Against | Shots Against | Saves | Save Percentage | Goals Against Average | Shutouts | PIM | TOI | Even Strength Goals Against | Power Play Goals Against | Short Handed Goals Against |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| 0 | NaN | Total | 1266 | 691 | 397 | 154 | 2781 | 31709 | 28928 | .912 | 2.24 | 125 | 122 | 74438:20 | 1576 | 503 | 73 |
| 1 | Split | Value | GP | W | L | T/O | GA | SA | SV | SV% | GAA | SO | PIM | TOI | EV GA | PP GA | SH GA |
| 2 | Place | Home | 642 | 380 | 183 | 69 | 1371 | 15336 | 13965 | .911 | 2.17 | 66 | 52 | 37941:36 | 777 | 246 | 39 |
| 3 | NaN | Road | 624 | 311 | 214 | 85 | 1410 | 16373 | 14963 | .914 | 2.32 | 59 | 70 | 36496:44 | 799 | 257 | 34 |
| 4 | Split | Value | GP | W | L | T/O | GA | SA | SV | SV% | GAA | SO | PIM | TOI | EV GA | PP GA | SH GA |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |
| 59 | NaN | Tampa Bay Lightning | 66 | 39 | 17 | 8 | 136 | 1648 | 1512 | .917 | 2.10 | 6 | 0 | 3887:33 | 79 | 26 | 2 |
| 60 | NaN | Toronto Maple Leafs | 53 | 22 | 20 | 10 | 135 | 1388 | 1253 | .903 | 2.54 | 3 | 4 | 3185:42 | 87 | 29 | 4 |
| 61 | NaN | Vancouver Canucks | 18 | 6 | 12 | 0 | 50 | 409 | 359 | .878 | 2.86 | 1 | 0 | 1047:09 | 31 | 6 | 0 |
| 62 | NaN | Winnipeg Jets | 43 | 25 | 9 | 8 | 88 | 971 | 883 | .909 | 2.10 | 7 | 8 | 2511:31 | 63 | 20 | 5 |
| 63 | NaN | Washington Capitals | 62 | 40 | 17 | 4 | 141 | 1496 | 1355 | .906 | 2.32 | 6 | 6 | 3651:32 | 77 | 21 | 3 |

<p>64 rows × 17 columns</p>
</div>
