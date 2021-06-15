from rest_framework import serializers
from encyclopedia.models import Entry

class EntrySerializer(serializers.ModelSerializer):
	class Meta:
		model = Entry
		fields = ['id','title','content']

class EntryListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Entry
		fields = ['id','title']