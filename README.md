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

## Scope and Limitations

### Scope

Develop a user-friendly platform for creating, editing, deleting, and browsing game reviews.  

### Limitations

1. **Content Moderation**:  
   The platform currently does not include advanced moderation features like profanity filters.  
2. **Authentication**:  
   The initial version does not require user accounts, which limits personalized features.

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


# Comparison of Index Page to Mockup

## Design Similarities
1. **Layout**:  
   The index page closely mirrors the mockup’s intended layout. It features a clear structure with a header, search bar, and list of reviews displayed in a vertical format.

2. **Styling**:  
   - The background design aligns well with the mockup, using a visually appealing image that provides depth to the page.  
   - Rounded corners, shadows, and slight transparency effects on elements like the search bar and review boxes enhance the page’s professional appearance, similar to the mockup.

3. **Review Presentation**:  
   Each review is displayed inside a styled box, with sections for the game title, review text, and rating, reflecting the mockup's clean and readable design.

## Differences
1. **H1 Customization**:  
   The index page features an H1 with the ability to include an image background. This addition provides flexibility in branding but slightly deviates from the mockup if the mockup had a simpler text-based header.

2. **Interactivity**:  
   - Functional links for editing and deleting reviews go beyond the static design of the mockup, introducing dynamic elements that improve usability.  
   - A confirmation prompt for deletion adds a layer of user experience enhancement not originally reflected in the mockup.

3. **Styling Adjustments**:  
   While the mockup may have relied on placeholder or generic designs, the index page applies a more polished color palette (e.g., white text on reviews, green buttons) and refined typography for better visual hierarchy and readability.

4. **Content Display**:  
   The mockup might have used placeholder text or limited examples, whereas the index page dynamically pulls real reviews from the MongoDB database, making the content dynamic and relevant.

## Conclusion
The index page successfully captures the essence of the mockup while introducing enhancements in functionality and interactivity. Minor deviations, such as the H1 customization, offer practical improvements while maintaining the mockup’s visual integrity. Overall, the final result provides a user-friendly and visually appealing experience that stays true to the mockup’s goals.

### Add/eviews

![alt text](<static/images/Gamereview hub screenshot Add review final.png>)
![alt text](<static/images/Gamereview hub screenshot Add review Mock up.png>)

### 1. **Layout and Design**  
The "Add" page layout is very similar to what was presented in the mock-up. The input fields for title, description, and additional information are clearly placed. However, in the live version, some spacing between fields is slightly off compared to the mock-up’s even padding and margins. The positioning of the submit button also differs slightly in the live version, which could be due to last-minute adjustments.

### 2. **Functionality**  
The functionality of the "Add" page works as expected, allowing users to add new entries. The mock-up envisioned a more interactive form submission process, where users could see a preview of the added content before confirming the addition. In the live version, there is no preview function, which could be a missed opportunity for better user engagement.

### 3. **Color Scheme and Typography**  
The color scheme on the "Add" page matches the mock-up’s design, with neutral backgrounds and accent colors for buttons and headings. The typography remains consistent as well. However, the hover effect for the submit button is more abrupt in the live version than in the mock-up, which could be softened for a smoother transition.

### 4. **User Experience**  
The user experience on the "Add" page largely aligns with the mock-up’s intentions, providing a clear and intuitive way to add content. However, the mock-up proposed a more dynamic, step-by-step addition process that would guide the user through each section. The live version uses a single-page form that might feel less guided, which could lead to confusion for some users.

### 5. **Responsiveness**  
The "Add" page is mostly responsive as shown in the mock-up, though the live page does face some issues on smaller screens. Some fields and buttons become hard to interact with on mobile devices due to their size and spacing, which was not a problem in the mock-up. This is an area that could be improved to make the page more user-friendly across all devices.

### 6. **Additional Features**  
The "Add" page in the mock-up envisioned a file upload feature for adding images or other media, which is absent in the live version. The live page is restricted to text input only, which limits the functionality compared to the original design. This feature might be considered for future updates to make the page more versatile.

### Edit Review
![alt text](<static/images/Gamereview hub screenshot Edit review final.png>)
![alt text](<static/images/Gamereview hub screenshot Edit review Mock up.png>)

