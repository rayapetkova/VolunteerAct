# 🌼 VolunteerAct
### A Django-based application that allows users to browse and participate in volunteer events across various categories. Users can register, login, add events to favourites, attend events, and more.

### Deployed version: https://volunteeract.azurewebsites.net/
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
  - **Emergency button**: Shows if there are emergency events or not. If the button flashes in red, then there are some emergency events. If the button is green, then there are no emergency events at the moment.
  - **About Us**: Redirects to the `About Us` page.
  - **Contact Us**: Redirects to the `Contact Us` page.
  - **All Events**: Redirects to the `All Events` page.
  - **User Authentication Buttons**:
    - **Log In**: Displays a login button if the user is not logged in.
    - **Sign Up**: Displays a sign up button if the user is not logged in.
    - **User Dropdown Menu**: Displays a dropdown with the user's profile image if logged in, which includes links to:
      - **Favourites**: Displays the events that the user has added to favourites.
      - **Tickets**: Displays the events that the user is attending.
      - **My Events**: Displays the events that the user has created.
      - **My Profile**: Displays an edit form with the user's information.

- Header if user is logged in:
![image](https://github.com/user-attachments/assets/14a0c43a-f96b-44a4-8afe-28810153bb72)


- Header if user is not logged in:
![image](https://github.com/user-attachments/assets/b8c4f2ef-fe83-4dc9-ab5b-36dbe1bab64e)




     



### Footer
- Links to `Log In` and `Sign Up` if the user is not logged in.
- Links to `Profile`, `Favourites`, `Tickets`, `My Events` if the user is logged in.
- Links to `Events`, `Upcoming Events`, `Past Events` in section "Discover".
- Links to `About Us`, `Contact Us` pages.
- Links to social accounts.


- Footer:
![image](https://github.com/user-attachments/assets/e37931f6-676c-41ec-8774-88e27545782a)





### 🏠 Home Page
- **Upcoming events**: See a part of the upcoming events.
- **Explore categories**: See all categories and explore them one by one.
- **Popular Cities on VolunteerAct**: See first six popular cities that have the most attendees.
- **Discover Events**: Section with a link that redirects to the events page.
- **Create an Event**: Section with a link that redirects to the create event page.

- Home Page:
![image](https://github.com/user-attachments/assets/ec9e9293-d5dd-4aca-a0e7-28510bcd735c)
![image](https://github.com/user-attachments/assets/1e6b7d37-75ff-4f9c-b882-551bb2ba3846)
![image](https://github.com/user-attachments/assets/89905c98-09e2-4c1c-bd01-51e04a64fecc)









### 📑 Category Page
- Short and long descriptions of the category.
- Number of events and members; Some of the cities that the events take place at.
- Part of the upcoming events in the category.
- Part of the past events in the category.
- Active members - members that participate in events in the category.
- Photos section - photos of the events in this category.
- Upload a photo - only active members of the category are allowed to upload a photo.


- Category Page:
![image](https://github.com/user-attachments/assets/11cc69e5-b6d2-4e71-9fdc-08d19cd5039c)
![image](https://github.com/user-attachments/assets/004fbdc1-e6f6-4911-a5a5-c2f98461bd94)
![image](https://github.com/user-attachments/assets/45601db8-3763-43c4-a1d3-9b76945003b2)
![image](https://github.com/user-attachments/assets/f4de0fd6-d521-4248-9e41-679f1d73595b)









### 🎉 Event Page
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

- Event Page:
![image](https://github.com/user-attachments/assets/3d4873ea-92da-464a-b6f5-29ea4d76b50a)
![image](https://github.com/user-attachments/assets/96d84a77-9da6-4470-9d62-cc1357036943)
![image](https://github.com/user-attachments/assets/bb887910-d907-41fb-91da-58565a863b58)
![image](https://github.com/user-attachments/assets/339a0571-3372-48dd-a13e-508be2fa2961)






### 💬 Event Comments Page
- Displays all the comments related to the event.

- Event Comments Page:
![image](https://github.com/user-attachments/assets/5124b94a-076c-4a05-8411-4ace551d6439)
![image](https://github.com/user-attachments/assets/05e6b9c9-0d3e-457e-bdbb-681718d2d25d)





### 📝 Edit Event Page
- Only the author of the event, a user of the 'staff_members' group or a superuser can access this page.
- The user can change the title, poster image, details, time, city, location and online meeting link (if the event is online).

- Edit Event Page:
![image](https://github.com/user-attachments/assets/c3c9a82e-4533-4bd4-9e28-732002e67d78)
![image](https://github.com/user-attachments/assets/6c7c55ca-3323-4eb0-8c5a-e6f3600ce00e)






### 🌆 City Page
- Short description of the city.
- Displays upcoming and past events in the city.

- City Page:
![image](https://github.com/user-attachments/assets/b8adef84-25d7-4f0d-9947-aeb80af748e3)
![image](https://github.com/user-attachments/assets/0f969104-dc97-4533-a720-aa1587f23f6e)
![image](https://github.com/user-attachments/assets/891bd5ed-f0d2-49ef-95ae-202593f08707)







### 🔍 Explore Events Page
- Only logged in users have access to this page.
- All events displayed.
- A search bar which allows users to search for an event case-insensetively.
- Filters for category, city and time.

- Explore Events Page:
![image](https://github.com/user-attachments/assets/4e089ea2-91da-419a-8f3c-30bdd0f724ff)
![image](https://github.com/user-attachments/assets/dd0e3b06-b606-4ce1-85e1-13e26753ea8a)







### 🗓️ Create An Event Page
- Only logged in users have access to this page.
- User needs to provide category, image, title, city and location (if the event is not going to be online), online meeting link (if the event is going to be online), time and details.

- Create An Event Page
![image](https://github.com/user-attachments/assets/be233872-03a2-4fa4-ada9-217c1d6c8a45)






### 🚨 Emergency Events
- Everyone has access to this page.
- This page is dedicated to urgent events.
- An event in this category becomes no longer urgent only when it is deleted.
- `Add Emergency Event` button - only logged in users can add emergency events.
- When an emergency event is added, all active members of its category will be notified by receiving an email.

- Emergency Events:
![image](https://github.com/user-attachments/assets/552a9c3c-f369-45f8-81f1-4f780c90597a)
![image](https://github.com/user-attachments/assets/ff61f6e8-9375-4d05-ac2c-fe1100afd9b0)






### 📋 About Us Page
- Provides more information about VolunteerAct and what you can do in it.

- About Us Page:
![image](https://github.com/user-attachments/assets/ddb5a1d5-487a-4965-a0fd-5ea7ea600fba)
![image](https://github.com/user-attachments/assets/63f570c6-acf5-4b2b-a81f-8ee83647766c)






### 📧 Contact Us Page
- A form for contacting the team of VolunteerAct through email. User needs to add his full name, email, subject and message.
- Contact information - phone number, email, location, social media links
- Location with a map

- Contact Us Page:
![image](https://github.com/user-attachments/assets/5d2fa9a9-cf18-48f9-b86a-518760e8abde)
![image](https://github.com/user-attachments/assets/19d74e3d-b236-4387-b6e9-aa6bf6c3f287)






### ⭐ Favourites Page
- Dislays all the events that the users has saved to favourites.
- A search bar which allows users to search for an event case-insensetively.
- Filters for category, city and time.

- Favourites Page:
![image](https://github.com/user-attachments/assets/d6acc6d6-8fd6-4d29-92dc-cfc86950cc43)





### 🎟️ Tickets Page
- Displays all the events that the user is attending.
- A search bar which allows users to search for an event case-insensetively.

- Tickets Page:
![image](https://github.com/user-attachments/assets/d09bc2dc-733a-4721-bece-5c64f509498c)





### 📅 My Events Page
- Displays upcoming and past events that the user has created.
- Attending participants in the events that the user has created.

- My Events Page
![image](https://github.com/user-attachments/assets/e6155f35-1c1d-414d-a8ad-e5ad01a83bb8)




### 👨‍🔧 Profile Page
- If the profile is of the currently logged in user, a form for editing will be displayed. The user can change his profile picture, first name, last name, phone number, email and bio.
- If the profile is not of the currently logged in user, a page with the information for the specific user will be displayed.
- `Delete` button - redirects to the delete profile page.

- Profile page of the currently logged in user:
![image](https://github.com/user-attachments/assets/9195483a-bbcd-452c-b5d2-f54c6360816d)

- Profile page of another user:
![image](https://github.com/user-attachments/assets/4bf4ed45-84d2-497f-a25c-47935dcf1529)




### ⚠️ 404 Page
![image](https://github.com/user-attachments/assets/b146586c-5514-473e-8ec5-b35a883cc784)



### 🔒 403 Page
![image](https://github.com/user-attachments/assets/050cfeac-1630-4568-a41f-eacff4786597)





## 🛠 Technologies
- **Python**: Core language for functionality.
- **Django**: Python-based framework.
- **PostgreSQL**: Database system.
- **JavaScript**: Language for functionalities on the front-end.
- **HTML**: Language for the structure of the templates.
- **CSS**: Styling the application.
- **Azure**: Deployment platform.
- **Cloudinary**: Storing user profile pictures.
- **Google AllAuth**: Login and register with Google.
- **Google Email**: Sending emails and receiving emails.
- **Pillow**: Validate if a file is an image.
- **Yake**: Extracting keywords from a text.
- **Whitenoise**: Serves static files.
- **Pixabay API**: Fetching images of cities.






## 🧪 Data for testing purposes
- **Users**:
  - **Email:** andy@email.com; **password:** Andy123!!AA (staff_members group)
  - **Email:** petya@email.com; **password:** Petya123!!PP (staff_members group)
  - **Email:** stanislav@email.com; **password:** Stani123!!SS (regular_users group)
  - **Email:** anastasia@email.com; **password:** Anii123!!AA (regular_users group)





## 🚀 Getting Started

### 📋 Prerequisites
- Python and Django installed.


### 🛠 Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/rayapetkova/VolunteerAct.git
   ```

2. Create and activate venv

2. Install requirements.txt:
   ```sh
   pip install -r requirements.txt
   ```

3. Open new terminal and run the command:
   ```sh
   celery -A VolunteerAct worker --pool=solo --loglevel=info 
   ```

4. Open the URL generated in the first teminal and enjoy! :))

---
Thank you for being a part of VolunteerAct! For questions or suggestions, don't hesitate to reach out with any thoughts or concerns!



