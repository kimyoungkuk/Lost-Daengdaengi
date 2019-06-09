from django.shortcuts import render,redirect
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from django.core.files.storage import FileSystemStorage
from django.core.mail import EmailMessage

from .models import *
from .serializers import *

from rest_framework.decorators import api_view
from rest_framework import viewsets

from datetime import datetime, timedelta

import logging
import base64
from PIL import Image, ImageFont, ImageDraw
import os
import numpy as np
import torch
from torch.utils.data import DataLoader
import torchvision
import torch.nn as nn
from torch.autograd import Variable
import torchvision.transforms as transforms
from numpy.linalg import norm
from numpy import dot
from math import radians, cos, sin, asin, sqrt

import cv2


class PostViewSet(viewsets.ModelViewSet):
    queryset = Owner_post.objects.all()
    serializer_class = Owner_postSerializer


# Create your views here.
@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            try: # 맞는 key를 가진 User가 있느냐
                user = User.objects.get(key = serializer.data['key'])
            except User.DoesNotExist:
                return Response({'state':0,'nickname':""}, status = status.HTTP_201_CREATED)
            return Response({'state':1,'nickname':user.nickname}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def signup(request):
    if request.method == 'POST':
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            user_num = User.objects.filter(nickname = serializer.data['nickname']).count()
            if user_num == 0:#같은 닉네임의 유저가 0명
                user = User()
                user.admin = 0
                user.key = serializer.data['key']
                user.nickname = serializer.data['nickname']
                user.save()
                return Response({'state':0,'nickname':serializer.data['nickname']}, status = status.HTTP_201_CREATED)
            else:
                return Response({'state':1,'nickname':serializer.data['nickname']}, status = status.HTTP_201_CREATED)
            
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def changeNickname(request):
    if request.method == 'POST':
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            user = User.objects.get(key = serializer.data['key'])
            user.nickname = serializer.data['nickname']
            user.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def Dog_shelter_list(request):
    if request.method == 'GET':
        queryset = Dog_shelter.objects.all()
        serializer = Dog_shelterSerializer(queryset, many = True)
        logging.error(serializer.data[0]['shelter_name'])
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = Dog_shelterSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

def haversine(currentLat, currentLng, shelterLat, shelterLng):
    # convert decimal degrees to radians
    currentLat, currentLng, shelterLat, shelterLng = map(radians, [currentLat, currentLng, shelterLat, shelterLng])
    # haversine formula
    dlon = shelterLat - currentLat
    dlat = shelterLng - currentLng
    a = sin(dlat/2)**2 + cos(currentLat) * cos(shelterLat) * sin(dlon/2)**2
    c = 2*asin(sqrt(a))
    km = 6367 * c
    return km

@api_view(['POST'])
def FindNearShelter(request):
    currentLocation = NearSerializer(data = request.data)
    if currentLocation.is_valid():
        queryset = Dog_shelter.objects.all()
        shelterList = Dog_shelterSerializer(queryset, many = True)

        distMIN = 1000
        id_value = 0
        for i in range(0,len(shelterList.data)):
            dist = haversine(currentLocation.data['lat'],currentLocation.data['lng'],shelterList.data[i]['lat'],shelterList.data[i]['lng']) 
            if dist <= distMIN:
                distMIN = dist
                id_value = i + 1
        
        nearestQueryset = Dog_shelter.objects.get(pk = id_value)
        nearestDogShelter = Dog_shelterSerializer(nearestQueryset)
        return Response(nearestDogShelter.data, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)




@api_view(['GET'])
def owner_post_list(request):

    owner_posts = Owner_post.objects.order_by('-id').filter(posted_due__gte=datetime.today()).filter(is_finished=0).values('title','id','posted_time','dog_type','lost_time','imageurl','view_count','lat','lng')
    serializer = Owner_postSerializer(owner_posts, many = True)
    return Response(owner_posts)
@api_view(['GET'])
def owner_post_list_portal(request):

    owner_posts = Owner_post.objects.order_by('-id').filter(posted_due__gte=datetime.today()).filter(is_finished=0).values('title','id','posted_time','dog_type','lost_time','imageurl','view_count','lat','lng')[:4]
    serializer = Owner_postSerializer(owner_posts, many = True)
    return Response(owner_posts)

@api_view(['GET'])
def finder_post_list(request):

    finder_posts = Finder_post.objects.order_by('-id').filter(posted_due__gte=datetime.today()).filter(is_finished=0).values('title','id','posted_time','dog_type','find_time','imageurl','view_count','lat','lng')
    serializer = Finder_postSerializer(finder_posts, many = True)
    return Response(finder_posts)
@api_view(['GET'])
def finder_post_list_portal(request):

    finder_posts = Finder_post.objects.order_by('-id').filter(posted_due__gte=datetime.today()).filter(is_finished=0).values('title','id','posted_time','dog_type','find_time','imageurl','view_count','lat','lng')[:4]
    serializer = Finder_postSerializer(finder_posts, many = True)
    return Response(finder_posts)

@api_view(['GET'])
def owner_post_detail(request,pk):
    owner_posts = Owner_post.objects.filter(id=pk)
    post_serializer = Owner_postSerializer(owner_posts, many = True)
    owner_post = Owner_post.objects.get(id=pk)
    # post_serializer = Owner_postSerializer(owner_post, many = True)
    owner_post.view_count = owner_post.view_count+1
    owner_post.save()
    comments = Comment.objects.filter(commented_post_type="owner").filter(commented_post=owner_post.id)
    comments_serializer = CommentSerializer(comments, many = True)
    
    return Response({'post':post_serializer.data,'comments':comments_serializer.data})

@api_view(['GET'])
def finder_post_detail(request,pk):
    finder_posts = Finder_post.objects.filter(id=pk)
    post_serializer = Finder_postSerializer(finder_posts, many = True)
    finder_post = Finder_post.objects.get(id=pk)
    # post_serializer = Finder_postSerializer(finder_post, many = True)
    finder_post.view_count = finder_post.view_count+1
    finder_post.save()
    comments = Comment.objects.filter(commented_post_type="finder").filter(commented_post=finder_post.id)
    comments_serializer = CommentSerializer(comments, many = True)
    
    return Response({'post':post_serializer.data,'comments':comments_serializer.data})


@api_view(['POST'])
def owner_post_create(request):
    serializer = Owner_postSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()

        if serializer.data['image'] != "":
            os.makedirs('./media/owner/'+str(serializer.data['id']))
            output = open('media/owner/'+str(serializer.data['id'])+'/profile.jpg', 'wb+')
            output.write(base64.b64decode(serializer.data['image']))
            output.close()

            post = Owner_post.objects.get(id=serializer.data['id'])
            post.image = ""
            post.imageurl = 'http://202.30.31.91:8000/' + 'media/owner/' + str(serializer.data['id']) + '/profile.jpg'
            post.save()
        else:
            pass
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def finder_post_create(request):
    serializer = Finder_postSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()

        tmp = Dog_shelter.objects.get(shelter_name = serializer.data['shelter_name'])
        post = Finder_post.objects.get(id = serializer.data['id'])
        post.shelter = tmp
        post.save()

        if serializer.data['image'] != "":
            os.makedirs('./media/finder/' + str(serializer.data['id']))
            output = open('media/finder/' + str(serializer.data['id']) + '/profile.jpg', 'wb+')
            output.write(base64.b64decode(serializer.data['image']))
            output.close()

            post = Finder_post.objects.get(id = serializer.data['id'])
            post.image = ""
            post.imageurl = 'http://202.30.31.91:8000/' + 'media/finder/' + str(serializer.data['id']) + '/profile.jpg'
            post.save()
        else:
            pass
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def owner_post_delete(request,pk):
    owner_post = Owner_post.objects.get(id=pk)
    owner_post.delete()
    return Response(1, status = status.HTTP_201_CREATED)

@api_view(['POST'])
def finder_post_delete(request,pk):
    finder_post = Finder_post.objects.get(id=pk)
    finder_post.delete()
    return Response(1, status = status.HTTP_201_CREATED)
    


@api_view(['GET','POST'])
def comment_create(request):
    if request.method == 'GET':
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many = True)
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    else:
        serializer = CommentSerializer(data = request.data)
        logging.error("IOP")
        if serializer.is_valid():
            logging.error("IOP")
            serializer.save()
            logging.error("JKL")

        logging.error("JKL")
        logging.error(serializer.data['user_key'])
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def report_create(request):
    if request.method == 'GET':
        reports = Report.objects.all()
        serializer = ReportSerializer(reports, many = True)
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    else:
        serializer = ReportSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            if serializer.data['reported_post_type']=='owner':
                owner_post = Owner_post.objects.get(id=serializer.data['reported_post'])
                owner_post.report_count = owner_post.report_count+1
                owner_post.save()
            elif serializer.data['reported_post_type']=='finder':
                finder_post = Finder_post.objects.get(id=serializer.data['reported_post'])
                finder_post.report_count = finder_post.report_count+1
                finder_post.save()

        return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


