class MemberInfo2 :
    ### *** 클래스 내에서 함수를 정의할 때는 무조건
    #       - 매개변수 첫번째에는 self를 붙여야 함.
    #         (받아올 매개변수가 없더라고 self는 붙여야 합니다.)
    #       - 외부에서 함수 호출시에는 self는 매개변수로 취급하지 않습니다.
    #         (없다고 생각하면 됩니다.)
    #       - self의 용도 : 클래스 내부 및 외부에서 어디서든지 접근 가능하도록 하기위한 속성입니다.

    ### 클래스 생성시 자동으로 호출되는 생성 함수
    def __init__(self):
        print("MemberInfo 클래스가 생성되었습니다.")

    ### 테스트 함수
    def viewPrint(self):
        print("viewPrint() 함수 호출")
        print(f"self.param = {self.param}")

    ### self 테스트
    def setParam(self) :
        print("setParam() 함수 호출")
        self.param = "홍길동"



### 단독함수 (클래스에 속하지 않음)
def viewGuGuDan(s_dan, e_dan, s_num, e_num) :
    # s_dan, e_dan, s_num, e_num = 3, 5, 4, 7

    for dan in range(s_dan, e_dan+1, 1) :
        print(f"============== [{dan} 단] ==============")
        for num in range(s_num, e_num+1, 1) :
            print(f"{dan} x {num} = {dan * num}")