from datetime import datetime, timedelta, timezone

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


# Create your views here.

# def get_assignment_due_dates(request):
#     # Make a GET request to the Canvas API
#     course_id=request.POST["custom_course_id"]
#     api_url = f'https://colostate.instructure.com/api/v1/courses/{course_id}/assignments'
#     headers = {
#         'Authorization': 'Bearer 7~riKce9ULcCYoj5kH8TNzXEOnW0F2vS7Xv9tW5xHf4HMtHUX4NRxx6HWSPkeLDzkE'
#     }
#     response = requests.get(api_url, headers=headers)

#     # Check if the request was successful
#     if response.status_code == 200:
#         # Extract the due dates from the response
#         assignments_data = response.json()

#         #due_dates = [assignment['due_at'] for assignment in assignments]

#         #print(due_dates)
#         # Render the due dates in a template
#         return render(request, 'assignments.html', {'assignments_data': assignments_data})
#     else:
#         # Return an error message
#         return HttpResponse('An error occurred while retrieving the due dates.')



# def get_student_email(course_id,user_id):
#     api_url = f'https://colostate.instructure.com/api/v1/courses/{course_id}/users/{user_id}'
#     headers = {
#         'Authorization': 'Bearer 7~riKce9ULcCYoj5kH8TNzXEOnW0F2vS7Xv9tW5xHf4HMtHUX4NRxx6HWSPkeLDzkE'
#     }
#     response = requests.get(api_url, headers=headers)
#     students_data = response.json()
#     student_email=students_data['login_id']
#     return student_email

# def get_student_name(course_id,user_id):
#     api_url = f'https://colostate.instructure.com/api/v1/courses/{course_id}/users/{user_id}'
#     headers = {
#         'Authorization': 'Bearer 7~riKce9ULcCYoj5kH8TNzXEOnW0F2vS7Xv9tW5xHf4HMtHUX4NRxx6HWSPkeLDzkE'
#     }
#     response = requests.get(api_url, headers=headers)
#     students_data = response.json()
#     student_name=students_data['name']
#     return student_name


# def get_assignments(course_id):
#     api_url = f"https://colostate.instructure.com/api/v1/courses/{course_id}/assignments"
#     headers = {
#         "Authorization": "Bearer 7~riKce9ULcCYoj5kH8TNzXEOnW0F2vS7Xv9tW5xHf4HMtHUX4NRxx6HWSPkeLDzkE"
#     }
#     response = requests.get(api_url, headers=headers)
#     return response.json()


# def get_assignment_submissions(course_id, assignment_id):
#     api_url = f"https://colostate.instructure.com/api/v1/courses/{course_id}/assignments/{assignment_id}/submissions"
#     headers = {
#         "Authorization": "Bearer 7~riKce9ULcCYoj5kH8TNzXEOnW0F2vS7Xv9tW5xHf4HMtHUX4NRxx6HWSPkeLDzkE"
#     }
#     response = requests.get(api_url, headers=headers)
#     return response.json()


# def list_assignment_submissions(request):
#     assignments = get_assignments(request.POST["custom_course_id"])
#     assignments_list=[]
#     for assignment in assignments:
#         submissions = get_assignment_submissions(request.POST["custom_course_id"], assignment["id"])
#         assignments_list.append({"assignment_name": assignment["name"],"submissions": submissions})
#     return render(request,"list_assignment_submissions.html",{"assignments_list": assignments_list})

# Set up API connection with Canvas
# API_URL = 'https://colostate.instructure.com/api/v1'
# API_URL = 'https://colostate.instructure.com/'
#API_URL = 'https://canvas.instructure.com/courses'
# ACCESS_TOKEN = '7~riKce9ULcCYoj5kH8TNzXEOnW0F2vS7Xv9tW5xHf4HMtHUX4NRxx6HWSPkeLDzkE'
# ACCESS_TOKEN = '7~XRkX8sezmLnLDWtQR259Tp7HFwUFaqzVFvi0M4j2BcAlMdEDAimeZpEpj16d4RiS' #canvas instructure
# headers = {'Authorization': 'Bearer ' + ACCESS_TOKEN}
# canvas = Canvas(API_URL, ACCESS_TOKEN)
# course = canvas.get_course(7887397)


