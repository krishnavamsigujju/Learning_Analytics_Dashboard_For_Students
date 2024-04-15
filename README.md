# Learning_Analytics_Dashboard_For_Students

This repository hosts the source code for one of the three planned developments of the Learning Analytics Dashboard (LAD) at Colorado State University, along with associated academic materials including a published paper and a project poster. The dashboard is designed to enhance student engagement, motivation, and academic performance by providing personalized feedback, sophisticated data visualization, and goal-setting mechanisms.

## Overview

The Learning Analytics Dashboard for Students leverages learning analytics to provide insights into students' educational activities. It aims to empower students to optimize their learning experiences in higher education settings by systematically analyzing data on student engagement and performance.

## Features

### Development and Implementation
- **Completed Feature: Upcoming Assignment Reminders**
  - Developed a feature that automatically sends reminder messages to students one day before an assignment's due date. This functionality aids in task management, ensuring timely submissions and addressing the need for better time management.

### Future Developments
- **Additional Notification Options**
  - Plans to implement customizable notification settings, allowing students greater control over the alerts they receive. This enhancement is aimed at improving the overall user experience.
- **Consolidated Grades Page**
  - Aiming to create a page that displays all course grades in one convenient location, potentially including a GPA estimator. This development is intended to simplify academic tracking and planning for students.


### Installation

This section provides the steps to install the "Upcoming Assignment Reminders" feature of the Learning Analytics Dashboard. Follow these instructions to set up this feature on your local machine:


## Clone the Repository
git clone https://github.com/krishnavamsigujju/Learning_Analytics_Dashboard_For_Students.git
cd Learning_Analytics_Dashboard_For_Students


## Installation
Create a Python virtual environment to manage dependencies:
# Create a virtual environment (ensure Python3 is installed)
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install Necessary Packages
Install the required Python packages using pip:
pip3 install django
pip3 install django-sslserver
pip3 install canvasapi

### Running Application

Run the dashboard using the Django development server over HTTPS:
sudo python ./manage.py runsslserver 127.0.0.1:1031

## Setting Up the Canvas LTI Application
Open your account on Canvas: Go to Canvas.
Create an Endpoint:
Navigate to your course in Canvas.
Go to Settings -> Apps -> View App Configurations -> +App.
Fill in the application details:
Name: Provide a name for your app.
Launch URL: https://127.0.0.1:1031/lti
Custom Fields: Enter course_id=$Canvas.course.id, user_id=$Canvas.user.id
Click Submit.
Add the LTI Tool to a Course Module:
Go to Home in your course.
Create a new module or select an existing one.
Click the + icon to add an item, select External Tool, then choose the app you just created.
Click Add Item.
## Using the Dashboard
After setting up the LTI tool in Canvas, navigate to the module where you added the tool.
You will see an option to "Load LTI Application in New Window".
Click on it to open your LAD URL. This will automatically trigger the feature that sends reminder messages to students' inboxes.
