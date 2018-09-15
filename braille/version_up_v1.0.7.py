"""
일단 띄어쓰기 단위로 리스트를 보내서 한글인지 아닌지 파악하고 이에 맞는 루틴을 실행한 후
띄어쓰기 코드를 실행
만들 수 있는 조합 : {영어},{ 한글, 숫자, 숫자+한글(약어없음), 한글 + 숫자(약어 없음) }
이렇게 분리해도 되겠다.
깔 때 받침이 ㅆ이라면 예외처리

최종적으로 라파한테 넘길때는 destination = value이렇게 해야겠다.
"""

"단어 인덱싱"
index_na = 0
index_da = 0
index_ba = 0
index_za = 0
index_ka = 0
index_ta = 0
index_pa = 0
index_ha = 0


"영어와 한글의 변환점을 확인할 변수"
if_character_change = 10 #한글 영어 숫자 변환 학인기


"약자 검증을 위한 리스트 인덱스"
check_index = 0
import re
# -*- coding: utf-8 -*-
#점자 표는 이진수로 생각하자

"목적지"
destination = 0

"띄어쓰기 번호"
space = 0b00000000

"영어 점자"
start_en = 0b001011 #영어 시작
a_en = 0b100000
b_en = 0b110000
c_en = 0b100100
d_en = 0b100110
e_en = 0b100010
f_en = 0b110100
g_en = 0b110110
h_en = 0b110010
i_en = 0b010100
j_en = 0b010110
k_en = 0b101000
l_en = 0b111000
m_en = 0b101100
n_en = 0b101110
o_en = 0b101010
p_en = 0b111100
q_en = 0b111110
r_en = 0b111010
s_en = 0b011100
t_en = 0b011110
u_en = 0b101001
v_en = 0b111001
w_en = 0b010111
x_en = 0b101101
y_en = 0b101111
z_en = 0b101011
end_en = 0b010011 #영어 끝

"숫자 점자"
n_1 = 0b100000
n_2 = 0b110000
n_3 = 0b100100
n_4 = 0b100110
n_5 = 0b100010
n_6 = 0b110100
n_7 = 0b110110
n_8 = 0b110010
n_9 = 0b010100
n_0 = 0b010110
start_number = 0b001111  #시작점

"된소리"
cho_dunsori = 0b000001

"한글 초성"
cho_giug = 0b000100
cho_niun = 0b100100
cho_diud = 0b010100
cho_riur = 0b000010
cho_mium = 0b100010
cho_biub = 0b000110
cho_sius = 0b000001
# ㅇ 은 점자가 없음
cho_ziuz = 0b000101
cho_ciuc = 0b000011
cho_kiuk = 0b110100
cho_tiut = 0b110010
cho_piup = 0b100110
cho_hiuh = 0b010110

"한글 중성"
jung_1 = 0b110001          #ㅏ
jung_2 = 0b001110          #ㅑ
jung_3 = 0b011100          #ㅓ
jung_4 = 0b100011          #ㅕ
jung_5 = 0b101001          #ㅗ
jung_6 = 0b001101          #ㅛ
jung_7 = 0b101100          #ㅜ
jung_8 = 0b100101          #ㅠ
jung_9 = 0b100101          #ㅡ
jung_10 = 0b010101         #ㅣ
jung_11 = 0b111010         #ㅐ
jung_12 = 0b001110111010   #ㅒ
jung_13 = 0b101110         #ㅔ
jung_14 = 0b001100         #ㅖ
jung_15 = 0b111001         #ㅘ
jung_16 = 0b111001111010   #ㅙ
jung_17 = 0b101111         #ㅚ
jung_18 = 0b111100         #ㅝ
jung_19 = 0b111100111010   #ㅞ
jung_20 = 0b101100111010   #ㅟ
jung_21 = 0b010111         #ㅢ


"한글 종성"
jong_giug = 0b000100
jong_niun = 0b010010
jong_diud = 0b001010
jong_riur = 0b010000
jong_mium = 0b010001
jong_biub = 0b110000
jong_sius = 0b001000
jong_oung = 0b011011
jong_ziuz = 0b101000
jong_ciuc = 0b011000
jong_kiuk = 0b011010
jong_tiut = 0b011001
jong_piup = 0b010011
jong_hiuh = 0b001011

