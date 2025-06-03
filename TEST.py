import os
import shutil
import sys
from pathlib import Path

def get_script_path():
    """Возвращает абсолютный путь к текущему исполняемому скрипту."""
    return Path(sys.argv[0]).resolve()

def create_dummy_files(target_dir: Path, num_files: int = 3):
    """Создает несколько пустых файлов в указанной директории."""
    for i in range(1, num_files + 1):
        try:
            dummy_file_path = target_dir / f"zarazhen_fayl_{i}.txt"
            with open(dummy_file_path, "w") as f:
                f.write("Eto testoviy fayl, sozdanniy bezobidnim skriptom.\n")
            print(f"  [+] Sozdan fayl: {dummy_file_path}")
        except Exception as e:
            print(f"  [!] Oshibka pri sozdanii fayla {dummy_file_path}: {e}")

def simulate_activity():
    """Основная функция для имитации вирусной активности."""
    print("Zapusk bezobidnoy imitatsii virusnoy aktivnosti...")
    
    script_path = get_script_path()
    script_name = script_path.name
    print(f"[INFO] Tekushchiy skript: {script_path}")

    # Определяем целевые директории относительно домашней папки пользователя
    # Используем os.path.expanduser('~') для кроссплатформенности
    home_dir = Path(os.path.expanduser('~'))
    target_relative_dirs = [
        "Documents/VirusTest", 
        "Downloads/VirusTest", 
        "Desktop/VirusTest",
        "Pictures/VirusTest"
    ]

    target_dirs = [home_dir / rel_dir for rel_dir in target_relative_dirs]

    for target_dir_base in target_dirs:
        try:
            # Добавляем подпапку с именем скрипта для наглядности
            # target_dir = target_dir_base / script_name.split('.')[0] 
            # Решил не делать подпапку с именем скрипта, чтобы не усложнять пути
            target_dir = target_dir_base

            print(f"\n[+] Obrabotka direktotii: {target_dir}")
            
            # 1. Создаем целевую директорию, если она не существует
            os.makedirs(target_dir, exist_ok=True)
            print(f"  [+] Direktoriya {target_dir} proverena/sozdana.")
            
            # 2. Копируем скрипт в целевую директорию
            destination_script_path = target_dir / script_name
            if script_path != destination_script_path: # Не копировать себя на себя же
                shutil.copy2(script_path, destination_script_path)
                print(f"  [+] Skript skopirovan v: {destination_script_path}")
            else:
                print(f"  [INFO] Propushcheno kopirovanie v iskhodnuyu direktoriyu: {destination_script_path}")

            # 3. Создаем несколько "зараженных" файлов
            create_dummy_files(target_dir)
            
        except Exception as e:
            print(f"[!] Oshibka pri obrabotke direktorii {target_dir_base}: {e}")

    print("\nImitatsiya aktivnosti zavershena.")
    print("CHto bilo sdelano:")
    print(f"1. Etot skript ({script_name}) byl skopirovan v neskol'ko papok vnutri vashey pol'zovatel'skoy direktorii ({home_dir}).")
    print("   Tselevyye papki:")
    for rel_dir in target_relative_dirs:
        print(f"     - {home_dir / rel_dir}")
    print("2. V kazhdoy iz etikh papok byli sozdany neskol'ko pustykh .txt faylov.")
    print("\nPomnite: eto BEZOBIDNAYA imitatsiya. Fayly ne soderzhat vreda.")
    print("Mozhete udalit' papki 'VirusTest' i skopirovannye skripty вручную.")

if __name__ == "__main__":
    simulate_activity()