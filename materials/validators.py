import re
from rest_framework.serializers import ValidationError


class VideoURLValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        reg = re.compile(r'(https?://)?(www\.)?youtube\.com')
        if not re.match(reg, value):
            raise ValidationError('Поддерживаются только youtube-видео!')
