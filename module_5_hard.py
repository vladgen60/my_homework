import time # Импортируем библиотеку time.
    # Создаем класс User.
class User:
    # Создаем методы класса User.
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age
        
    def __str__(self):
        return f'{self.nickname}'

    def __hash__(self):
        return hash(self.password)

    def __eq__(self, other):
        return self.nickname == other.nickname
    # Создаем класс Video.
class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return f'{self.title}'

    # Создаем класс UrTube.
class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None 

    def log_in(self, nickname, password): # Если пользователь существует, то текущий пользователь меняется на найденного.
        for user in self.users:
            if user.nickname == nickname and user.password == User(password):
                self.current_user = user 
                return None
    
    def register(self, nickname, password, age): 
        if any(user.nickname == nickname for user in self.users): # Проверяем есть ли пользователь в списке. 
            print(f'Пользователь {nickname} уже существует.')
            return None
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user

    def log_out(self): # Сброс текущего пользователя.
        self.current_user = None

    def add(self, *videos): # Добавление нового видео.
        for video in videos:
            if video not in self.videos:
                self.videos.append(video)
            continue

    def get_videos(self, word): # Поиск видео с учетом регистра.
        word = word.lower()
        search_list = []
        for video in self.videos:
            if word in video.title.lower():
                search_list.append(video.title)
        return search_list

    def watch_video(self, title): # Поиск и запуск нового видео.
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео.')
            return None
        elif title in self.videos is None:
            return None
        elif self.current_user and self.current_user.age < 18:
            print('Вам нет 18 лет, пожалуйста покиньте страницу')
            return None
        elif self.current_user:
            for video in self.videos:
                if title in video.title:
                    for i in range(1, 11):
                        print(i, end=' ')
                        time.sleep(1)
                    print('Конец видео') 

 
if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео

    ur.add(v1, v2)

# Проверка поиска

    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение

    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт

    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

# Попытка воспроизведения несуществующего видео

    ur.watch_video('Лучший язык программирования 2024 года!')