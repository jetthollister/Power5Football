# Power 5 Football Conferences
A quantitative analysis and redistribution of the NCAA  Division I football athletic conferences

## Problem Overview

### Understanding the Power 5

The Power 5 refers to five football conferences within the Football Bowl Subdivision (FBS) of the NCAA Division I, including the Atlantic Coast Conference (ACC), Big Ten Conference (B1G), Big 12 Conference, Pac-12 Conference, and Southeastern Conference (SEC)1 (Figure 1). The logic behind the current organization of schools is unknown and struggles to stay in tune with high-performing teams. Through application of both university- and athletics-level data, a clustering algorithm was designed to group Power 5 schools into their current conference. An understanding and automation of the conference groupings, which are based on a range of interdisciplinary factors, could produce a more streamlined process for adding new schools to the Power 5 or redistributing present ones.

Once an accurate clustering process had been generated, the algorithm was used to assign FBS independent programs, four-year institutions whose programs are not included in an NCAA-affiliated conference, to a Power 5 conference. These schools (University of Massachusetts-Amherst, Brigham Young University (BYU) and the University of Notre Dame) currently play against programs within the Power 5 conferences despite the fact that they are not members.

#### Redesigning the Power 5

Coming to an understanding on the factors that define the Power 5 structure also resulted in having a better grasp of its flaws. With these in mind, a new structure for the Power 5, both on a macro and micro scale, was explored. Through combination of athletic and academic data, an original set of criteria was conceived, and the current Power 5 schools were redistributed according to the new logic. 

### Datasets

#### [Integrated Postsecondary Education Data System](https://nces.ed.gov/ipeds/datacenter/InstitutionByName.aspx?goToReportId=1)

  Offers a range of statistics at the university and academic level, including, but not limited to, admission rates, latitude/longitude, research funding, financial aid, and graduation rates. The database is maintained by the National Center for Education Statistics. While there are a myriad of features offered in the database, only those related to admissions, financial aid, undergraduate population size, and location were considered for use in this project. 
  
---

### [Equity in Athletics Data Analysis](https://ope.ed.gov/athletics/#/customdata/search)

Focuses on university athletic program statistics, including program size, revenue, classification, and operating costs. The dataset was curated by the U.S. Department of Education. The Equity in Athletics Data Analysis (EADA) dataset offers important insights into the financial side of football programs and provides the ability to derive insights into the size of a school’s media market. A program’s ability to generate revenue directly correlates to their capacity to support their players and staff.

---

### [College Football Team Stats 2019](https://www.kaggle.com/jeffgallini/college-football-team-stats-2019)

Provides 145 team statistics for all 130 NCAA FBS level teams, including offensive, defensive, turnover, red zone, special teams, first down, third down, and fourth down stats. The data was scraped, cleaned, and coded from the NCAA statistics website by Jeff Gallini. While the dataset provides an in-depth look into play-by-play data for each team, only the aggregate measures of the 2019 football season were considered to control dimensionality and preserve the clustering accuracy.

## Understanding the Power 5

### Feature and Distance Metric Selection

- Feature Selection: The features reflected a combination of both general and athletic metrics, but primarily focus on the location and finances of each school’s football program. As shown by both the region-based names of the Power 5 conferences and their current distributions, location proved to be a strong indicator for each conference. The features attempted to cover all management aspects of the football program, including their size, revenue, and cost of operation. These metrics provided the best picture of a school’s “market” and offered further indications into the prestige of their football program.

- Scaling: To prevent large-valued features from dominating the decision-making, features were scaled to ensure that all criteria contributed equally. Min-Max scaling (below), also referred to as normalization, scaled the data to values between 0 and 1. While this suppressed range can reduce the impact of outliers, it ensured the algorithm’s decision making was not skewed by large features.

<a href="https://www.codecogs.com/eqnedit.php?latex=X_{sc}=\frac{X-X_{min}}{X_{max}-X_{min}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?X_{sc}=\frac{X-X_{min}}{X_{max}-X_{min}}" title="X_{sc}=\frac{X-X_{min}}{X_{max}-X_{min}}" /></a>

- Weighting: Since the features were normalized, weights were able to be applied to individual measures to increase their respective share on the clustering algorithm’s decision making. To fine tune these weights, a scoring metric was devised to gauge how well a combination of weights grouped schools. The metric, which found the percentage of schools that were assigned to the correct conference, allowed weights to be optimized by an exhaustive search.

### Performance

The k-means algorithm was able to group Power 5 conference schools into their correct conference with 79.69% accuracy (Figure 3). The algorithm likely struggled to reach a higher accuracy because football programs have repeatedly moved conferences and developed disproportionately, which made reaching 100% accuracy nearly impossible for the algorithm. It also struggled to place smaller-market schools (Vanderbilt) into their large-market conferences (SEC), but was able to capitalize on location similarities (Pac-12).

## Redesigning the Power 5

### Performance-Based Conferences

### Assessment of a Performance-Based Power 5 
