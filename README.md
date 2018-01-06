# It's a set of useful classes to work with Django choices

### How to install
```bash
pip install simple-choices
```

### How to use

```python
>>> class AttachmentType(simple_choices.SimpleChoice):
>>>    video = 'It is video'
>>>    image = 'It is image'
>>>
>>> AttachmentType.choices
(('media', 'Media'), ('image', 'Image'))
>>> Attachment.video
'video'
```
So it's simple to use with Django.
```python
class Attachment(django.db.models.Model):
    attachment_type = django.db.models.CharField(
    	choices=AttachmentType.choices, max_length=32)
```