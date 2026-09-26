🏨 Deluxe Hotel
Django asosida qurilgan to'liq funksional mehmonxona platformasi

Xona band qilish tizimi, restoran menyusi, blog va owner uchun boshqaruv paneli — barchasi bitta loyihada.

Python Django SQLite License

Imkoniyatlar • Texnologiyalar • O'rnatish • Loyiha tuzilishi • Rejalar

</div>
📖 Loyiha haqida

Deluxe Hotel — mehmonxonalar uchun ikki qismli veb-platforma:

🧳 Mehmonlar uchun sayt — xonalarni ko'rish, onlayn band qilish, restoran menyusi, blog va aloqa formasi
🗝️ Owner (admin) paneli — xonalar, buyurtmalar va mijozlar xabarlarini real vaqtda boshqarish

Loyiha Django'ning MVT (Model–View–Template) arxitekturasi asosida, har bir modul (rooms, booking, blog, restaurant, contact, users, owner) alohida ilova sifatida yozilgan — bu kodni tartibli, kengaytiriladigan va professional qiladi.

✨ Asosiy imkoniyatlar
<table> <tr> <td valign="top" width="50%">
🧳 Mehmonlar uchun
🏠 Zamonaviy, responsive bosh sahifa
🛏️ Xonalar ro'yxati — narx, sig'im, maydon, ko'rinish
📅 Onlayn booking (xona band qilish) formasi
🍽️ Restoran menyusi — taom va narxlar
📰 Blog — sahifalash (pagination) bilan
✉️ Aloqa (Contact) formasi
📱 To'liq mobil moslashuvchan dizayn
</td> <td valign="top" width="50%">
🗝️ Owner paneli
🔐 Xavfsiz autentifikatsiya tizimi
📊 Real vaqtdagi statistikali dashboard
🛏️ Xona qo'shish va holatini boshqarish
📋 Buyurtmalar va ularning statusi (Kutilmoqda / Keldi / Bekor qilingan)
📨 Mijozlar xabarlarini o'qish
🌗 Kun/tun (dark mode) rejimi
</td> </tr> </table>
🛠️ Texnologiyalar
Qatlam	Texnologiya
Backend	Python, Django 6.0
Ma'lumotlar bazasi	SQLite (development)
Frontend	HTML5, CSS3, JavaScript
Admin panel dizayni	Django Unfold
Rasmlar bilan ishlash	Pillow
Konfiguratsiya	python-dotenv (.env)
Shrift / ikonlar	Google Fonts, Font Awesome
📁 Loyiha tuzilishi
DELUXEHOTEL/
├── config/            # Django sozlamalari (settings, urls, wsgi/asgi)
├── core/               # Bosh sahifa, "Biz haqimizda"
├── rooms/               # Xonalar (modellar, ro'yxat)
├── booking/             # Xona band qilish tizimi
├── restaurant/          # Restoran menyusi
├── blog/                # Blog / yangiliklar
├── contact/             # Aloqa formasi
├── users/                # Autentifikatsiya (login/logout)
├── owner/                # Admin/owner boshqaruv paneli
├── static/               # CSS, JS, rasmlar
├── templates/             # HTML shablonlar (har bir ilova uchun alohida)
├── requirements.txt
└── manage.py
🚀 O'rnatish
1. Loyihani klonlash
bash
git clone https://github.com/mehroj-pirmamatov/deluxe-hotel-django.git
cd deluxe-hotel-django
2. Virtual muhit yaratish
bash
python -m venv venv
bash
# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
3. Kerakli paketlarni o'rnatish
bash
pip install -r requirements.txt
4. .env faylini sozlash
bash
cp .env.example .env

Yangi maxfiy kalit generatsiya qilish:

bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

Natijani .env faylidagi DJANGO_SECRET_KEY qiymatiga joylashtiring.

5. Ma'lumotlar bazasini tayyorlash
bash
python manage.py migrate
python manage.py createsuperuser
6. Serverni ishga tushirish
bash
python manage.py runserver
	
🌐 Sayt	http://127.0.0.1:8000/
🗝️ Owner panel	http://127.0.0.1:8000/auth/login/
🗺️ Rejadagi yaxshilanishlar
 Xonalar uchun rasm yuklash (ImageField)
 Booking uchun email orqali tasdiqlash xabarnomasi
 Xonalarni sana/narx bo'yicha filtrlash va qidiruv
 To'lov tizimini integratsiya qilish
 REST API (mobil ilova uchun)
📄 Litsenziya

Bu loyiha MIT License ostida tarqatiladi — kod ochiq, o'rganish va o'z loyihalaringizda erkin foydalanishingiz mumkin.

<div align="center">

Muallif: @mehroj-pirmamatov

⭐️ Agar loyiha yoqqan bo'lsa, repo'ga yulduzcha bosishni unutmang!