"특수문자"
zum = 0b010011 #.
what = 0b011001#?
fu8 = 0b011010 #!
coma = 0b000010 #,

"약자"
ga = 0b110101
na = 0b100100
da = 0b010100
ma = 0b100010
ba = 0b000110
sa = 0b111000
za = 0b000101
ka = 0b110100
ta = 0b110010
pa = 0b100110
ha = 0b010110
uek = 0b100111         #억
uen = 0b011111         #언
uel = 0b011110         #얼
uen = 0b100001         #연
uel = 0b110011         #열
ueng = 0b110111        #영
ok = 0b101101          #옥
on = 0b111011          #온
ong = 0b111111         #옹
un = 0b110110          #운
ul = 0b111101          #울
eun = 0b101011         #은
eul = 0b011101         #을
inn = 0b111110         #인
gueck = 0b000111011100 #것
tt = 0b001100          #ㅆ 받침

"약어"
graseo = 0b100000011100   #그래서
gruna = 0b100000100100    #그러나
grumeon = 0b100000010010  #그러면
grumuro = 0b100000010001  #그러므로
grunde = 0b100000101110   #그런데
grigo = 0b100000101001    #그리고
grihayeo = 0b100000100011 #그리하여

def change_english(change_list): #만약 처음이라면 끝이라면 등등 고려해야 되네
    global destination
    #이 루틴 영어를 받아서 점자로 출력한다. 그리고 단어를 받으면 시작은 영어를 알리고 영어로 끝낸다 (표시)
    for keyword in change_list:
        if keyword == 'a' or keyword == 'A': #라파한테 줄때는 mov input_value, a_en이렇게 하자
            print(a_en)
            destination = a_en
            
        elif keyword == 'b' or keyword == 'B': #띄어쓰기 번호도 넣어야 되네
            print(b_en)
            destination = b_en
            
        elif keyword == 'c' or keyword == 'C':
            print(c_en)
            destination = c_en
            
        elif keyword == 'd' or keyword == 'D':
            print(d_en)
            destination = d_en
            
        elif keyword == 'e' or keyword == 'E':
            print(e_en)
            destination = e_en
            
        elif keyword == 'f' or keyword == 'F':
            print(f_en)
            destination = f_en
            
        elif keyword == 'g' or keyword == 'G':
            print(g_en)
            destination = g_en
            
        elif keyword == 'h' or keyword == 'H':
            print(h_en)
            destination = h_en
            
        elif keyword == 'i' or keyword == 'I':
            print(i_en)
            destination = i_en
            
        elif keyword == 'j' or keyword == 'J':
            print(j_en)
            destination = j_en
            
        elif keyword == 'k' or keyword == 'K':
            print(k_en)
            destination = k_en
            
        elif keyword == 'l' or keyword == 'L':
            print(l_en)
            destination = l_en
            
        elif keyword == 'm' or keyword == 'M':
            print(m_en)
            destination = m_en
            
        elif keyword == 'n' or keyword == 'N':
            print(n_en)
            destination = n_en
            
        elif keyword == 'o' or keyword == 'O':
            print(o_en)
            destination = o_en
            
        elif keyword == 'p' or keyword == 'P':
            print(p_en)
            destination = p_en
            
        elif keyword == 'q' or keyword == 'Q':
            print(q_en)
            destination = q_en
            
        elif keyword == 'r' or keyword == 'R':
            print(r_en)
            destination = r_en
            
        elif keyword == 's' or keyword == 'S':
            print(s_en)
            destination = s_en
            
        elif keyword == 't' or keyword == 'T':
            print(t_en)
            destination = t_en
            
        elif keyword == 'u' or keyword == 'U':
            print(u_en)
            destination = u_en
            
        elif keyword == 'v' or keyword == 'V':
            print(v_en)
            destination = v_en
            
        elif keyword == 'w' or keyword == 'W':
            print(w_en)
            destination = w_en
            
        elif keyword == 'x' or keyword == 'X':
            print(x_en)
            destination = x_en
            
        elif keyword == 'y' or keyword == 'Y':
            print(y_en)
            destination = y_en
            
        elif keyword == 'z' or keyword == 'Z':
            print(z_en)
            destination = z_en

        elif keyword == "." or keyword == "?" or keyword == "!" or keyword == ",":
            check_special_character(keyword)
    
            