### 1. **Layout and Design**  
The layout of the "Edit" page closely follows the mock-up. Key elements like input fields for title and description are properly aligned. However, there is a slight discrepancy in the alignment of the fields, with the live page showing a minor shift to the left compared to the mock-up. This could be due to responsive adjustments for different screen sizes.

### 2. **Functionality**  
The functionality of the "Edit" page mostly matches the mock-up. Users can edit existing entries with ease. However, the mock-up proposed inline editing for a smoother experience, whereas the live page uses modal windows to edit content. This method is more structured but lacks the immediacy the mock-up envisioned.

### 3. **Color Scheme and Typography**  
The color scheme and typography on the live "Edit" page are consistent with the mock-up. The button hover effect, however, differs slightly, with a more abrupt transition in the live version compared to the smooth fade seen in the mock-up.

### 4. **User Experience**  
In the mock-up, the "Edit" page was designed for a seamless experience with clear entry distinctions. The live page mostly adheres to this but experiences a minor issue with the delay when saving changes, which could affect the user experience. Additionally, the breadcrumb navigation, which would help users navigate more easily, is missing from the live version, making it harder to move between pages quickly.

### 5. **Responsiveness**  
The mock-up anticipated full responsiveness, but on mobile devices, the "Edit" page shows some misalignment in fields and buttons, making it less comfortable to use on smaller screens. This issue is something that needs to be addressed for optimal mobile experience.

### 6. **Additional Features**  
The "Edit" page in the mock-up featured a media upload option, which hasn’t been implemented in the live version. The live version is limited to text-based input only, which may need to be revisited in future updates to match the mock-up’s vision.

### Delete review pop up

"A pop-up window is used when deleting a review to prevent accidental deletions and ensure users have a chance to confirm their action. This added layer of confirmation helps improve the user experience by reducing errors and promoting careful decision-making, especially when permanent changes like deletion are involved."

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

### Validation

- **HTML/CSS**: Validated with W3C tools.  
- **Python**: Code reviewed using **PyLint** for adherence to coding standards.  
- **Database**: MongoDB queries tested to ensure proper storage and retrieval.


![CSS Validation](<static/images/CSS validator.png>)



## Functional Testing

|Function|On platform|Works good| Fails|
|--------|-----------|----------|------|

|| browsers * |Yes |      |
|Search for reviews |browsers *|Yes|      |
|Add reviews |browsers *|Yes|      |
|Edit reviews |browsers *|Yes|      |
|Delete reviews |browsers *|Yes|      |
|X|browsers *|Yes||
Browsers *: Google Chrome, Oprah, Firefox, Microsoft Edge.

---

## Deployment

## Why I Chose Railway Over Heroku

I chose Railway to deploy my Flask app instead of Heroku because it offers several key advantages:

1. **Ease of Use**: Railway has a simple, beginner-friendly interface and automates much of the deployment process.

2. **Generous Free Tier**: Unlike Heroku, which limits free usage and requires credit card verification, Railway provides a more flexible free plan with fewer restrictions.

3. **Faster Deployment**: With built-in Continuous Integration/Continuous Deployment (CI/CD), Railway automatically updates my app whenever I make changes.

4. **No Cold Starts**: Railway avoids the delays caused by "cold starts" that Heroku's free tier often experiences, ensuring my app runs quickly.

5. **Easy MongoDB Integration**: Connecting my database was seamless with Railway's environment variable management.

6. **Modern Features**: Railway includes helpful tools like real-time logs and resource scaling, making it more efficient for development.

Overall, Railway's simplicity, better free tier, and faster performance made it the ideal choice for hosting my project.

Live site adress: [Game Review Hub](www.gamereviewhub.co.uk)


---

## Conclusion

# Game Reviews Hub: Platform Overview and Features

**Game Reviews Hub** successfully simplifies the process of sharing and managing game reviews. Its straightforward interface and core functionalities, showcased through the **index**, **add review**, **edit review**, and **delete pop-up** pages, provide a solid foundation for building a community of engaged gamers. Let's explore how each of these elements contributes to the platform’s user experience.

