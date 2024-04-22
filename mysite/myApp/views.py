import datetime
from datetime import datetime, timedelta, timezone
from dateutil import parser
from pytz import utc

from canvasapi import Canvas
from django.shortcuts import render

from collections import defaultdict

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

from django.core.mail import EmailMessage
from django.template.defaultfilters import striptags
from django.template.loader import render_to_string
from django.conf import settings

import requests
import logging
import pytz 

API_URL = "https://canvas.instructure.com/"
headers = {
        'Authorization': 'Bearer 7~riKce9ULcCYoj5kH8TNzXEOnW0F2vS7Xv9tW5xHf4HMtHUX4NRxx6HWSPkeLDzkE'
    }

def send_message_to_student(student_id,message):
    url = API_URL+f'/api/v1/conversations#filter=type=inbox'
    data = {
        'recipients[]': f'{student_id}',
        'subject': 'Reminder to complete assignment!',
        'body': message,      
    }

    print('data: '+ str(data))

    response = requests.post(url, headers=headers, data=data)
    print("response sent:",response)

    if response.status_code != 201:
        return 0
    else:
        return 1
    
    

def send_reminder_if_due_soon(student_id, due_date):
    """
    Sends a reminder to the student if the assignment is due within the next 24 hours.

    Parameters:
    - student_id: The ID of the student to send the reminder to.
    - due_date: The due date of the assignment as a datetime object.
    """
    print("entered into this method")
    print(student_id)
    # Calculate the time 24 hours before the due date
    reminder_time = due_date - timedelta(days=1)
    # Get the current time
    # current_time = datetime.now(timezone.utc)
    current_time = datetime.now(utc)
    # current_time = datetime.now(pytz.utc)
    print(due_date.tzinfo) 
    print(current_time.tzinfo)

    # Check if the current time is within 24 hours of the due date
    if current_time >= reminder_time and current_time < due_date:
        # Construct the message
        message = "Dear Student, This is a gentle reminder to complete your assignment.  Please submit it by tomorrow."
        send_message_to_student(student_id, message)

        print(f"Reminder sent to student {student_id}: {message}")

def get_assignments(course_id):
    api_url = f"https://canvas.instructure.com/api/v1/courses/{course_id}/assignments"
    response = requests.get(api_url, headers=headers)
    return response.json()


def index(request):
    print("method entered")
    # Canvas API URL
    course_id=7960598
    # user_id=111257313
    API_URL = "https://canvas.instructure.com/"
    API_KEY = '7~riKce9ULcCYoj5kH8TNzXEOnW0F2vS7Xv9tW5xHf4HMtHUX4NRxx6HWSPkeLDzkE'  # Replace with your own Canvas

    try:
        # Initialize a new Canvas object
        canvas = Canvas(API_URL, API_KEY)
        print("called to API")
        # course_id = request.POST["custom_course_id"]
        # print("course_id is",course_id)
        # Get the course by course ID
        course = canvas.get_course(7960598)
        print(course)
        # Get a list of users in the course 
        users = course.get_users(enrollment_type=['student'], per_page=100)  # Adjust per_page as needed
        
        print("users retreived are", users)
        
        
        
        # for user in users:
        #     # student_email = get_student_email(course, user.id)
        #     message = "This is a test notification from your course."
        # send_message_to_student(111257313)
        response_message = f"Welcomeee user: {request.POST['custom_course_id']} to the course with id: {request.POST['custom_user_id']}<br>"
        for user in users:
            
            user_assignments = get_assignments(7960598) 
            print("user assignmants printing")
            # just print the name of the user_assignment
            if user_assignments:
                assignments_url=f"https://canvas.instructure.com/api/v1/courses/{course_id}/assignments/{user_assignments[0]['id']}"
                # print("assignment url is", assignments_url)
                assignments_response = requests.get(assignments_url, headers=headers)
                # print("assignment response is", assignments_response)
                assignments = assignments_response.json()
                # print(assignments)
                due_at = assignments['due_at']
                due_date = parser.parse(due_at).astimezone(utc)
                print("user is", user.id)
                send_reminder_if_due_soon(user.id,due_date)
                response_message += f"Notification send to User: {user.name}<br>"
                
                
                
        # due_date = parser.parse(due_at)
        # due_date = datetime.strptime(due_at, '%Y-%m-%dT%H:%M:%SZ')
        
        # due_date = due_at.replace(tzinfo=None)
            # print("assignments retreiived", assignments)
            # print("due date is",due_date)
            # send_reminder_if_due_soon(111257313, due_date)
        
        

        # response_message = "Notifications sent to all students."
        # response_message = f"Welcomeee user: {request.POST['custom_course_id']} to the course with id: {request.POST['custom_user_id']}<br>"

        # for user in users:
        #     response_message += f"User: {user.name}<br>"

        #     # Get the list of assignments for the user in the course
        #     user_assignments = user.get_assignments(course.id, per_page=100)  # Adjust per_page as needed

        #     if user_assignments:
        #         response_message += "Assignments:<br>"
        #         for assignment in user_assignments:
        #             response_message += f"- Assignment: {assignment.name}<br>"
        #             submission = assignment.get_submission(user)
        #             if submission and submission.workflow_state == 'submitted':
        #                 response_message += "  - Submission: Submitted<br>"
        #             else:
        #                 response_message += "  - Submission: Not Submitted<br>"
        #     else:
        #         response_message += "No assignments found for this user in the course.<br>"
                

        #     assignments = course.get_assignments()

            
            
            
    except Exception as e:
        response_message = f"An error occurred: {str(e)}<br>"

    # Always return an HttpResponse
    return HttpResponse(response_message)