#이제 영어를 처음들어갔을 때 시작 점자랑 끝낫을 때의 끝 점자를 어떻게 넣을지...
#영 => 엉일때 반복문을 돌리면서 영의 index를 기억하자!
def find_hangul(print_list):
    young_index = 0
    change_yeong_index = 0
    change_yeong_value = 0
    for keyword in print_list: #만약 이 예외처리 조건에 부합하지 않는다면 분리시키고 각 각 함수로 넣는다.

        cho_index = int(((ord(keyword) - 0xAC00)/28)/21) #초성
        cho_value = cho_index + 0x1100


        jung_index = int(((ord(keyword) - 0xAC00)/28)%21) #중성
        jung_value = jung_index + 0x1161

                
        jong_index = int((ord(keyword) - 0xAC00)%28) #종성
        jong_value = jong_index + 0x11A8 - 1
        
        check_jong = jong_index #종성이 있냐 없냐를 판단

        if keyword == "가":
            print_yackja(keyword)
            
        elif keyword == "나": #이렇게 적어놓고 약자함수 호출하고 뒤에 더 확인하고 약자라면 출력후 반환값이 1, 약자가 아니라면 2로 해서
            check = check_yackja(print_list)
            if check == 1: #약자일시
                print_yackja(keyword)
                
            elif check == 2: #약자가 아닐 시
                choseung(cho_value)
                jungseung(jung_value,check_jong)
                jongseung(jong_value)

                
        elif keyword == "다":
            check = check_yackja(print_list)
            if check == 1:
                print_yackja(keyword)
                
            elif check == 2:
                choseung(cho_value)
                jungseung(jung_value,check_jong)
                jongseung(jong_value)
                
        elif keyword == "마":
            check = check_yackja(print_list)
            if check == 1:
                print_yackja(keyword)
                
            elif check == 2:
                choseung(cho_value)
                jungseung(jung_value,check_jong)
                jongseung(jong_value)

        elif keyword == "바":
            check = check_yackja(print_list)
            if check == 1:
                print_yackja(keyword)
                
            elif check == 2:
                choseung(cho_value)
                jungseung(jung_value,check_jong)
                jongseung(jong_value)

        elif keyword == "사":
                print_yackja(keyword)

        elif keyword == "자":
            check = check_yackja(print_list)
            if check == 1:
                print_yackja(keyword)
                
            elif check == 2:
                choseung(cho_value)
                jungseung(jung_value,check_jong)
                jongseung(jong_value)

        elif keyword == "카":
            check = check_yackja(print_list)
            if check == 1:
                print_yackja(keyword)
                
            elif check == 2:
                choseung(cho_value)
                jungseung(jung_value,check_jong)
                jongseung(jong_value)

        elif keyword == "타":
            check = check_yackja(print_list)
            if check == 1:
                print_yackja(keyword)
                
            elif check == 2:
                choseung(cho_value)
                jungseung(jung_value,check_jong)
                jongseung(jong_value)
                               
        elif keyword == "파":
            check = check_yackja(print_list)
            if check == 1:
                print_yackja(keyword)
                
            elif check == 2:
                choseung(cho_value)
                jungseung(jung_value,check_jong)
                jongseung(jong_value)

        elif keyword == "하":
            check = check_yackja(print_list)
            if check == 1:
                print_yackja(keyword)
                
            elif check == 2:
                choseung(cho_value)
                jungseung(jung_value,check_jong)
                jongseung(jong_value)
                
        elif keyword == "억":
            print_yackja(keyword)

        elif keyword == "언":
            print_yackja(keyword)
            
        elif keyword == "얼":
            print_yackja(keyword)
            
        elif keyword == "연":
            print_yackja(keyword)

        elif keyword == "열":
            print_yackja(keyword)

        elif keyword == "영": #여기서 진행해 볼까 생각중인데 음... 받침이 ㅅ ㅈ ㅊ ㅆ ㅉ => 엉
            if young_index >= 1:
                change_yeong_index = int(((ord(print_list[young_index - 1]) - 0xAC00)/28)/21)
                change_yeong_value = change_yeong_index + 0x1100
                if change_yeong_value == 0x1109 or change_yeong_value == 0x1112 or change_yeong_value == 0x110e or change_yeong_value == 0x110a or change_yeong_value == 0x110d:

                    keyword ="엉"
                    cho_index = int(((ord(keyword) - 0xAC00)/28)/21) #초성
                    cho_value = cho_index + 0x1100


                    jung_index = int(((ord(keyword) - 0xAC00)/28)%21) #중성
                    jung_value = jung_index + 0x1161

                
                    jong_index = int((ord(keyword) - 0xAC00)%28) #종성
                    jong_value = jong_index + 0x11A8 - 1

                    choseung(cho_value)
                    jungseung(jung_value,check_jong)
                    jongseung(jong_value)
                    
                else:
                    print_yackja(keyword)
            else:
                print_yackja(keyword)
                    

        elif keyword == "옥":
            print_yackja(keyword)

        elif keyword == "온":
            print_yackja(keyword)

        elif keyword == "옹":
            print_yackja(keyword)

        elif keyword == "운":
            print_yackja(keyword)

        elif keyword == "은":
            print_yackja(keyword)

        elif keyword == "을":
            print_yackja(keyword)

        elif keyword == "인":
            print_yackja(keyword)

        elif keyword == "것":
            print_yackja(keyword)

        elif keyword == "." or keyword == "?" or keyword == "!" or keyword == ",":
            check_special_character(keyword) #이 함수에서도 check_index를 증가시켜줘야 하네
                
        else: #그 밖에 장이나, 정 공 이런 단어들
            choseung(cho_value)
            jungseung(jung_value,check_jong)
            jongseung(jong_value)
        young_index += 1
        
    young_index = 0
    return

