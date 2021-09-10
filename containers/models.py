from django.db import models
from django.urls import reverse

class Contract(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField('date published')


class Rate(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    origin = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    currency = models.CharField(max_length=200)
    twenty = models.CharField(max_length=10)
    forty = models.CharField(max_length=10)
    fortyhc = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('contract_edit', kwargs={'pk': self.pk})

    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)

   #Calling model field instance - What im doing wrong here?
            obj.attachment = book.save("sample.xlsx")

            #Saving model instance
            obj.save()

            #Some return - required for AJAX
            return JsonResponse({"status": "OK"})