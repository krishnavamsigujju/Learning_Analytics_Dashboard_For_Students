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

def index(request):
    print("method entered")
    # Canvas API URL
    course_id=7960598
    # user_id=111257313
    API_URL = "https://canvas.instructure.com/"
    API_KEY = '7~riKce9ULcCYoj5kH8TNzXEOnW0F2vS7Xv9tW5xHf4HMtHUX4NRxx6HWSPkeLDzkE'  # Replace with your own Canvas

    grades, average_gpa = get_my_grades_and_calculate_gpa()
    response_message = ""
    for grade in grades:
        response_message += f"Course: {grade['course_name']}, Current Score: {grade['current_score']}, Letter Grade: {grade['letter_grade']}, GPA: {grade['GPA']}<br>"

    response_message += f"Average GPA: {average_gpa}<br>"
    print(response_message)
    
 
    return HttpResponse(response_message)

# Function to get grades for a student in all courses
# def get_my_grades():
#     API_URL = "https://canvas.instructure.com/"
#     API_KEY = '7~riKce9ULcCYoj5kH8TNzXEOnW0F2vS7Xv9tW5xHf4HMtHUX4NRxx6HWSPkeLDzkE'  # Replace with your own Canvas
#     canvas = Canvas(API_URL, API_KEY)
#     user = canvas.get_user('self')
#     # course = canvas.get_course(7960598)
#     courses = user.get_courses(enrollment_state='active')

#     # users = course.get_users(enrollment_type=['student'], per_page=100) 
#     grades_info = []

#     for course in courses:
#         enrollments = course.get_enrollments(user_id='self', type=['StudentEnrollment'])
#         for enrollment in enrollments:
#             if 'grades' in enrollment.__dict__:
#                 course_name = course.name
#                 grades = enrollment.grades
#                 current_score = grades.get('current_score', 'No current score')
#                 final_score = grades.get('final_score', 'No final score')
#                 grade_info = {
#                     'course_name': course_name,
#                     'current_score': current_score,
#                     'final_score': final_score
#                 }
#                 grades_info.append(grade_info)

#     return grades_info

def score_to_grade(score):
    if score is None:
        return 'F'
    elif score >= 90:
        return 'A'
    elif score >= 87:
        return 'A-'
    elif score >= 83:
        return 'B+'
    elif score >= 80:
        return 'B'
    elif score >= 77:
        return 'B-'
    elif score >= 73:
        return 'C+'
    elif score >= 70:
        return 'C'
    elif score >= 67:
        return 'C-'
    elif score >= 63:
        return 'D+'
    elif score >= 60:
        return 'D'
    elif score >= 57:
        return 'D-'
    else:
        return 'F'

# GPA values
grade_to_gpa = {
    'A+': 4.0, 'A': 4.0, 'A-': 3.667,
    'B+': 3.334, 'B': 3.0, 'B-': 2.667,
    'C+': 2.334, 'C': 2.0, 'C-': 1.667,
    'D+': 1.334, 'D': 1.0, 'D-': 0.667,
    'F': 0.0
}

# def get_my_grades_and_average():
#     API_URL = "https://canvas.instructure.com/"
#     API_KEY = '7~riKce9ULcCYoj5kH8TNzXEOnW0F2vS7Xv9tW5xHf4HMtHUX4NRxx6HWSPkeLDzkE'  # Replace with your own Canvas
#     canvas = Canvas(API_URL, API_KEY)
#     user = canvas.get_user('self')  # Using 'self' to refer to the authenticated user
#     courses = user.get_courses(enrollment_state='active')  # Fetch only active courses
#     grades_info = []

#     total_current_score = 0
#     total_final_score = 0
#     count_current_score = 0
#     count_final_score = 0

#     for course in courses:
#         enrollments = course.get_enrollments(user_id='self', type=['StudentEnrollment'])
#         for enrollment in enrollments:
#             if 'grades' in enrollment.__dict__:
#                 course_name = course.name
#                 grades = enrollment.grades
#                 current_score = grades.get('current_score')
#                 final_score = grades.get('final_score')

#                 if current_score is not None:
#                     total_current_score += current_score
#                     count_current_score += 1
                
#                 if final_score is not None:
#                     total_final_score += final_score
#                     count_final_score += 1

#                 grade_info = {
#                     'course_name': course_name,
#                     'current_score': current_score,
#                     'final_score': final_score
#                 }
#                 grades_info.append(grade_info)

#     average_current_score = total_current_score / count_current_score if count_current_score > 0 else "No scores available"
#     average_final_score = total_final_score / count_final_score if count_final_score > 0 else "No scores available"
    
#     return grades_info, average_current_score, average_final_score


def get_my_grades_and_calculate_gpa():
    API_URL = "https://canvas.instructure.com/"
    API_KEY = '7~riKce9ULcCYoj5kH8TNzXEOnW0F2vS7Xv9tW5xHf4HMtHUX4NRxx6HWSPkeLDzkE'  # Replace with your own Canvas
    canvas = Canvas(API_URL, API_KEY)
    user = canvas.get_user('self')  # Using 'self' to refer to the authenticated user
    courses = user.get_courses(enrollment_state='active')  # Fetch only active courses
    grades_info = []
    total_gpa = 0
    count_courses = 0

    for course in courses:
        enrollments = course.get_enrollments(user_id='self', type=['StudentEnrollment'])
        for enrollment in enrollments:
            if 'grades' in enrollment.__dict__:
                course_name = course.name
                grades = enrollment.grades
                current_score = grades.get('current_score')
                letter_grade = score_to_grade(current_score)
                gpa = grade_to_gpa[letter_grade]
                
                if current_score is not None or current_score is None:
                    total_gpa += gpa
                    count_courses += 1

                grade_info = {
                    'course_name': course_name,
                    'current_score': current_score,
                    'letter_grade': letter_grade,
                    'GPA': gpa
                }
                grades_info.append(grade_info)

    print(total_gpa)
    print(count_courses)
    average_gpa = total_gpa / count_courses if count_courses > 0 else "No valid grades available"
    
    return grades_info, average_gpa