def check_special_character(keyword):
    global destination
    global check_index

    if keyword == ".":
        print(zum)
        destination = zum
        
    elif keyword == ",":
        print(coma)
        destination = coma
        
    elif keyword == "!":
        print(fu8)
        destination = fu8
        
    elif keyword == "?":
        print(what)
        destination = what

    check_index +=1
    return

def print_yackja(keyword):
    global destination
    global check_index
    
    check_index += 1 #겹치네 #############################################3
    
    if keyword == "가":
        print(ga)
        destination = ga
        
    elif keyword == "나":   
        print(na)
        destination = na
        
    elif keyword == "다":
        print(da)
        destination = da

    elif keyword == "마":
        print(ma)
        destination = ma

    elif keyword == "바":
        print(ba)
        destination = ba

    elif keyword == "사":
        print(sa)
        destination = sa

    elif keyword == "자":
        print(za)
        destination = za

    elif keyword == "카":
        print(ka)
        destination = ka

    elif keyword == "타":
        print(ta)
        destination = ta

    elif keyword == "파":
        print(pa)
        destination = pa

    elif keyword == "하":
        print(ha)
        destination = ha

    elif keyword == "억":
        print(uek)
        destination = uek

    elif keyword == "언":
        print(uen)
        destination = uen

    elif keyword == "얼":
        print(uel)
        destination = uel

    elif keyword == "연":
        print(uen)
        destination = uen

    elif keyword == "열":
        print(uel)
        destination = uel

    elif keyword == "영":
        print(ueng)
        destination = ueng

    elif keyword == "옥":
        print(ok)
        destination = ok
        
    elif keyword == "온":
        print(on)
        destination = on
        
    elif keyword == "옹":
        print(ong)
        destination = ong
        
    elif keyword == "운":
        print(un)
        destination = un
        
    elif keyword == "울":
        print(ul)
        destination = ul
        
    elif keyword == "은":
        print(eun)
        destination = eun

    elif keyword == "을":
        print(eul)
        destination = eul

    elif keyword == "인":
        print(inn)
        destination = inn

    elif keyword == "것":
        print(gueck)
        destination = gueck

