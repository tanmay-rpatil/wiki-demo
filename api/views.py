from rest_framework import status
from rest_framework.reverse import reverse
from .serializers import EntrySerializer, EntryListSerializer
from encyclopedia.models import Entry
from rest_framework.decorators import api_view,authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import random
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
	'List':'/entry-list/',
	'Detail View':'/entry-detail/<int:pk>/',
	'Create':'/entry-create/',
	'Update':'/entry-update/<int:pk>/',
	'Random':'/entry-random/',
	'Search':'/entry-search/?q=<str:search_query>',
	'Delete':'/entry-delete/<int:pk>/',
	}
	return Response(api_urls)

@api_view(['GET'])
def entrylist(request,format=None):
	entrys = Entry.objects.all()
	serializer = EntryListSerializer(entrys,many=True)
	return Response(serializer.data)

@api_view(['GET'])
def entrysearch(request,format=None):
	entrys = Entry.objects.filter(title__contains= request.GET.get('q'))
	serializer = EntryListSerializer(entrys,many=True)
	return Response(serializer.data)

@api_view(['GET'])
def entryrandom(request,format=None):
	lst=[]
	for entry in Entry.objects.all():
		lst.append(entry.id)
	# lst = util.list_entries()
	size = len(lst)
	entry = Entry.objects.get(pk=lst[random.randint(0,size-1)])
	return Response( (EntrySerializer(entry,many=False)).data )


@api_view(['GET'])
def entrydeatil(request,pk,format=None):
	try:	
		entrys = Entry.objects.get(pk=pk)
	except:
		return Response(status=status.HTTP_404_NOT_FOUND)
	serializer = EntrySerializer(entrys,many=False)
	return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def entrycreate(request,format=None):
	serializer = EntrySerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	print(serializer.data)
	return Response(serializer.data)

@api_view(['PUT'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def entryupdate(request,pk,format=None):
	try:	
		entry = Entry.objects.get(pk=pk)
	except:
		return Response(status=status.HTTP_404_NOT_FOUND)
	serializer = EntrySerializer(instance=entry,data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def entrydelete(request,pk,format=None):
	try:	
		entry = Entry.objects.get(pk=pk)
	except:
		return Response(status=status.HTTP_404_NOT_FOUND)
	# serializer = TaskSerializer(instance=task,data=request.data)
	entry.delete()
	return Response("Item deleted")