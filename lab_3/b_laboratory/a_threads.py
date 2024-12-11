"""
Модуль в котором содержаться потоки Qt
"""

import time
import traceback

import psutil
import requests
from PySide6 import QtCore


class SystemInfo(QtCore.QThread):
    systemInfoReceived = QtCore.Signal(list)  # TODO Создайте экземпляр класса Signal и передайте ему в конструктор тип данных передаваемого значения (в текущем случае list)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.delay = None   # TODO создайте атрибут класса self.delay = None, для управлением задержкой получения данных

    def run(self) -> None:  # TODO переопределить метод run
        if self.delay is None:  # TODO Если задержка не передана в поток перед его запуском
            self.delay = 1  # TODO то устанавливайте значение 1

        while True:  # TODO Запустите бесконечный цикл получения информации о системе
            cpu_value = psutil.cpu_percent()  # TODO с помощью вызова функции cpu_percent() в пакете psutil получите загрузку CPU
            ram_value = psutil.virtual_memory().percent  # TODO с помощью вызова функции virtual_memory().percent в пакете psutil получите загрузку RAM
            self.systemInfoReceived.emit([cpu_value, ram_value])  # TODO с помощью метода .emit передайте в виде списка данные о загрузке CPU и RAM
            time.sleep(self.delay)  # TODO с помощью функции .sleep() приостановите выполнение цикла на время self.delay


class WeatherHandler(QtCore.QThread):
    # TODO Пропишите сигналы, которые считаете нужными
    weatherInfoReceived = QtCore.Signal(dict)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.lat = None
        self.lon = None
        self.__api_url = None
        self.__delay = None
        self.__status = None

    def setCoordinates(self, lat, lon):
        if -180 <= lat <= 180:
            self.lat = lat
        if -180 <= lon <= 180:
            self.lon = lon
        self.__api_url = f"https://api.open-meteo.com/v1/forecast?latitude={self.lat}&longitude={self.lon}&current_weather=true"

    def setDelay(self, delay) -> None:
        """
        Метод для установки времени задержки обновления сайта

        :param delay: время задержки обновления информации о доступности сайта
        :return: None
        """
        if delay:
            self.__delay = int(delay)
        else:
            self.__delay = 10

    def setStatus(self, status):
        self.__status = status

    def stop(self):
        self.__status = False

    def run(self) -> None:
        # TODO настройте метод для корректной работы
        self.__status = True

        while self.__status:
            # TODO Примерный код ниже
            """
            response = requests.get(self.__api_url)
            data = response.json()
            ваш_сигнал.emit(data)
            sleep(delay)
            """
            try:
                response = requests.get(self.__api_url)
                weather_data = response.json()
                self.weatherInfoReceived.emit(weather_data)
                time.sleep(self.__delay)
            except Exception:
                traceback.print_exc()
                self.stop()

