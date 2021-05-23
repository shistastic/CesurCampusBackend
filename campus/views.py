from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view

from CesurCampusBackend import settings
from .models import Students, Teachers, Courses, Subjects, Content
from django.contrib.auth.hashers import make_password, check_password

import stripe


# Create your views here.
@api_view(['POST'])
def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        content = Content.objects.create(content=myfile)
        content.save()
        # fs = FileSystemStorage()
        # filename = fs.save(myfile.name, myfile)

        return Response(200)
    else:
        return Response(400)


@api_view(['GET'])
def show_image(request, id):
    media_path = settings.MEDIA_ROOT
    print(media_path)
    content = Content.objects.get(id=id)

    image_data = open(media_path + "\\" + str(content.content), "rb").read()
    return HttpResponse(image_data, content_type="application/pdf")



# INSERT OPERATIONS
@api_view(['POST'])
def add_student(request):
    fullname = request.data['fullname']
    dni = request.data['dni']
    email = request.data['email']
    password = make_password(request.data['password'])

    try:
        student = Students.objects.create(fullname=fullname, dni=dni, email=email, password=password)
        student.save()
        return Response(200)
    except Exception as e:
        print(e)
        return Response(400)


@api_view(['POST'])
def show_student(request):
    response = JsonResponse(
        dict(student=list(Students.objects.values('id', 'fullname', 'email', 'course_id', 'acc_type')
                          .filter(id=request.data['id']))))

    # print(response)

    return response


@api_view(['POST'])
def show_student_course(request):
    response = JsonResponse(
        dict(student=list(Students.objects.values('id', 'fullname', 'email', 'course_id')
                          .filter(course_id=request.data['course_id']))))

    return response


@api_view(['POST'])
def login(request):
    dni = request.data['dni']
    password = request.data['password']

    # Get user instance from email
    student = Students.objects.get(dni=dni)
    if check_password(password, student.password):
        response = JsonResponse(dict(student=list(Students.objects.values('id', 'dni', 'fullname', 'email', 'acc_type')
                                                  .filter(id=student.id))))
    else:
        response = 400

    # if student is not None:
    #
    #     if check_password(password, student.password):
    #         response = JsonResponse(dict(student=list(Students.objects.values('id', 'fullname', 'email')
    #                                                  .filter(id=student.id))))
    #
    #     response = 400
    #     teacher = Teachers.objects.get(email=email)
    #
    # if teacher is not None:
    #     if check_password(password, teacher.password):
    #         response = JsonResponse(dict(teacher=list(Teachers.objects.values('id', 'fullname', 'email')
    #                                                  .filter(id=teacher.id))))
    #     response = 400

    return HttpResponse(response)


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
    year = request.data['year']

    try:
        course = Courses.objects.create(name=name, description=description, year=year)
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


@api_view(['POST'])
def add_content(request):
    title = request.data['title']
    description = request.data['description']
    # date_end = request.data['date_end']
    subject_id = request.data['subject_id']
    teacher_id = request.data['teacher_id']
    subject_name = request.data['subject_name']
    myfile = request.FILES['content']
    state = request.data['state']


    try:
        content = Content.objects.create(title=title, description=description, state=state,
                                         subject_id=subject_id, subject_name=subject_name, teacher_id=teacher_id, content=myfile)
        content.save()
        return Response(200)
    except Exception as e:
        print(e)
        return Response(400)


@api_view(['POST'])
def show_subject_content(request):
    response = JsonResponse(
        dict(content=list(Content.objects.values('id', 'title', 'description', 'content', 'state', 'subject_id', 'subject_name')
                          .filter(state=request.data['state']))))

    return response

@api_view(['POST'])
def show_subject_course_id(request):
    response = JsonResponse(
        dict(subjects=list(Subjects.objects.values('name', 'description', 'teacher_id', 'course_id')
                          .filter(course_id=request.data['course_id']))))

    return response


@api_view(['POST'])
def show_course(request):
    response = JsonResponse(
        dict(course=list(Courses.objects.values('name', 'description', 'price')
                         .filter(id=request.data['id']))))

    return response


@api_view(['POST'])
def show_course_year(request):
    response = JsonResponse(
        dict(course=list(Courses.objects.values('id', 'name', 'description', 'price', 'year')
                         .filter(year=request.data['year']))))

    return response


@api_view(['POST'])
def show_all_courses(request):
    response = JsonResponse(
        dict(course=list(Courses.objects.values('id', 'name', 'year', 'description', 'price'))))

    return response


stripe.api_key = "sk_test_51IaKKkGzLhkB9n77l28uh9cSIjWCwvuXji5bscyo0LjQ4YfS0wP2IU4671ywM6syyhkfUszbA1aqQNBYbqXLVb4F00Rc1t0RcM"


@csrf_exempt
def pay_course(request):
    if request.method == 'POST':
        print('Data:', request.POST)
        try:
            amount = request.POST['amount']
            customer = stripe.Customer.create(
                email=request.POST['email'],
                name=request.POST['nickname'],
                source=request.POST['stripeToken']
            )

            charge = stripe.Charge.create(
                customer=customer,
                amount=amount,
                currency='eur',
                description='CesurCampus',
            )
            return HttpResponse(200)
        except:
            return HttpResponse(400)
