Relationships in Consumption of calories, Health policies and GDP
Team name: LEG
Team member: Chen Luo, Eugene Koh, Georgina Fornés Albors

The project explores the relationship between economic development, health spending and food supply. The basic assumption is that the health spending and food supply are highly positive correlated with the income level. The folder named 'dataproject' contains seven documents: a README file, a notebook file and five dataset in both csv and excel format.

To study that, we import four datasets from https://www.gapminder.org/data/， which contains statistics of GDP per capita, total GDP, total health spending as a percentage of GDP and food supply for countries all over the world. To be more specific, food supply is measured by kilocalories /person & day. And GDP per capita and total GDP are in constant 2010 US dollars. The time-horizon of the datasets are different and will be adjusted in the project. The fifth dataset is an excel file which contains all the countries of the world and some information regarding them.

To make the indicators comparable, we drop the countries with missing data and select the years which are included in all dataset. Thereby, we end up with 150 countries and the period of study is from 1995 to 2010. Furthermore, we calculate the mean and median for each country over the 16 years to have an overview of each country.

After cleaning the data, we demonstrate the relationship between the economic indicators and health indicators by 8 graphs. More details of each graph are in the notebook. The first set of graphs is based on the mean of the indicators for each countries. That is, the overall relationship between different indicators, regardless of the fluctuation over the years. In addition, we group countries by regions to have an overview of each region. Finally, we select one country in each region and depict the correlation of GDP per capita and health spending / food supply over the 16 years.
