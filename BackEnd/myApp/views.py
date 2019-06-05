from django.shortcuts import render
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *

from rest_framework.decorators import api_view
from rest_framework import viewsets

from datetime import datetime, timedelta

import logging
import base64
from PIL import Image
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
        
    owner_posts = Owner_post.objects.filter(is_finished=0).values('title','id','dog_type','lost_time','imageurl','view_count','lat','lng')
    serializer = Owner_postSerializer(owner_posts, many = True)
    return Response(owner_posts)
@api_view(['GET'])
def finder_post_list(request):

    finder_posts = Finder_post.objects.filter(is_finished=0).values('title','id','dog_type','find_time','imageurl','view_count','lat','lng')
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
        if serializer.is_valid():
            serializer.save()

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
    owner_posts = Owner_post.objects.filter(is_finished=0).filter(
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
    finder_posts = Finder_post.objects.filter(is_finished=0).filter(
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
            finder_posts = Finder_post.objects.filter(is_finished=0).filter(dog_type = filtering.data['value'])
            serializerFinder = Finder_postSerializer(finder_posts, many = True)
        elif(filtering.data['category']=='작성자' and filtering.data['value']!=''):
            finder_posts = Finder_post.objects.filter(is_finished=0).filter(user_nickname = filtering.data['value'])
            serializerFinder = Finder_postSerializer(finder_posts, many = True)
        else:
            finder_posts = Finder_post.objects.filter(is_finished=0)
            serializerFinder = Finder_postSerializer(finder_posts, many = True)
    else: 
        if(filtering.data['category']=='견종' and filtering.data['value']!=''):
            finder_posts = Finder_post.objects.filter(is_finished=0).filter(dog_type = filtering.data['value']).filter(find_time__gte = filtering.data['starttime']).filter(find_time__lte = filtering.data['finaltime'])
            serializerFinder = Finder_postSerializer(finder_posts, many = True)
        elif(filtering.data['category']=='작성자' and filtering.data['value']!=''):
            finder_posts = Finder_post.objects.filter(is_finished=0).filter(user_nickname = filtering.data['value']).filter(find_time__gte = filtering.data['starttime']).filter(find_time__lte = filtering.data['finaltime'])
            serializerFinder = Finder_postSerializer(finder_posts, many = True)
        else:
            finder_posts = Finder_post.objects.filter(is_finished=0).filter(find_time__gte = filtering.data['starttime']).filter(find_time__lte = filtering.data['finaltime'])
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
            owner_posts = Owner_post.objects.filter(is_finished=0).filter(dog_type = filtering.data['value'])
            serializerOwner = Owner_postSerializer(owner_posts, many = True)
        elif(filtering.data['category']=='작성자' and filtering.data['value']!=''):
            owner_posts = Owner_post.objects.filter(is_finished=0).filter(user_nickname = filtering.data['value'])
            serializerOwner = Owner_postSerializer(owner_posts, many = True)
        else:
            owner_posts = Owner_post.objects.filter(is_finished=0)
            serializerOwner = Owner_postSerializer(owner_posts, many = True)
    else: 
        if(filtering.data['category']=='견종' and filtering.data['value']!=''):
            owner_posts = Owner_post.objects.filter(is_finished=0).filter(dog_type = filtering.data['value']).filter(lost_time__gte = filtering.data['starttime']).filter(lost_time__lte = filtering.data['finaltime'])
            serializerOwner = Owner_postSerializer(owner_posts, many = True)
        elif(filtering.data['category']=='작성자' and filtering.data['value']!=''):
            owner_posts = Owner_post.objects.filter(is_finished=0).filter(user_nickname = filtering.data['value']).filter(lost_time__gte = filtering.data['starttime']).filter(lost_time__lte = filtering.data['finaltime'])
            serializerOwner = Owner_postSerializer(owner_posts, many = True)
        else:
            owner_posts = Owner_post.objects.filter(is_finished=0).filter(lost_time__gte = filtering.data['starttime']).filter(lost_time__lte = filtering.data['finaltime'])
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


    finder_posts1 = Finder_post.objects.filter(is_finished=0).filter(dog_type=owner_post.dog_type).values('title','id','dog_type','find_time','imageurl','view_count','lat','lng')
    finder_posts2 = Finder_post.objects.filter(is_finished=0).filter(find_time__gte=owner_post.lost_time+timedelta(days=-7)).filter(find_time__lte=owner_post.lost_time+timedelta(days=7)).values('title','id','dog_type','find_time','imageurl','view_count','lat','lng')
    finder_posts3 = Finder_post.objects.filter(is_finished=0).filter(
        lat__gte = owner_post.lat - 0.005,
        lat__lte = owner_post.lat + 0.005,
        lng__gte = owner_post.lng - 0.005,
        lng__lte = owner_post.lng + 0.005
        ).values('title','id','dog_type','find_time','imageurl','view_count','lat','lng')
    serializerFinder1 = Finder_postSerializer(finder_posts1, many = True)
    serializerFinder2 = Finder_postSerializer(finder_posts2, many = True)
    serializerFinder3 = Finder_postSerializer(finder_posts3, many = True)
        
    finder_posts = Finder_post.objects.filter(is_finished=0).filter(dog_type=owner_post.dog_type).filter(find_time__gte=owner_post.lost_time+timedelta(days=-7)).filter(find_time__lte=owner_post.lost_time+timedelta(days=7)).filter(
        lat__gte = owner_post.lat - 0.005,
        lat__lte = owner_post.lat + 0.005,
        lng__gte = owner_post.lng - 0.005,
        lng__lte = owner_post.lng + 0.005
        ).values('title','id','dog_type','find_time','imageurl','view_count','lat','lng')
    serializerFinder = Finder_postSerializer(finder_posts, many = True)
    
    return Response({'recommend' : finder_posts}, status = status.HTTP_201_CREATED)  
    # return Response({'recommend1' : finder_posts1,'recommend2' : finder_posts2,'recommend3' : finder_posts3}, status = status.HTTP_201_CREATED)
    # return Response({'recommend1' : serializerFinder1.data,'recommend2' : serializerFinder2.data,'recommend3' : serializerFinder3.data}, status = status.HTTP_201_CREATED)
    # return Response(serializerFinder1.data+serializerFinder2.data+serializerFinder3.data, status = status.HTTP_201_CREATED)

@api_view(['GET'])
def f2o_recommend(request,pk):
    finder_post = Finder_post.objects.get(id=pk)
    

    owner_posts1 = Owner_post.objects.filter(is_finished=0).filter(dog_type=finder_post.dog_type).values('title','id','dog_type','lost_time','imageurl','view_count','lat','lng')
    owner_posts2 = Owner_post.objects.filter(is_finished=0).filter(lost_time__gte=finder_post.find_time+timedelta(days=-7)).filter(lost_time__lte=finder_post.find_time+timedelta(days=7)).values('title','id','dog_type','lost_time','imageurl','view_count','lat','lng')
    owner_posts3 = Owner_post.objects.filter(is_finished=0).filter(
        lat__gte = finder_post.lat - 0.01,
        lat__lte = finder_post.lat + 0.01,
        lng__gte = finder_post.lng - 0.01,
        lng__lte = finder_post.lng + 0.01
        ).values('title','id','dog_type','lost_time','imageurl','view_count','lat','lng')
    serializerOwner1 = Owner_postSerializer(owner_posts1, many = True)
    serializerOwner2 = Owner_postSerializer(owner_posts2, many = True)
    serializerOwner3 = Owner_postSerializer(owner_posts3, many = True)
    
    owner_posts = Owner_post.objects.filter(is_finished=0).filter(dog_type=finder_post.dog_type).filter(lost_time__gte=finder_post.find_time+timedelta(days=-7)).filter(lost_time__lte=finder_post.find_time+timedelta(days=7)).filter(
        lat__gte = finder_post.lat - 0.01,
        lat__lte = finder_post.lat + 0.01,
        lng__gte = finder_post.lng - 0.01,
        lng__lte = finder_post.lng + 0.01
        ).values('title','id','dog_type','lost_time','imageurl','view_count','lat','lng')
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
    finish_finder_posts = Finder_post.objects.filter(is_finished=1).values('title','id','dog_type','lost_time','imageurl','view_count','lat','lng')
    serializer = Finder_postSerializer(finish_finder_posts, many = True)
    finish_owner_posts = Owner_post.objects.filter(is_finished=1).values('title','id','dog_type','lost_time','imageurl','view_count','lat','lng')
    serializer = Owner_postSerializer(finish_owner_posts, many = True)
    return Response(finish_finder_posts.data+finish_owner_posts.data)

@api_view(['POST'])
def adopt_login(request):
    serializer = Adopt_adminSerializer(data = request.data)
    if serializer.is_valid():
        adopt_admin = Adopt_admin.objects.get(account=serializer.data['account'])
        if adopt_admin.pwd==serializer.data['pwd']:
            return Response(1)
        else:
            return Response(0)

@api_view(['GET'])
def adopt_post_list(request):
    adopt_posts = Adopt_post.objects.all().values('title','id','dog_type','imageurl','posted_time')
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
