# 1. Python bazasi
FROM python:3.10-slim

# 2. Ishchi papkani yaratish
WORKDIR /app

# 3. Tizim kerakli kutubxonalarini o‘rnatish
RUN apt-get update && apt-get install -y gcc libffi-dev libssl-dev

# 4. Requirements faylini qo‘shish
COPY requirements.txt .

# 5. Python kutubxonalarni o‘rnatish
RUN pip install --no-cache-dir -r requirements.txt

# 6. Bot faylini konteynerga nusxalash
COPY bot.py .

# 7. Botni ishga tushirish
CMD ["python", "bot.py"]
