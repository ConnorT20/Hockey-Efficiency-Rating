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

Here I am going to be scraping data from Hockey Reference. I will be
scraping both Brodeur’s regular season and playoff stats. I will then
clean the data and prepare it for my analysis and efficiency score
calculations. My main form of scraping will be using BeautifulSoup to
pull the HTML content of the pages and then using pandas to read the
tables into dataframes.

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

    /var/folders/vy/pldbp8tx5bzcr752wcc7m57h0000gn/T/ipykernel_5322/194281229.py:8: FutureWarning:

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
clean_playoff_df = brodeur_playoffs_df[brodeur_playoffs_df['Games Played'] != 'G'].copy()
clean_playoff_df
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

|  | Rank | Games Career | Games Team | Date | Team | Unnamed: 5_level_1 | Opp | Result | DEC | MIN | Goals Against | Saves | Shots | Save Percentage | PIM | Games Played | A | PTS |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| 0 | 1 | 1 | 5 | 1992-04-27 | NJD | @ | NYR | L 5-8 | 0-1-0 | 32:04 | 3 | 12 | 15 | .800 | 0 | 0 | 0 | 0 |
| 2 | 2 | 2 | 1 | 1994-04-17 | NJD | NaN | BUF | L 0-2 | 0-1-0 | 59:43 | 1 | 21 | 22 | .955 | 0 | 0 | 0 | 0 |
| 3 | 3 | 3 | 2 | 1994-04-19 | NJD | NaN | BUF | W 2-1 | 1-0-0 | 59:55 | 1 | 23 | 24 | .958 | 0 | 0 | 0 | 0 |
| 4 | 4 | 4 | 3 | 1994-04-21 | NJD | @ | BUF | W 2-1 | 1-0-0 | 60:00 | 1 | 29 | 30 | .967 | 0 | 0 | 0 | 0 |
| 5 | 5 | 5 | 4 | 1994-04-23 | NJD | @ | BUF | L 3-5 | 0-1-0 | 59:36 | 5 | 25 | 30 | .833 | 0 | 0 | 0 | 0 |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |
| 237 | 202 | 202 | 21 | 2012-06-04 | NJD | @ | LAK | L 0-4 | 0-1-0 | 59:55 | 4 | 17 | 21 | .810 | 0 | 0 | 0 | 0 |
| 238 | 203 | 203 | 22 | 2012-06-06 | NJD | @ | LAK | W 3-1 | 1-0-0 | 60:00 | 1 | 21 | 22 | .955 | 0 | 0 | 0 | 0 |
| 239 | 204 | 204 | 23 | 2012-06-09 | NJD | NaN | LAK | W 2-1 | 1-0-0 | 60:00 | 1 | 25 | 26 | .962 | 0 | 0 | 0 | 0 |
| 240 | 205 | 205 | 24 | 2012-06-11 | NJD | @ | LAK | L 1-6 | 0-1-0 | 59:24 | 5 | 19 | 24 | .792 | 0 | 0 | 0 | 0 |
| 241 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | 113-92 | 113-91-0 | 12717:01 | 428 | 4830 | 5258 | .919 | 30 | 1 | 12 | 13 |

<p>226 rows × 18 columns</p>
</div>

Above is the process of the scraping and cleaning of Martin Brodeur’s
playoff stats. I was able to successfully scrape and pull the data from
Hockey Reference. In doing so I acquired data from every playoff
game/series that Brodeur played in during the playoffs. The next step
will be to repeat this process for his regular season stats, shown
below.

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

    /var/folders/vy/pldbp8tx5bzcr752wcc7m57h0000gn/T/ipykernel_5322/2028733359.py:10: FutureWarning:

    Passing literal html to 'read_html' is deprecated and will be removed in a future version. To read from a literal string, wrap it in a 'StringIO' object.

In this step, I was able to successfully scrape Brodeur’s regular season
stats. I was able to pull data from every regular season game/series
that Brodeur played in during his career. The next step will be to clean
this data and prepare it for analysis and efficiency score calculations.
Additionally, I changed the column names to be easier to read and
understand for the sake of my analysis.

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

