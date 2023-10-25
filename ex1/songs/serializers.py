from rest_framework import serializers
from .models import Song
from datetime import date

class SongSerializer(serializers.ModelSerializer):
    # Q13 & Q14:
    youtube_url = serializers.CharField(read_only=True)
    class Meta:
        model = Song
        fields = '__all__'

    def update(self, instance, validated_data):
    # Implement here an update function
        instance.song_name = validated_data.get('song_name', instance.song_name)
        instance.song_id = validated_data.get('song_id', instance.song_id)
        instance.released_date = validated_data.get('released_date', instance.released_date)
        instance.singer_name = validated_data.get('singer_name', instance.singer_name)
        instance.save()
        return instance

# Q10:
    def validate(self, data):
        """
        Check that the song name is not empty
        """
        if data['song_name'] == " ":
            raise serializers.ValidationError("song name must not be empty")
        return data
    
# Q15:
    days_since_released_date =serializers.SerializerMethodField()
    def get_days_since_released_date(self, song):
        return(date.today() - song.released_date).days