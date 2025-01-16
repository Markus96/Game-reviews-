# Game Reviews Hub

## Project Overview

### Introduction

**Game Reviews Hub** is a web-based platform that allows users to share their opinions on video games. The site enables users to add new reviews, edit existing ones, and delete reviews they no longer want. Built with **HTML**, **CSS**, **Python**, and **MongoDB**, this platform ensures a user-friendly experience for sharing and managing game reviews.

---

## Development Plan

1. Research user needs for a game review platform.  
2. Design a clean, intuitive interface for browsing and managing reviews.  
3. Develop backend functionality for adding, editing, deleting, and viewing reviews.  
4. Test features for usability and bug resolution.  
5. Deploy the platform for public use and gather feedback for improvements.

---

## Motivation and Inspiration

### Motivation

The project aims to create a centralized platform where gamers can easily share and access reviews. This helps gamers make informed decisions about which games to play, while fostering a community of engaged players.

### Inspiration

Popular review platforms such as **IMDB**, **Metacritic**, and **Steam Reviews** inspired the idea, but this project focuses on simplicity and ease of use for gamers.

---

## User Stories

1. **As a user**,  
   I want to add reviews for games,  
   So that I can share my thoughts with others.  

2. **As a user**,  
   I want to edit my reviews,  
   So that I can update my opinions when needed.  

3. **As a user**,  
   I want to delete reviews,  
   So that I can remove content I no longer wish to share.  

4. **As a user**,  
   I want to browse reviews by game title or genre,  
   So that I can quickly find information relevant to my interests.  

5. **As a user**,  
   I want a visually appealing interface,  
   So that the experience of reading and managing reviews is enjoyable.

---

## Background

Most existing review platforms are either cluttered with excessive features or lack customization options. **Game Reviews Hub** offers a streamlined approach by focusing solely on the ability to write, edit, and manage reviews.

---

## Development Highlights

### Features

1. **Add Reviews**:  
   Users can create new reviews by filling out a simple form that includes fields for game title, review text, rating, and genre.

2. **Edit Reviews**:  
   Users can update their reviews through an intuitive editing interface.

3. **Delete Reviews**:  
   A single click allows users to remove reviews they no longer wish to keep.

4. **View Reviews**:  
   The homepage displays a list of reviews with search and filter options by title, genre, or rating.

### Technologies Used

- **HTML/CSS**: For designing the user interface.  
- **Python (Flask)**: To handle backend logic.  
- **MongoDB**: For storing and managing review data.

---

## Design and Features

### Homepage

![alt text](<static/images/Gamereview hub screenshot index Final.png>)
![alt text](<static/images/Gamereview hub screenshot index Mock up.png>)


- A welcoming and clean layout showcasing the latest game reviews.
- Search bar and filter options for quick navigation.
- A “Write a Review” button prominently displayed.

### Add/Edit/Delete Reviews

![alt text](<static/images/Gamereview hub screenshot Add review final.png>)
![alt text](<static/images/Gamereview hub screenshot Add review Mock up.png>)

![alt text](<static/images/Gamereview hub screenshot Edit review final.png>)
![alt text](<static/images/Gamereview hub screenshot Edit review Mock up.png>)

- **Add Review**: A form with fields for game title, genre, rating, and review text.  
- **Edit Review**: Pre-filled forms allow users to update their submissions seamlessly.  
- **Delete Review**: Simple confirmation modal ensures users don’t accidentally delete reviews.

---

## Scope and Limitations

### Scope

Develop a user-friendly platform for creating, editing, deleting, and browsing game reviews.  

### Limitations

1. **Content Moderation**:  
   The platform currently does not include advanced moderation features like profanity filters.  
2. **Authentication**:  
   The initial version does not require user accounts, which limits personalized features.

---

## Problem Statement

**Issue**: Gamers often struggle to find reliable, user-generated reviews in one place.  

**Solution**: **Game Reviews Hub** provides a centralized platform that focuses on simplicity and functionality, making it easy for gamers to contribute and access reviews.

---

## Bugs and Fixes

### Key Issues

1. **Database Connectivity**:  
   - Reviews occasionally failed to save to MongoDB during initial testing.  
2. **Form Validation**:  
   - Missing or invalid form inputs caused unexpected behavior.  
3. **Delete Confirmation**:  
   - Accidental deletions occurred due to the lack of a confirmation step.

### Solutions

1. **Database Fix**:  
   - Updated the Flask configuration to properly connect to MongoDB.  
2. **Validation**:  
   - Added front-end validation using JavaScript and back-end validation with Python.  
3. **Delete Confirmation**:  
   - Implemented a modal that asks users to confirm deletion.

---

## Testing and Validation

### Manual Testing

- Tested all functionalities (add, edit, delete, and view reviews) on multiple browsers, including Google Chrome, Firefox, and Microsoft Edge.

### Validation

- **HTML/CSS**: Validated with W3C tools.  
- **Python**: Code reviewed using **PyLint** for adherence to coding standards.  
- **Database**: MongoDB queries tested to ensure proper storage and retrieval.

---

## Deployment

The project was developed using **Gitpod** and deployed to **Heroku** for live access.  

**Live Site**: [Game Reviews Hub](https://gamereviewshub.herokuapp.com)  

---

## Conclusion

**Game Reviews Hub** successfully simplifies the process of sharing and managing game reviews. Its straightforward interface and core functionalities provide a solid foundation for building a community of engaged gamers.  

Future updates will focus on adding user accounts, advanced search features, and enhanced moderation to further improve the platform.

---

## Credits

- **Frontend Design**: Inspired by **Bootstrap** templates.  
- **Backend Logic**: Tutorials from [Flask Documentation](https://flask.palletsprojects.com/).  
- **Database Setup**: MongoDB guides from [MongoDB Documentation](https://www.mongodb.com/docs/).  
- **Icons**: [Font Awesome](https://fontawesome.com/).
