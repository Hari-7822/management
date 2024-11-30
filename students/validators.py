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