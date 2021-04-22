# Tasks

#### Preliminary remark

There is no right or wrong way to solve the tasks. We are not looking for fancy presentations or highly efficient code,
but for an impression of your working style. Please present the results as you would show them to a colleague in
everyday life. Develop one or more executable programs/scripts with Python, whether command line driven or with GUI is
up to you.

## 1. Task: API Implementation and Database design

a. Implement the PS01 API from Marine Traffic and retrieve the hourly position data (simple) of two consecutive days
from this year for the vessels with MMSI '269057489' and '269057500'.   
b. Read the attached CSV data.   
c. Create a database with an appropriate structure in which you store the data sets from (a.) and (b.).

- Allow a user to add additional records directly to the database using an MMSI and a time window.
- Note: When you create a free account at marinetraffic.com, you will receive 100 credits, which you can use to test and
  retrieve the required data. API
  documentation: https://www.marinetraffic.com/en/ais-api-services/documentation/api-service:ps01

## 2. Task: Webcrawling

Read the technical specifications for all engines
at https://www.finning.com/en_CA/products/new/power-systems/electric-power-generation.html
and add these data to the existing database in a meaningful way. Required data are Min. rating, Max. Rating, Voltage,
Frequency, Speed.

## 3. Task: Aggregation

Answer the following questions using SQL queries (each without the data retrieved in (1 a.)):

- What is the average speed per vessel per day across all vessels?
- What was the average number of nautical miles travelled per owner during the noon period 12-14?
- Show the ranking of the engine types (engine_name) in relation to the maximum speed shown. Does this ranking
  correspond to the maximum power output from the technical specifications? Note: The timestamp only shows the entry in
  the database. The speed value is always the average of the full previous hour.
  
## For running locally

This project needs Python v3.8 to run.

1. Make and activate a virtual environment and install all the dependencies as per the `requirements.txt`.
2. Run - `python3 main.py` from the shell from the root directory of this project.
