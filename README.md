
A very basic URL Shortener Django web app set up to deploy on Heroku with a Postgres database.

Key Development Decisions:

1. NO ReactJS on the front end. I first set up the front end using a Django form. This is my first time using Django, and I was quite impressed how simple this is! Then I started reading about React. I supperficially added it to the front end, which caused a bug and added no functionality. From the bug, it was clear that if I was going to use React, I needed a better understanding of React's event handling. I didn't have time to dig deep into this and do it right, so I left it as Django on the front end. Also, I have some deeper confusion about what the best practices are for using ReactJS and Django together; that is, where should one end and the other begin? I think it was probably intended that I not use a Django form and instead do the whole form in React? What benefit would I have gotten from using React? In such a simple app, does using React improve the product?

2. Only supports http, https, ftp, ftps. Why? Just because I am not really familiar with other protocols or if a URL shortener whould work with them. I'd like to do more reading to make sure there are no security or implementation concerns. Really, overall, I am not convinced I've adressed possible security concerns. Probably somewhere out there on the internet there is a nice list of (security-related) questions to ask oneself when "creating a web app with user input going into a database" that I would very much like to find.

3. Custum URL keys. I think it could be fun sometimes for the user to pick their own key. BUT a lot of users probably don't care, and they need to be unique, so... ideally, I'd add the following to my implmentation:
        a. A 'Suggest' button on the front end, that runs 
        b. A 'generateSuggestion' method on the backend that hashes the full URL and returns a not-yet-used random-seeming key, and then
        c. That valid suggestion populates the key field on the front end
    It's too bad I didn't get to this because it probably would have been the most fun part of the project!