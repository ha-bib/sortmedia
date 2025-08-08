import os
import shutil
from datetime import datetime

# Folder sumber & tujuan
SOURCE_DIR = "/storage/emulated/0/DCIM/Camera"
DEST_DIR = "/storage/emulated/0/DCIM"

BULAN_NAMA = {
    "01": "Januari", "02": "Februari", "03": "Maret", "04": "April",
    "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus",
    "09": "September", "10": "Oktober", "11": "November", "12": "Desember"
}

def get_file_date(file_path):
    """Get file date from modification time (fallback approach)"""
    try:
        # Use file modification time as fallback
        return datetime.fromtimestamp(os.path.getmtime(file_path))
    except Exception:
        return datetime.now()

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
                    # Get date from file modification time
                    date_obj = get_file_date(src_path)

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
