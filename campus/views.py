from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Students, Teachers, Courses, Subjects
from django.contrib.auth.hashers import make_password, check_password


# Create your views here.
# INSERT OPERATIONS
@api_view(['POST'])
def add_student(request):
    fullname = request.data['fullname']
    email = request.data['email']
    password = make_password(request.data['password'])

    try:
        student = Students.objects.create(fullname=fullname, email=email, password=password)
        student.save()
        return Response(200)
    except Exception as e:
        print(e)
        return Response(400)


@api_view(['POST'])
def show_student(request):
    response = JsonResponse(
        dict(student=list(Students.objects.values('id', 'fullname', 'email', 'course_id')
                          .filter(id=request.data['id']))))

    return response


@api_view(['POST'])
def show_student_course(request):
    response = JsonResponse(
        dict(student=list(Students.objects.values('id', 'fullname', 'email', 'course_id')
                          .filter(course_id=request.data['course_id']))))

    return response


@api_view(['POST'])
def login(request):
    email = request.data['email']
    password = request.data['password']

    # Get user instance from email
    student = Students.objects.get(email=email)
    if student is not None:

        if check_password(password, student.password):
            response = JsonResponse(dict(student=list(Students.objects.values('id', 'fullname', 'email')
                                                     .filter(id=student.id))))

        response = 400
        teacher = Teachers.objects.get(email=email)

    if teacher is not None:
        if check_password(password, teacher.password):
            response = JsonResponse(dict(teacher=list(Teachers.objects.values('id', 'fullname', 'email')
                                                     .filter(id=teacher.id))))
        response = 400

    return Response(response)


@api_view(['POST'])
def add_teacher(request):
    fullname = request.data['fullname']
    email = request.data['email']
    password = make_password(request.data['password'])

    try:
        teacher = Teachers.objects.create(fullname=fullname, email=email, password=password)
        teacher.save()
        return Response(200)
    except Exception as e:
        print(e)
        return Response(400)


@api_view(['POST'])
def add_course(request):
    name = request.data['name']
    description = request.data['description']

    try:
        course = Courses.objects.create(name=name, description=description)
        course.save()
        return Response(200)
    except Exception as e:
        print(e)
        return Response(400)


@api_view(['POST'])
def add_subject(request):
    name = request.data['name']
    description = request.data['description']
    teacher_id = request.data['teacher_id']
    course_id = request.data['course_id']

    try:
        subject = Subjects.objects.create(name=name, description=description, teacher_id=teacher_id,
                                          course_id=course_id)
        subject.save()
        return Response(200)
    except Exception as e:
        print(e)
        return Response(400)
