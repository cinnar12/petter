# Petter (View in Mobile)
Petter is a pet browsing app dedicated to helping you find the perfect companion. The app allows you to look through dogs and cats available for adoption in the Gainesville area with the ease and familiarity of a certain mobile app. Best viewed on iPhone or on Chrome DevTools set to iPhone 6/7.

Purrfect for if you've just moved to Gainesville for college and are looking for a furry friend. Or even if you are in your last semester, have developed a sense of responsibility and would rather not deal with people. Adopting has many benefits for both you and your pet! 

## Process
I began with testing my scraping program (made with BeautifulSoup) to retrieve information from some local shelter websites. I created a .csv file that contained information about each available pet such as their ID, Name, Age, Weight, etc.

Then, I began building the app. I carefully chose the colors and included my own vector graphics to define the app's branding. I created a single .html file and several divs for each section/page I wanted to include in the app. I used Swiper.js to enable swiping on the app, and you can navigate it by either clicking or swiping. JQuery was used to make the divs hide and show depending on button press.

## Problems Encountered (Too Many to Count)
Due to online pet adoption API's Terms of Services, I was unable to scrape as many sites as I would had plan when I initially came up with the project. In addition, a lot of the features (primarily the Flask and certain app functions I wanted to include) weren't possible in the limited time that I had. I really struggled with trying to figure out how to implement Flask/Jinja and Ajax together to update what could be viewed and filter results based on the form. Working with Swiper.js was convenient but also challenging as I nested more swipers.

Also, weirdly the cPanel Python Setup didn't work for me so the app doesn't load up at [my page](https://www.tho-tran.com/petter/). I've set up the files without the Python at [this page instead](https://tho-tran.com/petter/petter/index.html). The JQuery (list adding, element destroying, etc) also strangely works better here than with the Python scripts on the localhost:5000, but you can't see the elements here to see them get destroyed.

## Future Development
Overall, it was quite a challenging project, and I am disappointed that I wasn't able to finish it sooner. I'm still relatively new to the whole web dev thing. However, I still plan to keep updating this. I really want to fix most of the issues and understand them better to grow as a developer.