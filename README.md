# 🌼 MCTS (Movies, Celebrities and TV Shows)
### A Django-based application that allows users to browse and participate in volunteer events across various categories. Users can register, login, add events to favourites, attend events, and more.
### Recommended resolution on computer: 1920x1080
### Recommended resolution on phone: <600px

## ✨ Features
### 🔐 Authentication
- **Register**: Users can register, providing First Name, Last Name, Email, Password and Confirm Password - error messages are displayed if the values are not in the correct format. Users can also register with Google.
- **Login**: Users can log in to their account after it has been created. Users can also login with Google.
- **Logout**: Users can log out of their accounts after they have been logged in.



### 📌 Header
- **Navigation Buttons**:
  - **Home**: Redirects to the `Home` page.
  - **About Us**: Redirects to the `About Us` page.
  - **Contact Us**: Redirects to the `Contact Us` page.
  - **Search Bar**: Allows users to `Search` for movies.
  - **Contact Us**: Redirects to the `Contact Us` page.
  - **User Authentication Buttons**:
    - **Log In**: Displays a login button if the user is not logged in.
    - **Sign Up**: Displays a sign up button if the user is not logged in.
    - **User Dropdown Menu**: Displays a dropdown with the user's profile image if logged in, which includes links to:
      - **Profile Details**: Redirects to profile details page.
      - **Watchlist**: Redirects to user's watchlist page.
      - **Log Out**: Allows users to log out.




### 🏠 Home Page
- **Upcoming events**: See a part of the upcoming events.
- **Explore categories**: See all categories and explore them one by one.
- **Popular Cities on VolunteerAct**: See first six popular cities that have the most attendees.
- **Discover Events**: Section with a link that redirects to the events page.
- **Create an Event**: Section with a link that redirects to the create event page.






### Category Page
- Short and long descriptions of the category.
- Number of events and members; Some of the cities that the events take place at.
- Part of the upcoming events in the category.
- Part of the past events in the category.
- Active members - members that participate in events in the category.
- Photos section - photos of the events in this category.
- Upload a photo - only active members of the category are allowed to upload a photo.






### Event Page
- Title and details of the event.
- Category, city, location, online link (if online event) displayed.
- `Save Event to Favourites` button for logged in users.
- `Edit` and `Delete` for author of the event and admin (user who is from the staff_members group or is superuser)
- Comments section - only first three comments are displayed and every logged in user can add a new comment.
- Edit and delete comment - for author of the comment and admin (user who is from the staff_members group or is superuser).
- Attend button - for every logged in user except for the author because he is already attending the event.
- Share button - for every kind of users.
- See more section - displays other events from the category.
- After clicking the `Delete` button, a container is displayed on the page which asks for the confirmation for the deletion from the user.





### Edit Event Page
- Only the author of the event, a user of the 'staff_members' group or a superuser can access this page.
- The user can change the title, poster image, details, time, city, location and online meeting link (if the event is online).






### City Page
- Short description of the city.
- Displays upcoming and past events in the city.






### Explore Events Page
- Only logged in users have access to this page.
- All events displayed.
- A search bar which allows users to search for an event case-insensetively.
- Filters for category, city and time.






### Create An Event Page
- Only logged in users have access to this page.
- User needs to provide category, image, title, city and location (if the event is not going to be online), online meeting link (if the event is going to be online), time and details.






### Emergency Events
- Everyone has access to this page.
- This page is dedicated to urgent events.
- An event in this category becomes no longer urgent only when it is deleted.
- `Add Emergency Event` button - only logged in users can add emergency events.
- When an emergency event is added, all active members of its category will be notified by receiving an email.





### About Us Page
- Provides more information about VolunteerAct and what you can do in it.





### Contact Us Page
- A form for contacting the team of VolunteerAct through email. User needs to add his full name, email, subject and message.
- Contact information - phone number, email, location, social media links
- Location with a map





### Favourites Page
- Dislays all the events that the users has saved to favourites.
- A search bar which allows users to search for an event case-insensetively.
- Filters for category, city and time.





### Tickets Page
- Displays all the events that the user is attending.
- A search bar which allows users to search for an event case-insensetively.





### My events Page
- Displays upcoming and past events that the user has created.
- Attending participants in the events that the user has created.





### Profile Page
- If the profile is of the currently logged in user, a form for editing will be displayed. The user can change his profile picture, first name, last name, phone number, email and bio.
- If the profile is not of the currently logged in user, a page with the information for the specific user will be displayed.
- `Delete` button - redirects to the delete profile page.













