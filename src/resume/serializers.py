from rest_framework import serializers

from resume.models import Resume


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = [
            'status', 'grade', 'specialty', 'salary', 'education',
            'experience', 'portfolio', 'title', 'phone', 'email',
        ]
