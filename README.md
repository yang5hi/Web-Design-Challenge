# Web Visualization Dashboard (Latitude)
The purpose of this project was to analyze how weather changes as you get closer to the equator. To accomplish this analysis, I first pulled data from the OpenWeatherMap API to assemble a dataset on over 500 cities.

After assembling the dataset, I used Matplolib to plot various aspects of the weather vs. latitude. Factors I looked at included: temperature, cloudiness, wind speed, and humidity. This site provides the source data and visualizations created as part of the analysis, as well as explanations and descriptions of any trends and correlations witnessed.

## HTML and CSS (Bootstrap)

In building this dashboard, I created individual pages for each plot and a means by which I can navigate between them. These pages will contain the visualizations and their corresponding explanations. I also have a landing page, a page where you can see a comparison of all of the plots, and another page where you can view the data used to build them.

The website consists of 7 pages total, including:

* A landing page containing:
  * An explanation of the project.
  * Links to each visualization page. There should be a sidebar containing preview images of each plot, and clicking an image should take the user to that visualization.
* Four visualization pages, each with:
  * A descriptive title and heading tag.
  * The plot/visualization itself for the selected comparison.
  * A paragraph describing the plot and its significance.
* A "Comparisons" page that:
  * Contains all of the visualizations on the same page so we can easily visually compare them.
  * Uses a Bootstrap grid for the visualizations.
* A "Data" page that:
  * Displays a responsive table containing the data used in the visualizations.

The website also, at the top of every page, have a navigation menu that:

* Has the name of the site on the left of the nav, which allows users to return to the landing page from any page.
* Contains a dropdown menu on the right of the navbar named "Plots" that provides a link to each individual visualization page.
* Provides two more text links on the right: "Comparisons," which links to the comparisons page, and "Data," which links to the data page.
* Is responsive (using media queries).
