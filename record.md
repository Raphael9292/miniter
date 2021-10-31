```python
============================= test session starts =============================
collecting ... ERROR: not found: C:\Users\Administrator\Desktop\minitter\api\test\test_view.py::test_ping
(no name 'C:\\Users\\Administrator\\Desktop\\minitter\\api\\test\\test_view.py::test_ping' in any of [<Module test/test_view.py>])
```

window에서 했더니 경로가 저렇게 인식되서 pytest가 인식을 못하더라, window에 맞게 하거나 mac에서 하길...

boto3처럼 외부와 연결하는 라이브러리에 코드가 의존할 경우 unit test를 독립적으로 실행하기 어려웠다.  
테스트할때마다 신규 파일이 올라가야 기능이 되는지 확인하는데 이게 맞는건가??  

그래서 해당 라이브러리를 mock을 사용하여 unit test를 진행한다.  
mock은 정적으로도 가능하고 런타임에 mock을 객체화 할 수도 있다 (patch).  