# @api_view(['POST'])
# def post_filter(request):
#     currentLocation = NearSerializer(data = request.data)
#     if currentLocation.is_valid():  
#         owner_posts = Owner_post.objects.filter(
#                 lat__gte = currentLocation.data['lat'] - 0.003,
#                 lat__lte = currentLocation.data['lat'] + 0.003,
#                 lng__gte = currentLocation.data['lng'] - 0.003,
#                 lng__lte = currentLocation.data['lng'] + 0.003
#                 )
#         finder_posts = Finder_post.objects.filter(
#                 lat__gte = currentLocation.data['lat'] - 0.003,
#                 lat__lte = currentLocation.data['lat'] + 0.003,
#                 lng__gte = currentLocation.data['lng'] - 0.003,
#                 lng__lte = currentLocation.data['lng'] + 0.003
#                 )
#         serializerOwner = Owner_postSerializer(owner_posts, many = True)
#         serializerFinder = Finder_postSerializer(finder_posts, many = True)
#         return Response(serializerOwner.data + serializerFinder.data, status = status.HTTP_201_CREATED)
#     return Response(currentLocation.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def owner_post_filter_with(request):
    lat = float(request.GET.get("lat"))
    lng = float(request.GET.get("lng"))
    owner_posts = Owner_post.objects.order_by('-id').filter(posted_due__gte=datetime.today()).filter(is_finished=0).filter(
        lat__gte = lat - 0.003,
        lat__lte = lat + 0.003,
        lng__gte = lng - 0.003,
        lng__lte = lng + 0.003
        )
    serializerOwner = Owner_postSerializer(owner_posts, many = True)
    return Response(serializerOwner.data, status = status.HTTP_201_CREATED)
    
