from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
from rest_framework.response import responses,Response
from rest_framework.views import APIView
from rest_framework import status
from .serailizer import *

class student_views(APIView):
    def get(self,request):
        obj=SchoolData.objects.all().order_by('id').reverse()
        obj_id=SchoolData.objects.filter(id='0')

        if obj_id:
            serializ=StudentSerailizer(obj_id,many=True)
            success_message = {"msg":"You student data is this:"}
            return Response({**success_message, "data": serializ.data},status= status.HTTP_200_OK)
        else:
            serializ=StudentSerailizer(obj,many=True)
            success_message = {"msg":"You student data is this:"}
            return Response({**success_message, "data": serializ.data},status= status.HTTP_200_OK)
        

    
    def post(self,request):
        seriliz=StudentSerailizer(data=request.data)
        if seriliz.is_valid():
            seriliz.save()
            success_message = {"Registration successful."}
            return HttpResponse(success_message,{'data':seriliz.data},status=status.HTTP_201_CREATED)
        success_message={"Data is not stored in the Databse!..."}
        return HttpResponse(success_message,seriliz.data, status=status.HTTP_400_BAD_REQUEST)
    





# class IdData(APIView):
#     def get(self,request):

#         id_value = request.query_params.get('21')
        
#         # id_value=SchoolData.objects.get('20')
#         if id_value is not None:
            
#             try:
#                 obj = SchoolData.objects.get(id=id_value)
#                 serializer = StudentSerailizer(obj)
#                 return Response(serializer.data, status=status.HTTP_200_OK)
#             except SchoolData.DoesNotExist:
#                 return Response({"error": "School data with the given id does not exist."}, status=status.HTTP_404_NOT_FOUND)
#         else:
#             return Response({"error": "Please provide an 'id' parameter in the query."}, status=status.HTTP_400_BAD_REQUEST)
       
        
 