def choseung(cho_value):
    global desination
    if cho_value == 0x1100:
        print(cho_giug)
        destination = cho_giug
        
    elif cho_value == 0x1102:
        print(cho_niun)
        destination = cho_niun

    elif cho_value == 0x1103:
        print(cho_diud)
        destination = cho_diud

    elif cho_value == 0x1105:
        print(cho_riur)
        destination = cho_riur

    elif cho_value == 0x1106:
        print(cho_mium)
        destination = cho_mium

    elif cho_value == 0x1107:
        print(cho_biub)
        destination = cho_biub

    elif cho_value == 0x1109:
        print(cho_sius)
        destination = cho_sius

    #if ord(cho_value) = "ㅇ":

    elif cho_value == 0x1112:
        print(cho_ziuz)
        destination = cho_ziuz

    elif cho_value == 0x110e:
        print(cho_ciuc)
        destination = cho_ciuc

    elif cho_value == 0x110f:
        print(cho_kiuk)
        destination = cho_kiuk

    elif cho_value == 0x1110:
        print(cho_tiut)
        destination = cho_tiut

    elif cho_value == 0x1111:
        print(cho_piup)
        destination = cho_piup

    elif cho_value == 0x1112:
        print(cho_hiuh)
        destination = cho_hiuh

    elif cho_value == 0x1101:
        print(cho_dunsori)
        destination = cho_dunsori
        print(cho_giug)
        destination = cho_giug

    elif cho_value == 0x1104:
        print(cho_dunsori)
        destination = cho_dunsori
        print(cho_diud)
        destination = cho_diud

    elif cho_value == 0x1108:
        print(cho_dunsori)
        destination = cho_dunsori
        print(cho_biub)
        destination = cho_biub

    elif cho_value == 0x110a:
        print(cho_dunsori)
        destination = cho_dunsori
        print(cho_sius)
        destination = cho_sius

    elif cho_value == 0x110d:
        print(cho_dunsori)
        destination = cho_dunsori
        print(cho_ziuz)
        destination = cho_ziuz

def jungseung(jung_value, check_jong): #종성이 없는 경우를 준다. (매개변수로 받자... )
    global destination
    global check_index
    
    if check_jong == 0:
        check_index += 1
        
    if jung_value == 0x1161:
        print(jung_1)
        destination = jung_1

    elif jung_value == 0x1163:
        print(jung_2)
        destination = jung_2

    elif jung_value == 0x1165:
        print(jung_3)
        destination = jung_3

    elif jung_value == 0x1167:
        print(jung_4)
        destination = jung_4

    elif jung_value == 0x1169:
        print(jung_5)
        destination = jung_5

    elif jung_value == 0x116d:
        print(jung_6)
        destination = jung_6

    elif jung_value == 0x116e:
        print(jung_7)
        destination = jung_7

    elif jung_value == 0x1172:
        print(jung_8)
        destination = jung_8

    elif jung_value == 0x1173:
        print(jung_9)
        destination = jung_9

    elif jung_value == 0x1175:
        print(jung_10)
        destination = jung_10

    elif jung_value == 0x1162:
        print(jung_11)
        destination = jung_11

    elif jung_value == 0x1164:
        print(jung_12)
        destination = jung_12

    elif jung_value == 0x1166:
        print(jung_13)
        destination = jung_13

    elif jung_value == 0x1168:
        print(jung_14)
        destination = jung_14

    elif jung_value == 0x116a:
        print(jung_15)
        destination = jung_15

    elif jung_value == 0x116b:
        print(jung_16)
        destination = jung_16

    elif jung_value == 0x116c:
        print(jung_17)
        destination = jung_17

    elif jung_value == 0x116f:
        print(jung_18)
        destination = jung_18

    elif jung_value == 0x1170:
        print(jung_19)
        destination = jung_19

    elif jung_value == 0x1171:
        print(jung_20)
        destination = jung_20

    elif jung_value == 0x1174:
        print(jung_21)
        destination = jung_21


