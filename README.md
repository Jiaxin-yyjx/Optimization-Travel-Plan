# Optimization Graduating Travel Plan

### Introduction & Motivation
  Due to the travel constraints made by the officials to prevent the spreading of COVID-19, a lot of students have no choice but to cancel their travel plans made earlier. However, recently, since the vaccination was invented and the number of people who have been vaccinated is increasing, the number of new COVID-19 cases has been in a decreasing tendency, which has loosened the travel ban between states and even internationally. Since all members in our group have not traveled for more than two years and will graduate next year, we are planning to take a crazy graduation trip that travels around the United States.   
     
  As college students, when it comes to travel, we would always prefer a trip with lower spending on transportation (whether it is by flights, trains, or driving). Here, we assume that students will travel by flight as it is the most time-efficient transportation. We plan to visit 24 cities during this trip. The cost during transportation will take huge amount of our overall travel budget, so it is important for us to plan accordingly on our travel route.   
     
  The goal of this project is aimed at optimizing the route of the trip that can minimize the cost of plane tickets. It can help us save a lot of money during our graduation trip.To achieve this project, we are going to solve this as a MTSP (Multiple Traveling Salesman Problem) problem. We collected all plane tickets price data via Expedia, and we will optimize our travel route among 24 cities with certain constrains such as: the overall budget for plane tickets is $4000 and every city can only be visited once.   

## Files
- FinalProject.py: source code
- FlightData.csv: the dataset of all plane tickets
- ISE3230_Group25_Presentation.pptx: the presentation slides
- README.md

## Team Members
- Jiaxin Yang
- Ben He
- Yuyang He

## Codes and descriptions
We are trying to minimize the total flight cost of this trip under the condition that we are only going to visit each city once and that we will at least visit each city once. Therefore, we calculate the cost of flight Cij  between each pair of cities i and j. Also, we did some research and found out that according to United Airline, standard checked baggage fees for US domestic flights: First bag: $35.00 USD. We made an assumption that all the travelers will only be carrying one baggage. Thus, we added an extra 35 dollars on top of the cost for each flight. The total cost of flights for the whole trip is then the sum of the total costs of the edges included in the trip.

## Goal
In this Multiple Traveling Salesman Problem, we have a list of all cities we need to visit and a dataset containing all plane ticket price between cities. Our goal is to minimize the cost of airplane tickets with the route that can start at Columbus; travel through all cities in the city list once and turn back to Columbus. Besides that, the summation of all plane tickets cannot exceed $4000, all plane tickets are non-stop, and we cannot use other cities as a transition to our destination.

## Result
Best route:   

Columbus -> San Diego-> Washington DC -> Salt Lake City -> New York -> Las Vegas -> Chicago -> Portland -> Phoenix -> Indianapolis -> Los Angeles -> Detroit -> New Orleans -> Houston -> Nashville -> San Francisco -> Seattle -> Dallas -> Pittsburgh -> Fairbanks -> Albuquerque -> Miami -> Philiadelphia -> Denver -> Columbus    

Minimum cost: $3001.0    
