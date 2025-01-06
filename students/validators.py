from django.forms import ValidationError

age_grade_logic = {"5":"Pre-KG",}


def AgeValidator(age):
    if age <= 5 and age > 18:
        return age
    elif age > 5:
        return ValidationError(f"Age- {age} is underage")
    elif age < 18:
        return ValidationError(f"Age- {age} is Over the hill")


def ClassValidator(age, grade):
    pass



def EmailCompletionValidator(self, email):
    if "@gmail.com" not in email:
        return email.append("@gmail.com")
    

def IsAdmin(self, request):
    if request.user.is_superuser and request.user.is_staff is True:
        if request.user.is_active is True:
            return True
        return f"{request.user.username} is not active"
    else:
        return False

def mobile_no_validator(value): 
  mobile = str(value) 
  if len(mobile) != 10: 
    raise ValidationError("Mobile Number Should 10 digit")     



class Fee():
    pass

class Filters():
    class __init__(self):
        pass

    def Sibling(self,):
        # res= student.
        pass