## Index Page: Streamlined Navigation for Easy Browsing

The **index page** mock-up offers a clean and intuitive layout where users can easily navigate through reviews. By focusing on minimal design and clear categorization, the page ensures that users can quickly browse through various games and reviews. The layout incorporates essential features such as:

- **Search bar and filters** for narrowing down reviews based on game titles, genres, or ratings, ensuring users can find the most relevant content to them.
- **Highlighted reviews** or a "featured" section, drawing attention to popular or top-rated games, encouraging community interaction and engagement.

This mock-up reflects the platform’s goal of creating a space that is both engaging and easy to use, inviting users to explore new content with minimal effort.

## Add Review Page: Simplified Submission Process

The **add review** page mock-up focuses on creating a frictionless process for users to submit their reviews. The layout is designed to be straightforward, with clearly defined fields and options for adding game titles, ratings, and written reviews. Key aspects include:

- **Rating system** that allows users to assign scores to different aspects of the game (e.g., gameplay, graphics, sound), offering a structured way to express opinions.
- **Text input field** for detailed written reviews, encouraging users to elaborate on their experiences and share valuable insights with the community.
- **User-friendly interface** with simple buttons and prompts that ensure the process is quick and easy, making it more likely for users to contribute their thoughts without feeling overwhelmed.

This mock-up reinforces the platform's focus on ease of use, making the review submission process as simple and accessible as possible, which is essential for fostering an active and growing community.

## Edit Review Page: Empowering Users with Control

The **edit review** page mock-up empowers users by allowing them to modify their reviews after submission. This feature ensures that users can update their content based on new experiences or changing opinions. The mock-up includes:

- **Editable fields** for both the game rating and written review, ensuring users can update both easily.
- **Clear save and cancel options**, so users feel confident in their decisions and can quickly revert to the original version if necessary.
- **Version history** or revision log (potential future feature), so users can track changes to their reviews and maintain transparency.

This mock-up demonstrates the platform’s commitment to giving users control over their content, allowing them to express themselves more freely and update reviews as their understanding of the game evolves.

## Delete Pop-up: Confirmation to Prevent Accidental Deletion

The **delete pop-up** mock-up serves an essential function: preventing accidental deletions of reviews. When a user chooses to delete a review, a confirmation pop-up appears, ensuring they are fully aware of the action. The key features of this pop-up include:

- **Clear warning message** that explains the action being taken (e.g., "Are you sure you want to delete this review? This action cannot be undone.").
- **Confirmation buttons**: One for confirming the deletion and another to cancel the action, giving the user the option to reconsider and avoid mistakes.
- **Visual cues** (such as color changes or icons) to clearly indicate the severity of the action, reducing the chances of accidental clicks.

This feature is crucial for user satisfaction and trust, as it ensures users don’t lose valuable content without being fully aware of the consequences. It’s a simple yet powerful design choice that enhances the platform’s usability and safeguards user-generated content.

## Conclusion: Building a Strong Foundation for the Future

Together, these mock-ups highlight **Game Reviews Hub**'s commitment to creating a user-centric platform that encourages engagement, fosters a sense of community, and prioritizes ease of use. The simplicity of the interface combined with clear functionalities ensures that users can quickly and effectively interact with the platform, whether they are browsing reviews, submitting their own, or editing their contributions.

In the future, updates will further improve the platform by introducing **user accounts**, allowing gamers to have personalized profiles and track their review history. **Advanced search features** will make it even easier to find specific content based on detailed criteria, while **enhanced moderation tools** will help maintain a positive and respectful community environment.

**Game Reviews Hub** has set a strong foundation, and these ongoing improvements will only enhance its capabilities, making it the go-to place for passionate gamers to share and discover reviews in a seamless, enjoyable way.


---

## Credits

  - **Deployment**: deployed to railway [Railway](https://railway.com/). 
- **Backend Logic**: Tutorials from [Flask Documentation](https://flask.palletsprojects.com/).  
- **Database Setup**: MongoDB guides from [MongoDB Documentation](https://www.mongodb.com/docs/). 
- Photos from Pixabay: MongoDB guides from [Pixalbay](https://pixabay.com/images/search/loyalty/). 