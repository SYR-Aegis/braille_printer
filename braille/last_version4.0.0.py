# -*- coding: utf-8 -*-


# 일단 띄어쓰기 단위로 리스트를 보내서 한글인지 아닌지 파악하고 이에 맞는 루틴을 실행한 후
# 띄어쓰기 코드를 실행
# 만들 수 있는 조합 : {영어},{ 한글, 숫자, 숫자+한글(약어없음), 한글 + 숫자(약어 없음) }
# 이렇게 분리해도 되겠다.
# 깔 때 받침이 ㅆ이라면 예외처리

# 최종적으로 라파한테 넘길때는 destination = value이렇게 해야겠다.


# 반환함수에 쓰일 전역 리스트
def change(in_str):
    return_list = []
    destination=0
    tmp_list = []

    # 단어 인덱싱
    index_na = 0
    index_da = 0
    index_ba = 0
    index_za = 0
    index_ka = 0
    index_ta = 0
    index_pa = 0
    index_ha = 0

    # 영어와 한글의 변환점을 확인할 변수#
    if_character_change = 10  # 한글 영어 숫자 변환 학인기

    # 약자 검증을 위한 리스트 인덱스#
    check_index = 0
    import re

    # 점자 표는 이진수로 생각하자

    # give to rapa
    destination = 0

    # space bar#
    space = 0b00000000

    # English
    start_en = 0b001011  # 영어 시작
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
    end_en = 0b010011  # 영어 끝

    # number
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
    start_number = 0b001111  # 시작점

    # dunsori
    cho_dunsori = 0b000001

    # hangul choseong
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

    # hangul jongseong#
    jung_1 = 0b110001  # ㅏ
    jung_2 = 0b001110  # ㅑ
    jung_3 = 0b011100  # ㅓ
    jung_4 = 0b100011  # ㅕ
    jung_5 = 0b101001  # ㅗ
    jung_6 = 0b001101  # ㅛ
    jung_7 = 0b101100  # ㅜ
    jung_8 = 0b100101  # ㅠ
    jung_9 = 0b100101  # ㅡ
    jung_10 = 0b010101  # ㅣ
    jung_11 = 0b111010  # ㅐ
    jung_12 = 0b001110111010  # ㅒ
    jung_13 = 0b101110  # ㅔ
    jung_14 = 0b001100  # ㅖ
    jung_15 = 0b111001  # ㅘ
    jung_16 = 0b111001111010  # ㅙ
    jung_17 = 0b101111  # ㅚ
    jung_18 = 0b111100  # ㅝ
    jung_19 = 0b111100111010  # ㅞ
    jung_20 = 0b101100111010  # ㅟ
    jung_21 = 0b010111  # ㅢ

    # hangul jongseong#
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

    # special character#
    zum = 0b010011  # .
    what = 0b011001  # ?
    fu8 = 0b011010  # !
    coma = 0b000010  # ,

    # yackja#
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
    uek = 0b100111  # 억
    uen = 0b011111  # 언
    uel = 0b011110  # 얼
    uen = 0b100001  # 연
    uel = 0b110011  # 열
    ueng = 0b110111  # 영
    ok = 0b101101  # 옥
    on = 0b111011  # 온
    ong = 0b111111  # 옹
    un = 0b110110  # 운
    ul = 0b111101  # 울
    eun = 0b101011  # 은
    eul = 0b011101  # 을
    inn = 0b111110  # 인
    gueck = 0b000111011100  # 것
    tt = 0b001100  # ㅆ 받침

    # yacka#
    graseo = 0b100000011100  # 그래서
    gruna = 0b100000100100  # 그러나
    grumeon = 0b100000010010  # 그러면
    grumuro = 0b100000010001  # 그러므로
    grunde = 0b100000101110  # 그런데
    grigo = 0b100000101001  # 그리고
    grihayeo = 0b100000100011  # 그리하여


    def return_list_for_rapa(return_list):
        #printreturn_list)
        return return_list


    def change_english(change_list):  # 만약 처음이라면 끝이라면 등등 고려해야 되네
        nonlocal destination
        nonlocal return_list
        nonlocal tmp_list
        # 이 루틴 영어를 받아서 점자로 출력한다. 그리고 단어를 받으면 시작은 영어를 알리고 영어로 끝낸다 (표시)
        for keyword in change_list:
            if keyword == 'a' or keyword == 'A':  # 라파한테 줄때는 mov input_value, a_en이렇게 하자
                #printa_en)
                destination = a_en
                return_list.append(destination)

            elif keyword == 'b' or keyword == 'B':  # 띄어쓰기 번호도 넣어야 되네
                #printb_en)
                destination = b_en
                return_list.append(destination)

            elif keyword == 'c' or keyword == 'C':
                #printc_en)
                destination = c_en
                return_list.append(destination)

            elif keyword == 'd' or keyword == 'D':
                #printd_en)
                destination = d_en
                return_list.append(destination)

            elif keyword == 'e' or keyword == 'E':
                #printe_en)
                destination = e_en
                return_list.append(destination)

            elif keyword == 'f' or keyword == 'F':
                #printf_en)
                destination = f_en
                return_list.append(destination)

            elif keyword == 'g' or keyword == 'G':
                #printg_en)
                destination = g_en
                return_list.append(destination)

            elif keyword == 'h' or keyword == 'H':
                #printh_en)
                destination = h_en
                return_list.append(destination)

            elif keyword == 'i' or keyword == 'I':
                #printi_en)
                destination = i_en
                return_list.append(destination)

            elif keyword == 'j' or keyword == 'J':
                #printj_en)
                destination = j_en
                return_list.append(destination)

            elif keyword == 'k' or keyword == 'K':
                #printk_en)
                destination = k_en
                return_list.append(destination)

            elif keyword == 'l' or keyword == 'L':
                #printl_en)
                destination = l_en
                return_list.append(destination)

            elif keyword == 'm' or keyword == 'M':
                #printm_en)
                destination = m_en
                return_list.append(destination)

            elif keyword == 'n' or keyword == 'N':
                #printn_en)
                destination = n_en
                return_list.append(destination)

            elif keyword == 'o' or keyword == 'O':
                #printo_en)
                destination = o_en
                return_list.append(destination)

            elif keyword == 'p' or keyword == 'P':
                #printp_en)
                destination = p_en
                return_list.append(destination)

            elif keyword == 'q' or keyword == 'Q':
                #printq_en)
                destination = q_en
                return_list.append(destination)

            elif keyword == 'r' or keyword == 'R':
                #printr_en)
                destination = r_en
                return_list.append(destination)

            elif keyword == 's' or keyword == 'S':
                #prints_en)
                destination = s_en
                return_list.append(destination)

            elif keyword == 't' or keyword == 'T':
                #printt_en)
                destination = t_en
                return_list.append(destination)

            elif keyword == 'u' or keyword == 'U':
                #printu_en)
                destination = u_en
                return_list.append(destination)

            elif keyword == 'v' or keyword == 'V':
                #printv_en)
                destination = v_en
                return_list.append(destination)

            elif keyword == 'w' or keyword == 'W':
                #printw_en)
                destination = w_en
                return_list.append(destination)

            elif keyword == 'x' or keyword == 'X':
                #printx_en)
                destination = x_en
                return_list.append(destination)

            elif keyword == 'y' or keyword == 'Y':
                #printy_en)
                destination = y_en
                return_list.append(destination)

            elif keyword == 'z' or keyword == 'Z':
                #printz_en)
                destination = z_en
                return_list.append(destination)

            elif keyword == "." or keyword == "?" or keyword == "!" or keyword == ",":
                check_special_character(keyword)

        ################
        return


    # 이제 영어를 처음들어갔을 때 시작 점자랑 끝낫을 때의 끝 점자를 어떻게 넣을지...
    # 영 => 엉일때 반복문을 돌리면서 영의 index를 기억하자!
    def find_hangul(print_list):
        young_index = 0
        change_yeong_index = 0
        change_yeong_value = 0
        check_index_number = 1 # 숫자였냐 한글이였나 판단한다.
        #초기값을 1로 해야겠다. "2개" 일떄 처리할려면? 
        
        for keyword in print_list:  # 만약 이 예외처리 조건에 부합하지 않는다면 분리시키고 각 각 함수로 넣는다.

            cho_index = int(((ord(keyword) - 0xAC00) / 28) / 21)  # 초성
            cho_value = cho_index + 0x1100

            jung_index = int(((ord(keyword) - 0xAC00) / 28) % 21)  # 중성
            jung_value = jung_index + 0x1161

            jong_index = int((ord(keyword) - 0xAC00) % 28)  # 종성
            jong_value = jong_index + 0x11A8 - 1

            check_jong = jong_index  # 종성이 있냐 없냐를 판단

            if keyword == "가":
                print_yackja(keyword)
                check_index_number = 1

            elif keyword == "나":  # 이렇게 적어놓고 약자함수 호출하고 뒤에 더 확인하고 약자라면 출력후 반환값이 1, 약자가 아니라면 2로 해서
                check = check_yackja(print_list)
                if check == 1:  # 약자일시
                    print_yackja(keyword)
                    check_index_number = 1

                elif check == 2:  # 약자가 아닐 시
                    choseung(cho_value)
                    jungseung(jung_value, check_jong)
                    jongseung(jong_value)
                    check_index_number = 1


            elif keyword == "다":
                check = check_yackja(print_list)
                if check == 1:
                    print_yackja(keyword)
                    check_index_number = 1

                elif check == 2:
                    choseung(cho_value)
                    jungseung(jung_value, check_jong)
                    jongseung(jong_value)
                    check_index_number = 1

            elif keyword == "마":
                check = check_yackja(print_list)
                if check == 1:
                    print_yackja(keyword)
                    check_index_number = 1

                elif check == 2:
                    choseung(cho_value)
                    jungseung(jung_value, check_jong)
                    jongseung(jong_value)
                    check_index_number = 1

            elif keyword == "바":
                check = check_yackja(print_list)
                if check == 1:
                    print_yackja(keyword)
                    check_index_number = 1

                elif check == 2:
                    choseung(cho_value)
                    jungseung(jung_value, check_jong)
                    jongseung(jong_value)
                    check_index_number = 1

            elif keyword == "사":
                print_yackja(keyword)
                check_index_number = 1

            elif keyword == "자":
                check = check_yackja(print_list)
                if check == 1:
                    print_yackja(keyword)
                    check_index_number = 1

                elif check == 2:
                    choseung(cho_value)
                    jungseung(jung_value, check_jong)
                    jongseung(jong_value)
                    check_index_number = 1

            elif keyword == "카":
                check = check_yackja(print_list)
                if check == 1:
                    print_yackja(keyword)
                    check_index_number = 1

                elif check == 2:
                    choseung(cho_value)
                    jungseung(jung_value, check_jong)
                    jongseung(jong_value)
                    check_index_number = 1

            elif keyword == "타":
                check = check_yackja(print_list)
                if check == 1:
                    print_yackja(keyword)
                    check_index_number = 1

                elif check == 2:
                    choseung(cho_value)
                    jungseung(jung_value, check_jong)
                    jongseung(jong_value)
                    check_index_number = 1

            elif keyword == "파":
                check = check_yackja(print_list)
                if check == 1:
                    print_yackja(keyword)
                    check_index_number = 1

                elif check == 2:
                    choseung(cho_value)
                    jungseung(jung_value, check_jong)
                    jongseung(jong_value)
                    check_index_number = 1

            elif keyword == "하":
                check = check_yackja(print_list)
                if check == 1:
                    print_yackja(keyword)
                    check_index_number = 1

                elif check == 2:
                    choseung(cho_value)
                    jungseung(jung_value, check_jong)
                    jongseung(jong_value)
                    check_index_number = 1

            elif keyword == "억":
                print_yackja(keyword)
                check_index_number = 1

            elif keyword == "언":
                print_yackja(keyword)
                check_index_number = 1

            elif keyword == "얼":
                print_yackja(keyword)
                check_index_number = 1

            elif keyword == "연":
                print_yackja(keyword)
                check_index_number = 1

            elif keyword == "열":
                print_yackja(keyword)
                check_index_number = 1

            elif keyword == "영":  # 여기서 진행해 볼까 생각중인데 음... 받침이 ㅅ ㅈ ㅊ ㅆ ㅉ => 엉
                if young_index >= 1:
                    change_yeong_index = int(((ord(print_list[young_index - 1]) - 0xAC00) / 28) / 21)
                    change_yeong_value = change_yeong_index + 0x1100
                    if change_yeong_value == 0x1109 or change_yeong_value == 0x1112 or change_yeong_value == 0x110e or change_yeong_value == 0x110a or change_yeong_value == 0x110d:

                        keyword = "엉"
                        cho_index = int(((ord(keyword) - 0xAC00) / 28) / 21)  # 초성
                        cho_value = cho_index + 0x1100

                        jung_index = int(((ord(keyword) - 0xAC00) / 28) % 21)  # 중성
                        jung_value = jung_index + 0x1161

                        jong_index = int((ord(keyword) - 0xAC00) % 28)  # 종성
                        jong_value = jong_index + 0x11A8 - 1

                        choseung(cho_value)
                        jungseung(jung_value, check_jong)
                        jongseung(jong_value)
                        check_index_number = 1

                    else:
                        print_yackja(keyword)
                        check_index_number = 1
                else:
                    print_yackja(keyword)
                    check_index_number = 1


            elif keyword == "옥":
                print_yackja(keyword)
                check_index_number = 1

            elif keyword == "온":
                print_yackja(keyword)
                check_index_number = 1

            elif keyword == "옹":
                print_yackja(keyword)
                check_index_number = 1

            elif keyword == "운":
                print_yackja(keyword)
                check_index_number = 1

            elif keyword == "은":
                print_yackja(keyword)
                check_index_number = 1

            elif keyword == "을":
                print_yackja(keyword)
                check_index_number = 1

            elif keyword == "인":
                print_yackja(keyword)
                check_index_number = 1

            elif keyword == "것":
                print_yackja(keyword)
                check_index_number = 1

            elif keyword == "." or keyword == "?" or keyword == "!" or keyword == ",":
                check_special_character(keyword)  # 이 함수에서도 check_index를 증가시켜줘야 하네

            elif keyword == "1" or keyword == "2" or keyword == "3" or keyword == "4" or keyword == "5" or keyword == "6" or keyword == "7" or keyword == "8" or keyword == "9" or keyword == "0":
                if check_index_number == 1:
                    change_number(keyword, 1) #1일때 수표를 출력함
                    check_index_number = 2
                    
                elif check_index_number == 2:
                    change_number(keyword, 2)
                    check_index_number = 2

            else:  # 그 밖에 장이나, 정 공 이런 단어들
                choseung(cho_value)
                jungseung(jung_value, check_jong)
                jongseung(jong_value)
                check_index_number = 1
                
            young_index += 1

        young_index = 0
        return

    def change_number(keyword, check_start_number):
        nonlocal destination
        nonlocal check_index
        nonlocal return_list

        if check_start_number == 1:
            destination = start_number
            return_list.append(destination)

        if keyword == "1":
            destination = n_1
            return_list.append(destination)

        if keyword == "2":
            destination = n_2
            return_list.append(destination)

        if keyword == "3":
            destination = n_3
            return_list.append(destination)

        if keyword == "4":
            destination = n_4
            return_list.append(destination)

        if keyword == "5":
            destination = n_5
            return_list.append(destination)

        if keyword == "6":
            destination = n_6
            return_list.append(destination)

        if keyword == "7":
            destination = n_7
            return_list.append(destination)

        if keyword == "8":
            destination = n_8
            return_list.append(destination)

        if keyword == "9":
            destination = n_9
            return_list.append(destination)

        if keyword == "0":
            destination = n_0
            return_list.append(destination)
        return 
        


    def check_special_character(keyword):
        nonlocal destination
        nonlocal check_index
        nonlocal return_list

        if keyword == ".":
            #printzum)
            destination = zum
            return_list.append(destination)

        elif keyword == ",":
            #printcoma)
            destination = coma
            return_list.append(destination)

        elif keyword == "!":
            #printfu8)
            destination = fu8
            return_list.append(destination)

        elif keyword == "?":
            #printwhat)
            destination = what
            return_list.append(destination)

        check_index += 1
        # return_list.append(destination) ############
        return


    def print_yackja(keyword):  ###################################################################
        nonlocal destination
        nonlocal check_index

        check_index += 1  # 겹치네 #############################################3

        if keyword == "가":
            #printga)
            destination = ga
            return_list.append(destination)

        elif keyword == "나":
            #printna)
            destination = na
            return_list.append(destination)

        elif keyword == "다":
            #printda)
            destination = da
            return_list.append(destination)

        elif keyword == "마":
            #printma)
            destination = ma
            return_list.append(destination)

        elif keyword == "바":
            #printba)
            destination = ba
            return_list.append(destination)

        elif keyword == "사":
            #printsa)
            destination = sa
            return_list.append(destination)

        elif keyword == "자":
            #printza)
            destination = za
            return_list.append(destination)

        elif keyword == "카":
            #printka)
            destination = ka
            return_list.append(destination)

        elif keyword == "타":
            #printta)
            destination = ta
            return_list.append(destination)

        elif keyword == "파":
            #printpa)
            destination = pa
            return_list.append(destination)

        elif keyword == "하":
            #printha)
            destination = ha
            return_list.append(destination)

        elif keyword == "억":
            #printuek)
            destination = uek
            return_list.append(destination)

        elif keyword == "언":
            #printuen)
            destination = uen
            return_list.append(destination)

        elif keyword == "얼":
            #printuel)
            destination = uel
            return_list.append(destination)

        elif keyword == "연":
            #printuen)
            destination = uen
            return_list.append(destination)

        elif keyword == "열":
            #printuel)
            destination = uel
            return_list.append(destination)

        elif keyword == "영":
            #printueng)
            destination = ueng
            return_list.append(destination)

        elif keyword == "옥":
            #printok)
            destination = ok
            return_list.append(destination)

        elif keyword == "온":
            #printon)
            destination = on
            return_list.append(destination)

        elif keyword == "옹":
            #printong)
            destination = ong
            return_list.append(destination)

        elif keyword == "운":
            #printun)
            destination = un
            return_list.append(destination)

        elif keyword == "울":
            #printul)
            destination = ul
            return_list.append(destination)

        elif keyword == "은":
            #printeun)
            destination = eun
            return_list.append(destination)

        elif keyword == "을":
            #printeul)
            destination = eul
            return_list.append(destination)

        elif keyword == "인":
            #printinn)
            destination = inn
            return_list.append(destination)

        elif keyword == "것":
            #printgueck)
            destination = gueck
            return_list.append(destination)

        # return_list.append(destination) ###############
        return


    def choseung(cho_value):  # 여기 부분은 2개를 출력하는 부분때문에 다 적어야 겠다.
        nonlocal destination
        nonlocal return_list

        if cho_value == 0x1100:
            #printcho_giug)
            destination = cho_giug
            return_list.append(destination)

        elif cho_value == 0x1102:
            #printcho_niun)
            destination = cho_niun
            return_list.append(destination)

        elif cho_value == 0x1103:
            #printcho_diud)
            destination = cho_diud
            return_list.append(destination)

        elif cho_value == 0x1105:
            #printcho_riur)
            destination = cho_riur
            return_list.append(destination)

        elif cho_value == 0x1106:
            #printcho_mium)
            destination = cho_mium
            return_list.append(destination)

        elif cho_value == 0x1107:
            #printcho_biub)
            destination = cho_biub
            return_list.append(destination)

        elif cho_value == 0x1109:
            #printcho_sius)
            destination = cho_sius
            return_list.append(destination)

        # if ord(cho_value) = "ㅇ":

        elif cho_value == 0x1112:
            #printcho_ziuz)
            destination = cho_ziuz
            return_list.append(destination)

        elif cho_value == 0x110e:
            #printcho_ciuc)
            destination = cho_ciuc
            return_list.append(destination)

        elif cho_value == 0x110f:
            #printcho_kiuk)
            destination = cho_kiuk
            return_list.append(destination)

        elif cho_value == 0x1110:
            #printcho_tiut)
            destination = cho_tiut
            return_list.append(destination)

        elif cho_value == 0x1111:
            #printcho_piup)
            destination = cho_piup
            return_list.append(destination)

        elif cho_value == 0x1112:
            #printcho_hiuh)
            destination = cho_hiuh
            return_list.append(destination)

        elif cho_value == 0x1101:
            #printcho_dunsori)
            destination = cho_dunsori
            return_list.append(destination)
            #printcho_giug)
            destination = cho_giug
            return_list.append(destination)

        elif cho_value == 0x1104:
            #printcho_dunsori)
            destination = cho_dunsori
            return_list.append(destination)
            #printcho_diud)
            destination = cho_diud
            return_list.append(destination)

        elif cho_value == 0x1108:
            #printcho_dunsori)
            destination = cho_dunsori
            return_list.append(destination)
            #printcho_biub)
            destination = cho_biub
            return_list.append(destination)

        elif cho_value == 0x110a:
            #printcho_dunsori)
            destination = cho_dunsori
            return_list.append(destination)
            #printcho_sius)
            destination = cho_sius
            return_list.append(destination)

        elif cho_value == 0x110d:
            #printcho_dunsori)
            destination = cho_dunsori
            return_list.append(destination)
            #printcho_ziuz)
            destination = cho_ziuz
            return_list.append(destination)

        return


    def jungseung(jung_value, check_jong):  # 종성이 없는 경우를 준다. (매개변수로 받자... )
        nonlocal destination
        nonlocal check_index
        nonlocal return_list

        if check_jong == 0:
            check_index += 1

        if jung_value == 0x1161:
            #printjung_1)
            destination = jung_1
            return_list.append(destination)

        elif jung_value == 0x1163:
            #printjung_2)
            destination = jung_2
            return_list.append(destination)

        elif jung_value == 0x1165:
            #printjung_3)
            destination = jung_3
            return_list.append(destination)

        elif jung_value == 0x1167:
            #printjung_4)
            destination = jung_4
            return_list.append(destination)

        elif jung_value == 0x1169:
            #printjung_5)
            destination = jung_5
            return_list.append(destination)

        elif jung_value == 0x116d:
            #printjung_6)
            destination = jung_6
            return_list.append(destination)

        elif jung_value == 0x116e:
            #printjung_7)
            destination = jung_7
            return_list.append(destination)

        elif jung_value == 0x1172:
            #printjung_8)
            destination = jung_8
            return_list.append(destination)

        elif jung_value == 0x1173:
            #printjung_9)
            destination = jung_9
            return_list.append(destination)

        elif jung_value == 0x1175:
            #printjung_10)
            destination = jung_10
            return_list.append(destination)

        elif jung_value == 0x1162:
            #printjung_11)
            destination = jung_11
            return_list.append(destination)

        elif jung_value == 0x1164:
            #printjung_12)
            destination = jung_12
            return_list.append(destination)

        elif jung_value == 0x1166:
            #printjung_13)
            destination = jung_13
            return_list.append(destination)

        elif jung_value == 0x1168:
            #printjung_14)
            destination = jung_14
            return_list.append(destination)

        elif jung_value == 0x116a:
            #printjung_15)
            destination = jung_15
            return_list.append(destination)

        elif jung_value == 0x116b:
            #printjung_16)
            destination = jung_16
            return_list.append(destination)

        elif jung_value == 0x116c:
            #printjung_17)
            destination = jung_17
            return_list.append(destination)

        elif jung_value == 0x116f:
            #printjung_18)
            destination = jung_18
            return_list.append(destination)

        elif jung_value == 0x1170:
            #printjung_19)
            destination = jung_19
            return_list.append(destination)

        elif jung_value == 0x1171:
            #printjung_20)
            destination = jung_20
            return_list.append(destination)

        elif jung_value == 0x1174:
            #printjung_21)
            destination = jung_21
            return_list.append(destination)

        # return_list.append(destination)
        return


    def jongseung(jong_value):
        nonlocal check_index  # ? index네 ####################################
        nonlocal return_list

        if jong_value >= 0x11A8:
            check_index += 1
        # check_index += 1

        nonlocal destination
        if jong_value == 0x11a8:
            #printjong_giug)
            destination = jong_giug
            return_list.append(destination)

        elif jong_value == 0x11ab:
            #printjong_niun)
            destination = jong_niun
            return_list.append(destination)

        elif jong_value == 0x11ae:
            #printjong_diud)
            destination = jong_diud
            return_list.append(destination)

        elif jong_value == 0x11af:
            #printjong_riur)
            destination = jong_riur
            return_list.append(destination)

        elif jong_value == 0x11b7:
            #printjong_mium)
            destination = jong_mium
            return_list.append(destination)

        elif jong_value == 0x11b8:
            #printjong_biub)
            destination = jong_biub
            return_list.append(destination)

        elif jong_value == 0x11ba:
            #printjong_sius)
            destination = jong_sius
            return_list.append(destination)

        elif jong_value == 0x11bc:
            #printjong_oung)
            destination = jong_oung
            return_list.append(destination)

        elif jong_value == 0x11bd:
            #printjong_ziuz)
            destination = jong_ziuz
            return_list.append(destination)

        elif jong_value == 0x11be:
            #printjong_ciuc)
            destination = jong_ciuc
            return_list.append(destination)

        elif jong_value == 0x11bf:
            #printjong_kiuk)
            destination = jong_kiuk
            return_list.append(destination)

        elif jong_value == 0x11c0:
            #printjong_tiut)
            destination = jong_tiut
            return_list.append(destination)

        elif jong_value == 0x11c1:
            #printjong_piup)
            destination = jong_piup
            return_list.append(destination)

        elif jong_value == 0x11c2:
            #printjong_hiuh)
            destination = jong_hiuh
            return_list.append(destination)

        elif jong_value == 0x11a9:
            #printjong_giug)
            destination = jong_giug
            return_list.append(destination)
            #printjong_giug)
            destination = jong_giug
            return_list.append(destination)


        elif jong_value == 0x11bb:
            #printtt)
            destination = tt
            return_list.append(destination)

        elif jong_value == 0x11aa:
            #printjong_giug)
            destination = jong_giug
            return_list.append(destination)
            #printjong_sius)
            destination = jong_sius
            return_list.append(destination)

        elif jong_value == 0x11ac:
            #printjong_niun)
            destination = jong_niun
            return_list.append(destination)
            #printjong_ziuz)
            destination = jong_ziuz
            return_list.append(destination)

        elif jong_value == 0x11ad:
            #printjong_niun)
            destination = jong_niun
            return_list.append(destination)
            #printjong_hiuh)
            destination = jong_hiuh
            return_list.append(destination)

        elif jong_value == 0x11b0:
            #printjong_riur)
            destination = jong_riur
            return_list.append(destination)
            #printjong_giug)
            destination = jong_giug
            return_list.append(destination)

        elif jong_value == 0x11b1:
            #printjong_riur)
            destination = jong_riur
            return_list.append(destination)
            #printjong_mium)
            destination = jong_mium
            return_list.append(destination)

        elif jong_value == 0x11b2:
            #printjong_riur)
            destination = jong_riur
            return_list.append(destination)
            #printjong_biub)
            destination = jong_biub
            return_list.append(destination)

        elif jong_value == 0x11b3:
            #printjong_riur)
            destination = jong_riur
            return_list.append(destination)
            #printjong_sius)
            destination = jong_sius
            return_list.append(destination)

        elif jong_value == 0x11b4:
            #printjong_riur)
            destination = jong_riur
            return_list.append(destination)
            #printjong_tiut)
            destination = jong_tiut
            return_list.append(destination)

        elif jong_value == 0x11b5:
            #printjong_riur)
            destination = jong_riur
            return_list.append(destination)
            #printjong_piup)
            destination = jong_piup
            return_list.append(destination)

        elif jong_value == 0x11b9:
            #printjong_biub)
            destination = jong_biub
            return_list.append(destination)
            #printjong_sius)
            destination = jong_sius
            return_list.append(destination)
        return


    def check_yackja(print_list):  # 약자를 출력한다. 단어 프린트가 끝나면 이들은 0으로 초기화 된다.
        nonlocal check_index
        list_len = len(print_list)

        # 만약 index가 list_len이라면 그냥 바로 약자를 출력한다.
        if list_len > 1:
            list_len -= 1
            if print_list[check_index] == "나":
                if check_index == list_len:
                    return 1
                cho_index = int(((ord(print_list[check_index + 1]) - 0xAC00) / 28) / 21)  # 1 이라서 뒤에께 안되네
                # check_index += 1
                cho_value = cho_index + 0x1100
                if cho_value == 4363:  # 초성 분리 시전 만약 나 뒤에 모음이라면
                    return 2  # 약자가 아닐 시
                return 1  # 나 뒤에 모음이 아니라면 즉, 약자일시

            if print_list[check_index] == "다":  # 끝에 잇을 경유 뒤에게 없어서 그렇네 조건문 넣자
                if check_index == list_len:
                    return 1
                cho_index = int(((ord(print_list[check_index + 1]) - 0xAC00) / 28) / 21)
                # check_index += 1
                cho_value = cho_index + 0x1100
                if cho_value == 4363:
                    return 2
                return 1

            if print_list[check_index] == "마":
                if check_index == list_len:
                    return 1
                cho_index = int(((ord(print_list[check_index + 1]) - 0xAC00) / 28) / 21)
                # check_index += 1
                cho_value = cho_index + 0x1100
                if cho_value == 4363:
                    return 2
                return 1

            if print_list[check_index] == "바":
                if check_index == list_len:
                    return 1
                cho_index = int(((ord(print_list[check_index + 1]) - 0xAC00) / 28) / 21)
                # check_index += 1
                cho_value = cho_index + 0x1100
                if cho_value == 4363:
                    return 2
                return 1

            if print_list[check_index] == "자":
                if check_index == list_len:
                    return 1
                cho_index = int(((ord(print_list[check_index + 1]) - 0xAC00) / 28) / 21)
                # check_index += 1
                cho_value = cho_index + 0x1100
                if cho_value == 4363:
                    return 2
                return 1

            if print_list[check_index] == "카":
                if check_index == list_len:
                    return 1
                cho_index = int(((ord(print_list[check_index + 1]) - 0xAC00) / 28) / 21)
                # check_index += 1
                cho_value = cho_index + 0x1100
                if cho_value == 4363:
                    return 2
                return 1

            if print_list[check_index] == "타":
                if check_index == list_len:
                    return 1
                cho_index = int(((ord(print_list[check_index + 1]) - 0xAC00) / 28) / 21)
                # check_ndex += 1
                cho_value = cho_index + 0x1100
                if cho_value == 4363:
                    return 2
                return 1

            if print_list[check_index] == "파":
                if check_index == list_len:
                    return 1
                cho_index = int(((ord(print_list[check_index + 1]) - 0xAC00) / 28) / 21)
                # check_index += 1
                cho_value = cho_index + 0x1100
                if cho_value == 4363:
                    return 2
                return 1

            if print_list[check_index] == "하":
                if check_index == list_len:
                    return 1
                cho_index = int(((ord(print_list[check_index + 1]) - 0xAC00) / 28) / 21)
                # check_index += 1
                cho_value = cho_index + 0x1100
                if cho_value == 4363:
                    return 2
                return 1
        elif check_index == list_len:
            return 1  # 1이 약자 2가 일반

        return 1  # 한 문자 '나' 라면


    def yacka(print_list):  # 약어를 출력한다.
        nonlocal destination
        nonlocal check_index
        check_list_len_g = len(print_list)
        if check_list_len_g == 1:
            return

        if print_list[0] == "그":
            if print_list[1] == "리":
                if print_list[2] == "고":
                    #printgrigo)
                    destination = grigo
                    # #print"SPACE zero : %d" %space)
                    # destination = space
                    check_index += 1
                    return_list.append(destination)  #########
                    return 1

                if print_list[2] == "하":
                    if print_list[3] == "여":
                        #printgrihayeo)
                        destination = grihayeo
                        # #print"SPACE zero : %d" %space)
                        # destination = space
                        return_list.append(destination)
                        check_index += 1
                        return 1

            if print_list[1] == "래":
                if print_list[2] == "서":
                    #printgraseo)
                    destination = graseo
                    # #print"SPACE zero : %d" %space)
                    # destination = space
                    return_list.append(destination)
                    check_index += 1
                    return 1

            if print_list[1] == "러":
                if print_list[2] == "나":
                    #printgruna)
                    destination = gruna
                    # #print"SPACE zero : %d" %space)
                    # destination = space
                    return_list.append(destination)
                    check_index += 1
                    return 1

                if print_list[2] == "면":
                    #printgrumeon)
                    destination = grumeon
                    # #print"SPACE zero : %d" %space)
                    # destination = space
                    return_list.append(destination)
                    check_index += 1
                    return 1

                if print_list[2] == "므":
                    if print_list[3] == "로":
                        #printgrumuro)
                        destination = grumuro
                        # #print"SPACE zero : %d" %space)
                        # destination = space
                        return_list.append(destination)
                        check_index += 1
                        return 1

            if print_list[1] == "런":
                if print_list[2] == "데":
                    #printgrunde)
                    destination = grunde
                    # #print"SPACE zero : %d" %space)
                    # destination = space
                    return_list.append(destination)
                    check_index += 1
                    return 1

                check_index += 1
                return 2
            return 2

        check_index += 1
        return 2


    def change_hangul(change_list):
        # #printchange_list[0])
        if change_list[0] == '그':
            check = yacka(change_list)  # 약어만 출력하는 함수
            if check == 1:
                return

        find_hangul(change_list)  # 띄어쓰기 단위로 받아온 단어를 예외가 될 수 있는 글을 판단한다.


    def check_letter(check_list):  # 첫 글자가 한글이나 아니냐 파악 루틴
        check = ord(check_list[0])
        # #printcheck_list[0])
        #print(check_list[0])
        if check >= 0xAC00 and check <= 0xD7A3:
            return 1
            # hangul routine
        if check >= 65 and check <= 122:
            return 2
            # english routine
        if check >= 32 and check <= 64: #만약 체크하는 
            return 1
            # single number and special char routine. So same hangul routine 한글 루틴에서 처리할꺼야


    def sep(sep_letter):  # 단어를 문자로 분리해주는 함수
        word = []
        return_word = []
        for keyword in sep_letter:
            for i in range(0, len(keyword)):
                word.append(keyword[i])
            return_word.append(word)
            word = []
        return return_word


    # 띄어쓰기를 위한 index#
    index = 0

    string = in_str
    list_string = []
    list_string = string.split()  # 1중 리스트로 구성됨
    # 이중 리스트로 구현해야 띄어쓰기 용이함
    tmp = []  # 단어 중심의 이중 리스트
    letter = []  # 문자 중심의 최종 이중 리스트
    for keyword in list_string:  # 띄어쓰기를 기준으로 이중리스트를 구현함
        letter.append(keyword)
        tmp.append(letter)
        letter = []
    #printtmp)

    sep_word = []
    letter = []

    for i in range(0, len(tmp)):
        sep_word = tmp[i]
        sep_word = sep(sep_word)  # 단어를 쪼개고 이중 리스트로 반환
        letter = letter + (sep_word)  # 단어중심의 이중리스트가 아닌 문자 중심의 이중리스트
    # #printletter)
    # #printlen(letter)) ### 여기까지가 문자 리스트 ###
    routine_value = len(letter)  # 반복문을 돌리기 위한 길이 변수

    # letter[value] 이 문자로 쪼개진 리스트를 넘긴다.
    for i in range(0, routine_value):
        list_letter = []
        list_letter = letter[i]  # 이중리스트에 있는 것중 하나를 옮긴다.
        #printlist_letter)
        # list_letter_number = len(list_letter)

        check = check_letter(list_letter)  # 한글인지 아닌지 확인한다
        # list_letter[i+1]해서 값을 확인해도 될듯?
        if check == 1:
            # if index > 0:
            change_hangul(list_letter)  # 한글 조합일시
            #print"SPACE : %d" % space)
            destination = space
            return_list.append(destination)
            check_index = 0  # 약자를 검사하는 변수 단어가 끝나면 초기화 시킨다.
            if_character_change = 10  # 한글 반환값
        # index += 1 #띄어쓰기

        if check == 2:
            if if_character_change == 10:  # 그전이 한글이었는지 확인한다.
                #printstart_en)
                destination = start_en
                return_list.append(destination)

            change_english(list_letter)  # 영어 조합일시
            # for_print_list_len = len(letter) #문자중심의 문자들이 담긴 이중 리스트

            if i < routine_value - 1:  # 한글과 숫자를...
                if ord(letter[i + 1][0]) >= 0xAC00 and ord(letter[i + 1][0]) <= 0xD7A3:
                    #printend_en)
                    destination = end_en
                    return_list.append(destination)

                if ord(letter[i + 1][0]) >= 32 and ord(letter[i + 1][0]) <= 64:
                    #printend_en)
                    destination = end_en
                    return_list.append(destination)

            if i == routine_value - 1:
                #printend_en)
                destination = end_en
                return_list.append(destination)

            #print"SPACE : %d" % space)
            destination = space
            return_list.append(destination)  ########
            if_character_change = 20

    return_list_for_rapa(return_list)  ####
    return return_list
    return_list = []  # 다시 초기화

    # index += 1 #다음부터 띄어쓰기를 한다.

    # 에러 발견 : ex) 가 나 야 했을 때 에러가 뜸
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


    # 어떤 앞 문자를 처리하면서 check_index를 늘려줘야 하네


    # 영어반환값을 20으로하고 한글 반환값을 10으로 해야하겠다. 그럼 초기값을 10으로 해야겠네?

    # 그리고 한글 루틴에서 20을 체크하면 먼저 영어 끝을 알리는 걸 날리고

a=input("input your hangul : ")
print(change(a))


# 함수 콜할때 change(__str_ )
