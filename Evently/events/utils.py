from datetime import timedelta
from threading import Timer
from django.core.mail import send_mail
from django.utils.timezone import now
from datetime import datetime, timedelta


from django.core.mail import send_mail

def send_event_email(event_user):
    """Функция отправки email-напоминания"""
    subject = f"📅 Нагадування: {event_user.event.name} вже скоро!"

    message = f"""
    <html>
    <body style="font-family: Arial, sans-serif; color: #333;">
        <h2 style="color: #d63384;">✨ Вітаємо, {event_user.user.first_name}! ✨</h2>
        
        <p>Ви зареєстровані на подію <strong>{event_user.event.name}</strong>, яка відбудеться:</p>
        
        <p>📅 <strong>Дата та час:</strong> {event_user.event.date.strftime('%d.%m.%Y %H:%M')}</p>
        <p>📍 <strong>Місце:</strong> {event_user.event.location}</p>

        <p>📝 <strong>Опис події:</strong></p>
        <p>{event_user.event.description}</p>

        <p>🚀 Не забудьте про подію! Ми з нетерпінням чекаємо на вас.</p>

        <hr style="border: none; border-top: 1px solid #ccc; margin: 20px 0;">
        
        <p>❓ <strong>Є питання?</strong></p>
        <p>📞 Звертайтесь до нашої підтримки: <strong>+38 (098) 123-45-67</strong></p>
        <p>📧 Або пишіть нам: <a href="mailto:support@evently.com" style="color: #007bff;">support@evently.com</a></p>

        <p>До зустрічі! 💙</p>
        <p><strong>Ваша команда Evently</strong></p>
    </body>
    </html>
    """

    send_mail(
        subject,
        "",
        "dereruditor@gmail.com",  # Email отправителя
        [event_user.user.email],  # Email получателя
        fail_silently=False,
        html_message=message,  
    )

    print(f"✅ Нагадування відправлено на {event_user.user.email}!")

def schedule_email(event_user, hours_before):
    """Запланировать отправку email-напоминания за N часов до события"""
    send_time = event_user.event.date - timedelta(hours=hours_before)
    time_until_send = (send_time - now()).total_seconds()

    if time_until_send <= 0:
        # Если время уже прошло или меньше 1 часа → отправляем СРАЗУ
        send_event_email(event_user)
        return

    print(f"⏳ Email буде надіслано через {int(time_until_send)} секунд для {event_user.user.email} ({hours_before} годин до події)")
    Timer(time_until_send, send_event_email, args=[event_user]).start()