@api_view(['GET'])
def finder_post_filter_with(request):
    lat = float(request.GET.get("lat"))
    lng = float(request.GET.get("lng"))
    finder_posts = Finder_post.objects.order_by('-id').filter(posted_due__gte=datetime.today()).filter(is_finished=0).filter(
        lat__gte = lat - 0.003,
        lat__lte = lat + 0.003,
        lng__gte = lng - 0.003,
        lng__lte = lng + 0.003
        )
    serializerFinder = Finder_postSerializer(finder_posts, many = True)
    return Response(serializerFinder.data, status = status.HTTP_201_CREATED)
    
@api_view(['POST'])
def filteringFinder(request):
    filtering = FilteringSerializer(data = request.data)
    if filtering.is_valid():
        pass
    if (filtering.data['starttime']==None or filtering.data['finaltime']==None):

        if(filtering.data['category']=='견종' and filtering.data['value']!=''):
            finder_posts = Finder_post.objects.order_by('-id').filter(posted_due__gte=datetime.today()).filter(is_finished=0).filter(dog_type = filtering.data['value'])
            serializerFinder = Finder_postSerializer(finder_posts, many = True)
        elif(filtering.data['category']=='작성자' and filtering.data['value']!=''):
            finder_posts = Finder_post.objects.order_by('-id').filter(posted_due__gte=datetime.today()).filter(is_finished=0).filter(user_nickname = filtering.data['value'])
            serializerFinder = Finder_postSerializer(finder_posts, many = True)
        else:
            finder_posts = Finder_post.objects.order_by('-id').filter(posted_due__gte=datetime.today()).filter(is_finished=0)
            serializerFinder = Finder_postSerializer(finder_posts, many = True)
    else: 
        if(filtering.data['category']=='견종' and filtering.data['value']!=''):
            finder_posts = Finder_post.objects.order_by('-id').filter(posted_due__gte=datetime.today()).filter(is_finished=0).filter(dog_type = filtering.data['value']).filter(find_time__gte = filtering.data['starttime']).filter(find_time__lte = filtering.data['finaltime'])
            serializerFinder = Finder_postSerializer(finder_posts, many = True)
        elif(filtering.data['category']=='작성자' and filtering.data['value']!=''):
            finder_posts = Finder_post.objects.order_by('-id').filter(posted_due__gte=datetime.today()).filter(is_finished=0).filter(user_nickname = filtering.data['value']).filter(find_time__gte = filtering.data['starttime']).filter(find_time__lte = filtering.data['finaltime'])
            serializerFinder = Finder_postSerializer(finder_posts, many = True)
        else:
            finder_posts = Finder_post.objects.order_by('-id').filter(posted_due__gte=datetime.today()).filter(is_finished=0).filter(find_time__gte = filtering.data['starttime']).filter(find_time__lte = filtering.data['finaltime'])
            serializerFinder = Finder_postSerializer(finder_posts, many = True)
        
    return Response(serializerFinder.data, status = status.HTTP_201_CREATED)
    # return Response(filtering.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def filteringOwner(request):
    filtering = FilteringSerializer(data = request.data)
    if filtering.is_valid():
        pass
    if (filtering.data['starttime']==None or filtering.data['finaltime']==None):

        if(filtering.data['category']=='견종' and filtering.data['value']!=''):
            owner_posts = Owner_post.objects.order_by('-id').filter(posted_due__gte=datetime.today()).filter(is_finished=0).filter(dog_type = filtering.data['value'])
            serializerOwner = Owner_postSerializer(owner_posts, many = True)
        elif(filtering.data['category']=='작성자' and filtering.data['value']!=''):
            owner_posts = Owner_post.objects.order_by('-id').filter(posted_due__gte=datetime.today()).filter(is_finished=0).filter(user_nickname = filtering.data['value'])
            serializerOwner = Owner_postSerializer(owner_posts, many = True)
        else:
            owner_posts = Owner_post.objects.order_by('-id').filter(posted_due__gte=datetime.today()).filter(is_finished=0)
            serializerOwner = Owner_postSerializer(owner_posts, many = True)
    else: 
        if(filtering.data['category']=='견종' and filtering.data['value']!=''):
            owner_posts = Owner_post.objects.order_by('-id').filter(posted_due__gte=datetime.today()).filter(is_finished=0).filter(dog_type = filtering.data['value']).filter(lost_time__gte = filtering.data['starttime']).filter(lost_time__lte = filtering.data['finaltime'])
            serializerOwner = Owner_postSerializer(owner_posts, many = True)
        elif(filtering.data['category']=='작성자' and filtering.data['value']!=''):
            owner_posts = Owner_post.objects.order_by('-id').filter(posted_due__gte=datetime.today()).filter(is_finished=0).filter(user_nickname = filtering.data['value']).filter(lost_time__gte = filtering.data['starttime']).filter(lost_time__lte = filtering.data['finaltime'])
            serializerOwner = Owner_postSerializer(owner_posts, many = True)
        else:
            owner_posts = Owner_post.objects.order_by('-id').filter(posted_due__gte=datetime.today()).filter(is_finished=0).filter(lost_time__gte = filtering.data['starttime']).filter(lost_time__lte = filtering.data['finaltime'])
            serializerOwner = Owner_postSerializer(owner_posts, many = True)
        
    return Response(serializerOwner.data, status = status.HTTP_201_CREATED)
    # return Response(filtering.errors, status = status.HTTP_400_BAD_REQUEST)



