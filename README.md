# Coffee Lover Blog

Coffee Lover Blog is a vibrant online community that serves as a haven for coffee enthusiasts to share and celebrate their passion for the world's favorite caffeinated beverage. Our platform invites users from around the globe to indulge in the rich tapestry of coffee culture by exchanging personalized coffee recommendations, detailing memorable brewing experiences, and engaging in lively discussions about the nuances of various coffee blends. With a sleek and user-friendly interface, Coffee Lover Blog ensures a seamless experience for both novices and seasoned coffee aficionados alike. 

Our platform encourages users to create accounts, fostering a sense of community where members can interact, comment on each other's posts, and build connections with fellow coffee lovers. Admins have the power to curate the platform, ensuring a positive and inclusive environment. 

Whether you're seeking the perfect espresso recipe or eager to share your latest coffee discovery, Coffee Lover Blog is the ultimate destination for all things coffee-related. 

![Website Image](/static/images/responsiveness.png)

## Website Requirements

### Target Audience

- Coffee enthusiasts who want to share their love and knowledge about coffee
- People who aren't as knowledgable about coffee but want to know more
- People who'd like to make friends with people who have the same interests
- Blog readers in general who want are just interested in reading other people's interests

### User Stories

- As a user, I want to log in to my account to participate in discussions and share my favourite coffee experiences.
- As a user, I want to know the main function of the site
- As a user, I want to be recognised as a top contributor based on the number of quality posts I make.
- As a user, I want to be able to delete my own comments when I want
- As a user, I want to access the website's content and comments without having to log in all the time

## Agile Methodology

- The agile methodology is a flexible and iterative approach to software development that prioritises collaboration, customer feedback, and the ability to respond to change. 
- User stories were used to manage the website's progression.


## Design

### Colour Scheme

- These colors collectively create a warm and inviting palette that aligns with the cozy and comforting theme of a coffee lover's blog. The combination of rich, yet subtle, brown font and creamy beige captures the essence of coffee. Subtle grey serves as a neutral background to ensure readability and visual balance.
- It doesn't look like a typical coffee blog website, drowned with different shades of brown, but the subtle and soft touch of these neutral colours, including a hint of brown (the text), allows invites the user to a mature and sleek look for the website.

![Website Image](/static/images/colourtheme.png)

## Features

### Navbar

- Coffee Lover Blog header links back to homepage, as well as the home button
- Comments page to take users to the blog comments
- Login button to take user to the login page
- Register button to take user to the register page
- Navbar present in all pages

- ![Navbar](/static/images/navbar.png)

### Footer

- Footer present in all pages

- ![Footer](/static/images/footer.png)

## Pages

### Homepage

![Homepage Info](/static/images/home-info.png)

- Contains information about what the website is for

![Recommendations](/static/images/recomm.png)

- Recommendations for coffee enthusiasts

![Contributers](/static/images/top.png)

- Users who have contributed the most comments

![Logged in user](/static/images/usercomment.png)

- Logged in users are able to see this so they can add comments

### Comments

![Comments](/static/images/comments.png)

- Comments are available to see for users and non users. 

- A logged in user is only able to see a delete and edit button on their own comment

- Any visitor of the site is able to see the name of the user, as well as the date and time it was posted


### Login Page

![Login](/static/images/login.png)

- This is where the user signs into their account


### Register

![Register](/static/images/register.png)

- This is where a visitor decides to be part of the community and signs up to be part of the blog

### Features left to implement

- May need a page that includes detailed information about different types of coffees
- May add an option to like other comments
- May add an option to comment underneath another user's comment directly

## Languages

- HTML
- CSS
- Javascript
- Python

## Testing

![Testing](/static/images/test.png)

## Frameworks and Libraries

### Django Framework:

- Purpose: Django is a high-level Python web framework that follows the Model-View-Controller (MVC) architectural pattern. It simplifies the development of web applications by providing a structured and reusable codebase.
- Usage in Coffee Lover Blog: Django is the primary framework for handling HTTP requests, managing database models, rendering templates, and handling user authentication.

### Bootstrap:

- Purpose: Bootstrap is a popular front-end framework that provides a collection of pre-designed HTML, CSS, and JavaScript components. It simplifies the process of creating responsive and visually appealing web pages.
- Usage in Coffee Lover Blog: Bootstrap is used for styling the user interface of the Coffee Lover Blog, ensuring a consistent and mobile-friendly design.

### Cloudinary:

- Purpose: Cloudinary is a cloud-based media management solution that provides image and video storage, optimization, and delivery services. It allows for easy integration of media assets into web applications.
- Usage in Coffee Lover Blog: Cloudinary may be used for handling the storage and optimization of coffee-related images in the blog.

### Gunicorn:

- Purpose: Gunicorn is a WSGI HTTP server for running Python web applications. It is commonly used to deploy Django applications in production.
- Usage in Coffee Lover Blog: Gunicorn could be used as the server to deploy the Coffee Lover Blog in a production environment.

## Tools

- Heroku: where the app is getting deployed 
- ElephantSQL: PosgreSQL database
- ChatGPT: used occasionally for support, certain requirements as well as to fix bugs
- Gitpod: where the code is based
- Github: hosts Git repositories

## Unfixed Bugs

- When the screen is at mobile size, the navbar turns into a dropdown feature but it isn't opening when clicked.

## Deployment

1. Go on the Heroku site and log in
2. Click 'create new app'
3. Create a name for the app and choose the region
4. Go to settings and click Reveal Config Vars
5. Input the keys and values in your env.py into the Config Vars, including PORT 8000
6. Add buildpacks: Python
7. Preferably, click automatic deployment so it deploys everytime git is pushed
8. Click Deploy

## Credits

- Thank you to everyone on Slack and those on Tutor support who have continously helped me during this time. It definitely has been the most challenging project so far.
- ChatGPT was an immense and great help. It provided me with resolutions to bugs/errors, tips and resources which led me to the right direction. 










