# Лабораторная работа №4 - Nextcloud & PostgreSQL
# Развертывание Nextcloud и PostgreSQL в Minikube

## Описание

Этот проект предназначен для развертывания двух сервисов (Nextcloud и PostgreSQL) в Minikube с использованием Kubernetes. Проект включает в себя кастомный образ для Nextcloud, использование ConfigMap и Secret, init-контейнеры, volumes, а также настройки liveness и readiness проб.

## Требования

- Minikube
- Docker
- kubectl

## Содержание

- [Подготовка окружения](#подготовка-окружения)
- [Создание кастомного Docker-образа](#создание-кастомного-docker-образа)
- [Kubernetes манифесты](#kubernetes-манифесты)
- [Применение манифестов](#применение-манифестов)
- [Проверка состояния](#проверка-состояния)
- [Удаление ресурсов](#удаление-ресурсов)

## Подготовка окружения

1. Убедитесь, что у вас установлен Minikube, Docker и kubectl.
2. Запустите Minikube:

    ```bash
    minikube start --driver=docker
    ```

3. Настройте Docker окружение для использования Docker-демона внутри Minikube:

    ```bash
    & minikube -p minikube docker-env --shell powershell | Invoke-Expression
    ```

## Создание кастомного Docker-образа

1. Соберите и загрузите образ в локальный Docker-реестр Minikube:

    ```bash
    docker build -t custom-nextcloud:latest .
    ```
## Запуск minikube
![image](https://github.com/VRnewreality/itmo_devops/assets/115554194/cfa31bb3-79a2-4fda-ae6f-b3d405492e54)

## Kubernetes манифесты
![image](https://github.com/VRnewreality/itmo_devops/assets/115554194/7be6c1ec-061c-4391-83af-e2ef1a229381)

## Проверка состояния
![image](https://github.com/VRnewreality/itmo_devops/assets/115554194/3424d0f2-1aed-4639-96d9-5a33db0e9e38)
![image](https://github.com/VRnewreality/itmo_devops/assets/115554194/9cdc7e14-1544-47f3-b1b0-d5a4ddc3162c)
![image](https://github.com/VRnewreality/itmo_devops/assets/115554194/0c029fa6-ab38-4edc-897d-b538ba28af95)


![image](https://github.com/VRnewreality/itmo_devops/assets/115554194/53d3c180-f469-4d68-9a28-c6156f967a35)
![image](https://github.com/VRnewreality/itmo_devops/assets/115554194/016f6532-cd71-48de-a66b-89294ab09242)
![image](https://github.com/VRnewreality/itmo_devops/assets/115554194/5adf2639-46be-46a9-a6ab-052d5bf344b6)

![image](https://github.com/VRnewreality/itmo_devops/assets/115554194/f54bc61f-1dd0-4dc5-aafb-b817e3fe34e7)

Проверьте состояние подов и сервисов:
```bash
kubectl get pods
kubectl get svc
kubectl describe pod <pod-name>
```
## Удаление ресурсов
Чтобы удалить все созданные ресурсы, выполните:

```bash
kubectl delete -f nextcloud-secret.yml
kubectl delete -f nextcloud-configmap.yml
kubectl delete -f nextcloud-deployment.yml
kubectl delete -f nextcloud-service.yml
kubectl delete -f pg-secret.yml
kubectl delete -f pg-configmap.yml
kubectl delete -f pg-deployment.yml
kubectl delete -f pg-service.yml
```
