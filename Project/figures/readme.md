# graphs
Firest off the graphs were plotted with datastudio.
The problem I had with datastudio was that I had to process alot of the data before hand, and coudn't sum up,m or aggregate the data like I needed.


[Here is a link to tthe report](https://datastudio.google.com/embed/reporting/1c4qP_OnsTjOXpLOW9RgIkri9FjE4GrWo/page/B4aM)

Then I decided to use pandas, that can directly plot graphs using python.

This choice was smarter because I didn't have to reimport my data all the time, and could modify the groupngs, etc...

This lead to the following plots:

1. Number of claims per month

![fig1](exploratory/1.png)

2. Total delays per month, per airline

![fig2](exploratory/2.png)

With a bit of filtering out only the 10 biggest

![fig2](exploratory/2.png)

3. Total amount of value lost by company

![fig3](exploratory/3.png)

Sorted this gives

![fig3](final/3.png)

4. Mean average of delays per month, per airline

![fig4](exploratory/4.png)

5. Most valuable lost item per airline

![fig5](exploratory/5.png)

Sorted and taken only the 10 biggest ones gives us:
![fig5](exploratory/5.png)

6. Final graph

![](final/6.png)