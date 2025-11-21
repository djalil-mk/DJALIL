import os
import time

# ألوان
G = "\033[1;32m"
Y = "\033[1;33m"
R = "\033[1;31m"
C = "\033[1;36m"
W = "\033[1;37m"

os.system("clear")

print(G + "==============================")
print(C + "     DJALIL SCRIPT TOOL")
print(G + "==============================")
print(W + "ضع أي سكربت داخل مجلد scripts وسيظهر هنا\n")

scripts = os.listdir("scripts")

if not scripts:
    print(R + "⚠ لا يوجد أي سكربت داخل مجلد scripts !")
    exit()

for i, s in enumerate(scripts):
    print(Y + f"[{i+1}] تشغيل {s}")

choice = input(G + "\nاختر رقم السكربت: ")

try:
    idx = int(choice) - 1
    script = scripts[idx]
except:
    print(R + "خيار خاطئ!")
    exit()

print(C + f"\n🔰 جاري تشغيل: {script}\n")
time.sleep(1)

# تشغيل السكربت حسب نوعه
if script.endswith(".py"):
    os.system(f"python scripts/{script}")
elif script.endswith(".sh"):
    os.system(f"bash scripts/{script}")
else:
    print(R + "⚠ نوع السكربت غير مدعوم!")
