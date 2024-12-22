import subprocess
import os


def run_script(script_path, txtf_path, *args):
    if not os.path.isfile(script_path):
        print(f"Скрипт {script_path} не существует")
        return

    # Передача пути к txtf
    env = os.environ.copy()
    env['TXT_FILE_PATH'] = txtf_path

    result = subprocess.run(["python", script_path] + list(args), capture_output=True, text=True, env=env)
    print(result.stdout)

    # Проверка, не является ли скрипт тестовым файлом
    if 'test' in os.path.basename(script_path):
        # Проверка для предотвращения вывода ошибки
        if result.stderr and 'Ran' not in result.stdout:
            print(result.stderr)
    else:
        if result.stderr:
            print(f"Ошибка записи {script_path}:")
            print(result.stderr)
    if "test" not in str(script_path):
        print(f"Закончено выполнение {script_path}\n")


def run_task(task_path):
    print('---------------------------------------')
    print(f"Выполнение задания {task_path}")
    src_path = os.path.join(task_path, "src")
    tests_path = os.path.join(task_path, "tests")
    txtf_path = os.path.join(task_path, "txtf")
    if not os.path.isdir(tests_path):
        print(f"Папка тестов {tests_path} не существует")
        return

    for test in os.listdir(tests_path):
        if test.endswith(".py"):
            run_script(os.path.join(tests_path, test), txtf_path)
            
    if not os.path.isdir(src_path):
        print(f"Папка с кодами {src_path} не существует")
        return

    for script in os.listdir(src_path):
        if script.endswith(".py"):
            run_script(os.path.join(src_path, script), txtf_path)

    print(f"Конец выполнения задания {task_path}")
    print('---------------------------------------\n')


def run_lab(lab_path):
    print(f"Выполнение лаборатрной {lab_path}")
    for task in os.listdir(lab_path):
        task_path = os.path.join(lab_path, task)
        if os.path.isdir(task_path) and not task.startswith('__pycache__'):
            run_task(task_path)
    print(f"Окончание выполнения лабораторной {lab_path}\n")
    print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')


def main():
    labs = ["lab2", "lab3", "lab4", "lab5", "lab6"]
    for lab in labs:
        run_lab(lab)


if __name__ == "__main__":
    main()