dirnames=['치와와','골든리트리버','보스턴불독','포메라니안','말티즈','도베르만','비글','시베리안허스키','셰퍼드','시츄','푸들','코카스패니얼','콜리','요크셔테리어','퍼그']

loader = transforms.Compose([transforms.Scale(224), transforms.ToTensor()])

def image_loader(image_name):
    """load image, returns cuda tensor"""
    image = Image.open(image_name).convert('RGB')
    image = loader(image).float()
    image = Variable(image, requires_grad=True)
    image = image.unsqueeze(0)  #this is for VGG, may not be needed for ResNet
    return image

def cos_sim(A, B):
       return dot(A, B)/(norm(A)*norm(B))

@api_view(['POST'])
def classificationImage(request):
    getImage = GetImageSerializer(data = request.data)
    if getImage.is_valid():
        if getImage.data['image'] != "":
            output = open('media/classification.jpg', 'wb+')
            output.write(base64.b64decode(getImage.data['image']))
            output.close()



            # Classification
            Resnet50_model = load_model('media/modeldir/weights.best.ResNet50.hdf5')##추후 개선안 생각할부분
            bottleneck_feature = extract_Resnet50(path_to_tensor('media/classification.jpg'))
            bottleneck_feature = np.expand_dims(bottleneck_feature,axis=0)
            bottleneck_feature = np.expand_dims(bottleneck_feature,axis=0)
            predicted_vector = Resnet50_model.predict(bottleneck_feature) #shape error occurs hers
            outputs = dog_names[np.argmax(predicted_vector)]
            
            return Response(outputs, status = status.HTTP_201_CREATED)

            # # Classification
            # model = torch.load('media/modeldir/flower_70.pth', map_location='cpu')
            # image = image_loader('media/classification.jpg')
            # outputs = model(image)
            
            # sm = nn.Softmax()
            
            # k = 3
            # one,labelarr = torch.topk(outputs,k)
            # problarr,two = torch.topk(sm(outputs),k)
            # candi = []

            # for i in range(k):
            #     x = problarr[0][i].__float__()
            #     candi.append([labelarr[0][i].__int__(),float("{0:.2f}".format(x)),dirnames[labelarr[0][i].__int__()]])

	        # #print(candi[0][2])

            # dogType = "abc"
            # dogType = candi[0][2]

            # return Response(dogType, status = status.HTTP_201_CREATED)

        else :
            logging.error("getImage.data['image'] is empty!!!!!")
    return Response(getImage.errors, status = status.HTTP_400_BAD_REQUEST)






# model = torch.load('media/modeldir/flower_70.pth', map_location='cpu')
            

