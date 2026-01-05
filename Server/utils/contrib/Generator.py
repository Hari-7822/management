from django.core.cache import cache
import random

import random

class PasswordGenerator:
    upper = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    lower = list("abcdefghijklmnopqrstuvwxyz")
    numbers = list("0123456789")
    symbols = list("!@#$%^&*()_-+={[}]|:;\"'<>,.?/")

    def generate(self,request, length: int, letters: bool, numbers: bool, symbols: bool, duration:int=5000) -> str:
        passkey = []
        if letters:
            passkey.extend(self.upper + self.lower)
        if numbers:
            passkey.extend(self.numbers)
        if symbols:
            passkey.extend(self.symbols)

        if not passkey:
            raise ValueError("At least one character type must be selected.")

        password = random.sample(passkey, length)
        cache.set(f"OTP for {request.user}", password, timeout=duration)
        return "".join(password)


    def generate_otp(self, request, length:int,duration:int=5000) -> str:
        otp = random.sample(self.numbers,length)
        cache.set(f"OTP for {request.user}", otp, timeout=duration)
        return "".join(otp)

    def generate_key(self, request, length:int) -> str:
        key = random.sample(self.numbers,length=4)
        cache.set(f"OTP for {request.user}", key)
        return "".join(key)
    
    def validate(self,request) -> bool:
        return True if str(request.otp) == str(cache.get(f"OTP for {request.user}")) else False
    
    