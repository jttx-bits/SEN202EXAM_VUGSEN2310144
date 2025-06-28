from rest_framework import serializers
from.models import Manager, Intern

class StaffBaseSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()
    email = serializers.EmailField(read_only = True)

    class Meta:
        fields = ('id', 'name', 'email', 'join_date', 'role')

    def get_role(self, obj):
        return obj.get_role()
    

class ManagerSerializer(StaffBaseSerializer):

    class Meta(StaffBaseSerializer.Meta):
        model= Manager
        fields= StaffBaseSerializer.Meta.fields + ("departmemt", "has_company_card")


class InternSerializer(StaffBaseSerializer):

    class Meta(StaffBaseSerializer.Meta):
        model = Intern
        fields = StaffBaseSerializer.Meta.fields + ("mentor", "internship_end")