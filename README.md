# Joes-Apartments
Web service that provides apartment listings to users based on search criteria
## Web Page
Apartments.html provides a structured web page with drop down menus to filter the users apartment search. Once the serch button is clicked the search is executed using the current values of bedrooms, a custom search, and price sorting.
## JavaScript
The JavaScript pulls the search values and passes them to the python filtering methods. The apartments that meet the search criteria are then passed the web page using the apt_search_results method.
## Web Service
The web service which is provided by pythonanywhere.com provides the link between the JSON database and the JavaScript by searching the JSON file for apartments that meet the search criteria and relaying them to the apt_search_results method in script.js.
## Database
apartments.json provides a database functionality for this web page. It currently holds 10 fake apartment listings.

