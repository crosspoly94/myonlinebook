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

Two basic mathematical concepts will be used in this analysis and here gives a brief review of them.

## Inflation Adjusted Gross Income(IAGI)

AGI can be calculated by this equation:

```{math}
:label: eq_label
IAGI=GI \times (1+IR)

IR=((B-A)/A) \times 100

```

```{note}
- A=Starting cost
- B=Ending cost
- GI=Gross income
- IAGI=Inflation adjusted gross income
- IR=Inflation rate
```

         
## Mean value

The mean is the average of the numbers.It is easy to calculate: add up all the numbers, then divide by how many numbers there are. In other words it is the sum divided by the count. Mathematically, the definion of the mean value can be explained by the following equaiton.

$$
\begin{equation}
\bar{x}=\frac{x_{1}+x_{2}+\cdots+x_{n}}{n}
\end{equation}
$$ (my_other_label)

In python, the mean can be calculated by the following codes:

```{code-cell}
numbers = [1,2,3,4,5]

x = sum(numbers)/len(numbers)
print("Mean is :", x)
```
Also, mean() function can be used to calculate mean/average of a given list of numbers shown as follows:

```{code-cell}
import statistics
numbers = [1,2,3,4,5]

x = statistics.mean(numbers)
print("Mean is :", x)
```


## Dataset description

The below descripitions were taken directly from the website where the datasets were obtained.

```{margin} Did you know?
The highest grossing income Disney movie in history
```

This database contains information on the films regarding their genre, actors, directors, and yearly gross income which can be found in different datasets. The Disney dataset is composed of 5 tables, disney_movie_total_gross.csv, disney_revenue_1991-2016.csv, disney_characters.csv, disney_directors.csv, disney_voice_actors.csv. Each table is stored in a .csv file and contains different information about disney movies including genre, actors, directors, yearly gross income, and so forth. 

```{note}
I will be using the disney_movie_total_gross table formally described below:

* **disney_movie_total_gross.csv**
    * This file contains information on Disney movies, including moive titles, release date, genre, MPAA rating, total_gross, inflation_adjusted_gross. 

```

 




