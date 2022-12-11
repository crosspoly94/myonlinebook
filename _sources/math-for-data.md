---
jupytext:
  cell_metadata_filter: -all
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Mathematical Processing of Data 

Two basic mathematics will be used in this analysis and here gives a brief review of them.

## Inflation Adjusted Gross Income(IAGI)

AGI can be calculated by this equation:

```
IAGI=GI(1+IR)
IR=((B-A)/A)\times100

```
where,
- A=Starting cost
- B=Ending cost
- GI=Gross income
- IAGI=Inflation adjusted gross income
         
## Mean value

The mean is the average of the numbers.It is easy to calculate: add up all the numbers, then divide by how many numbers there are. In other words it is the sum divided by the count. Mathematically, the definion of the mean value can be explained by the following equaiton.

$$
\begin{equation}
\bar{x}=\frac{x_{1}+x_{2}+\cdots+x_{n}}{n}=\frac{1}{n}\left(\sum_{i=1}^{n}{x_i}\right)
\end{equation}
$$

## Dataset description

The below descripitions were taken directly from the website where the datasets were obtained.

"The Walt Disney Studios is an American film and entertainment studio, and is the Studios Content segment of the Walt Disney Company. Based mainly at the namesake studio lot in Burbank, California, the studio is best known for its multifaceted film divisions. Founded in 1923, it is the fourth-oldest and one of the "Big Five" major film studios"{cite}`McKittrick`.

This database contains information on the films regarding their genre, actors, directors, and yearly gross income which can be found in different datasets. The Disney dataset is composed of 5 tables, disney_movie_total_gross.csv, disney_revenue_1991-2016.csv, disney_characters.csv, disney_directors.csv, disney_voice_actors.csv. Each table is stored in a .csv file and contains different information about disney movies including genre, actors, directors, yearly gross income, and so forth. I will be using the disney_movie_total_gross table formally described below:

* **disney_movie_total_gross.csv**
    * This file contains information on Disney movies, including moive titles, release date, genre, MPAA rating, total_gross, inflation_adjusted_gross.  