@api_view(['GET'])
def o2f_recommend(request,pk):
    owner_post = Owner_post.objects.get(id=pk)


    finder_posts1 = Finder_post.objects.order_by('-id').filter(posted_due__gte=datetime.today()).filter(is_finished=0).filter(dog_type=owner_post.dog_type).values('title','id','posted_time','dog_type','find_time','imageurl','view_count','lat','lng')
    finder_posts2 = Finder_post.objects.order_by('-id').filter(posted_due__gte=datetime.today()).filter(is_finished=0).filter(find_time__gte=owner_post.lost_time+timedelta(days=-7)).filter(find_time__lte=owner_post.lost_time+timedelta(days=7)).values('title','id','posted_time','dog_type','find_time','imageurl','view_count','lat','lng')
    finder_posts3 = Finder_post.objects.order_by('-id').filter(posted_due__gte=datetime.today()).filter(is_finished=0).filter(
        lat__gte = owner_post.lat - 0.005,
        lat__lte = owner_post.lat + 0.005,
        lng__gte = owner_post.lng - 0.005,
        lng__lte = owner_post.lng + 0.005
        ).values('title','id','posted_time','dog_type','find_time','imageurl','view_count','lat','lng')
    serializerFinder1 = Finder_postSerializer(finder_posts1, many = True)
    serializerFinder2 = Finder_postSerializer(finder_posts2, many = True)
    serializerFinder3 = Finder_postSerializer(finder_posts3, many = True)
        
    finder_posts = Finder_post.objects.order_by('-id').filter(posted_due__gte=datetime.today()).filter(is_finished=0).filter(dog_type=owner_post.dog_type).filter(find_time__gte=owner_post.lost_time+timedelta(days=-7)).filter(find_time__lte=owner_post.lost_time+timedelta(days=7)).filter(
        lat__gte = owner_post.lat - 0.005,
        lat__lte = owner_post.lat + 0.005,
        lng__gte = owner_post.lng - 0.005,
        lng__lte = owner_post.lng + 0.005
        ).values('title','id','posted_time','dog_type','find_time','imageurl','view_count','lat','lng')
    serializerFinder = Finder_postSerializer(finder_posts, many = True)
    
    return Response({'recommend' : finder_posts}, status = status.HTTP_201_CREATED)  
    # return Response({'recommend1' : finder_posts1,'recommend2' : finder_posts2,'recommend3' : finder_posts3}, status = status.HTTP_201_CREATED)
    # return Response({'recommend1' : serializerFinder1.data,'recommend2' : serializerFinder2.data,'recommend3' : serializerFinder3.data}, status = status.HTTP_201_CREATED)
    # return Response(serializerFinder1.data+serializerFinder2.data+serializerFinder3.data, status = status.HTTP_201_CREATED)

@api_view(['GET'])
def f2o_recommend(request,pk):
    finder_post = Finder_post.objects.get(id=pk)
    

    owner_posts1 = Owner_post.objects.order_by('-id').filter(posted_due__gte=datetime.today()).filter(is_finished=0).filter(dog_type=finder_post.dog_type).values('title','id','posted_time','dog_type','lost_time','imageurl','view_count','lat','lng')
    owner_posts2 = Owner_post.objects.order_by('-id').filter(posted_due__gte=datetime.today()).filter(is_finished=0).filter(lost_time__gte=finder_post.find_time+timedelta(days=-7)).filter(lost_time__lte=finder_post.find_time+timedelta(days=7)).values('title','id','posted_time','dog_type','lost_time','imageurl','view_count','lat','lng')
    owner_posts3 = Owner_post.objects.order_by('-id').filter(posted_due__gte=datetime.today()).filter(is_finished=0).filter(
        lat__gte = finder_post.lat - 0.01,
        lat__lte = finder_post.lat + 0.01,
        lng__gte = finder_post.lng - 0.01,
        lng__lte = finder_post.lng + 0.01
        ).values('title','id','posted_time','dog_type','lost_time','imageurl','view_count','lat','lng')
    serializerOwner1 = Owner_postSerializer(owner_posts1, many = True)
    serializerOwner2 = Owner_postSerializer(owner_posts2, many = True)
    serializerOwner3 = Owner_postSerializer(owner_posts3, many = True)
    
    owner_posts = Owner_post.objects.order_by('-id').filter(posted_due__gte=datetime.today()).filter(is_finished=0).filter(dog_type=finder_post.dog_type).filter(lost_time__gte=finder_post.find_time+timedelta(days=-7)).filter(lost_time__lte=finder_post.find_time+timedelta(days=7)).filter(
        lat__gte = finder_post.lat - 0.01,
        lat__lte = finder_post.lat + 0.01,
        lng__gte = finder_post.lng - 0.01,
        lng__lte = finder_post.lng + 0.01
        ).values('title','id','posted_time','dog_type','lost_time','imageurl','view_count','lat','lng')
    serializerOwner = Owner_postSerializer(owner_posts, many = True)

    return Response({'recommend' : owner_posts}, status = status.HTTP_201_CREATED)
    # return Response({'recommend1' : owner_posts1,'recommend2' : owner_posts2,'recommend3' : owner_posts3}, status = status.HTTP_201_CREATED)
    # return Response({'recommend1' : serializerOwner1.data,'recommend2' : serializerOwner2.data,'recommend3' : serializerOwner3.data}, status = status.HTTP_201_CREATED)
    # return Response(serializerOwner1.data+serializerOwner2.data+serializerOwner3.data, status = status.HTTP_201_CREATED)


@api_view(['POST'])
def owner_post_finish(request,pk):
    owner_post = Owner_post.objects.get(id=pk)
    owner_post.is_finished = 1
    owner_post.save()
    return Response(1, status = status.HTTP_201_CREATED)
    
@api_view(['POST'])
def finder_post_finish(request,pk):
    finder_post = Finder_post.objects.get(id=pk)
    finder_post.is_finished = 1
    finder_post.save()
    return Response(1, status = status.HTTP_201_CREATED)
    


