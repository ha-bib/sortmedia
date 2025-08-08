import os
import shutil
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS

# Folder sumber & tujuan
SOURCE_DIR = "/storage/emulated/0/DCIM/Camera"
DEST_DIR = "/storage/emulated/0/DCIM"

BULAN_NAMA = {
    "01": "Januari", "02": "Februari", "03": "Maret", "04": "April",
    "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus",
    "09": "September", "10": "Oktober", "11": "November", "12": "Desember"
}

def get_exif_date(file_path):
    try:
        img = Image.open(file_path)
        exif_data = img._getexif()
        if exif_data:
            for tag, value in exif_data.items():
                tag_name = TAGS.get(tag, tag)
                if tag_name == "DateTimeOriginal":
                    # Format as "YYYY MM"
                    return datetime.strptime(value, "%Y:%m:%d %H:%M:%S")
    except Exception:
        pass
    return None

def sort_media():
    if not os.path.exists(SOURCE_DIR):
        print(f"❌ Folder sumber tidak ditemukan: {SOURCE_DIR}")
        return

    os.makedirs(DEST_DIR, exist_ok=True)

    count = 0
    for root, dirs, files in os.walk(SOURCE_DIR):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.mp4', '.mov')):
                src_path = os.path.join(root, file)
                try:
                    # Ambil tanggal dari metadata EXIF
                    date_obj = get_exif_date(src_path)

                    # Fallback ke modified time kalau EXIF tidak ada
                    if date_obj is None:
                        date_obj = datetime.fromtimestamp(os.path.getmtime(src_path))

                    year = date_obj.strftime("%Y")
                    month_num = date_obj.strftime("%m")
                    month_name = BULAN_NAMA[month_num]

                    # Format: "YYYY MM NamaBulan"
                    folder_name = f"{year} {month_num} {month_name}"
                    target_folder = os.path.join(DEST_DIR, folder_name)
                    os.makedirs(target_folder, exist_ok=True)

                    shutil.move(src_path, os.path.join(target_folder, file))
                    count += 1
                except Exception as e:
                    print(f"⚠ Gagal memindahkan {file}: {e}")

    print(f"✅ Selesai! {count} file berhasil dipindahkan.")

if __name__ == "__main__":
    sort_media()
