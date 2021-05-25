selected = None
computer = '가위'
while selected not in ['가위','바위','보'] :
    selected = input('가위, 바위, 보 중에서 선택하세요>')
    if(selected == '가위' or selected == '바위' or selected == '보') :
        if(selected == '바위') :
            selected == selected
            print('U Win')
        else :
            selected = None
            print('이길 때까지 못나와')
    else :
        print("가위, 바위, 보 중에서 하나 선택하세요.")