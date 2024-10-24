from django.shortcuts import get_object_or_404

class GenericCRUDManager:
    def __init__(self, model):
        self.model = model

    def get_all(self):
        return self.model.objects.all()

    def get(self, id):
        return get_object_or_404(self.model, id=id)

    def create(self, data):
        return self.model.objects.create(**data)

    def update(self, id, data):
        instance = get_object_or_404(self.model, id=id)
        for key, value in data.items():
            setattr(instance, key, value)
        instance.save()
        return instance

    def delete(self, id):
        instance = get_object_or_404(self.model, id=id)
        instance.delete()
