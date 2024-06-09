# Лабораторная работа №3 - Nextcloud & PostgreSQL

## Задачи

1. Установить Kubernetes на локальную машину. 
2. Создать yml-файлы
3. Осуществить туннелирование трафика
4. Установить допкомпонент dashboard для minikube

## Результаты

- Minikube start:
![image](https://github.com/VRnewreality/itmo_devops/assets/48685561/18866afb-e7e2-4cf3-b9c0-4cd896dd1627)

- Контейнер minikube:
![image](https://github.com/VRnewreality/itmo_devops/assets/48685561/3d91ca6f-0f7a-4ad1-8fe7-8476debb6d3d)

- Манифесты:
![image](https://github.com/VRnewreality/itmo_devops/assets/48685561/5e95c0da-d271-4ae0-a1ce-81b5f1fa8530)

- Проверим успешность установки ресурсов:
![image](https://github.com/VRnewreality/itmo_devops/assets/48685561/3c071c90-1a30-4789-bbac-a05a9d470176)

- Никаких паролей:
![image](https://github.com/VRnewreality/itmo_devops/assets/48685561/a8b8a94a-3891-4c8f-925d-db4de1053338)

- Перенаправление портов
![image](https://github.com/VRnewreality/itmo_devops/assets/48685561/2244d2e3-3a74-4247-9ea3-3202cb3e3469)

- Туннелирование трафика между нодой minikube и сервисом
![image](https://github.com/VRnewreality/itmo_devops/assets/48685561/6560c9a0-da4b-4017-bac2-d5ff7db8e2e7)

- Всем присутствующим добрый вечер
![image](https://github.com/VRnewreality/itmo_devops/assets/48685561/e9704327-0da7-456a-a595-d77a8dad4644)

- Dashboard для minikube
![image](https://github.com/VRnewreality/itmo_devops/assets/48685561/bad02418-db4d-4a6d-8c7b-54aafe61f370)

## Ответы на вопросы

1. **Важен ли порядок выполнения этих манифестов? Почему?**

   Порядок важен, если одни манифесты ссылаются на другие. Например, Deployment может зависеть от наличия Configmap или Secret для получения необходимых данных. Если ConfigMap или Secret не созданы до создания Deployment, контейнеры в подах могут не запуститься корректно из-за отсутствия конфигурационных данных.

2. **Что и почему произойдет, если отскейлить количество реплик postgres-deployment в 0, затем обратно в 1, после чего попробовать снова зайти на Nextcloud?**

  При уменьшении количества реплик до 0, это остановит все поды PostgreSQL. Из-за этого база данных, которую использует Nextcloud, будет недоступна.
  Если увеличить обратно до 1 реплики, то, когда под PostgreSQL запустится, база данных станет доступной. Но нужно будет подождать некоторое время для восстановления соединений.
   