Here is the initial dataframe for Brodeur’s regular season stats. As you
can see, there are some rows that are not actual data but rather header
rows that are repeated throughout the dataframe. These rows need to be
removed in order to properly analyze the data and calculate efficiency
scores.

``` python
clean_career_df = brodeur_career_df[brodeur_career_df['GP'] != 'GP'].copy()
```

``` python
clean_career_df
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
| 2 | Place | Home | 642 | 380 | 183 | 69 | 1371 | 15336 | 13965 | .911 | 2.17 | 66 | 52 | 37941:36 | 777 | 246 | 39 |
| 3 | NaN | Road | 624 | 311 | 214 | 85 | 1410 | 16373 | 14963 | .914 | 2.32 | 59 | 70 | 36496:44 | 799 | 257 | 34 |
| 5 | All-Star\* | Pre | 788 | 422 | 259 | 87 | 1762 | 19683 | 17921 | .910 | 2.29 | 79 | 76 | 46091:15 | 1006 | 324 | 49 |
| 6 | NaN | Post | 478 | 269 | 138 | 67 | 1019 | 12026 | 11007 | .915 | 2.16 | 46 | 46 | 28347:05 | 570 | 179 | 24 |
| 8 | Result | Win | 699 | 691 | 0 | 0 | 1078 | 17586 | 16508 | .939 | 1.55 | 122 | 54 | 41755:08 | 576 | 221 | 28 |
| 9 | NaN | Loss | 395 | 0 | 380 | 0 | 1278 | 9344 | 8066 | .863 | 3.54 | 0 | 40 | 21689:05 | 756 | 206 | 38 |
| 10 | NaN | Tie | 172 | 0 | 17 | 154 | 425 | 4779 | 4354 | .911 | 2.32 | 3 | 28 | 10994:07 | 244 | 76 | 7 |
| 12 | Month | October | 151 | 77 | 60 | 11 | 365 | 3819 | 3454 | .904 | 2.49 | 14 | 24 | 8805:29 | 207 | 87 | 7 |
| 13 | NaN | November | 176 | 97 | 58 | 17 | 384 | 4345 | 3961 | .912 | 2.22 | 12 | 18 | 10398:19 | 231 | 58 | 12 |
| 14 | NaN | December | 205 | 112 | 63 | 24 | 444 | 5044 | 4600 | .912 | 2.24 | 28 | 14 | 11881:18 | 258 | 78 | 17 |
| 15 | NaN | January | 204 | 111 | 59 | 31 | 445 | 5321 | 4876 | .916 | 2.20 | 22 | 16 | 12156:58 | 261 | 79 | 10 |
| 16 | NaN | February | 172 | 95 | 47 | 30 | 371 | 4348 | 3977 | .915 | 2.17 | 16 | 22 | 10268:12 | 206 | 76 | 6 |
| 17 | NaN | March | 249 | 136 | 77 | 33 | 550 | 6249 | 5699 | .912 | 2.25 | 22 | 20 | 14677:24 | 312 | 88 | 16 |
| 18 | NaN | April | 108 | 63 | 33 | 8 | 220 | 2578 | 2358 | .915 | 2.12 | 11 | 8 | 6237:29 | 101 | 37 | 5 |
| 19 | NaN | May | 1 | NaN | NaN | NaN | 2 | 5 | 3 | .600 | 9.10 | 0 | 0 | 13:11 | NaN | NaN | NaN |
| 21 | Conference | Eastern | 980 | 546 | 294 | 122 | 2142 | 24453 | 22311 | .912 | 2.23 | 98 | 100 | 57599:59 | 1217 | 404 | 58 |
| 22 | NaN | Western | 282 | 143 | 102 | 32 | 629 | 7171 | 6542 | .912 | 2.27 | 27 | 22 | 16659:50 | 359 | 99 | 15 |
| 23 | NaN | Prince of Wales | 4 | 2 | 1 | 0 | 10 | 85 | 75 | .882 | 3.36 | 0 | 0 | 178:31 | NaN | NaN | NaN |
| 25 | Division | Patrick | 2 | 0 | 1 | 0 | 6 | 34 | 28 | .824 | 6.13 | 0 | 0 | 58:41 | NaN | NaN | NaN |
| 26 | NaN | Adams | 2 | 2 | 0 | 0 | 4 | 51 | 47 | .922 | 2.00 | 0 | 0 | 119:50 | NaN | NaN | NaN |
| 27 | NaN | Northeast | 337 | 172 | 108 | 48 | 740 | 8536 | 7796 | .913 | 2.25 | 29 | 30 | 19757:16 | 396 | 109 | 17 |
| 28 | NaN | Pacific | 112 | 61 | 39 | 11 | 233 | 2802 | 2569 | .917 | 2.10 | 10 | 14 | 6643:10 | 117 | 40 | 9 |
| 29 | NaN | Central | 107 | 54 | 36 | 14 | 231 | 2817 | 2586 | .918 | 2.19 | 12 | 4 | 6322:38 | 111 | 30 | 1 |
| 30 | NaN | Atlantic | 406 | 228 | 123 | 48 | 885 | 10243 | 9358 | .914 | 2.23 | 46 | 52 | 23857:03 | 447 | 171 | 22 |
| 31 | NaN | Southeast | 218 | 136 | 58 | 22 | 473 | 5198 | 4725 | .909 | 2.20 | 22 | 16 | 12874:29 | 337 | 119 | 17 |
| 32 | NaN | Northwest | 63 | 28 | 27 | 7 | 165 | 1552 | 1387 | .894 | 2.68 | 5 | 4 | 3694:02 | 131 | 29 | 5 |
| 33 | NaN | Metropolitan | 19 | 10 | 5 | 4 | 44 | 476 | 432 | .908 | 2.38 | 1 | 2 | 1111:11 | 37 | 5 | 2 |
| 35 | Opponent | Anaheim Ducks | 23 | 15 | 7 | 1 | 44 | 597 | 553 | .926 | 1.97 | 2 | 2 | 1337:03 | 22 | 9 | 3 |
| 36 | NaN | Boston Bruins | 61 | 26 | 23 | 10 | 153 | 1642 | 1489 | .907 | 2.59 | 4 | 4 | 3539:44 | 83 | 29 | 5 |
| 37 | NaN | Buffalo Sabres | 62 | 33 | 16 | 9 | 126 | 1485 | 1359 | .915 | 2.11 | 3 | 8 | 3575:49 | 71 | 16 | 4 |
| 38 | NaN | Carolina Hurricanes | 62 | 39 | 16 | 6 | 127 | 1518 | 1391 | .916 | 2.10 | 9 | 8 | 3625:49 | 67 | 29 | 6 |
| 39 | NaN | Columbus Blue Jackets | 13 | 7 | 3 | 3 | 29 | 326 | 297 | .911 | 2.19 | 2 | 0 | 795:22 | 24 | 5 | 0 |
| 40 | NaN | Calgary Flames | 17 | 7 | 6 | 3 | 38 | 401 | 363 | .905 | 2.33 | 1 | 0 | 977:47 | 19 | 8 | 1 |
| 41 | NaN | Chicago Blackhawks | 21 | 9 | 4 | 6 | 42 | 573 | 531 | .927 | 2.11 | 1 | 0 | 1195:22 | 25 | 5 | 1 |
| 42 | NaN | Colorado Avalanche | 33 | 18 | 8 | 6 | 70 | 789 | 719 | .911 | 2.17 | 5 | 6 | 1936:30 | 35 | 10 | 1 |
| 43 | NaN | Dallas Stars | 21 | 11 | 9 | 1 | 41 | 557 | 516 | .926 | 1.99 | 4 | 0 | 1237:20 | 18 | 5 | 2 |
| 44 | NaN | Detroit Red Wings | 20 | 10 | 9 | 1 | 45 | 514 | 469 | .912 | 2.24 | 2 | 0 | 1206:49 | 25 | 9 | 0 |
| 45 | NaN | Edmonton Oilers | 18 | 9 | 6 | 3 | 45 | 451 | 406 | .900 | 2.45 | 0 | 2 | 1103:04 | 30 | 3 | 2 |
| 46 | NaN | Florida Panthers | 66 | 41 | 16 | 9 | 136 | 1593 | 1457 | .915 | 2.06 | 6 | 4 | 3957:43 | 69 | 25 | 4 |
| 47 | NaN | Los Angeles Kings | 17 | 8 | 7 | 1 | 39 | 437 | 398 | .911 | 2.37 | 1 | 2 | 988:12 | 22 | 10 | 1 |
| 48 | NaN | Minnesota Wild | 11 | 7 | 2 | 2 | 26 | 312 | 286 | .917 | 2.49 | 1 | 0 | 626:40 | 20 | 5 | 1 |
| 49 | NaN | Montreal Canadiens | 70 | 45 | 19 | 6 | 128 | 1818 | 1690 | .930 | 1.83 | 9 | 2 | 4188:56 | 63 | 22 | 3 |
| 50 | NaN | Nashville Predators | 14 | 7 | 6 | 1 | 35 | 368 | 333 | .905 | 2.48 | 1 | 0 | 847:52 | 25 | 10 | 0 |
| 51 | NaN | New York Islanders | 91 | 52 | 28 | 9 | 195 | 2217 | 2022 | .912 | 2.22 | 10 | 6 | 5273:49 | 94 | 47 | 9 |
| 52 | NaN | New York Rangers | 101 | 49 | 32 | 20 | 217 | 2600 | 2383 | .917 | 2.17 | 9 | 12 | 6002:31 | 120 | 41 | 5 |
| 53 | NaN | Ottawa Senators | 69 | 37 | 24 | 7 | 150 | 1768 | 1618 | .915 | 2.20 | 6 | 8 | 4094:20 | 104 | 19 | 2 |
| 54 | NaN | Philadelphia Flyers | 92 | 50 | 31 | 10 | 216 | 2356 | 2140 | .908 | 2.37 | 12 | 10 | 5465:23 | 124 | 41 | 3 |
| 55 | NaN | Arizona Coyotes | 22 | 12 | 9 | 1 | 47 | 547 | 500 | .914 | 2.21 | 4 | 0 | 1275:51 | 24 | 5 | 2 |
| 56 | NaN | Pittsburgh Penguins | 84 | 48 | 28 | 5 | 193 | 2018 | 1825 | .904 | 2.45 | 9 | 18 | 4728:26 | 111 | 37 | 3 |
| 57 | NaN | San Jose Sharks | 20 | 10 | 8 | 2 | 49 | 479 | 430 | .898 | 2.45 | 0 | 8 | 1199:13 | 27 | 8 | 1 |
| 58 | NaN | St. Louis Blues | 16 | 9 | 5 | 2 | 40 | 431 | 391 | .907 | 2.46 | 1 | 4 | 975:18 | 17 | 3 | 0 |
| 59 | NaN | Tampa Bay Lightning | 66 | 39 | 17 | 8 | 136 | 1648 | 1512 | .917 | 2.10 | 6 | 0 | 3887:33 | 79 | 26 | 2 |
| 60 | NaN | Toronto Maple Leafs | 53 | 22 | 20 | 10 | 135 | 1388 | 1253 | .903 | 2.54 | 3 | 4 | 3185:42 | 87 | 29 | 4 |
| 61 | NaN | Vancouver Canucks | 18 | 6 | 12 | 0 | 50 | 409 | 359 | .878 | 2.86 | 1 | 0 | 1047:09 | 31 | 6 | 0 |
| 62 | NaN | Winnipeg Jets | 43 | 25 | 9 | 8 | 88 | 971 | 883 | .909 | 2.10 | 7 | 8 | 2511:31 | 63 | 20 | 5 |
| 63 | NaN | Washington Capitals | 62 | 40 | 17 | 4 | 141 | 1496 | 1355 | .906 | 2.32 | 6 | 6 | 3651:32 | 77 | 21 | 3 |

</div>

In the above code, we can see the cleaning of the dataframe in order to
make things easier to read and view. Without the cleaning there is a lot
of stats that are in the columns/rows that are not actually data points,
but are actually sub headers that Hockey Reference is using to separate
different sections of Brodeur’s career. By excluding these, we get a
much cleaner and readable dataframe that we can then use for our
analysis.