@api_view(['GET'])
def finish_post_list(request):
    finish_finder_posts = Finder_post.objects.order_by('-id').filter(is_finished=1).values('title','id','posted_time','dog_type','find_time','imageurl','view_count','lat','lng')
    serializer = Finder_postSerializer(finish_finder_posts, many = True)
    finish_owner_posts = Owner_post.objects.order_by('-id').filter(is_finished=1).values('title','id','posted_time','dog_type','lost_time','imageurl','view_count','lat','lng')
    serializer = Owner_postSerializer(finish_owner_posts, many = True)
    return Response(finish_owner_posts.data+finish_finder_posts.data)

@api_view(['GET'])
def finish_post_list_portal(request):
    finish_finder_posts = Finder_post.objects.order_by('-id').filter(is_finished=1).values('title','id','posted_time','dog_type','find_time','imageurl','view_count','lat','lng')
    serializer = Finder_postSerializer(finish_finder_posts, many = True)[:2]
    finish_owner_posts = Owner_post.objects.order_by('-id').filter(is_finished=1).values('title','id','posted_time','dog_type','lost_time','imageurl','view_count','lat','lng')
    serializer = Owner_postSerializer(finish_owner_posts, many = True)[:2]
    return Response(finish_owner_posts.data+finish_finder_posts.data)


@api_view(['POST'])
def adopt_login(request):
    serializer = Adopt_adminSerializer(data = request.data)
    if serializer.is_valid():
        try:
            adopt_admin = Adopt_admin.objects.get(account=serializer.data['account'])
        except:
            return Response(0)
        if adopt_admin.pwd==serializer.data['pwd']:
            return Response(1)
        else:
            return Response(0)

@api_view(['GET'])
def adopt_post_list(request):
    adopt_posts = Adopt_post.objects.order_by('-id').all().values('title','id','posted_time','dog_type','imageurl','posted_time')
    serializer = Adopt_postSerializer(adopt_posts, many = True)
    return Response(adopt_posts)

@api_view(['GET'])
def adopt_post_list_portal(request):
    adopt_posts = Adopt_post.objects.order_by('-id').all().values('title','id','posted_time','dog_type','imageurl','posted_time')[:4]
    serializer = Adopt_postSerializer(adopt_posts, many = True)
    return Response(adopt_posts)

@api_view(['POST'])
def adopt_post_create(request):
    serializer = Adopt_postSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        
        if serializer.data['image'] != "":
            os.makedirs('./media/adopt/'+str(serializer.data['id']))
            output = open('media/adopt/'+str(serializer.data['id'])+'/profile.jpg', 'wb+')
            
            # x = serializer.data['image'][22:]
            # x += "=" * ((4 - len(x) % 4) % 4)
            output.write(base64.b64decode(serializer.data['image'][22:]))
            output.close()

            post = Adopt_post.objects.get(id=serializer.data['id'])
            post.image = ""
            post.imageurl = 'http://202.30.31.91:8000/' + 'media/adopt/' + str(serializer.data['id']) + '/profile.jpg'
            post.save()
        else:
            pass

    return Response(serializer.data)

@api_view(['GET'])
def adopt_post_detail(request,pk):
    adopt_posts = Adopt_post.objects.filter(id=pk)
    post_serializer = Adopt_postSerializer(adopt_posts, many = True)
    adopt_post = Adopt_post.objects.get(id=pk)
    # post_serializer = Adopt_postSerializer(adopt_post, many = True)
    adopt_post.view_count = adopt_post.view_count+1
    adopt_post.save()
    comments = Comment.objects.filter(commented_post_type="adopt").filter(commented_post=adopt_post.id)
    comments_serializer = CommentSerializer(comments, many = True)
    
    return Response({'post':post_serializer.data,'comments':comments_serializer.data})

@api_view(['POST'])
def adopt_post_delete(request,pk):
    adopt_post = Adopt_post.objects.get(id=pk)
    adopt_post.delete()
    return Response(1, status = status.HTTP_201_CREATED)







def master_login(request):
    
    if request.method == "GET":
        return render(request,"login.html")
    else:
        try:
            master_admin=Master_admin.objects.get(account=request.POST['account'])
        except:
            return render(request,"login.html")
        if master_admin.pwd == request.POST['pwd']:
            return render(request,"master_home.html",{'report_num':Report.objects.all().count()})
        else:
            return render(request,"login.html")







def master_home(request):

    return render(request,"master_home.html",{'report_num':Report.objects.all().count()})



def master_user_list(request):
    
    if request.method == "GET":
        users = User.objects.all()
        ks = User.objects.all().values('key','id')
        return render(request,"master_user_list.html",{'users':users,'ks':ks})
    else:
        users = User.objects.filter(nickname=request.POST['nickname'])
        return render(request,"master_user_list.html",{'users':users})
    

def master_user_detail(request,pk):

    user = User.objects.get(id=pk)
    return render(request,"master_user_detail.html",{'user':user})



def master_user_update(request,pk):

    if request.method == "GET":
        user = User.objects.get(id=pk)
        return render(request,"master_user_update.html",{'user':user})
    else:
        user = User()
        user.nickname = request.POST['nickname']
        user.key = request.POST['key']
        user.save()
        return render(request,"master_user_detail.html",{'user':user})

def master_user_delete(request,pk):

    user = User.objects.get(id=pk)
    user.delete()
    users = User.objects.all()
    return render(request,"master_user_list.html",{'users':users})




