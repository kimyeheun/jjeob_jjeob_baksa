# sosohan_project

# 통합 브랜치 
* main

# 토픽 브랜치
미정


## 초기화
* `git clone `
* `python -m venv venv`
* `source venv/Scripts/activate`
* `cd sosohan_project`  
* `git branch [브랜치 이름]`
* `git checkout [브랜치 이름]`
* `git push -u origin [브랜치 이름]`

## 필요한 것들
* `pip install django`
* `pip install pip --upgrade`
  
## 개발
* `source venv/Scripts/activate`
* developing~~
* `git add [파일]`
* `git commit -m "Commit Message"`
* `git push`

## 주의사항
* 커밋 메세지는 한가지의 역할만을 반영하여 작성하기!
* 자신이 수정한 파일만 지정해서 `staging area`에 반영하기!  
* `git pull origin main` 명령어는  수정된 파일이 commit 되어 있지않으면 작동하지
    않아서, 자신의 코드가 모두 원격 저장소에 올라가 있다고 생각한다면 `git fetch --all`, `git reset --hard origin/main`
    으로 원격 저장소의 main 브랜치와 동기화시키기!
* `git push`가 작동하지 않는다면, branch를 정확히 확인했다는 가정 하에 `git push -f` 해도 됨!   

## 서버 운용
* `python mange.py makemigrations`
* `python mange.py migrate`
* `python manage.py runserver`
