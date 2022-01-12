import string    
import random


def generate_subject(n: int) -> str:
    return ''.join(random.choices(string.ascii_letters + string.digits, k=n))


def generate_message(n: int) -> str:
    return ''.join(random.choices(string.ascii_letters + string.digits, k=n))
