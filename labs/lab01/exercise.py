import time
import sys

def animate_text(text, speed=0.1):
    """Animasi teks per karakter"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def sing_song():
    lyrics = [
        ("Tante...", 0.08),
        ("Sudah Terbiasa Terjadi Tante...", 0.09),
        ("Teman Datang ketika lagi Butuh Saja...", 0.08),
        ("Cuba Kalau Lagi Susah...", 0.15),
        ("Mereka Semua Menghilaaaaang...", 0.12),
    ]

    delays = [0.3, 1.2, 2.0, 2.8, 3.6]   # delay sebelum setiap baris

    for i, (lyric, speed) in enumerate(lyrics):
        time.sleep(delays[i] - (delays[i-1] if i > 0 else 0))  # tunggu selisih delay
        animate_text(lyric, speed)

    print("\n=== Lagu selesai ===")

# Jalankan
sing_song()