def master_owner_post_list(request):

    if request.method == "GET":
        owner_posts = Owner_post.objects.all()
        return render(request,"master_owner_post_list.html",{'owner_posts':owner_posts})
    else:
        if request.POST['title']=="":
            if request.POST['posted_time_from']=="" or request.POST['posted_time_to']=="":
                owner_posts = Owner_post.objects.all()
            else:
                owner_posts = Owner_post.objects.filter(posted_time__gte=request.POST['posted_time_from'],posted_time__lte=request.POST['posted_time_to'])
        else:
            if request.POST['posted_time_from']=="" or request.POST['posted_time_to']=="":
                owner_posts = Owner_post.objects.filter(title=request.POST['title'])
            else:
                owner_posts = Owner_post.objects.filter(title=request.POST['title'],posted_time__gte=request.POST['posted_time_from'],posted_time__lte=request.POST['posted_time_to'])
            
        return render(request,"master_owner_post_list.html",{'owner_posts':owner_posts})
    
def master_owner_post_detail(request,pk):

    owner_post = Owner_post.objects.get(id=pk)
    return render(request,"master_owner_post_detail.html",{'owner_post':owner_post})
    
def master_owner_post_update(request,pk):

    if request.method == "GET":
        owner_post = Owner_post.objects.get(id=pk)
        return render(request,"master_owner_post_update.html",{'owner_post':owner_post})
    else:
        owner_post = Owner_post()
        owner_post.title = request.POST['title']
        owner_post.user_nickname = request.POST['user_nickname']
        owner_post.phone_num = request.POST['phone_num']
        owner_post.dog_name = request.POST['dog_name']
        owner_post.dog_type = request.POST['dog_type']
        owner_post.dog_sex = request.POST['dog_sex']
        owner_post.dog_age = request.POST['dog_age']
        owner_post.lost_time = request.POST['lost_time']
        owner_post.dog_feature = request.POST['dog_feature']
        owner_post.remark = request.POST['remark']
        owner_post.save()
        a=request.FILES['picture']
        fs=FileSystemStorage()
        fn=fs.save(owner_post.imageurl,a)
        return render(request,"master_owner_post_detail.html",{'owner_post':owner_post})

def master_owner_post_delete(request,pk):

    owner_post = Owner_post.objects.get(id=pk)
    owner_post.delete()
    owner_posts = Owner_post.objects.all()
    return render(request,"master_owner_post_list.html",{'owner_posts':owner_posts})



def master_finder_post_list(request):

    if request.method == "GET":
        finder_posts = Finder_post.objects.all()
        return render(request,"master_finder_post_list.html",{'finder_posts':finder_posts})
    else:
        if request.POST['title']=="":
            if request.POST['posted_time_from']=="" or request.POST['posted_time_to']=="":
                finder_posts = Finder_post.objects.all()
            else:
                finder_posts = Finder_post.objects.filter(posted_time__gte=request.POST['posted_time_from'],posted_time__lte=request.POST['posted_time_to'])
        else:
            if request.POST['posted_time_from']=="" or request.POST['posted_time_to']=="":
                finder_posts = Finder_post.objects.filter(title=request.POST['title'])
            else:
                finder_posts = Finder_post.objects.filter(title=request.POST['title'],posted_time__gte=request.POST['posted_time_from'],posted_time__lte=request.POST['posted_time_to'])
          
        return render(request,"master_finder_post_list.html",{'finder_posts':finder_posts})
    
def master_finder_post_detail(request,pk):

    finder_post = Finder_post.objects.get(id=pk)
    return render(request,"master_finder_post_detail.html",{'finder_post':finder_post})
    
def master_finder_post_update(request,pk):

    if request.method == "GET":
        finder_post = Finder_post.objects.get(id=pk)
        return render(request,"master_finder_post_update.html",{'finder_post':finder_post})
    else:
        finder_post = Finder_post()
        finder_post.title = request.POST['title']
        finder_post.user_nickname = request.POST['user_nickname']
        finder_post.phone_num = request.POST['phone_num']
        finder_post.dog_type = request.POST['dog_type']
        finder_post.find_time = request.POST['find_time']
        finder_post.shelter = request.POST['shelter']
        finder_post.dog_feature = request.POST['dog_feature']
        finder_post.save()
        a=request.FILES['picture']
        fs=FileSystemStorage()
        fn=fs.save(finder_post.imageurl,a)
        return render(request,"master_finder_post_detail.html",{'finder_post':finder_post})

def master_finder_post_delete(request,pk):

    finder_post = Finder_post.objects.get(id=pk)
    finder_post.delete()
    finder_posts = Finder_post.objects.all()
    return render(request,"master_finder_post_list.html",{'finder_posts':finder_posts})



def master_dog_shelter_list(request):

    dog_shelters = Dog_shelter.objects.all()
    return render(request,"master_dog_shelter_list.html",{'dog_shelters':dog_shelters})

