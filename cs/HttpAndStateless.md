## HTTP와 무상태(stateless)

> ### Http는 클라이언트와 서버 사이에 의사소통 방식이다.
> Http는 __비연결성__ 과 __무상태__ 라는 특징을 가진다.
> > 비연결성: 요청을 하고 응답을 하면 바로 __연결을 끊는__ 성질\
> > 무상태: 연결이 해제됨과 동시에 클라이언트와 서버는 __요청을 잊어버리는__ 성질

> ### 무상태(stateless)로 얻는 장점
> 서버가 더이상 클라이언트를 기억하지 않아도 된다. 
> - 전체 프로세스를 한 서버(같은 서버)가 요청을 유지하지 않음
> 
> 시스템 확장에 유리하다.
> - 응답할 수 있는 서버를 증설하면 된다.(스케일 아웃)
> 
> 현재 상태를 클라이언트가 가지고 있기 때문에 프로세스중에 에러가 생겨도 다시 요청하면 된다.
> - stateful의 경우 처음부터 다시해야한다.

하지만 어플리케이션을 만들 때에는 필연적으로 상태를 저장해야하는 상황이 발생한다. ex) 로그인

이때 사용되는 방법에는 세션, 쿠키, 토큰 등이 있다.
> ### 1. 쿠키
> 쿠키는 클라이언트 로컬에 저장되는 데이터 파일(키 밸류로 구성)\
> 쿠키에는 유효한 시간을 명시할 수 있으며, 시간이 정해지면 브라우저가 종료되어도 유지\
> 쿠키는 클라이언트의 상태 정보를 로컬에 저장했다가 참조\
> 하나의 도메인당 __최대 쿠키 개수는 20개, 최대 크기는 4KB__\
> 쿠키는 사용자가 따로 요청하지 않아도 클라이언트가 자동으로 요청 헤더에 넣어서 서버로 전송

> ### 2. 세션
> 세션은 쿠키를 기반하고 있지만, 사용자 정보 파일을 클라이언트에 저장하는 쿠키와 달리 __세션은 서버 측에서 관리__\
> 서버에서 클라이언트를 구분하기 위해 세션 ID(ex __톰캣 JSESSIONID__)를 부여하며 웹 브라우저로 서버에 접속한 뒤 브라우저를 종료할 때까지 __인증 상태__ 를 유지\
> __세션 ID__ : 클라이언트가 요청을 보내면, 해당 서버의 엔진이 클라이언트에게 유일한 ID를 부여\
> 클라이언트에 대한 정보를 서버에 두기 때문에 쿠키보다 보안에 좋음\
> 클라이언트 정보가 많아 질 수록 서버 메모리를 차지하여 성능 저하의 원인이 됨

> ### 3. 토큰
> 쿠키, 세션은 별도의 저장소에 값을 저장하고 관리해야한다.\
> 하지만 토큰은 발급한 뒤 검증만 하기 때문에 추가 저장소가 필요하지 않음\
> 다중 서버 환경에서 추가 작업이 필요한 세션과 달리 추가 작업이 필요 없음
> - 다중 서버에서 세션을 인식시켜주려면 redis을 사용하는 것 같은 세션 클러스터링이 필요하다. 