def jongseung(jong_value):
    
    global check_index #? index네 ####################################
    if jong_value >= 0x11A8:
        check_index += 1
    #check_index += 1
    
    global destination
    if jong_value == 0x11a8:
        print(jong_giug)
        destination =jong_giug

    elif jong_value == 0x11ab:
        print(jong_niun)
        destination =jong_niun

    elif jong_value == 0x11ae:
        print(jong_diud)
        destination =jong_diud

    elif jong_value == 0x11af:
        print(jong_riur)
        destination =jong_riur

    elif jong_value == 0x11b7:
        print(jong_mium)
        destination =jong_mium

    elif jong_value == 0x11b8:
        print(jong_biub)
        destination =jong_biub

    elif jong_value == 0x11ba:
        print(jong_sius)
        destination =jong_sius

    elif jong_value == 0x11bc:
        print(jong_oung)
        destination =jong_oung

    elif jong_value == 0x11bd:
        print(jong_ziuz)
        destination =jong_ziuz

    elif jong_value == 0x11be:
        print(jong_ciuc)
        destination =jong_ciuc

    elif jong_value == 0x11bf:
        print(jong_kiuk)
        destination =jong_kiuk

    elif jong_value == 0x11c0:
        print(jong_tiut)
        destination =jong_tiut

    elif jong_value == 0x11c1:
        print(jong_piup)
        destination =jong_piup

    elif jong_value == 0x11c2:
        print(jong_hiuh)
        destination =jong_hiuh

    elif jong_value == 0x11a9:
        print(jong_giug)
        destination =jong_giug
        print(jong_giug)
        destination =jong_giug


    elif jong_value == 0x11bb:
        print(tt)
        destination = tt

    elif jong_value == 0x11aa:
        print(jong_giug)
        destination =jong_giug
        print(jong_sius)
        destination =jong_sius

    elif jong_value == 0x11ac:
        print(jong_niun)
        destination =jong_niun
        print(jong_ziuz)
        destination =jong_ziuz

    elif jong_value == 0x11ad:
        print(jong_niun)
        destination =jong_niun
        print(jong_hiuh)
        destination =jong_hiuh

    elif jong_value == 0x11b0:
        print(jong_riur)
        destination =jong_riur
        print(jong_giug)
        destination =jong_giug

    elif jong_value == 0x11b1:
        print(jong_riur)
        destination =jong_riur
        print(jong_mium)
        destination =jong_mium

    elif jong_value == 0x11b2:
        print(jong_riur)
        destination =jong_riur
        print(jong_biub)
        destination =jong_biub

    elif jong_value == 0x11b3:
        print(jong_riur)
        destination =jong_riur
        print(jong_sius)
        destination =jong_sius

    elif jong_value == 0x11b4:
        print(jong_riur)
        destination =jong_riur
        print(jong_tiut)
        destination =jong_tiut

    elif jong_value == 0x11b5:
        print(jong_riur)
        destination =jong_riur
        print(jong_piup)
        destination =jong_piup

    elif jong_value == 0x11b9:
        print(jong_biub)
        destination =jong_biub
        print(jong_sius)
        destination =jong_sius