# Retrieve data on missing assignments
# def get_missing_assignments(course_id):
#     assignments = get_assignments(course_id)
#     missing_assignments = []
#     for assignment in assignments:
#         submissions = get_assignment_submissions(course_id, assignment["id"])
#         for submission in submissions:
#             if submission["workflow_state"] == "unsubmitted":
#                 student_email=get_student_email(course_id,submission['user_id'])
#                 student_name = get_student_name(course_id, submission['user_id'])
#                 missing_assignment = {
#                     'assignment_name': assignment['name'],
#                     'due_date': assignment['due_at'],
#                     'student_email': student_email,
#                     'student_name': student_name
#                 }
#                 missing_assignments.append(missing_assignment)
#     return missing_assignments

# Implement automation script using Django
# def send_assignment_reminder(student_name, student_email, assignment_name, due_date):
#     message = render_to_string('assignment_reminder.html', {'student_name': student_name, 'assignment_name': assignment_name, 'due_date': due_date})
#     email = EmailMessage(subject='Missing Assignment Reminder', body=message, to=[student_email])
#     email.send()

# # Schedule the automation script
# def assignment_reminder(request):
#     course_id= request.POST["custom_course_id"]
#     missing_assignments = get_missing_assignments(course_id)
#     print(missing_assignments)
#     for ma in missing_assignments:
#         assignment_name = ma['assignment_name']
#         due_date = ma['due_date']
#         student_email = ma['student_email']
#         student_name = ma['name']
#         send_assignment_reminder(student_name, student_email, assignment_name, due_date)
#     return HttpResponse('Email sent sucessfully')

# def get_instructor_name():
#
#     return instructor_name

# def send_message_to_student(student_id,instructor_name,student_name, assignment_name, due_date):
#     headers = {'Authorization': 'Bearer ' + '7~riKce9ULcCYoj5kH8TNzXEOnW0F2vS7Xv9tW5xHf4HMtHUX4NRxx6HWSPkeLDzkE'}

#     url = API_URL+f'/conversations#filter=type=inbox'
#     date_obj = datetime.strptime(due_date, "%Y-%m-%dT%H:%M:%SZ")
#     formatted_due_date = date_obj.strftime("%d %B %Y")
#     print('student name:' + str(student_name))
#     body= render_to_string('assignment_reminder.html', {'student_name': student_name, 'assignment_name': assignment_name, 'formatted_due_date': formatted_due_date, 'instructor_name': instructor_name})
#     plain_text_content = striptags(body)
#     data = {
#         'recipients[]': f'{student_id}',
#         'subject': 'Missing Assignment',
#         'body': plain_text_content,
#         "force_new": True,
#         "group_conversation": False,
#          "bulk_message": True,
#     }

#     print('data: '+ str(data))

#     response = requests.post(url, headers=headers, data=data)

#     if response.status_code != 201:
#         return 0
#     else:
#         return 1
    
# def send_welcome_message_to_all_students(request):
#     # course_id = request.POST.get("custom_course_id")
#     course_id=7887397
#     API_URL = 'https://colostate.instructure.com/api/v1'
#     ACCESS_TOKEN = '7~riKce9ULcCYoj5kH8TNzXEOnW0F2vS7Xv9tW5xHf4HMtHUX4NRxx6HWSPkeLDzkE'
#     headers = {'Authorization': 'Bearer ' + '7~riKce9ULcCYoj5kH8TNzXEOnW0F2vS7Xv9tW5xHf4HMtHUX4NRxx6HWSPkeLDzkE'}
#     print("hi")
#     # Initialize a new Canvas object
#     canvas = Canvas(API_URL, ACCESS_TOKEN)
#     course = canvas.get_course(course_id)
    
