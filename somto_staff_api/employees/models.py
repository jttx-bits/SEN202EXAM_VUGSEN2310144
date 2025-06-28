from django.db import models

class StaffBase (models.Model):
    name = models.CharField(max_length=100)
    email= models.EmailField(unique=True)
    join_date =  models.DateField(auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name
    
    def get_role(self):
        return "Staff"
    
class Manager (StaffBase):
    department = models.CharField(max_length=50)
    has_company_card = models.BooleanField(default=True)

    class Meta:
        verbose_name= "Manager"

    def get_role(self):
        return f"Manger (Department: {self.department})"


class Intern(StaffBase):
    mentor = models.ForeignKey(
        Manager, on_delete=models.SET_NULL,
        null=True, 
        blank=True, 
        related_name="Interns")
        
    
                                            
    internship_end = models.DateField()

    class Meta:
        verbose_name = "Intern"

    def get_role(self):
        return f"Intern (Mentor: {self.mentor.name})"


# Create your models here.