def check_yackja(print_list):    #약자를 출력한다. 단어 프린트가 끝나면 이들은 0으로 초기화 된다.
    global check_index
    list_len = len(print_list)

    #만약 index가 list_len이라면 그냥 바로 약자를 출력한다.
    if list_len > 1:
        list_len -= 1
        if print_list[check_index] == "나":
            if check_index == list_len:
                return 1
            cho_index = int(((ord(print_list[check_index+1]) - 0xAC00)/28)/21) # 1 이라서 뒤에께 안되네
            #check_index += 1
            cho_value = cho_index + 0x1100
            if cho_value == 4363: #초성 분리 시전 만약 나 뒤에 모음이라면
                return 2 #약자가 아닐 시
            return 1 #나 뒤에 모음이 아니라면 즉, 약자일시

        
        if print_list[check_index] == "다": #끝에 잇을 경유 뒤에게 없어서 그렇네 조건문 넣자
            if check_index == list_len:
                return 1
            cho_index = int(((ord(print_list[check_index+1]) - 0xAC00)/28)/21)
           # check_index += 1
            cho_value = cho_index + 0x1100
            if cho_value == 4363:  
                return 2
            return 1
        
        if print_list[check_index] == "마":
            if check_index == list_len:
                return 1
            cho_index = int(((ord(print_list[check_index+1]) - 0xAC00)/28)/21)
           # check_index += 1
            cho_value = cho_index + 0x1100
            if cho_value == 4363:
                return 2  
            return 1
        
        if print_list[check_index] == "바":
            if check_index == list_len:
                return 1    
            cho_index = int(((ord(print_list[check_index+1]) - 0xAC00)/28)/21)
            #check_index += 1
            cho_value = cho_index + 0x1100
            if cho_value == 4363:
                return 2
            return 1
        
        if print_list[check_index] == "자":
            if check_index == list_len:
                return 1    
            cho_index = int(((ord(print_list[check_index+1]) - 0xAC00)/28)/21)
            #check_index += 1
            cho_value = cho_index + 0x1100
            if cho_value == 4363:
                return 2
            return 1

        if print_list[check_index] == "카":
            if check_index == list_len:
                return 1
            cho_index = int(((ord(print_list[check_index+1]) - 0xAC00)/28)/21)
            #check_index += 1
            cho_value = cho_index + 0x1100
            if cho_value == 4363:
                return 2  
            return 1

        if print_list[check_index] == "타":
            if check_index == list_len:
                return 1
            cho_index = int(((ord(print_list[check_index+1]) - 0xAC00)/28)/21)
            #check_ndex += 1
            cho_value = cho_index + 0x1100
            if cho_value == 4363:
                return 2
            return 1

        if print_list[check_index] == "파":
            if check_index == list_len:
                return 1
            cho_index = int(((ord(print_list[check_index+1]) - 0xAC00)/28)/21)
            #check_index += 1
            cho_value = cho_index + 0x1100
            if cho_value == 4363:
                return 2
            return 1

        if print_list[check_index] == "하":
            if check_index == list_len:
                return 1            
            cho_index = int(((ord(print_list[check_index+1]) - 0xAC00)/28)/21)
            #check_index += 1
            cho_value = cho_index + 0x1100
            if cho_value == 4363:
                return 2
            return 1
    elif check_index == list_len:
        return 1 #1이 약자 2가 일반


        
    return 1 #한 문자 '나' 라면
            
            

def yacka(print_list): #약어를 출력한다.
    global destination
    global check_index
    
    if print_list[0] == "그":
        if print_list[1] == "리":
            if print_list[2] == "고":
                print(grigo)
                destination = grigo
                print("SPACE zero : %d" %space)
                destination = space
                check_index += 1
                
                return 1
                
            if print_list[2] == "하":
                if print_list[3] == "여":
                    print(grihayeo)
                    destination = grihayeo
                    print("SPACE zero : %d" %space)
                    destination = space
                    check_index += 1
                    return 1
                
        if print_list[1] == "래":
            if print_list[2] == "서":
                print(graseo)
                destination = graseo
                print("SPACE zero : %d" %space)
                destination = space
                check_index += 1
                return 1
            
        if print_list[1] == "러":
            if print_list[2] == "나":
                print(gruna)
                destination = gruna
                print("SPACE zero : %d" %space)
                destination = space
                check_index += 1
                return 1
            
            if print_list[2] == "면":
                print(grumeon)
                destination = grumeon
                print("SPACE zero : %d" %space)
                destination = space
                check_index += 1
                return 1
            
            if print_list[2] == "므":
                if print_list[3] == "로":
                    print(grumuro)
                    destination = grumuro
                    print("SPACE zero : %d" %space)
                    destination = space
                    check_index += 1
                    return 1
                
        if print_list[1] == "런":
            if print_list[2] == "데":
                print(grunde)
                destination = grunde
                print("SPACE zero : %d" %space)
                destination = space
                check_index += 1
                return 1
            
            check_index += 1
            return 1
            
    check_index += 1    
    return 2

def change_hangul(change_list):
    #print(change_list[0])
    if change_list[0] == '그':
        check = yacka(change_list) #약어만 출력하는 함수
        if check == 1:
            return
    
    find_hangul(change_list) #띄어쓰기 단위로 받아온 단어를 예외가 될 수 있는 글을 판단한다.
                
        
def check_letter(check_list): #첫 글자가 한글이나 아니냐 파악 루틴
    check = ord(check_list[0])
    #print(check_list[0])
    if check >= 0xAC00 and check <= 0xD7A3:
        return 1
        #hangul routine
    if check >= 65 and check <= 122:
        return 2
        #english routine
    if check >=32 and check <= 64:
        return 1
        #single number and special char routine. So same hangul routine 한글 루틴에서 처리할꺼야
            