#     # Fetch all students in the course
#     students = course.get_users(enrollment_type=['student'])
    
#     # Send a message to each student
#     for student in students:
#         student_id = student.id
#         # Construct the API endpoint for sending messages
#         url = API_URL + f'/conversations'
#         data = {
#             'recipients[]': student_id,
#             'subject': 'Welcome to the Course',
#             'body': 'Welcome to this course!',
#             'context_code': f'course_{course_id}'
#         }
#         # Make the POST request to send the message
#         response = requests.post(url, headers=headers, data=data)
        
#         if response.status_code != 201:
#             logger.error(f"Failed to send welcome message to student {student_id}. Response: {response.text}")
#             print(f"Failed to send welcome message to student {student_id}. Response: {response.text}")
#         else:
#             logger.info(f"Welcome message sent to student {student_id}.")
#             print(f"Welcome message sent to student {student_id}.")

#     return HttpResponse("Welcome messages sent to all students.")

# def assignment_reminder(request):
#     course_id=7887397
#     API_URL = 'https://colostate.instructure.com/api/v1'
#     ACCESS_TOKEN = '7~riKce9ULcCYoj5kH8TNzXEOnW0F2vS7Xv9tW5xHf4HMtHUX4NRxx6HWSPkeLDzkE'
#     headers = {'Authorization': 'Bearer ' + '7~riKce9ULcCYoj5kH8TNzXEOnW0F2vS7Xv9tW5xHf4HMtHUX4NRxx6HWSPkeLDzkE'}

#     # Initialize a new Canvas object
#     canvas = Canvas(API_URL, ACCESS_TOKEN)
#     course = canvas.get_course(course_id)
#     students = course.get_users(enrollment_type=['student'])
#     for i in students:
#         assignment_name = i['assignment_name']
#         due_date = i['due_date']
#         student_email = i['student_email']
#         student_name = i['name']
#         send_assignment_reminder(student_name, student_email, assignment_name, due_date)
#     return HttpResponse('Email sent sucessfully')

# def send_assignment_reminder(student_name, student_email, assignment_name, due_date):
#     message = render_to_string('assignment_reminder.html', {'student_name': student_name, 'assignment_name': assignment_name, 'due_date': due_date})
#     email = EmailMessage(subject='Missing Assignment Reminder', body=message, to=[student_email])
#     email.send()

    
# def send_due_date_reminders(request):
    
#     course_id = request.POST.get("custom_course_id")
#     assignments = get_assignments(course_id)
#     now = datetime.now(timezone.utc)
#     for assignment in assignments:
#         due_date_str = assignment.get("due_at")
#         if due_date_str:
#             due_date = datetime.strptime(due_date_str, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
#             if 0 < (due_date - now).total_seconds() <= 86400:  # Check if due within next 24 hours
#                 submissions = get_assignment_submissions(course_id, assignment["id"])
#                 for submission in submissions:
#                     if submission["workflow_state"] == "unsubmitted":
#                         student_id = submission["user_id"]
#                         student_email = get_student_email(course_id, student_id)
#                         student_name = get_student_name(course_id, student_id)
#                         message = "You have only one day to submit your assignment, Hurry Up!"
#                         send_message_to_student(student_id, "Instructor Name", student_name, assignment["name"], due_date_str)
#     return HttpResponse("Reminders sent for assignments due in the next 24 hours.")

# def send_notification(student_email, message):
#     email = EmailMessage(
#         subject='Course Notification',
#         body=message,
#         to=[student_email]
#     )
#     email.send()
API_URL = "https://canvas.instructure.com/"
headers = {
        'Authorization': 'Bearer 7~riKce9ULcCYoj5kH8TNzXEOnW0F2vS7Xv9tW5xHf4HMtHUX4NRxx6HWSPkeLDzkE'
    }