def master_dog_shelter_detail(request,pk):

    dog_shelter = Dog_shelter.objects.get(id=pk)
    return render(request,"master_dog_shelter_detail.html",{'dog_shelter':dog_shelter})

def master_dog_shelter_update(request,pk):
    
    if request.method == "GET":
        dog_shelter = Dog_shelter.objects.get(id=pk)
        return render(request,"master_dog_shelter_update.html",{'dog_shelter':dog_shelter})
    else:
        dog_shelter = Dog_shelter()
        dog_shelter.shelter_name = request.POST['shelter_name']
        dog_shelter.phone_num = request.POST['phone_num']
        dog_shelter.description = request.POST['description']
        dog_shelter.save()
        return render(request,"master_dog_shelter_detail.html",{'dog_shelter':dog_shelter})

def master_dog_shelter_delete(request,pk):

    dog_shelter = Dog_shelter.objects.get(id=pk)
    dog_shelter.delete()
    dog_shelters = Dog_shelter.objects.all()
    return render(request,"master_dog_shelter_list.html",{'dog_shelters':dog_shelters})



def master_report_list(request):

    reports = Report.objects.all()
    return render(request,"master_report_list.html",{'reports':reports})

def master_report_detail(request,pk):

    report = Report.objects.get(id=pk)
    return render(request,"master_report_detail.html",{'report':report})

def master_report_update(request,pk):

    if request.method == "GET":
        report = Report.objects.get(id=pk)
        return render(request,"master_report_update.html",{'report':report})
    else:
        report = Report()
        report.user_nickname = request.POST['user_nickname']
        report.contents = request.POST['contents']
        report.save()
        return render(request,"master_report_detail.html",{'report':report})

def master_report_delete(request,pk):

    report = Report.objects.get(id=pk)
    report.delete()
    reports = Report.objects.all()
    return render(request,"master_report_list.html",{'reports':reports})


def master_adopt_post_list(request):

    adopt_posts = Adopt_post.objects.all()
    return render(request,"master_adopt_post_list.html",{'adopt_posts':adopt_posts})

def master_adopt_post_detail(request,pk):

    adopt_post = Adopt_post.objects.get(id=pk)
    return render(request,"master_adopt_post_detail.html",{'adopt_post':adopt_post})

def master_adopt_post_update(request,pk):
    
    if request.method == "GET":
        adopt_post = Adopt_post.objects.get(id=pk)
        return render(request,"master_adopt_post_update.html",{'adopt_post':adopt_post})
    else:
        adopt_post = Adopt_post()
        adopt_post.title = request.POST['title']
        adopt_post.user_nickname = request.POST['user_nickname']
        adopt_post.phone_num = request.POST['phone_num']
        adopt_post.dog_sex = request.POST['dog_sex']
        adopt_post.dog_type = request.POST['dog_type']
        adopt_post.is_neu = request.POST['is_neu']
        adopt_post.is_vac = request.POST['is_vac']
        adopt_post.shelter = request.POST['shelter']
        adopt_post.contents = request.POST['contents']
        adopt_post.save()
        a=request.FILES['picture']
        fs=FileSystemStorage()
        fn=fs.save(adopt_post.imageurl,a)
        return render(request,"master_adopt_post_detail.html",{'adopt_post':adopt_post})



def master_adopt_post_delete(request,pk):

    adopt_post = Adopt_post.objects.get(id=pk)
    adopt_post.delete()
    adopt_posts = Adopt_post.objects.all()
    return render(request,"master_adopt_post_list.html",{'adopt_posts':adopt_posts})


def poster_mail(request):
    
    formimg = cv2.imread('media/poster/poster_form.jpg',1)
    dogimg = cv2.imread('media/owner/6/profile.jpg')
    dogimg = cv2.resize(dogimg,(344,344))
    formimg[85:85+344,17:17+344] = dogimg
    cv2.imwrite('media/owner/6/poster.jpg',formimg)
    img = Image.open('media/owner/6/poster.jpg')
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("media/poster/NanumGothic.ttf",30)
    draw.text((15,435),"연락처:010-4478-3569",(255,255,255),font=font)
    font = ImageFont.truetype("media/poster/NanumGothic.ttf",20)
    draw.text((15,470),"견종 : 포메라니안    이름 : 멍멍이",(255,255,255),font=font)
    draw.text((15,490),"성별 : 수컷    나이 : 10살",(255,255,255),font=font)
    draw.text((15,510),"실종시간 : 2019-06-09",(255,255,255),font=font)
    draw.text((15,530),"특징 : 어쩌고저쩌고 블라블라~~",(255,255,255),font=font)

    img.save("media/owner/6/poster.jpg")

    
    email = 'kyk1047715@ajou.ac.kr'
    mail = EmailMessage("포스터 보내드립니다.", "포스터를 제작하여 보내드렸습니다.", to=[email])
    fp = open('media/owner/6/poster.jpg', 'rb')
    file_data = fp.read()
    mail.attach('media/owner/6/poster.jpg',file_data,'image/jpeg')

    mail.send()
    t="QWE"
    return render(request,"home.html",{'t':t})
