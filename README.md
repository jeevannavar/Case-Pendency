# Case-Pendency
An interactive visualization of case pendency in Indian courts

### Data Source

I obtained (scraped) the data from the National Judicial Data Grid, on Friday, the 29th of January, 2021. Case pendency for District and Taluka courts are available here: <https://njdg.ecourts.gov.in/njdgnew/>.

I obtained the map and population data from ArcGIS hub, here <https://hub.arcgis.com/datasets/esriindia1::demographics-of-india>. The data source is esri and can be checked out using the living atlas service here <https://livingatlas.esri.in/server/rest/services/LivingAtlas/IND_Demography/MapServer/0>.


### Methods

I've used R and RStudio to create these visualizations. I've been learning these visualization skills as part of a Coursera course on [Data Visualization and Dashboarding with R](https://www.coursera.org/specializations/jhu-data-visualization-dashboarding-with-r), and this is my first independent project. Do checkout the course. It's plenty useful.

I've used the `rvest` and `xml2` R packages to scrape the data from the National Judicial Data Grid, where the data were stored as html tables on multiple webpages. I've used `tidyverse`, `flexdashboard`, `shiny`, `plotly`, `sf`, `ggrepel`, and `scales` R packages and their dependencies for the dashboard itself. 

### This repository

This repository contains two folders: Data Scraping and Final Visualization. The Data Scraping folder contains an R Markdown file containing code to scrape the  data from the National Judicial Data Grid and some additional manually curated files required for data scraping and processing. The Final Visualization contains the processed data and the R Markdown file which forms a Shiny Flexdashboard. You can download the repository and run the R Markdown file on your computer or find it online at <jeevannavar.shinyapps.io/Pending_Cases_Dashboard>.