def send_message_to_student(student_id):
    url = API_URL+f'/conversations#filter=type=inbox'
    data = {
        'recipients[]': f'{student_id}',
        'subject': 'Missing Assignment',
        'body': 'hello test',      
    }

    # print('data: '+ str(data))

    response = requests.post(url, headers=headers, data=data)
    print("response sent:",response)

    if response.status_code != 201:
        return 0
    else:
        return 1
    
# def get_student_email(course, user_id):
#     user = course.get_user(user_id)
#     return user.email

# def get_student_email(course_id,user_id):
#     # api_url = f'https://colostate.instructure.com/api/v1/courses/{course_id}/users/{user_id}'
#     api_url = "https://canvas.instructure.com/api/v1/courses/{course_id}/users/{user_id}"
#     headers = {
#         'Authorization': 'Bearer 7~riKce9ULcCYoj5kH8TNzXEOnW0F2vS7Xv9tW5xHf4HMtHUX4NRxx6HWSPkeLDzkE'
#     }
#     response = requests.get(api_url, headers=headers)
#     students_data = response.json()
#     student_email=students_data['login_id']
#     return student_email

# def index(request):
#     API_URL = "https://canvas.instructure.com/"
#     API_KEY = '7~riKce9ULcCYoj5kH8TNzXEOnW0F2vS7Xv9tW5xHf4HMtHUX4NRxx6HWSPkeLDzkE'

#     try:
#         canvas = Canvas(API_URL, API_KEY)
#         course = canvas.get_course(7887397)
#         users = course.get_users(enrollment_type=['student'], per_page=100)

#         for user in users:
#             student_email = get_student_email(course, user.id)
#             message = "This is a test notification from your course."
#             send_notification(student_email, message)

#         response_message = "Notifications sent to all students."

#     except Exception as e:
#         response_message = f"An error occurred: {str(e)}"

#     return HttpResponse(response_message)
    
    
def index(request):
    print("method entered")
    # Canvas API URL
    course_id=7887397
    user_id=111257313
    API_URL = "https://canvas.instructure.com/"
    # API_URL = "https://canvas.instructure.com/courses/{course_id}/users/{user_id}"

    # Canvas API key
    # API_KEY = "7~veaPySTkEmDFUDiNlij52F02lwcczr2sT8vyTO9OZzzkzZoRVPKPM4Av1KfbxGRZ"  # Replace with your Canvas API key
    API_KEY = '7~riKce9ULcCYoj5kH8TNzXEOnW0F2vS7Xv9tW5xHf4HMtHUX4NRxx6HWSPkeLDzkE'  # Replace with your own Canvas

    try:
        # Initialize a new Canvas object
        canvas = Canvas(API_URL, API_KEY)
        print("called to API")

        # Get the course by course ID
        course = canvas.get_course(7887397)
        print(course)
        # Get a list of users in the course 
        users = course.get_users(enrollment_type=['student'], per_page=100)  # Adjust per_page as needed
        print("users retreived")
        response_message = f"Welcome user: {request.POST['custom_course_id']} to the course with id: {request.POST['custom_user_id']}<br>"
        
        for user in users:
            # student_email = get_student_email(course, user.id)
            message = "This is a test notification from your course."
            send_message_to_student(111257313)

        # response_message = "Notifications sent to all students."

        for user in users:
            response_message += f"User: {user.name}<br>"
           
            
            

            # Get the list of assignments for the user in the course
            user_assignments = user.get_assignments(course.id, per_page=100)  # Adjust per_page as needed

            if user_assignments:
                response_message += "Assignments:<br>"
                for assignment in user_assignments:
                    response_message += f"- Assignment: {assignment.name}<br>"
                    submission = assignment.get_submission(user)
                    if submission and submission.workflow_state == 'submitted':
                        response_message += "  - Submission: Submitted<br>"
                    else:
                        response_message += "  - Submission: Not Submitted<br>"
            else:
                response_message += "No assignments found for this user in the course.<br>"
                

            assignments = course.get_assignments()

            
            
            
    except Exception as e:
        response_message = f"An error occurred: {str(e)}<br>"

    # Always return an HttpResponse
    return HttpResponse(response_message)