def sep(sep_letter): #단어를 문자로 분리해주는 함수
    word = []
    return_word = []
    for keyword in sep_letter:
        for i in range(0, len(keyword)):
            word.append(keyword[i])
        return_word.append(word)
        word = []
    return return_word

'띄어쓰기를 위한 index'
index = 0

string = input("input your hangul : ")
list_string = []
list_string = string.split() #1중 리스트로 구성됨
                             #이중 리스트로 구현해야 띄어쓰기 용이함
tmp = []                     #단어 중심의 이중 리스트  
letter = []                  #문자 중심의 최종 이중 리스트
for keyword in list_string:  #띄어쓰기를 기준으로 이중리스트를 구현함
    letter.append(keyword)
    tmp.append(letter)
    letter = []
print(tmp)

sep_word = []
letter = []
                               
for i in range(0,len(tmp)):
    sep_word = tmp[i]
    sep_word = sep(sep_word)    #단어를 쪼개고 이중 리스트로 반환
    letter = letter + (sep_word)#단어중심의 이중리스트가 아닌 문자 중심의 이중리스트
#print(letter)
#print(len(letter)) ### 여기까지가 문자 리스트 ###
routine_value = len(letter) #반복문을 돌리기 위한 길이 변수

#letter[value] 이 문자로 쪼개진 리스트를 넘긴다.
for i in range(0, routine_value):
    list_letter = []
    list_letter = letter[i] #이중리스트에 있는 것중 하나를 옮긴다.
    print(list_letter)
    #list_letter_number = len(list_letter)

    check = check_letter(list_letter) #한글인지 아닌지 확인한다
    #list_letter[i+1]해서 값을 확인해도 될듯? 
    if check == 1:
        #if index > 0:
        change_hangul(list_letter) #한글 조합일시
        print("SPACE : %d"%space)
        destination = space
        check_index = 0 #약자를 검사하는 변수 단어가 끝나면 초기화 시킨다.
        if_character_change = 10 #한글 반환값 
    #index += 1 #띄어쓰기
    
    if check == 2:
        if if_character_change == 10: #그전이 한글이었는지 확인한다. 
            print(start_en)
            destination = start_en      
        change_english(list_letter) #영어 조합일시
        #for_print_list_len = len(letter) #문자중심의 문자들이 담긴 이중 리스트
        
        if i < routine_value-1: # 한글과 숫자를... 
            if ord(letter[i+1][0]) >= 0xAC00 and ord(letter[i+1][0]) <= 0xD7A3:
                print(end_en)
                destination = end_en
                
            if ord(letter[i+1][0]) >= 32 and ord(letter[i+1][0]) <= 64:
                print(end_en)
                destination = end_en
                
        if i == routine_value-1:
            print(end_en)
            destination = end_en

        print("SPACE : %d" %space)
        destination = space
        if_character_change = 20
    #index += 1 #다음부터 띄어쓰기를 한다.

""" #에러 발견 : ex) 가 나 야 했을 때 에러가 뜸
# ((초성x21)+중성)x28 + 종성 + 0xAC00
# 초성index = ((문자코드 - 0xAC00) / 28 ) / 21
# 중성index = ((문자코드 - 0xAC00) / 28 ) % 21
# 종성index = ((문자코드 - 0xAC00) % 28
# 초성 자모 시작 값 : 0x1100
# 중성 시작 값 : 0x1161
# 종성 시작 값 : 0x11A8

# 초성 코드 : 초성index + 0x1100
# 중성 코드 : 종성index + 0x1161
# 종성 코드 : 중성index + 0x11A8 - 1

# 즉, 어느 문자를 받고 유니코드값을(ord()) 얻고 각 각의 index를 얻고 각 각의 코드를 얻자
# 그리고 chr()
"""



#어떤 앞 문자를 처리하면서 check_index를 늘려줘야 하네


#영어반환값을 20으로하고 한글 반환값을 10으로 해야하겠다. 그럼 초기값을 10으로 해야겠네?

#그리고 한글 루틴에서 20을 체크하면 먼저 영어 끝을 알리는 걸 날리고 


