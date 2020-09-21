# Power 5 Football Conferences
A quantitative analysis and redistribution of the NCAA  Division I football athletic conferences

## Problem Overview

### Understanding the Power 5

The Power 5 refers to five football conferences within the Football Bowl Subdivision (FBS) of the NCAA Division I, including the Atlantic Coast Conference (ACC), Big Ten Conference (B1G), Big 12 Conference, Pac-12 Conference, and Southeastern Conference (SEC). The logic behind the current organization of schools is unknown and struggles to stay in tune with high-performing teams. Through application of both university- and athletics-level data, a clustering algorithm was designed to group Power 5 schools into their current conference. An understanding and automation of the conference groupings, which are based on a range of interdisciplinary factors, could produce a more streamlined process for adding new schools to the Power 5 or redistributing present ones.

Once an accurate clustering process had been generated, the algorithm was used to assign FBS independent programs, four-year institutions whose programs are not included in an NCAA-affiliated conference, to a Power 5 conference. These schools (University of Massachusetts-Amherst, Brigham Young University (BYU) and the University of Notre Dame) currently play against programs within the Power 5 conferences despite the fact that they are not members.

#### Redesigning the Power 5

Coming to an understanding on the factors that define the Power 5 structure also resulted in having a better grasp of its flaws. With these in mind, a new structure for the Power 5, both on a macro and micro scale, was explored. Through combination of athletic and academic data, an original set of criteria was conceived, and the current Power 5 schools were redistributed according to the new logic. 

### Datasets

#### [Integrated Postsecondary Education Data System](https://nces.ed.gov/ipeds/datacenter/InstitutionByName.aspx?goToReportId=1)

  Offers a range of statistics at the university and academic level, including, but not limited to, admission rates, latitude/longitude, research funding, financial aid, and graduation rates. The database is maintained by the National Center for Education Statistics. While there are a myriad of features offered in the database, only those related to admissions, financial aid, undergraduate population size, and location were considered for use in this project. 
  
---

#### [Equity in Athletics Data Analysis](https://ope.ed.gov/athletics/#/customdata/search)

Focuses on university athletic program statistics, including program size, revenue, classification, and operating costs. The dataset was curated by the U.S. Department of Education. The Equity in Athletics Data Analysis (EADA) dataset offers important insights into the financial side of football programs and provides the ability to derive insights into the size of a school’s media market. A program’s ability to generate revenue directly correlates to their capacity to support their players and staff.

---

#### [College Football Team Stats 2019](https://www.kaggle.com/jeffgallini/college-football-team-stats-2019)

Provides 145 team statistics for all 130 NCAA FBS level teams, including offensive, defensive, turnover, red zone, special teams, first down, third down, and fourth down stats. The data was scraped, cleaned, and coded from the NCAA statistics website by Jeff Gallini. While the dataset provides an in-depth look into play-by-play data for each team, only the aggregate measures of the 2019 football season were considered to control dimensionality and preserve the clustering accuracy.

## Understanding the Power 5

### Feature and Distance Metric Selection

- Feature Selection: The features reflected a combination of both general and athletic metrics, but primarily focus on the location and finances of each school’s football program. As shown by both the region-based names of the Power 5 conferences and their current distributions, location proved to be a strong indicator for each conference. The features attempted to cover all management aspects of the football program, including their size, revenue, and cost of operation. These metrics provided the best picture of a school’s “market” and offered further indications into the prestige of their football program.

- Scaling: To prevent large-valued features from dominating the decision-making, features were scaled to ensure that all criteria contributed equally. Min-Max scaling (below), also referred to as normalization, scaled the data to values between 0 and 1. While this suppressed range can reduce the impact of outliers, it ensured the algorithm’s decision making was not skewed by large features.

<a href="https://www.codecogs.com/eqnedit.php?latex=X_{sc}=\frac{X-X_{min}}{X_{max}-X_{min}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?X_{sc}=\frac{X-X_{min}}{X_{max}-X_{min}}" title="X_{sc}=\frac{X-X_{min}}{X_{max}-X_{min}}" /></a>

- Weighting: Since the features were normalized, weights were able to be applied to individual measures to increase their respective share on the clustering algorithm’s decision making. To fine tune these weights, a scoring metric was devised to gauge how well a combination of weights grouped schools. The metric, which found the percentage of schools that were assigned to the correct conference, allowed weights to be optimized by an exhaustive search. When optimizing the feature weighting, longitude (2.5) was weighted more heavily than latitude (1.5). This difference could have resulted from the shape and distribution of Power 5 schools within the U.S., which have a wider distribution longitudinally.

### Performance

The k-means algorithm was able to group Power 5 conference schools into their correct conference with 79.69% accuracy. The algorithm likely struggled to reach a higher accuracy because football programs have repeatedly moved conferences and developed disproportionately, which made reaching 100% accuracy nearly impossible for the algorithm. It also struggled to place smaller-market schools (Vanderbilt) into their large-market conferences (SEC), but was able to capitalize on location similarities (Pac-12).

## Redesigning the Power 5

### Performance-Based Conferences

- Feature Selection: The features reflected an intense focus on team statistics and performance from only the year previous. The forgetful system aimed to provide all teams with an equal opportunity for a competitive season and gave no consideration to the history of their team or the revenue of their program. The features, which include point spread per game (ratio of points scored to points scored by opposing team), win percentage, offensive rank, defensive rank, and yard spread per game (ratio of yards gained to yards gained by opposing team), attempted to fully capture the overall performance of a team while minimizing dimensionality. 

- Weighting: No weights were assigned to the features, as each performance metric should hold equal weight to ensure that highly-ranked teams are well-rounded across all observed metrics.

- Considerations: While the features selected attempted to group schools into conferences based on their current level of play, the performance-based system as it is proposed would require adjusted inputs to ensure an accurate and stable Power 5 in the long run. This system will have an immediate normalization effect on the metrics used to determine conferences each year, as teams will be largely playing those of equal caliber. As a result, a team’s previous season conference rank and schedule difficulty will need to be fed back into the algorithm to more accurately reflect each team’s performance.

### Assessment of a Performance-Based Power 5 

- Conference Equality: A focus on statistics and performance from the previous season generated a more equitable distribution of teams. The redistribution decreased the average range in conference point spread per game from 40.38 to 15.88 and generated similar performance shifts over multiple metrics (Figure 8). Not only would this system create more competitive matchups, but it would allow for all teams of similar caliber, despite the history of their program, to compete at the highest level in NCAA Division I.

- Talent Emersion: The redistribution could have an additional impact of highlighting talent from mid- and lower-tier Power 5 schools. These programs, who are traditionally dominated by the elite schools in their conferences, would now have the opportunity to showcase their athletes and coaching staff against teams of similar caliber.
