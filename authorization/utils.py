import random
def generate_key()->str:
    key = str(random.randint(0, 999999))
    return ('0' * (6-len(key))) + key
    

from django.core.mail import send_mail
def send_email(to: str, key: str)->bool:
    subject = "나 뻔뻔 아니다 이메일 인증"
    message = f"인증코드는 {key} 입니다."

    return send_mail(
        subject=subject,
        message=message,
        from_email="notppeonppeon@gmail.com",
        recipient_list=[to]
    )