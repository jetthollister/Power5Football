<h1 align="center">Power 5 Football Clustering</h1>

A quantitative analysis and redistribution of five football conferences within the Football Bowl Subdivision (FBS) of the NCAA Division I, including the Atlantic Coast Conference (ACC), Big Ten Conference (B1G), Big 12 Conference, Pac-12 Conference, and Southeastern Conference (SEC). The final slidedoc presentation can be found under `Power_5_Slidedoc.pdf`.

### Datasets

- [Integrated Postsecondary Education Data System](https://nces.ed.gov/ipeds/datacenter/InstitutionByName.aspx?goToReportId=1): Offers a range of statistics at the university and academic level, including, but not limited to, admission rates, latitude/longitude, research funding, financial aid, and graduation rates. The database is maintained by the National Center for Education Statistics.
- [Equity in Athletics Data Analysis](https://ope.ed.gov/athletics/#/customdata/search): Focuses on university athletic program statistics, including program size, revenue, classification, and operating costs. The dataset was curated by the U.S. Department of Education.
- [College Football Team Stats 2019](https://www.kaggle.com/jeffgallini/college-football-team-stats-2019): Provides 145 team statistics for all 130 NCAA FBS level teams, including offensive, defensive, turnover, red zone, special teams, first down, third down, and fourth down stats. The data was scraped, cleaned, and coded from the NCAA statistics website by Jeff Gallini.

## Approximating the Current Power 5

### Feature and Distance Metric Selection

- Feature Selection: The features reflected a combination of both general and athletic metrics, but primarily focus on the location and finances of each school’s football program. The features attempted to cover all management aspects of the football program, including their size, revenue, location, and cost of operation. These metrics provided the best picture of a school’s “market” and offered further indications into the prestige of their football program.

- Scaling: To prevent large-valued features from dominating the decision-making, features were normalized between 0 and 1 to ensure that all criteria contributed equally.

- Weighting: Since the features were normalized, weights were able to be applied to individual measures to increase their respective share on the clustering algorithm’s decision making. To fine tune these weights, a scoring metric was devised to gauge how well a combination of weights grouped schools and an exhaustive search found the optimal weights.

### Performance

The k-means algorithm was able to group Power 5 conference schools into their correct conference with 79.69% accuracy. The algorithm likely struggled to reach a higher accuracy because football programs have repeatedly moved conferences and developed disproportionately, which made reaching 100% accuracy nearly impossible for the algorithm. It also struggled to place smaller-market schools (Vanderbilt) into their large-market conferences (SEC), but was able to capitalize on location similarities (Pac-12).

<p align="center">
  <img src="https://github.com/jetthollister/Power5Football/blob/master/pics/Power%205%20Conference%20Distributions%20with%20Independets.png" width="750" />
</p>

## Redesigning the Power 5

### Performance-Based Conferences

- Feature Selection: The features reflected an intense focus on team statistics and performance from only the year previous. The forgetful system aimed to provide all teams with an equal opportunity for a competitive season and gave no consideration to the history of their team or the revenue of their program. The features, which include point spread per game (ratio of points scored to points scored by opposing team), win percentage, offensive rank, defensive rank, and yard spread per game (ratio of yards gained to yards gained by opposing team), attempted to fully capture the overall performance of a team while minimizing dimensionality. 

- Weighting: No weights were assigned to the features, as each performance metric should hold equal weight to ensure that highly-ranked teams are well-rounded across all observed metrics.

- Considerations: While the features selected attempted to group schools into conferences based on their current level of play, the performance-based system as it is proposed would require adjusted inputs to ensure an accurate and stable Power 5 in the long run. This system will have an immediate normalization effect on the metrics used to determine conferences each year, as teams will be largely playing those of equal caliber. As a result, a team’s previous season conference rank and schedule difficulty will need to be fed back into the algorithm to more accurately reflect each team’s performance.

### Assessment of a Performance-Based Power 5 

- Conference Equality: A focus on statistics and performance from the previous season generated a more equitable distribution of teams. The redistribution decreased the average range in conference point spread per game from 40.38 to 15.88 and generated similar performance shifts over multiple metrics (Figure 8). Not only would this system create more competitive matchups, but it would allow for all teams of similar caliber, despite the history of their program, to compete at the highest level in NCAA Division I.

- Talent Emersion: The redistribution could have an additional impact of highlighting talent from mid- and lower-tier Power 5 schools. These programs, who are traditionally dominated by the elite schools in their conferences, would now have the opportunity to showcase their athletes and coaching staff against teams of similar caliber.

Before             |  After
:-------------------------:|:-------------------------:
 <img src="https://github.com/jetthollister/Power5Football/blob/master/pics/Point%20Spread%20by%20Current%20Conference.png" width="500" /> |  <img src="https://github.com/jetthollister/Power5Football/blob/master/pics/Point%20Spread%20by%20New%20Conference.png" width="500" />

