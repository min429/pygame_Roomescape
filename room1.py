import pygame
from pygame.locals import *
import sys
from mainclass import *  # 객체 관리용 클래스
import room1
from main import *

while True:
    mousePosition = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:
        mousePressed = True
    else:
        mousePressed = False

    clock.tick(60)  # 60프레임 고정
    countframe = 0  # 무한반복 방지용 변수 다시 반복문에서 0으로 초기화

    #### 메인 사운드 관련 ####
    if mainsound_on == 0:
        mainsound.stop()
    if mainsound_on == 1:
        mainsound.play(-1)

    if moonopen == 1:
        mainsound_on = 0
        rabbit = 1

    if nodoll == 0:
        doll2.set_alpha(0)

    if nodoll == 1:
        doll2.set_alpha(255)

    ######################### 맨 처음 게임 실행 시 검은 화면 출력 ####################################
    if once == 0:
        fade(1140, 720, blackbg, oncebg)  # 첫 실행시 검은 화면에서 1번 화면으로 나옴
        screen.blit(textbox.m_img, textbox.m_location)
        textbox.change_img(textbox_p2, (70, 450))
        once = 1

    ######################### 도어락 해제 성공 시 ###################################################
    if success_doorlock == 1:
        noroom = 1
        closet.change_img(open_closet_p1, (360, 105))

    if success_doorlock == 2:
        if get_key == 1:
            closet.change_img(open_closet_p2, (360, 105))
            success_doorlock = 3

    ################################### 다이얼 해제 성공 시 ##############################
    if control3 == 0:
        if dial_success == 1:
            dial_list = []
            dial.set_alpha(0)
            dial_num = 0
            safe.change_img(safe_p2, safe.m_firstlocation)  # 이미지파일 원래대로
            small_blackbg.set_alpha(0)  # 화면 투명도를 원래대로
            safe.clicked()  # m_state = 0
            dial.clicked()
            dial.set_alpha(0)
            safe.set_alpha(255)
            x.set_alpha(0)
            control = 1
            control2 = 1
            control3 = 1

    ########### 인형이 침대 위에 올라오면 인형의 집 문 열림
    if baby_in_bed == 1 and first_house_open == 0:
        house_door_open = 1
        house.change_img(house_open, (450, 330))  # 하우스 모양 변경
        first_house_open = 2

    if p1back == 1:
        img.change_img(img1_p1, startpoint)
        for obj in object1:
            obj.set_alpha(255)
        arrow_left.set_alpha(255)
        arrow_right.set_alpha(255)
        ##작업

        noroom = 500
        dolldoll = 2
        p1back2 = 1
        p1back = 2

    if p1back2 == 1:
        pygame.time.delay(800)
        noise.set_alpha(0)
        textbox.set_alpha(0)
        p1back2 = 2

    ########################## 공구상자 오픈 성공 시 ##################################################
    ## xx

    ######################### 마우스 클릭 시 ####################################################
    if mousePressed:
        countframe = 1  # 화살표 클릭시 프레임 구현용 (무한반복 방지) 한번 클릭시 무조건 1으로 됨
        if mainsound_on == 0:
            mainsound_on = 1
        ####################### 객체 클릭 시(확대 시 다른 객체 클릭 방지) ###############################
        if control == 1:  # 객체 클릭할 때
            if control2 == 0:
                if 449 <= mousePosition[0] <= 539:
                    if 494 <= mousePosition[1] <= 580:  # 도어락 클릭시
                        if doorlock.m_state == 1 and len(lock_number) == 4:
                            if password_doorlock == lock_number:
                                success_doorlock = 1
                                control2 = 1
                                control = 0
                                doorlock.m_state = 0
                                doorlock.set_alpha(0)
                                for i in slist:
                                    i.set_alpha(0)
                                lock_number = []
                                lock_filled = {0: 0, 1: 0, 2: 0, 3: 0}

                            else:
                                lock_number = []
                                lock_filled = {0: 0, 1: 0, 2: 0, 3: 0}
                                control2 = 1
                                control = 0
                                doorlock.m_state = 0
                                doorlock.set_alpha(0)
                                for i in slist:
                                    i.set_alpha(0)

                ######의자 두번눌렀을 때
                if 410 < mousePosition[0] < 747:
                    if 212 < mousePosition[1] < 519:
                        if get_record == 0 and get_one_driver == 1 and open_chair == 1:
                            chair.change_img(chair_p3,(370,100))
                            pygame.time.delay(100)
                            control2 = 1
                            control = 0
                            pygame.mixer.music.load("driver_use.mp3")
                            pygame.mixer.music.play(1)
                            ready_get_record = 1

                ######문위치 두번눌렀을 때
                if textbox.m_x <= mousePosition[0] <= textbox.m_x+textbox.m_size_x:
                    if textbox.m_y <= mousePosition[1] <= textbox.m_y+textbox.m_size_y:
                        if MOONcheck == 1:
                            textbox.set_alpha(0)
                            pygame.time.delay(100)
                            control2 = 1
                            control = 1
                            MOONcheck = 2

                #######  곰인형 두번 눌렀을 때 아기 아이템으로 가져가기
                if 580 < mousePosition[0] < 680:
                    if 414 < mousePosition[1] < 537:
                        if bear_cut == 1:
                            textbox.set_alpha(0)
                            bear.change_img(bear_big3, (400, 100))  # 상처난 곰으로 바뀜
                            get_doll = 1
                            pygame.mixer.music.load("laugh_doll.mp3")
                            pygame.mixer.music.play(1)
                            pygame.time.delay(200)
                            bear_cut = 2
                            control2 = 1
                            control = 0


            else:  ## control = 1, control2 = 0
                if once == 1:  # 처음 게임 시작시 나오는 어두운 화면
                    if textbox.m_x <= mousePosition[0] <= textbox.m_x + textbox.m_size_x:
                        if textbox.m_y <= mousePosition[1] <= textbox.m_y + textbox.m_size_y:
                            screen.blit(textbox.m_img, textbox.m_location)
                            once_text_check = 1

                    if 765 <= mousePosition[0] <= 782:
                        if 405 <= mousePosition[1] <= 443:  # 스위치 클릭시
                            if once_text_check == 1:
                                switch_on = pygame.mixer.Sound("switch.mp3")
                                switch_on.play()
                                img.m_img.set_alpha(255)  # 1p 출력
                                fadeonce(1140, 720, oncebg, img.m_img, object1)  # 1p와 객체들 출력
                                once, count, leftright = 2, 1, 0
                                textbox.set_alpha(0)

                if 545 <= mousePosition[0] <= 675:
                    if 515 <= mousePosition[1] <= 690:
                        if dolldoll == 1:

                            noise.set_alpha(255)
                            pygame.mixer.music.load("zizizik.mp3")
                            pygame.mixer.music.play(1)
                            pygame.time.delay(200)
                            control = 1
                            control2 = 1
                            p1back = 1

                ####################### (어느 화면에서든)프랑스 인형 클릭 시 ################################# # (이승민 5/26 01:00 추가)
                # if (
                #         count == 1 or get_doll == 1) and not use_doll:  # 인형을 사용하지 않았을 때 프랑스 인형을 1번 화면에서 클릭 or 인벤에서 클릭
                #     if doll.m_x <= mousePosition[0] <= doll.m_x + doll.m_size_x:
                #         if doll.m_y <= mousePosition[1] <= doll.m_y + doll.m_size_y:  # 인형 클릭 시
                #             if not get_doll:  # 인형을 얻지 않았다면 인형을 크게 확대해서 화면에 띄워줌
                #                 small_blackbg.set_alpha(172)
                #                 doll.change_img(doll_big, (440, 160))  # 단순 확대 사진
                #                 x.set_alpha(255)
                #             elif get_doll == 1:  # 인형을 얻은 상태라면 인형을 눌렀을 때 인형이 빛남
                #                 doll.change_img(doll_edge, doll.m_location)  # 빛나는 이미지
                #                 doll_glow = 1  # 인벤에서 눌렀을 때 테두리 생김
                #                 pygame.time.delay(100)  # 자동 클릭 방지
                #             doll.clicked()  # m_state = 1
                #             control = 0  # 인형 눌렀을 때는 다른 객체 클릭 불가
                #
                ####################### 인벤에서 ten_driver 클릭 시 ################################# # (이승민 5/28 18:30 추가)
                if get_ten_driver == 1 and not use_ten_driver:  # 사용한 상태면 클릭해도 반응 없게 해야해서 not use_ten_driver 추가
                    if ten_driver.m_x <= mousePosition[0] <= ten_driver.m_x + ten_driver.m_size_x:
                        if ten_driver.m_y <= mousePosition[1] <= ten_driver.m_y + ten_driver.m_size_y:
                            ten_driver.change_img(ten_driver_edge, ten_driver.m_location)  # 빛나는 이미지
                            ten_driver.clicked()  # m_state = 1
                            ten_driver_glow = 1  # 인벤에서 눌렀을 때 테두리 생김
                            pygame.time.delay(100)  # 자동 클릭 방지
                            control = 0  # ten_driver 눌렀을 때는 다른 객체 클릭 불가

                ####################### 인벤에서 one_driver 클릭 시 ################################# # (이승민 5/28 18:30 추가)
                if get_one_driver == 1 and not use_one_driver:  # 사용한 상태면 클릭해도 반응 없게 해야함
                    if one_driver.m_x <= mousePosition[0] <= one_driver.m_x + one_driver.m_size_x:
                        if one_driver.m_y <= mousePosition[1] <= one_driver.m_y + one_driver.m_size_y:
                            one_driver.change_img(one_driver_edge, one_driver.m_location)  # 빛나는 이미지
                            one_driver.clicked()  # m_state = 1
                            one_driver_glow = 1  # 인벤에서 눌렀을 때 테두리 생김
                            pygame.time.delay(100)
                            control = 0

                ####################### 인벤에서 knife 클릭 시 ################################# # (이승민 5/28 18:30 추가)
                if get_knife == 1 and not use_knife:  # 사용한 상태면 클릭해도 반응 없게 해야함
                    if knife.m_x <= mousePosition[0] <= knife.m_x + knife.m_size_x:
                        if knife.m_y <= mousePosition[1] <= knife.m_y + knife.m_size_y:
                            knife.change_img(knife_edge, knife.m_location)  # 빛나는 이미지
                            knife.clicked()  # m_state = 1
                            knife_glow = 1  # 인벤에서 눌렀을 때 테두리 생김
                            pygame.time.delay(100)
                            control = 0

                ####################### 인벤에서 record 클릭 시 ################################# # (이승민 5/30 14:30 추가)
                if get_record == 1 and not use_record:  # 사용한 상태면 클릭해도 반응 없게 해야함
                    if inven_record_location[0] <= mousePosition[0] <= inven_record_location[0] + 59:
                        if inven_record_location[1] <= mousePosition[1] <= inven_record_location[0] + 56:
                            record.change_img(record_edge, inven_record_location)  # 빛나는 이미지
                            record.clicked()  # m_state = 1
                            record_glow = 1  # 인벤에서 눌렀을 때 테두리 생김
                            pygame.time.delay(100)
                            control = 0

                ####################### 인벤에서 key 클릭 시 ################################# # (이승민 5/30 14:30 추가)
                if get_key == 1 and not use_key:  # 사용한 상태면 클릭해도 반응 없게 해야함
                    if key.m_x <= mousePosition[0] <= key.m_x + key.m_size_x:
                        if key.m_y <= mousePosition[1] <= key.m_y + key.m_size_y:
                            key.change_img(key_edge, key.m_location)  # 빛나는 이미지
                            key.clicked()  # m_state = 1
                            key_glow = 1  # 인벤에서 눌렀을 때 테두리 생김
                            pygame.time.delay(100)
                            control = 0
                ######################## 객체 클릭 후 1번 방 일때 #######################################
                if count == 1:
                    ###### 문부분 누를 때 사진없는 문 객체 추가
                    if 812 <= mousePosition[0] <= 984:
                        if 249 <= mousePosition[1] <= 634:
                            if MOONcheck == 0:
                                if use_record == 0:
                                    textbox.set_alpha(0)
                                    textbox.set_alpha(255)
                                    textbox.change_img(textbox_p3, (70, 450))
                                    MOON.clicked()
                                    pygame.time.delay(100)
                                    control = 0
                                    print(MOON.m_state)

                    ######################## 화분 클릭 시 (05/25 17:23 추가)
                    if pot.m_x <= mousePosition[0] <= pot.m_x + pot.m_size_x:
                        if pot.m_y <= mousePosition[1] <= pot.m_y + pot.m_size_y:
                            ################### 깨지기 전 ##############
                            if dial_scary >= 0 and noroom < 300:
                                small_blackbg.set_alpha(172)
                                pot.change_img(pot_big, (450, 0))  # 확대된 화분
                                pot.set_alpha(255)
                                x.set_alpha(255)
                                pot.clicked()  # m_state = 1
                                textbox.set_alpha(255)
                                textbox.change_img(textbox_p5, (70, 450))
                                control = 0

                    # (525, 585) ######### 넘어진 화분 클릭 시 #########################
                    if 525 <= mousePosition[0] <= 525 + 279:
                        if 585 <= mousePosition[1] <= 585 + 115:
                            if dial_scary < 0:
                                small_blackbg.set_alpha(172)
                                pot.change_img(pot2_big, (290, 290))  # 확대된 넘어진 화분
                                pot.set_alpha(255)
                                x.set_alpha(255)
                                pot.clicked()  # m_state = 1
                                control = 0

                    ######################## 책 클릭 시 (05/25 17:50 추가)
                    if books.m_x <= mousePosition[0] <= books.m_x + books.m_size_x:
                        if books.m_y <= mousePosition[1] <= books.m_y + books.m_size_y:
                            small_blackbg.set_alpha(172)
                            books.change_img(books_p2, (400, 130))  # 확대된 책
                            books.set_alpha(255)
                            x.set_alpha(255)
                            books.clicked()  # m_state = 1
                            control = 0

                    ######################## 공구상자 클릭 시 (05/25 18:04 추가)
                    if toolbox.m_x <= mousePosition[0] <= toolbox.m_x + toolbox.m_size_x:
                        if toolbox.m_y <= mousePosition[1] <= toolbox.m_y + toolbox.m_size_y:
                            small_blackbg.set_alpha(172)
                            if open_toolbox == 0:
                                toolbox.change_img(toolbox_big, (340, 170))  # 확대된 잠긴 공구상자
                                textbox.set_alpha(255)
                                textbox.change_img(textbox_p10, (70, 450))
                            if open_toolbox == 1:
                                toolbox.change_img(empty_toolbox, (340, 170))  # 확대된 열린 공구상자 단면

                            toolbox.set_alpha(255)
                            x.set_alpha(255)
                            toolbox.clicked()  # m_state = 1
                            control = 0

                    ######################## 트로피 클릭 시 (05/25 18:08 추가)
                    if trophy.m_x <= mousePosition[0] <= trophy.m_x + trophy.m_size_x:
                        if trophy.m_y <= mousePosition[1] <= trophy.m_y + trophy.m_size_y:
                            small_blackbg.set_alpha(172)
                            trophy.change_img(trophy_big, (500, 200))  # 확대된 트로피
                            trophy.set_alpha(255)
                            x.set_alpha(255)
                            trophy.clicked()  # m_state = 1
                            control = 0

                    ######################## 나무액자 클릭 시 (05/30 16:48 추가)
                    if photoframe.m_x <= mousePosition[0] <= photoframe.m_x + photoframe.m_size_x:
                        if photoframe.m_y <= mousePosition[1] <= photoframe.m_y + photoframe.m_size_y:
                            small_blackbg.set_alpha(172)
                            if open_photo == 0:
                                photoframe.change_img(photoframe_big, (480, 100))
                                textbox.set_alpha(255)
                                textbox.change_img(textbox_p8, (70, 450))
                            if open_photo == 1:
                                photoframe.change_img(photoframe2_big, (480, 100))
                            photoframe.set_alpha(255)
                            x.set_alpha(255)
                            photoframe.clicked()  # m_state = 1
                            control = 0

                    ######################## 철제 액자 클릭 시 (05/30 21:04 추가)
                    if steelframe.m_x <= mousePosition[0] <= steelframe.m_x + steelframe.m_size_x:
                        if trophy.m_y <= mousePosition[1] <= steelframe.m_y + steelframe.m_size_y:
                            small_blackbg.set_alpha(172)
                            steelframe.change_img(steelframe_big, (390, 160))  # 확대된 트로피
                            steelframe.set_alpha(255)
                            x.set_alpha(255)
                            steelframe.clicked()  # m_state = 1
                            control = 0

                    if Matryoshka.m_x <= mousePosition[0] <= Matryoshka.m_x + Matryoshka.m_size_x:
                        if Matryoshka.m_y <= mousePosition[1] <= Matryoshka.m_y + Matryoshka.m_size_y:
                            Matryoshka.change_img(Matryoshka_big, (230, 360 - 125))  # 마트료시카 본체

                            Matryoshka.change_img_scale(
                                (58.19, 363.125))  # 마트료시카 본체 크기
                            pygame.time.delay(100)  # 자동 클릭 방지
                            small_blackbg.set_alpha(172)
                            x.set_alpha(255)
                            Matryoshka.clicked()  # m_state = 1
                            control = 0  # control 0일 때 계속 마트료시카를 클릭(control == 0일 때도 마트료시카는 클릭할 수 있게 해놓음) or x버튼으로 나가기 위해

                    ######################### 문 클릭 시 ########################## (이승민 05/25 18:19 추가)
                    if 810 < mousePosition[0] < 985:
                        if 250 < mousePosition[1] < 635:
                            if use_record:  # 레코드 틀었을 때
                                pygame.mixer.music.stop()  # 음악 멈춤
                                pygame.mixer.music.unload()  # 음악 unload
                                #img.change_img(ending, startpoint)
                                pygame.mixer.music.load("horrormusic.mp3")
                                pygame.mixer.music.play(1)
                                fade_out(1140, 720, img.m_img, object1)
                                img.change_img(ending, startpoint)
                                doll2.set_alpha(0)
                                nodoll = 0
                                for i in object1:
                                    i.set_alpha(0)
                                for j in invenlist:
                                    j.set_alpha(0)
                                arrow_left.set_alpha(0)
                                arrow_right.set_alpha(0)
                                pygame.time.delay(2000)
                                fade_in(1140, 720, ending, object1)
                                control = 0
                                control2 = 1
                ######################## 객체 클릭 후 2번 방 일때 #######################################
                if count == 2:
                    # 마네킹 부분 누를 때
                    if 310 <= mousePosition[0] <= 407:
                        if 200 <= mousePosition[1] <= 666:
                            if mqcheck == 0:
                                textbox.set_alpha(0)
                                textbox.set_alpha(255)
                                textbox.change_img(textbox_p11, (70, 450))
                                mannequin.clicked()
                                pygame.time.delay(100)
                                control = 0

                    if mirror.m_x <= mousePosition[0] <= mirror.m_x + mirror.m_size_x:
                        if mirror.m_y <= mousePosition[1] <= mirror.m_y + mirror.m_size_y:
                            small_blackbg.set_alpha(172)
                            mirror.change_img(big_mirror, (458, 132))
                            x.set_alpha(255)
                            mirror.clicked()  # m_state = 1
                            control = 0

                        ################################## 옷장 클릭 시 #######################################
                    if closet.m_x <= mousePosition[0] <= closet.m_x + closet.m_size_x:
                        if closet.m_y <= mousePosition[1] <= closet.m_y + closet.m_size_y:
                            small_blackbg.set_alpha(172)
                            if success_doorlock == 0:
                                closet.change_img(big_closet, (437, 119))
                            if success_doorlock == 2:
                                closet.change_img(open_closet_p1, (360, 105))
                            if success_doorlock == 3:
                                closet.change_img(open_closet_p2, (360, 105))
                            closet.set_alpha(255)
                            x.set_alpha(255)
                            closet.clicked()  # m_state = 1
                            control = 0

                ######################## 객체 클릭 후 3번 방 일때 #######################################
                if count == 3:
                    # 곰인형 클릭 시 (05/25 19:56 추가)
                    if bear.m_x <= mousePosition[0] <= bear.m_x + bear.m_size_x - 50:
                        if bear.m_y <= mousePosition[1] <= bear.m_y + bear.m_size_y:
                            small_blackbg.set_alpha(172)

                            if bear_cut == 0:
                                bear.change_img(bear_big, (400, 100))  # 확대된 곰인형
                                textbox.set_alpha(255)
                                textbox.change_img(textbox_p16, (70, 450))
                            if bear_cut == 1:
                                bear.change_img(bear_big2, (400, 95))  # 확대된 곰인형
                            if bear_cut == 2:
                                bear.change_img(bear_big3, (400, 100))  # 확대된 곰인형
                            pygame.time.delay(500)
                            bear.set_alpha(255)
                            x.set_alpha(255)
                            bear.clicked()  # m_state = 1
                            control = 0

                    # 인형의 집 클릭 시
                    if house.m_x <= mousePosition[0] <= house.m_x + house.m_size_x:
                        if house.m_y <= mousePosition[1] <= house.m_y + house.m_size_y:
                            if safe_out == 0:
                                small_blackbg.set_alpha(172)
                                if house_door_open == 0:
                                    house.change_img(house_big, (400, 100))  # 확대된 장난감집
                                    textbox.set_alpha(255)
                                    textbox.change_img(textbox_p14, (70, 450))
                                if house_door_open == 1:
                                    house.change_img(house_big2, (400, 150))  # 확대된 장난감집
                                if safe_out == 1:
                                    house.change_img(house_big3, (400, 150))
                                house.set_alpha(255)
                                x.set_alpha(255)
                                house.clicked()  # m_state = 1
                                control = 0

                    ################ 금고 클릭 시 ####################################
                    if 660 <= mousePosition[0] <= 759:
                        if 492 <= mousePosition[1] <= 657:
                            if safe_out == 1:
                                small_blackbg.set_alpha(172)
                                safe.change_img(safe_big, (460, 110))
                                safe.set_alpha(255)
                                x.set_alpha(255)
                                safe.clicked()  # m_state = 1
                                control = 0
                            if dial_success == 1:
                                if get_one_driver == 0:
                                    small_blackbg.set_alpha(172)
                                    safe.change_img(safe2_big, (460, 110))
                                    safe.set_alpha(255)
                                    x.set_alpha(255)
                                    control = 0
                                if get_one_driver == 1:
                                    small_blackbg.set_alpha(172)
                                    safe.change_img(safe3_big, (460, 110))
                                    safe.set_alpha(255)
                                    x.set_alpha(255)
                                    control = 0

                    # 침대 클릭 시
                    if bed.m_x <= mousePosition[0] <= bed.m_x + bed.m_size_x:
                        if bed.m_y <= mousePosition[1] <= bed.m_y + bed.m_size_y:
                            small_blackbg.set_alpha(172)
                            if baby_in_bed == 0:
                                bed.change_img(bed_p1_big, (400, 250))  # 확대된 침대
                                textbox.set_alpha(255)
                                textbox.change_img(textbox_p13, (70, 450))
                            if baby_in_bed == 1:
                                bed.change_img(bed_baby_big, (400, 250))  # 확대된 침대
                            bed.set_alpha(255)
                            x.set_alpha(255)
                            bed.clicked()  # m_state = 1
                            control = 0

                ######################## 객체 클릭 후 4번 방 일때 #######################################
                if count == 4:
                    ######################## 베토벤 액자 클릭 시 ##################################
                    if frame1.m_x <= mousePosition[0] <= frame1.m_x + frame1.m_size_x:
                        if frame1.m_y <= mousePosition[1] <= frame1.m_y + frame1.m_size_y:
                            small_blackbg.set_alpha(172)
                            frame1.change_img(frame1_big, (430, 150))
                            x.set_alpha(255)
                            frame1.clicked()  # m_state = 1
                            control = 0

                    ######################### 바흐 액자 클릭 시###################################
                    if frame2.m_x <= mousePosition[0] <= frame2.m_x + frame2.m_size_x:
                        if frame2.m_y <= mousePosition[1] <= frame2.m_y + frame2.m_size_y:
                            small_blackbg.set_alpha(172)
                            frame2.change_img(frame2_big, (430, 150))
                            x.set_alpha(255)
                            frame2.clicked()  # m_state = 1
                            control = 0

                    ######################### 모차르트 액자 클릭 시###################################
                    if frame3.m_x <= mousePosition[0] <= frame3.m_x + frame3.m_size_x:
                        if frame3.m_y <= mousePosition[1] <= frame3.m_y + frame3.m_size_y:
                            small_blackbg.set_alpha(172)
                            frame3.change_img(frame3_big, (430, 150))
                            x.set_alpha(255)
                            frame3.clicked()  # m_state = 1
                            control = 0

                    ######################### 슈베르트 액자 클릭 시###################################
                    if frame4.m_x <= mousePosition[0] <= frame4.m_x + frame4.m_size_x:
                        if frame4.m_y <= mousePosition[1] <= frame4.m_y + frame4.m_size_y:
                            small_blackbg.set_alpha(172)
                            frame4.change_img(frame4_big, (430, 150))
                            x.set_alpha(255)
                            frame4.clicked()  # m_state = 1
                            control = 0

                    ######################### 레코드 플레이어  클릭 시###################################
                    if rp.m_x <= mousePosition[0] <= rp.m_x + rp.m_size_x:
                        if rp.m_y <= mousePosition[1] <= rp.m_y + rp.m_size_y:
                            small_blackbg.set_alpha(172)
                            rp.change_img(rp_big, (550, 50))
                            x.set_alpha(255)
                            rp.clicked()  # m_state = 1
                            textbox.set_alpha(255)
                            if use_record:
                                textbox.change_img(textbox_p20, (70, 450))
                            else:
                                textbox.change_img(textbox_p17, (70, 450))
                            control = 0

                    ######################### 의자 클릭 시###################################
                    if chair.m_x <= mousePosition[0] <= chair.m_x + chair.m_size_x:
                        if chair.m_y <= mousePosition[1] <= chair.m_y + chair.m_size_y:
                            small_blackbg.set_alpha(172)
                            chair.change_img(chair_big, (430, 150))
                            x.set_alpha(255)
                            chair.clicked()  # m_state = 1
                            textbox.set_alpha(255)
                            textbox.change_img(textbox_p19, (70, 450))
                            control = 0

                ######################## 왼쪽 화살표 클릭 시 #####################################
                if arrow_left.m_x <= mousePosition[0] <= arrow_left.m_x + arrow_left.m_size_x:
                    if arrow_left.m_y <= mousePosition[1] <= arrow_left.m_y + arrow_left.m_size_y:
                        # (0, 250) <= 마우스 위치 <= (100, 350)
                        leftright = -1  # 왼쪽 화살표 클릭시
                        if dial_success == 1:
                            dial_scary += 1
                        if count == 1:
                            count = 4
                        elif count == 2:
                            count = 1
                        elif count == 3:
                            count = 2
                        elif count == 4:
                            count = 3
                        ## 방 옮길때 count를 감소시키며 방을 왼쪽으로 옮김
                        if noroom == 1 and count == 1:
                            noroom = 300
                            pygame.mixer.music.load("horrorchange.mp3")
                            pygame.mixer.music.play(1)
                            img.change_img(img_scary, startpoint)
                            arrow_left.set_alpha(0)
                            arrow_right.set_alpha(0)
                            for i in object1:
                                i.set_alpha(0)
                            control = 0

                            ##################### noroom 스크립트 추가 ################

                ########################### 오른쪽 화살표 클릭 시 #################################
                if arrow_right.m_x <= mousePosition[0] <= arrow_right.m_x + arrow_right.m_size_x:
                    if arrow_right.m_y <= mousePosition[1] <= arrow_right.m_y + arrow_right.m_size_y:
                        # (700, 250) <= 위치 <= (1280, 350)
                        leftright = 1
                        ########################## 문두드리는 소리
                        if dial_success == 1:
                            dial_scary += 1

                        if count == 1:
                            count = 2
                        elif count == 2:
                            count = 3
                        elif count == 3:
                            count = 4
                        elif count == 4:
                            count = 1
                        ## 방 옮길때 count를 증가시키며 방을 오른쪽으로 옮김
                        if noroom == 1 and count == 1:
                            noroom = 300
                            img.change_img(img_scary, startpoint)
                            arrow_left.set_alpha(0)
                            arrow_right.set_alpha(0)
                            for i in object1:
                                i.set_alpha(0)
                            control = 0

        ######################### control이 0일때 (객체 확대 후 다시 돌아가는 코드) ##########################
        else:
            if 109 < mousePosition[0] < 109 + 95:
                if 522 < mousePosition[1] < 673:
                    if moonopen == 1 and rabbit == 1:
                        img.change_img(ending2, startpoint)
                        gomain = 1
            ######################### 일자 드라이버 클릭 후 의자 클릭 시###################################### # (이승민 05/30 14:30 수정)
            if chair.m_state == 0 and one_driver_glow == 1:  # 일자 드라이버를 클릭했을 때만
                if chair.m_x <= mousePosition[0] <= chair.m_x + chair.m_size_x:
                    if chair.m_y <= mousePosition[1] <= chair.m_y + chair.m_size_y:
                        chair.change_img(chair_back, (430, 150))  # 의자 뒷면(열기 전)
                        chair.change_img_scale(
                            (300, 400))  # 사진 크기 말고 실제 의자 사진크기에 맞춰 객체의 크기정보를 수정해줌 -> 의자를 클릭하는 범위도 바뀌기 때문에
                        #small_blackbg.set_alpha(172)
                        chair.clicked()  # m_state = 1
                        pygame.mixer.music.load("driver_use.mp3")
                        pygame.mixer.music.play(1)
                        control = 0  # 밑에 코드에서 일자 드라이버를 "인벤"에서 뻬기 위해

            ######################### 레코드 클릭 후 레코드 플레이어 클릭 시################################### # (이승민 05/30 14:30 추가)
            if rp.m_state == 0 and record_glow == 1:
                if rp.m_x <= mousePosition[0] <= rp.m_x + rp.m_size_x:
                    if rp.m_y <= mousePosition[1] <= rp.m_y + rp.m_size_y:
                        mainsound.stop()
                        pygame.mixer.music.load("dooropen.mp3")
                        pygame.mixer.music.play(1)
                        pygame.time.delay(1500)  # 연속 클릭 방지
                        use_record = 1  # 레코드 사용
                        moonopen = 1
                        pygame.mixer.music.load("record_music.mp3")
                        pygame.mixer.music.play(1)
                        img.change_img(final1p, startpoint)
                        doll2.set_alpha(255)
                        nodoll = 1
                        control = 0  # 밑에 코드에서 레코드를 인벤에서 뻬기 위해


            ################################## doll 테두리 생겼을 시 or 확대 시 # (이승민 05/26 01:00 추가)
            # if doll.m_state == 1:  # doll 클릭한 경우
            #     if not get_doll:  # doll 얻지 않았을 때
            #         if x.m_x <= mousePosition[0] <= x.m_x + x.m_size_x:
            #             if x.m_y <= mousePosition[1] <= x.m_y + x.m_size_y:
            #                 x.set_alpha(0)  # x 버튼 투명화
            #                 if object1.count(doll):  # 리스트에 doll가 있으면
            #                     object1.remove(doll)  # doll를 삭제해줌(인벤에 들어가기 때문에 1번화면에 출력하면 안됨)
            #                 small_blackbg.set_alpha(0)  # 화면 투명도를 원래대로
            #                 doll.clicked()
            #                 pygame.mixer.music.load("laugh_doll.mp3")
            #                 pygame.mixer.music.play(1)
            #                 get_doll = 1  # 인형을 얻음
            #                 control = 1  # 다시 아무거나 클릭할 수 있게 돌아감
            #     if doll_glow == 1:  # doll 빛날 때
            #         if doll.m_x <= mousePosition[0] <= doll.m_x + doll.m_size_x:
            #             if doll.m_y <= mousePosition[1] <= doll.m_y + doll.m_size_y:
            #                 doll.return_img(inven_doll, doll.m_location)  # 빛나지 않는 상태로 돌아감
            #                 doll.clicked()
            #                 doll_glow = 0  # 테두리 사라짐
            #                 pygame.time.delay(100)  # 연속클릭 방지
            #                 control = 1  # 다시 아무거나 클릭할 수 있게 돌아감

            ################################## ten_driver 테두리 생겼을 시 # (이승민 05/26 01:00 추가)
            if ten_driver.m_state == 1 and ten_driver_glow == 1:  # 클릭, 빛날 때
                if ten_driver.m_x <= mousePosition[0] <= ten_driver.m_x + ten_driver.m_size_x:
                    if ten_driver.m_y <= mousePosition[1] <= ten_driver.m_y + ten_driver.m_size_y:
                        ten_driver.return_img(inven_ten_driver, ten_driver.m_location)  # 빛나지 않는 상태로 돌아감
                        ten_driver.clicked()
                        ten_driver_glow = 0  # 테두리 사라짐
                        pygame.time.delay(100)  # 연속클릭 방지
                        control = 1  # 다시 아무거나 클릭할 수 있게 돌아감

            ################################## one_driver 테두리 생겼을 시 # (이승민 05/26 01:00 추가)
            if one_driver.m_state == 1 and one_driver_glow == 1:
                if one_driver.m_x <= mousePosition[0] <= one_driver.m_x + one_driver.m_size_x:
                    if one_driver.m_y <= mousePosition[1] <= one_driver.m_y + one_driver.m_size_y:
                        one_driver.return_img(inven_one_driver, one_driver.m_location)  # 빛나지 않는 상태로 돌아감
                        one_driver.clicked()
                        one_driver_glow = 0  # 테두리 사라짐
                        pygame.time.delay(100)  # 연속클릭 방지
                        control = 1  # 다시 아무거나 클릭할 수 있게 돌아감

            ################################## knife 테두리 생겼을 시 # (이승민 05/26 01:00 추가)
            if knife.m_state == 1 and knife_glow == 1:
                if knife.m_x <= mousePosition[0] <= knife.m_x + knife.m_size_x:
                    if knife.m_y <= mousePosition[1] <= knife.m_y + knife.m_size_y:
                        knife.return_img(inven_knife, knife.m_location)  # 빛나지 않는 상태로 돌아감
                        knife.clicked()
                        knife_glow = 0  # 테두리 사라짐
                        pygame.time.delay(100)  # 연속클릭 방지
                        control = 1  # 다시 아무거나 클릭할 수 있게 돌아감

            ################################## record 테두리 생겼을 시 # (이승민 5/30 14:30 추가)
            if record.m_state == 0 and record_glow == 1:
                if rp.m_x <= mousePosition[0] <= rp.m_x + rp.m_size_x:
                    if rp.m_y <= mousePosition[1] <= rp.m_y + rp.m_size_y:
                        record.return_img(inven_record, record.m_location)  # 빛나지 않는 상태로 돌아감
                        record.clicked()
                        record_glow = 0  # 테두리 사라짐
                        pygame.time.delay(100)  # 연속클릭 방지
                        control = 1  # 다시 아무거나 클릭할 수 있게 돌아감

            ################################## key 테두리 생겼을 시 # (이승민 5/30 14:30 추가)
            if key.m_state == 1 and key_glow == 1:
                if key.m_x <= mousePosition[0] <= key.m_x + key.m_size_x:
                    if key.m_y <= mousePosition[1] <= key.m_y + key.m_size_y:
                        key.return_img(inven_key, key.m_location)  # 빛나지 않는 상태로 돌아감
                        key.clicked()
                        key_glow = 0  # 테두리 사라짐
                        pygame.time.delay(100)  # 연속클릭 방지
                        control = 1  # 다시 아무거나 클릭할 수 있게 ㅂ돌아감

            ################################
            # 문위치 다시 누를 때
            if MOON.m_state == 1:
                if textbox.m_x <= mousePosition[0] <= textbox.m_x+textbox.m_size_x:
                    if textbox.m_y <= mousePosition[1] <= textbox.m_y+textbox.m_size_y:
                        if MOONcheck == 0:
                            textbox.change_img(textbox_p4, (70, 450))
                            MOON.clicked()
                            control = 1
                            control2 = 0
                            pygame.time.delay(100)
                            MOONcheck = 1

            # 마네킹 다시 누를 때
            if mannequin.m_state == 1:
                if textbox.m_x < mousePosition[0] < textbox.m_x + textbox.m_size_x:
                    if textbox.m_y < mousePosition[1] < textbox.m_y + textbox.m_size_y:
                        textbox.set_alpha(0)
                        mannequin.clicked()
                        control = 1
                        pygame.time.delay(100)
                        mqcheck = 1
            ################################## 무서운방 인형 클릭시
            if 545 <= mousePosition[0] <= 675:
                if 515 <= mousePosition[1] <= 690:
                    if dolldoll == 0 and noroom == 300:
                        img.change_img(img_scary2, startpoint)
                        dolldoll = 1
                        control = 1
                        control2 = 1
                        pygame.time.delay(100)

            ################################## 화분 확대 시 (05/25 17:23 추가)
            if pot.m_state == 1:
                if x.m_x < mousePosition[0] < x.m_x + x.m_size_x:
                    if x.m_y < mousePosition[1] < x.m_y + x.m_size_y:  # x 버튼 클릭시
                        if dial_scary < 0:
                            x.set_alpha(0)  # x 버튼 투명화
                            pot.return_img(pot_p2, (525, 585))  # 이미지파일 원래대로
                            small_blackbg.set_alpha(0)  # 화면 투명도를 원래대로
                            pot.clicked()  # m_state = 0
                            textbox.set_alpha(0)
                            control = 1
                        else:
                            x.set_alpha(0)  # x 버튼 투명화
                            pot.return_img(pot_p1, pot.m_firstlocation)  # 이미지파일 원래대로
                            small_blackbg.set_alpha(0)  # 화면 투명도를 원래대로
                            pot.clicked()  # m_state = 0
                            textbox.set_alpha(0)
                            control = 1

            ################################## 책 확대 시 (05/25 17:52 추가)
            if books.m_state == 1:
                if 410 < mousePosition[0] < 726:
                    if 142 < mousePosition[1] < 597:  # 책클릭 시
                        books.change_img(books_p3, (320, 150))

                if x.m_x < mousePosition[0] < x.m_x + x.m_size_x:
                    if x.m_y < mousePosition[1] < x.m_y + x.m_size_y:  # x 버튼 클릭시
                        x.set_alpha(0)  # x 버튼 투명화
                        books.return_img(books_p1, books.m_firstlocation)  # 이미지파일 원래대로
                        small_blackbg.set_alpha(0)  # 화면 투명도를 원래대로
                        books.clicked()  # m_state = 0
                        control = 1

            ################################## 공구상자 확대 시 (05/25 18:03 추가)
            if toolbox.m_state == 1:
                if 340 < mousePosition[0] < toolbox_p2.get_width() + 340:
                    if 170 < mousePosition[1] < toolbox_p2.get_height() + 170:
                        if get_key == 1 or get_key == 2:
                            textbox.set_alpha(0)
                            #### 열쇠로 공구상자를 열 수 있을 것 같다 (스크립트 추가) ####
                            if open_toolbox == 0:
                                toolbox.change_img(toolbox_p2, toolbox.m_location)
                                open_toolbox = 1
                                use_key = 1
                                pygame.time.delay(500)

                            elif open_toolbox == 1 and get_key == 2:
                                get_key = 3
                                get_knife, get_ten_driver = 1, 1
                                pygame.mixer.music.load("item_get.mp3")
                                pygame.mixer.music.play(1)
                                toolbox.change_img(empty_toolbox, (340, 170))

                if x.m_x < mousePosition[0] < x.m_x + x.m_size_x:
                    if x.m_y < mousePosition[1] < x.m_y + x.m_size_y:  # x 버튼 클릭시
                        x.set_alpha(0)  # x 버튼 투명화
                        if open_toolbox == 0:
                            toolbox.return_img(toolbox_p1, (137, 474))  # 이미지파일 원래대로
                        if open_toolbox == 1:
                            toolbox.return_img(toolbox2_p1, (137, 474))
                        textbox.set_alpha(0)
                        small_blackbg.set_alpha(0)  # 화면 투명도를 원래대로
                        toolbox.clicked()  # m_state = 0
                        control = 1

            ################################## 트로피 확대 시 (05/25 18:09 추가)
            if trophy.m_state == 1:
                if x.m_x < mousePosition[0] < x.m_x + x.m_size_x:
                    if x.m_y < mousePosition[1] < x.m_y + x.m_size_y:  # x 버튼 클릭시
                        x.set_alpha(0)  # x 버튼 투명화
                        trophy.return_img(trophy_p1, trophy.m_firstlocation)  # 이미지파일 원래대로
                        small_blackbg.set_alpha(0)  # 화면 투명도를 원래대로
                        trophy.clicked()  # m_state = 0
                        control = 1

            ################################## 나무액자 확대 시 (05/30 16:51 추가)
            if photoframe.m_state == 1:
                if x.m_x < mousePosition[0] < x.m_x + x.m_size_x:
                    if x.m_y < mousePosition[1] < x.m_y + x.m_size_y:  # x 버튼 클릭시
                        x.set_alpha(0)  # x 버튼 투명화
                        if open_photo == 0:
                            photoframe.return_img(photoframe_p1, photoframe.m_firstlocation)  # 확대된 트로피
                        if open_photo == 1:
                            photoframe.return_img(photoframe_p2, photoframe.m_firstlocation)
                        small_blackbg.set_alpha(0)  # 화면 투명도를 원래대로
                        photoframe.clicked()  # m_state = 0
                        textbox.set_alpha(0)
                        control = 1

                if 480 < mousePosition[0] < 800.5:
                    if 30 < mousePosition[1] < 538.5:
                        if get_ten_driver == 1:
                            if open_photo == 0:
                                textbox.set_alpha(0)
                                photoframe.change_img(photoframe2_big, photoframe.m_location)
                                open_photo = 1
                                pygame.mixer.music.load("driver_use.mp3")
                                pygame.mixer.music.play(1)
                                #### 드라이버로 액자를 열 수 있을 것 같다 (스크립트 추가) ####

            ################################## 철제 액자 확대 시 (05/30 16:51 추가)
            if steelframe.m_state == 1:
                if x.m_x < mousePosition[0] < x.m_x + x.m_size_x:
                    if x.m_y < mousePosition[1] < x.m_y + x.m_size_y:  # x 버튼 클릭시
                        x.set_alpha(0)  # x 버튼 투명화
                        steelframe.return_img(steelframe_p1, steelframe.m_firstlocation)  # 이미지파일 원래대로
                        small_blackbg.set_alpha(0)  # 화면 투명도를 원래대로
                        steelframe.clicked()  # m_state = 0
                        control = 1

            ################################## 곰인형 확대 시 (05/25 19:57 추가)
            if bear.m_state == 1:
                if x.m_x < mousePosition[0] < x.m_x + x.m_size_x:
                    if x.m_y < mousePosition[1] < x.m_y + x.m_size_y:  # x 버튼 클릭시
                        x.set_alpha(0)  # x 버튼 투명화
                        if bear_cut == 0:
                            bear.return_img(bear_p1, bear.m_firstlocation)  # 이미지파일 원래대로
                        if bear_cut == 1:
                            bear.return_img(bear_p2, bear.m_firstlocation)  # 이미지파일 원래대로
                        if bear_cut == 2:
                            bear.return_img(bear_p3, bear.m_firstlocation)
                        small_blackbg.set_alpha(0)  # 화면 투명도를 원래대로
                        bear.clicked()  # m_state = 0
                        textbox.set_alpha(0)
                        control = 1

                # 거대해진 곰 클릭 시 / 칼을 가지고 있다면
                if 441 < mousePosition[0] < 917:
                    if 128 < mousePosition[1] < 663:
                        if get_knife == 1:
                            textbox.set_alpha(0)
                            bear.change_img(bear_big2, (400, 95))  # 상처난 곰으로 바뀜
                            bear_cut = 1
                            get_knife = 2
                            control = 1
                            control2 = 0
                            pygame.mixer.music.load("bear_cut.mp3")
                            pygame.mixer.music.play(1)
                            pygame.time.delay(400)

                ################################## 장난감집 확대 시 (05/25 20:08 추가)
            if house.m_state == 1:
                if x.m_x < mousePosition[0] < x.m_x + x.m_size_x:
                    if x.m_y < mousePosition[1] < x.m_y + x.m_size_y:  # x 버튼 클릭시
                        x.set_alpha(0)  # x 버튼 투명화
                        if house_door_open == 0:
                            textbox.set_alpha(0)
                            house.return_img(house_p1, house.m_firstlocation)  # 이미지파일 원래대로
                        if house_door_open == 1:
                            house.return_img(house_open, (450, 330))  # 이미지파일 원래대로
                            pygame.time.delay(100)
                        if safe_out == 1:
                            house.return_img(house_p3, (450, 330))
                        small_blackbg.set_alpha(0)  # 화면 투명도를 원래대로
                        house.clicked()  # m_state = 0
                        textbox.set_alpha(0)
                        control = 1

                if 695 < mousePosition[0] < 762:
                    if 323 < mousePosition[1] < 439:
                        if house_door_open == 1:
                            control = 0
                            house.change_img(house_big3, (400, 152))
                            safe.set_alpha(255)
                            safe_out = 1

            #################################### 침대 확대 시 (05/25 20:08 추가)
            if bed.m_state == 1:
                # 애기 가지고 있을 때 커진 침대 누르면
                if 466 < mousePosition[0] < 939:
                    if 294 < mousePosition[1] < 589:
                        if get_doll == 1 and baby_in_bed == 0:
                            textbox.set_alpha(0)
                            baby_in_bed = 1
                            use_doll = 1
                            bed.change_img(bed_baby_big, (400, 250))  # 애기있는 침대로 바뀜

                # x 누를 때
                if x.m_x < mousePosition[0] < x.m_x + x.m_size_x:
                    if x.m_y < mousePosition[1] < x.m_y + x.m_size_y:  # x 버튼 클릭시
                        x.set_alpha(0)  # x 버튼 투명화
                        if baby_in_bed == 0:
                            bed.return_img(bed_p1, bed.m_firstlocation)  # 이미지파일 원래대로
                        if baby_in_bed == 1:
                            bed.return_img(bed_baby, bed.m_firstlocation)  # 이미지파일 원래대로

                        small_blackbg.set_alpha(0)  # 화면 투명도를 원래대로
                        bed.clicked()  # m_state = 0
                        textbox.set_alpha(0)
                        control = 1

            ################################## 금고 확대 시 ##############################
            if safe.m_state == 1:
                if x.m_x < mousePosition[0] < x.m_x + x.m_size_x:
                    if x.m_y < mousePosition[1] < x.m_y + x.m_size_y:  # x 버튼 클릭시
                        ###################### 성공 후 드라이버 안먹은 상태 ##############
                        if dial_success == 1:
                            if get_one_driver == 0:
                                x.set_alpha(0)  # x 버튼 투명화
                                safe.return_img(safe_p2, safe.m_firstlocation)  # 이미지파일 원래대로

                                small_blackbg.set_alpha(0)  # 화면 투명도를 원래대로
                                safe.clicked()  # m_state = 0
                                if dial.m_state == 1:
                                    dial.clicked()  # 금고 클릭 때 상태를
                                    dial.set_alpha(0)
                                control = 1
                                control3 = 1

                            ######################### 드라이버 먹었을 시#########3
                            if get_one_driver == 1:
                                x.set_alpha(0)  # x 버튼 투명화
                                safe.return_img(safe_p3, safe.m_firstlocation)  # 이미지파일 원래대로

                                small_blackbg.set_alpha(0)  # 화면 투명도를 원래대로
                                safe.clicked()  # m_state = 0
                                if dial.m_state == 1:
                                    dial.clicked()  # 금고 클릭 때 상태를
                                    dial.set_alpha(0)
                                control = 1
                                control3 = 1

                        else:
                            x.set_alpha(0)  # x 버튼 투명화
                            safe.return_img(safe_p1, safe.m_firstlocation)  # 이미지파일 원래대로

                            small_blackbg.set_alpha(0)  # 화면 투명도를 원래대로
                            safe.clicked()  # m_state = 0
                            if dial.m_state == 1:
                                dial.clicked()  # 금고 클릭 때 상태를
                                dial.set_alpha(0)
                            control = 1
                            control3 = 1

                # 금고 확대 후 다이얼 클릭
                if 642 < mousePosition[0] < 671:
                    if 313 < mousePosition[1] < 345:
                        if control3 == 1 and dial_success == 0:
                            safe.set_alpha(0)  # 금고 투명화
                            dial.set_alpha(255)
                            dial.clicked()
                            control3 = 0

                # 일자 드라이버 얻고 나서 금고 클릭 시 비어있는 금고 확대
                if 540 < mousePosition[0] < 607:
                    if 287 < mousePosition[1] < 457:
                        if dial_success == 1:
                            get_one_driver = 1
                            pygame.mixer.music.load("item_get.mp3")
                            pygame.mixer.music.play(1)
                            ################# 인벤토리에 일자 드라이버 들어가야함
                            safe.change_img(safe3_big, (460, 110))

            ############################## 베토벤 확대 시 ###################################
            if frame1.m_state == 1:
                if x.m_x < mousePosition[0] < x.m_x + x.m_size_x:
                    if x.m_y < mousePosition[1] < x.m_y + x.m_size_y:  # x 버튼 클릭시
                        x.set_alpha(0)  # x 버튼 투명화
                        frame1.return_img(frame1_p1, frame1.m_firstlocation)  # 이미지파일 원래대로
                        small_blackbg.set_alpha(0)  # 화면 투명도를 원래대로
                        frame1.clicked()  # m_state = 0
                        control = 1

            ############################## 바흐 확대 시 ###################################
            if frame2.m_state == 1:
                if x.m_x < mousePosition[0] < x.m_x + x.m_size_x:
                    if x.m_y < mousePosition[1] < x.m_y + x.m_size_y:  # x 버튼 클릭시
                        x.set_alpha(0)  # x 버튼 투명화
                        frame2.return_img(frame2_p1, frame2.m_firstlocation)  # 이미지파일 원래대로
                        small_blackbg.set_alpha(0)  # 화면 투명도를 원래대로
                        frame2.clicked()  # m_state = 0
                        control = 1

            ############################## 모차르트 확대 시 ###################################
            if frame3.m_state == 1:  # 베토벤 액자 확대 시
                if x.m_x < mousePosition[0] < x.m_x + x.m_size_x:
                    if x.m_y < mousePosition[1] < x.m_y + x.m_size_y:  # x 버튼 클릭시
                        x.set_alpha(0)  # x 버튼 투명화
                        frame3.return_img(frame3_p1, frame3.m_firstlocation)  # 이미지파일 원래대로
                        small_blackbg.set_alpha(0)  # 화면 투명도를 원래대로
                        frame3.clicked()  # m_state = 0
                        control = 1

            ############################## 슈베르트 확대 시 ###################################
            if frame4.m_state == 1:
                if x.m_x < mousePosition[0] < x.m_x + x.m_size_x:
                    if x.m_y < mousePosition[1] < x.m_y + x.m_size_y:  # x 버튼 클릭시
                        x.set_alpha(0)  # x 버튼 투명화
                        frame4.return_img(frame4_p1, frame4.m_firstlocation)  # 이미지파일 원래대로
                        small_blackbg.set_alpha(0)  # 화면 투명도를 원래대로
                        frame4.clicked()  # m_state = 0
                        control = 1

            ############################## 레코드 플레이어 확대 시 ###################################
            if rp.m_state == 1 and not record_glow:
                if x.m_x < mousePosition[0] < x.m_x + x.m_size_x:
                    if x.m_y < mousePosition[1] < x.m_y + x.m_size_y:  # x 버튼 클릭시
                        x.set_alpha(0)  # x 버튼 투명화
                        rp.return_img(rp_p1, rp.m_firstlocation)  # 이미지파일 원래대로
                        small_blackbg.set_alpha(0)  # 화면 투명도를 원래대로
                        rp.clicked()  # m_state = 0
                        textbox.set_alpha(0)
                        control = 1

            ############################## 의자 확대 시 ###################################
            if chair.m_state == 1:
                # 드라이버 없이 눌렀을 때
                if 410 < mousePosition[0] < 747:
                    if 212 < mousePosition[1] < 519:
                        if get_record == 0 and get_one_driver == 0 and open_chair == 0:
                            textbox.set_alpha(0)
                            chair.change_img(chair_p2, (370, 100))
                            textbox.set_alpha(0)
                            pygame.time.delay(300)
                # 드라이버 가지고 눌렀을 때
                if 410 < mousePosition[0] < 747:
                    if 212 < mousePosition[1] < 519:
                        if get_record == 0 and get_one_driver == 1 and open_chair == 0:
                            textbox.set_alpha(0)
                            chair.change_img(chair_p2, (370, 100))
                            pygame.time.delay(300)
                            textbox.set_alpha(0)
                            open_chair = 1
                            control2 = 0
                            control = 1


                # 의자 열고 누를 때
                if 410 < mousePosition[0] < 747:
                    if 212 < mousePosition[1] < 519:
                        if ready_get_record == 1 and get_record == 0 and get_one_driver == 1 and open_chair == 1:
                            textbox.set_alpha(0)
                            chair.change_img(chair_p4, (370, 100))
                            pygame.time.delay(300)
                            get_record = 1
                            pygame.mixer.music.load("item_get.mp3")
                            pygame.mixer.music.play(1)
                # 레코드 얻고 난 이후
                if 410 < mousePosition[0] < 747:
                    if 212 < mousePosition[1] < 519:
                        if ready_get_record == 1 and get_record == 1 and get_one_driver == 1 and open_chair == 1:
                            textbox.set_alpha(0)
                            pygame.time.delay(300)
                            chair.change_img(chair_p4, (370, 100))

                if x.m_x < mousePosition[0] < x.m_x + x.m_size_x:
                    if x.m_y < mousePosition[1] < x.m_y + x.m_size_y:  # x 버튼 클릭시
                        x.set_alpha(0)  # x 버튼 투명화
                        chair.return_img(chair_p1, chair.m_firstlocation)  # 이미지파일 원래대로
                        small_blackbg.set_alpha(0)  # 화면 투명도를 원래대로
                        chair.clicked()  # m_state = 0
                        control = 1
                        textbox.set_alpha(0)

            ############################## 마트료시카 확대 시 ################################### (이승민 05/30 14:30 추가)
            if Matryoshka.m_state == 1:  # 마트료시카만 밝게 보일 때
                if x.m_x < mousePosition[0] < x.m_x + x.m_size_x:
                    if x.m_y < mousePosition[1] < x.m_y + x.m_size_y:  # x 버튼 클릭시
                        Matryoshka_count = 0  # 다시 마트료시카 안 깐 상태로 돌아감
                        # 다시 마트료시카 안 깐 상태로 투명도 조절
                        Matryoshka_head1.set_alpha(0)
                        Matryoshka_head2.set_alpha(0)
                        Matryoshka_head3.set_alpha(0)
                        x.set_alpha(0)  # x 버튼 투명화
                        small_blackbg.set_alpha(0)  # 화면 투명도를 원래대로
                        Matryoshka.return_img(Matryoshka.m_firstimg, Matryoshka.m_firstlocation)  # 확대 전 이미지
                        Matryoshka.change_img_scale(Matryoshka.m_firstsize)  # 다시 확대 전 사이즈로 돌아감
                        Matryoshka.clicked()  # m_state = 0
                        control = 1  # 다시 마트료시카 확대 전 상태로 돌아감
                if Matryoshka.m_x - 100 < mousePosition[0] < Matryoshka.m_x + Matryoshka.m_size_x + 200:
                    if Matryoshka.m_y - 100 < mousePosition[1] < Matryoshka.m_y + Matryoshka.m_size_y + 100:
                        if Matryoshka_count == 0:  # 마트료시카 한번도 안깠을 때
                            Matryoshka_head1.set_alpha(255)  # 첫번째 뚜껑 보이게
                            Matryoshka.change_img(Matryoshka_p2, Matryoshka.m_location)  # 마트료시카 한번 깐 사진
                        elif Matryoshka_count == 1:  # 마트료시카 한번 깠을 때
                            Matryoshka_head2.set_alpha(255)  # 두번째 뚜껑 보이게
                            Matryoshka.change_img_scale(
                                (58.19, 363.125))  # 마트료시카 크기 바꿔줌
                            Matryoshka.change_img(Matryoshka_p3, (
                                Matryoshka.m_location))  # 마트료시카 두번 깐 사진
                        elif Matryoshka_count == 2:  # 마트료시카 두번 깠을 때
                            Matryoshka_head3.set_alpha(255)  # 마지막 뚜껑 보이게
                            Matryoshka.change_img_scale(
                                (58.19, 363.725))  # 마트료시카 크기 바꿔줌
                            Matryoshka.change_img(Matryoshka_p4, (
                                230, 332.275))  # 마트료시카 다 깐 사진
                        Matryoshka_count += 1  # 마트료시카 사진 넘어가는 카운트
                        control = 0  # 바로 다음 이미지로 넘어가게 함
                        pygame.time.delay(400)  # 연속클릭 방지

            ######################### 거울 확대 시 ########################## (이승민 05/25 18:19 추가)
            if mirror.m_state == 1:
                if x.m_x < mousePosition[0] < x.m_x + x.m_size_x:
                    if x.m_y < mousePosition[1] < x.m_y + x.m_size_y:  # x 버튼 클릭시
                        x.set_alpha(0)  # x 버튼 투명화
                        mirror.return_img(mirror_p1, mirror.m_firstlocation)  # 이미지파일 원래대로
                        small_blackbg.set_alpha(0)  # 화면 투명도를 원래대로
                        mirror.clicked()  # m_state = 0
                        control = 1

            ######################### 옷장 확대 시 ########################## (이승민 05/25 18:19 추가)
            if closet.m_state == 1:
                #################################### 도어락 누를 때 ############################
                if 641 < mousePosition[0] < 700:
                    if 356 < mousePosition[1] < 427:
                        if success_doorlock == 0:
                            control2 = 0
                            control = 1
                            doorlock.set_alpha(255)
                            doorlock.clicked()

                #################################### 열쇠 누를 때 ####################################
                if 625 < mousePosition[0] < 678:
                    if 450 < mousePosition[1] < 480:
                        if success_doorlock == 1 or 2:
                            get_key = 1
                            pygame.mixer.music.load("item_get.mp3")
                            pygame.mixer.music.play(1)
                            closet.change_img(open_closet_p2, (360, 105))
                            success_doorlock = 3

                if x.m_x < mousePosition[0] < x.m_x + x.m_size_x:
                    if x.m_y < mousePosition[1] < x.m_y + x.m_size_y:  # x 버튼 클릭시
                        if success_doorlock == 0:
                            closet.return_img(closet_p1, closet.m_firstlocation)  # 이미지파일 원래대로
                        if success_doorlock == 1:
                            closet.change_img(open_closet_p1, (640, 144))
                            success_doorlock = 2  # 바뀐 옷장 영원히 유지 !!!!!!!!!!!!!!!!!!!!!!!!
                        if success_doorlock == 2:
                            closet.change_img(open_closet_p1, (640, 144))
                        if success_doorlock == 3:
                            closet.change_img(open_closet_p2, (640, 144))

                        x.set_alpha(0)  # x 버튼 투명화
                        small_blackbg.set_alpha(0)  # 화면 투명도를 원래대로
                        closet.clicked()  # m_state = 0
                        control = 1

            # if get_Matryoshka:
            #     if textbox.m_x < mousePosition[0] < textbox.m_x + textbox.m_size_x:
            #         if textbox.m_y < mousePosition[1] < textbox.m_y + textbox.m_size_y:
            #             textbox.change_img(textbox2, textbox.m_firstlocation)

    ############################## 배경 출력 ####################################################
    ############################################################################################
    ############################## 1번 화면 #####################################################
    if count == 1:
        if leftright == -1:  # 1번 화면이고 왼쪽 화살표 클릭시
            if countframe == 1:  # countframe 0이면
                if noroom == 300:  # 빈방 출력 fade 느리게
                    fade_out2(1140, 720, img2.m_img, object2)
                    fade_in2(1140, 720, img.m_img, object1)
                else:
                    fade_out(1140, 720, img2.m_img, object2)
                    fade_in(1140, 720, img.m_img, object1)
                leftright = 0
        elif leftright == 1:  # 오른쪽 화살표로 4번방->1번방 올 시
            if countframe == 1:  # countframe 1이면
                if dial_scary < 0:  #### 노크 소리후 다시 1번 방문 시
                    pot.change_img(pot_p2, (525, 585))

                fade_out(1140, 720, img4.m_img, object4)
                fade_in(1140, 720, img.m_img, object1)
                leftright = 0
        screen.blit(img.m_img, startpoint)
        screen.blit(arrow_left.m_img, arrow_left.m_location)  # 왼쪽화살표 출력
        screen.blit(arrow_right.m_img, arrow_right.m_location)  # 오른쪽화살표 출력

        for obj in object1:
            if obj.m_state == 0:
                screen.blit(obj.m_img, obj.m_location)
        screen.blit(small_blackbg, (0, 0))
        screen.blit(Matryoshka_head1, (450, 360-125))
        screen.blit(Matryoshka_head2, (635, 360 - 100))
        screen.blit(Matryoshka_head3, (800, 360 - 75))
        for obj in object1:
            if obj.m_state == 1:
                screen.blit(obj.m_img, obj.m_location)

        screen.blit(noise, startpoint)
        screen.blit(textbox.m_img, textbox.m_location)
        screen.blit(x.m_img, x.m_location)
        countframe = 0  # 무한반복 방지용

    ############################## 2번 화면 #####################################################
    elif count == 2:  # 2번 화면
        if leftright == -1:
            if countframe == 1:
                fade_out(1140, 720, img3.m_img, object3)
                fade_in(1140, 720, img2.m_img, object2)
                leftright = 0
        elif leftright == 1:
            if countframe == 1:
                fade_out(1140, 720, img.m_img, object1)
                fade_in(1140, 720, img2.m_img, object2)
                leftright = 0
        screen.blit(img2.m_img, startpoint)

        for obj in object2:
            if obj.m_state == 0:
                screen.blit(obj.m_img, obj.m_location)

        screen.blit(arrow_left.m_img, arrow_left.m_location)
        screen.blit(arrow_right.m_img, arrow_right.m_location)
        screen.blit(small_blackbg, (0, 0))

        for obj in object2:
            if obj.m_state == 1:
                screen.blit(obj.m_img, obj.m_location)
        screen.blit(textbox.m_img, textbox.m_location)
        screen.blit(x.m_img, x.m_location)

        for obj in slist:
            screen.blit(obj.m_img, obj.m_location)
        countframe = 0

    ############################## 3번 화면 #####################################################
    elif count == 3:  # 3번 화면
        if leftright == -1:
            if countframe == 1:
                fade_out(1140, 720, img4.m_img, object4)
                fade_in(1140, 720, img3.m_img, object3)
                leftright = 0
        elif leftright == 1:
            if countframe == 1:
                fade_out(1140, 720, img2.m_img, object2)
                fade_in(1140, 720, img3.m_img, object3)
                leftright = 0

        screen.blit(img3.m_img, startpoint)
        screen.blit(arrow_left.m_img, arrow_left.m_location)
        screen.blit(arrow_right.m_img, arrow_right.m_location)
        for obj in object3:
            if obj.m_state == 0:
                screen.blit(obj.m_img, obj.m_location)
        screen.blit(small_blackbg, (0, 0))
        for obj in object3:
            if obj.m_state == 1:
                screen.blit(obj.m_img, obj.m_location)
        screen.blit(textbox.m_img, textbox.m_location)
        screen.blit(x.m_img, x.m_location)
        countframe = 0

    ############################## 4번 화면 #####################################################
    elif count == 4:
        if leftright == -1:
            if countframe == 1:
                fade_out(1140, 720, img.m_img, object1)
                fade_in(1140, 720, img4.m_img, object4)
                leftright = 0
        elif leftright == 1:
            if countframe == 1:
                if dial_scary >= 1:  #### 노크 소리후 다시 1번 방문 시
                    pygame.mixer.music.load("knockknock.mp3")
                    pygame.mixer.music.play(1)
                    fade_out(1140, 720, img3.m_img, object3)
                    dial_scary = -100000
                    pygame.time.delay(700)
                    fade_in(1140, 720, img4.m_img, object4)
                    pygame.mixer.music.load("pot_break.mp3")
                    pygame.mixer.music.play(1)
                else:
                    fade_out(1140, 720, img3.m_img, object3)
                    fade_in(1140, 720, img4.m_img, object4)
                leftright = 0
        screen.blit(img4.m_img, startpoint)
        screen.blit(arrow_left.m_img, arrow_left.m_location)
        screen.blit(arrow_right.m_img, arrow_right.m_location)
        for obj in object4:
            if obj.m_state == 0:
                screen.blit(obj.m_img, obj.m_location)
        screen.blit(small_blackbg, (0, 0))
        for obj in object4:
            if obj.m_state == 1:
                screen.blit(obj.m_img, obj.m_location)
        screen.blit(textbox.m_img, textbox.m_location)
        screen.blit(x.m_img, x.m_location)
        countframe = 0

    ######################## 객체를 얻은 상태에서 프랑스 인형의 위치를 설정해줌 ###################### # (이승민 5/26 01:00 추가)
    if get_doll == 1 and not inven_doll_location:
        # 프랑스 인형을 얻은 상태에서 인벤위치가 결정되지 않았을 때
        for idx, exist in enumerate(spot_count, 0):  # idx: 0->1->2... exist: spot_count값 차례대로 가져옴
            if not exist:  # 인벤의 여유 공간이 있을 때
                inven_doll_location = spot_location[idx]  # 프랑스 인형의 위치를 그 공간으로 설정
                spot_count[idx] = 1  # 그 공간은 이제 프랑스 인형으로 채워짐
                break
        doll.change_img(inven_doll, inven_doll_location)  # 인벤 이미지로 바꾸고 인벤 위치로 바꿔줌
        doll.change_img_scale(spot_size)  # 인벤 이미지 크기에 맞게 객체 크기도 바꿔줌 -> 클릭 범위 변경
    if inven_doll_location and not use_doll:  # 프랑스 인형이 인벤에 있으면(인벤 위치가 결정되어 있으면)
        screen.blit(doll.m_img, doll.m_location)  # 화면에 띄워줌

    ######################## 객체를 얻은 상태에서 ten_driver의 위치를 설정해줌 ###################### # (이승민 5/28 18:30 추가)
    if get_ten_driver == 1 and not inven_ten_driver_location:
        # ten_driver를 얻은 상태에서 인벤위치가 결정되지 않았을 때
        for idx, exist in enumerate(spot_count, 0):  # idx: 0->1->2... exist: spot_count값 차례대로 가져옴
            if not exist:  # 인벤의 여유 공간이 있을 때
                inven_ten_driver_location = spot_location[idx]  # ten_driver의 위치를 그 공간으로 설정
                spot_count[idx] = 1  # 그 공간은 이제 ten_driver로 채워짐
                break
        ten_driver.change_img(inven_ten_driver, inven_ten_driver_location)  # 인벤 이미지로 바꾸고 인벤 위치로 바꿔줌
    if inven_ten_driver_location and not use_ten_driver:  # ten_driver가 인벤에 있으면(인벤 위치가 결정되어 있으면)
        screen.blit(ten_driver.m_img, ten_driver.m_location)  # 화면에 띄워줌

    ######################## 객체를 얻은 상태에서 one_driver의 위치를 설정해줌 ###################### # (이승민 5/28 18:30 추가)
    if get_one_driver == 1 and not inven_one_driver_location:
        # one_driver를 얻은 상태에서 인벤위치가 결정되지 않았을 때
        for idx, exist in enumerate(spot_count, 0):  # idx: 0->1->2... exist: spot_count값 차례대로 가져옴
            if not exist:  # 인벤의 여유 공간이 있을 때
                inven_one_driver_location = spot_location[idx]  # one_driver의 위치를 그 공간으로 설정
                spot_count[idx] = 1  # 그 공간은 이제 one_driver로 채워짐
                break
        one_driver.change_img(inven_one_driver, inven_one_driver_location)  # 인벤 이미지로 바꾸고 인벤 위치로 바꿔줌
    if inven_one_driver_location and not use_one_driver:  # one_driver가 인벤에 있으면(인벤 위치가 결정되어 있으면)
        screen.blit(one_driver.m_img, one_driver.m_location)  # 화면에 띄워줌

    ######################## 객체를 얻은 상태에서 knife의 위치를 설정해줌 ###################### # (이승민 5/28 18:30 추가)
    if get_knife == 1 and not inven_knife_location:
        # knife를 얻은 상태에서 인벤위치가 결정되지 않았을 때
        for idx, exist in enumerate(spot_count, 0):  # idx: 0->1->2... exist: spot_count값 차례대로 가져옴
            if not exist:  # 인벤의 여유 공간이 있을 때
                inven_knife_location = spot_location[idx]  # knife의 위치를 그 공간으로 설정
                spot_count[idx] = 1  # 그 공간은 이제 knife로 채워짐
                break
        knife.change_img(inven_knife, inven_knife_location)  # 인벤 이미지로 바꾸고 인벤 위치로 바꿔줌
    if inven_knife_location and not use_knife:  # knife가 인벤에 있으면(인벤 위치가 결정되어 있으면)
        screen.blit(knife.m_img, knife.m_location)  # 화면에 띄워줌

    ######################## 객체를 얻은 상태에서 record의 위치를 설정해줌 ###################### # (이승민 5/30 14:30 추가)
    if get_record == 1 and not inven_record_location:
        # record를 얻은 상태에서 인벤위치가 결정되지 않았을 때
        for idx, exist in enumerate(spot_count, 0):  # idx: 0->1->2... exist: spot_count값 차례대로 가져옴
            if not exist:  # 인벤의 여유 공간이 있을 때
                inven_record_location = spot_location[idx]  # record의 위치를 그 공간으로 설정
                spot_count[idx] = 1  # 그 공간은 이제 record로 채워짐
                break
        record.change_img(inven_record, inven_record_location)  # 인벤 이미지로 바꾸고 인벤 위치로 바꿔줌
    if inven_record_location and not use_record:  # record가 인벤에 있으면(인벤 위치가 결정되어 있으면)
        screen.blit(record.m_img, record.m_location)  # 화면에 띄워줌

    ######################## 객체를 얻은 상태에서 key의 위치를 설정해줌 ###################### # (이승민 5/30 14:30 추가)
    if get_key == 1 and not inven_key_location:
        # key를 얻은 상태에서 인벤위치가 결정되지 않았을 때
        for idx, exist in enumerate(spot_count, 0):  # idx: 0->1->2... exist: spot_count값 차례대로 가져옴
            if not exist:  # 인벤의 여유 공간이 있을 때
                inven_key_location = spot_location[idx]  # key의 위치를 그 공간으로 설정
                spot_count[idx] = 1  # 그 공간은 이제 key로 채워짐
                break
        key.change_img(inven_key, inven_key_location)  # 인벤 이미지로 바꾸고 인벤 위치로 바꿔줌
    if inven_key_location and not use_key:  # key가 인벤에 있으면(인벤 위치가 결정되어 있으면)
        screen.blit(key.m_img, key.m_location)  # 화면에 띄워줌

    ######################## doll를 사용한 후 인벤에서 doll 삭제 ###################### # (이승민 5/30 14:30 추가)
    if use_doll == 1:  # 사용하고 난 직후
        doll.set_alpha(0)  # 인벤 아이템을 투명하게 만듬
        for idx, exist in enumerate(spot_count, 0):  # idx: 0->1->2... exist: spot_count값 차례대로 가져옴
            if exist and spot_location[idx] == inven_doll_location:  # 인벤 아이템의 위치를 찾음
                spot_count[idx] = 0  # 그 공간은 이제 비워짐
                pygame.draw.rect(screen, (30, 30, 30), [inven_doll_location, spot_size])  # 비워있는 화면 덮어씌움
                break
        doll_glow = 0  # 사용한 후에는 빛나지 않아야 control = 1일 때 객체 클릭 가능
        get_doll = 2  # 얻은 상태와 얻고나서 얻고나서 사용도 한 상태로 나눔 -> 사용 후에는 클릭해도 사용하지 못하는 상태를 유지해야 함
        use_doll = 2  # 사용한 직후와 그 이후로 나눔 -> 이 조건문 한번만 들어오게 하기 위해
        # 상태를 3개로 나눔 0->사용전, 1->사용후, 2->사용후 조건문에 다시 들어가지 못하는 상태

    ######################## ten_driver를 사용한 후 인벤에서 ten_driver 삭제 ###################### # (이승민 5/30 14:30 추가)
    if use_ten_driver == 1:  # 사용하고 난 직후
        ten_driver.set_alpha(0)  # 인벤 아이템을 투명하게 만듬
        for idx, exist in enumerate(spot_count, 0):  # idx: 0->1->2... exist: spot_count값 차례대로 가져옴
            if exist and spot_location[idx] == inven_ten_driver_location:  # 인벤 아이템의 위치를 찾음
                spot_count[idx] = 0  # 그 공간은 이제 비워짐
                pygame.draw.rect(screen, (51, 51, 51), [inven_ten_driver_location, spot_size])  # 비워있는 화면 덮어씌움
                break
        ten_driver_glow = 0  # 사용한 후에는 빛나지 않아야 control = 1일 때 객체 클릭 가능
        get_ten_driver = 2  # 얻은 상태와 얻고나서 얻고나서 사용도 한 상태로 나눔 -> 사용 후에는 클릭해도 사용하지 못하는 상태를 유지해야 함
        use_ten_driver = 2  # 사용한 직후와 그 이후로 나눔 -> 이 조건문 한번만 들어오게 하기 위해
        # 상태를 3개로 나눔 0->사용전, 1->사용후, 2->사용후 조건문에 다시 들어가지 못하는 상태

    ######################## one_driver를 사용한 후 인벤에서 one_driver 삭제 ###################### # (이승민 5/30 14:30 추가)
    if use_one_driver == 1:  # 사용하고 난 직후
        one_driver.set_alpha(0)  # 인벤 아이템을 투명하게 만듬
        for idx, exist in enumerate(spot_count, 0):  # idx: 0->1->2... exist: spot_count값 차례대로 가져옴
            if exist and spot_location[idx] == inven_one_driver_location:  # 인벤 아이템의 위치를 찾음
                spot_count[idx] = 0  # 그 공간은 이제 비워짐
                pygame.draw.rect(screen, (30, 30, 30), [inven_one_driver_location, spot_size])  # 비워있는 화면 덮어씌움
                break
        one_driver_glow = 0  # 사용한 후에는 빛나지 않아야 control = 1일 때 객체 클릭 가능
        get_one_driver = 2  # 얻은 상태와 얻고나서 얻고나서 사용도 한 상태로 나눔 -> 사용 후에는 클릭해도 사용하지 못하는 상태를 유지해야 함
        use_one_driver = 2  # 사용한 직후와 그 이후로 나눔 -> 이 조건문 한번만 들어오게 하기 위해
        # 상태를 3개로 나눔 0->사용전, 1->사용후, 2->사용후 조건문에 다시 들어가지 못하는 상태

    ######################## knife를 사용한 후 인벤에서 knife 삭제 ###################### # (이승민 5/30 14:30 추가)
    if use_knife == 1:  # 사용하고 난 직후
        knife.set_alpha(0)  # 인벤 아이템을 투명하게 만듬
        for idx, exist in enumerate(spot_count, 0):  # idx: 0->1->2... exist: spot_count값 차례대로 가져옴
            if exist and spot_location[idx] == inven_knife_location:  # 인벤 아이템의 위치를 찾음
                spot_count[idx] = 0  # 그 공간은 이제 비워짐
                pygame.draw.rect(screen, (30, 30, 30), [inven_knife_location, spot_size])  # 비워있는 화면 덮어씌움
                break
        knife_glow = 0  # 사용한 후에는 빛나지 않아야 control = 1일 때 객체 클릭 가능
        get_knife = 2  # 얻은 상태와 얻고나서 얻고나서 사용도 한 상태로 나눔 -> 사용 후에는 클릭해도 사용하지 못하는 상태를 유지해야 함
        use_knife = 2  # 사용한 직후와 그 이후로 나눔 -> 이 조건문 한번만 들어오게 하기 위해
        # 상태를 3개로 나눔 0->사용전, 1->사용후, 2->사용후 조건문에 다시 들어가지 못하는 상태

    ######################## record를 사용한 후 인벤에서 record 삭제 ###################### # (이승민 5/30 14:30 추가)
    if use_record == 1:  # 사용하고 난 직후
        record.set_alpha(0)  # 인벤 아이템을 투명하게 만듬
        for idx, exist in enumerate(spot_count, 0):  # idx: 0->1->2... exist: spot_count값 차례대로 가져옴
            if exist and spot_location[idx] == inven_record_location:  # 인벤 아이템의 위치를 찾음
                spot_count[idx] = 0  # 그 공간은 이제 비워짐
                pygame.draw.rect(screen, (30, 30, 30), [inven_record_location, spot_size])  # 비워있는 화면 덮어씌움
                break
        record_glow = 0  # 사용한 후에는 빛나지 않아야 control = 1일 때 객체 클릭 가능
        get_record = 2  # 얻은 상태와 얻고나서 얻고나서 사용도 한 상태로 나눔 -> 사용 후에는 클릭해도 사용하지 못하는 상태를 유지해야 함
        use_record = 2  # 사용한 직후와 그 이후로 나눔 -> 이 조건문 한번만 들어오게 하기 위해
        # 상태를 3개로 나눔 0->사용전, 1->사용후, 2->사용후 조건문에 다시 들어가지 못하는 상태
        control = 1  # 레코드 사용 후 다른 객체 클릭이 가능해야 함(아이템 사용 직후 객체(ex 의자)의 확대된 사진이 유지되는 경우가 아니면 무조건 설정해야함)

    ######################## key를 사용한 후 인벤에서 key 삭제 ###################### # (이승민 5/30 14:30 추가)
    if use_key == 1:  # 사용하고 난 직후
        key.set_alpha(0)  # 인벤 아이템을 투명하게 만듬
        for idx, exist in enumerate(spot_count, 0):  # idx: 0->1->2... exist: spot_count값 차례대로 가져옴
            if exist and spot_location[idx] == inven_key_location:  # 인벤 아이템의 위치를 찾음
                spot_count[idx] = 0  # 그 공간은 이제 비워짐
                pygame.draw.rect(screen, (30, 30, 30), [inven_key_location, spot_size])  # 비워있는 화면 덮어씌움
                break
        key_glow = 0  # 사용한 후에는 빛나지 않아야 control = 1일 때 객체 클릭 가능
        get_key = 2  # 얻은 상태와 얻고나서 얻고나서 사용도 한 상태로 나눔 -> 사용 후에는 클릭해도 사용하지 못하는 상태를 유지해야 함
        use_key = 2  # 사용한 직후와 그 이후로 나눔 -> 이 조건문 한번만 들어오게 하기 위해
        # 상태를 3개로 나눔 0->사용전, 1->사용후, 2->사용후 조건문에 다시 들어가지 못하는 상태

    ############################ 키보드 이벤트 ##########################################################
    for event in pygame.event.get():  # pygame 이벤트 실행
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == KEYDOWN:  # 키 입력시
            if event.key == K_ESCAPE:
                pygame.quit()  # esc 입력시 게임 종료

            if gomain == 1:
                exec(open("gamestart.py", 'r', encoding="UTF-8").read())

            ########################## enter로 비밀번호 입력 #############################
            if event.key == K_RETURN and doorlock.m_state == 1 and len(lock_number) == 4 and control2 == 0:
                if password_doorlock == lock_number:
                    pygame.mixer.music.load("closet_open.mp3")
                    pygame.mixer.music.play(1)
                    success_doorlock = 1
                    control2 = 1
                    control = 0
                    doorlock.m_state = 0
                    doorlock.set_alpha(0)
                    for i in slist:
                        i.set_alpha(0)
                    lock_number = []
                    lock_filled = {0: 0, 1: 0, 2: 0, 3: 0}

                else:
                    pygame.mixer.music.load("doorlock_wrong.mp3")
                    pygame.mixer.music.play(1)
                    lock_number = []
                    lock_filled = {0: 0, 1: 0, 2: 0, 3: 0}
                    control2 = 1
                    control = 0
                    doorlock.m_state = 0
                    doorlock.set_alpha(0)
                    slist[0].change_img(sblack, slist[0].m_firstlocation)
                    slist[1].change_img(sblack, slist[1].m_firstlocation)
                    slist[2].change_img(sblack, slist[2].m_firstlocation)
                    slist[3].change_img(sblack, slist[3].m_firstlocation)
                    for i in slist:
                        i.set_alpha(0)
                    #slist[0].change_img(s1.m_img, slist[key_num].m_firstlocation)


            ######################################## 다이얼 클릭 시 넘버패드 #############################################
            if control3 == 0:
                dial_p2.set_alpha(255)

                if dial.m_state == 1 and event.key == K_RIGHT:
                    pygame.mixer.music.load("rotate.mp3")
                    pygame.mixer.music.play(1)
                    dial_num += 1
                    if dial_num >= 10:
                        dial_num = 0
                    if dial_num == 1:
                        dial.change_img(dial_p1, (310, 60))
                    if dial_num == 2:
                        dial.change_img(dial_p2, (310, 60))
                    if dial_num == 3:
                        dial.change_img(dial_p3, (310, 60))
                    if dial_num == 4:
                        dial.change_img(dial_p4, (310, 60))
                    if dial_num == 5:
                        dial.change_img(dial_p5, (310, 60))
                    if dial_num == 6:
                        dial.change_img(dial_p6, (310, 60))
                    if dial_num == 7:
                        dial.change_img(dial_p7, (310, 60))
                    if dial_num == 8:
                        dial.change_img(dial_p8, (310, 60))
                    if dial_num == 9:
                        dial.change_img(dial_p9, (310, 60))
                    if dial_num == 0:
                        dial.change_img(dial_p0, (310, 60))
                    break

                if dial.m_state == 1 and event.key == K_LEFT:
                    pygame.mixer.music.load("rotate.mp3")
                    pygame.mixer.music.play(1)
                    dial_num -= 1
                    if dial_num <= -1:
                        dial_num = 9
                    if dial_num == 1:
                        dial.change_img(dial_p1, (310, 60))
                    if dial_num == 2:
                        dial.change_img(dial_p2, (310, 60))
                    if dial_num == 3:
                        dial.change_img(dial_p3, (310, 60))
                    if dial_num == 4:
                        dial.change_img(dial_p4, (310, 60))
                    if dial_num == 5:
                        dial.change_img(dial_p5, (310, 60))
                    if dial_num == 6:
                        dial.change_img(dial_p6, (310, 60))
                    if dial_num == 7:
                        dial.change_img(dial_p7, (310, 60))
                    if dial_num == 8:
                        dial.change_img(dial_p8, (310, 60))
                    if dial_num == 9:
                        dial.change_img(dial_p9, (310, 60))
                    if dial_num == 0:
                        dial.change_img(dial_p0, (310, 60))
                    break

                if dial.m_state == 1 and event.key == K_RETURN:
                    dial_list.append(dial_num)
                    pygame.mixer.music.load("enter.mp3")
                    pygame.mixer.music.play(1)
                    if len(dial_list) == 3:
                        if dial_list == dial_password:
                            dial_success = 1
                            pygame.mixer.music.load("unlock.mp3")
                            pygame.mixer.music.play(1)
                        else:
                            pygame.mixer.music.load("error_006.ogg")
                            pygame.mixer.music.play(1)
                            dial_list = []
                            # 틀리면 다이얼 흔들림
                            change_speed = 5
                            y = 60
                            for i in range(310, 325, change_speed):
                                screen.blit(dial.m_img, (i, y))
                                pygame.display.update()
                                pygame.time.delay(1)
                                y += 1.66666666666666666

                            # y = 70
                            for i in range(325, 310, -change_speed):
                                screen.blit(dial.m_img, (i, y))
                                pygame.display.update()
                                pygame.time.delay(1)
                                y -= 1.66666666666666666

                            # y = 60
                            for i in range(310, 295, -change_speed):
                                screen.blit(dial.m_img, (i, y))
                                pygame.display.update()
                                pygame.time.delay(1)
                                y -= 3.333333333333333333

                            # y = 50
                            for i in range(310, 295, -change_speed):
                                screen.blit(dial.m_img, (i, y))
                                pygame.display.update()
                                pygame.time.delay(1)
                                y -= 3.333333333333333333

                            screen.blit(dial.m_img, (310, 60))
                            pygame.display.update()
                            ###### 틀리면 소리
                    break

            ######################################## 자물쇠 클릭 시 넘버패드 #############################################
            if control2 == 0:
                if closet.m_state == 1 and event.key == K_1:  # 자물쇠 확대후 숫자 입력
                    for key_num, value_num in lock_filled.items():
                        if value_num == 0:
                            pygame.mixer.music.load("doorlock_button.mp3")
                            pygame.mixer.music.play(1)
                            lock_filled[key_num] = 1
                            lock_number.insert(key_num, 1)
                            slist[key_num].change_img(n1.m_img, slist[key_num].m_firstlocation)
                            slist[key_num].set_alpha(255)
                            print(lock_number)
                            print(lock_filled)
                            slist[key_num].clicked
                            break

                if closet.m_state == 1 and event.key == K_2:  # 자물쇠 확대후 숫자 입력
                    for key_num, value_num in lock_filled.items():
                        if value_num == 0:
                            pygame.mixer.music.load("doorlock_button.mp3")
                            pygame.mixer.music.play(1)
                            lock_filled[key_num] = 1
                            lock_number.insert(key_num, 2)
                            slist[key_num].change_img(n2.m_img, slist[key_num].m_firstlocation)
                            slist[key_num].set_alpha(255)
                            print(lock_number)
                            print(lock_filled)
                            slist[key_num].clicked
                            break

                if closet.m_state == 1 and event.key == K_3:  # 자물쇠 확대후 숫자 입력
                    for key_num, value_num in lock_filled.items():
                        if value_num == 0:
                            pygame.mixer.music.load("doorlock_button.mp3")
                            pygame.mixer.music.play(1)
                            lock_filled[key_num] = 1
                            lock_number.insert(key_num, 3)
                            slist[key_num].change_img(n3.m_img, slist[key_num].m_firstlocation)
                            slist[key_num].set_alpha(255)
                            print(lock_number)
                            print(lock_filled)
                            slist[key_num].clicked
                            break

                if closet.m_state == 1 and event.key == K_4:  # 자물쇠 확대후 숫자 입력
                    for key_num, value_num in lock_filled.items():
                        if value_num == 0:
                            pygame.mixer.music.load("doorlock_button.mp3")
                            pygame.mixer.music.play(1)
                            lock_filled[key_num] = 1
                            lock_number.insert(key_num, 4)
                            slist[key_num].change_img(n4.m_img, slist[key_num].m_firstlocation)
                            slist[key_num].set_alpha(255)
                            print(lock_number)
                            print(lock_filled)
                            slist[key_num].clicked
                            break

                if closet.m_state == 1 and event.key == K_5:  # 자물쇠 확대후 숫자 입력
                    for key_num, value_num in lock_filled.items():
                        if value_num == 0:
                            pygame.mixer.music.load("doorlock_button.mp3")
                            pygame.mixer.music.play(1)
                            lock_filled[key_num] = 1
                            lock_number.insert(key_num, 5)
                            slist[key_num].change_img(n5.m_img, slist[key_num].m_firstlocation)
                            slist[key_num].set_alpha(255)
                            print(lock_number)
                            print(lock_filled)
                            slist[key_num].clicked
                            break

                if closet.m_state == 1 and event.key == K_6:  # 자물쇠 확대후 숫자 입력
                    for key_num, value_num in lock_filled.items():
                        if value_num == 0:
                            pygame.mixer.music.load("doorlock_button.mp3")
                            pygame.mixer.music.play(1)
                            lock_filled[key_num] = 1
                            lock_number.insert(key_num, 6)
                            slist[key_num].change_img(n6.m_img, slist[key_num].m_firstlocation)
                            slist[key_num].set_alpha(255)
                            print(lock_number)
                            print(lock_filled)
                            slist[key_num].clicked
                            break

                if closet.m_state == 1 and event.key == K_7:  # 자물쇠 확대후 숫자 입력
                    for key_num, value_num in lock_filled.items():
                        if value_num == 0:
                            pygame.mixer.music.load("doorlock_button.mp3")
                            pygame.mixer.music.play(1)
                            lock_filled[key_num] = 1
                            lock_number.insert(key_num, 7)
                            slist[key_num].change_img(n7.m_img, slist[key_num].m_firstlocation)
                            slist[key_num].set_alpha(255)
                            print(lock_number)
                            print(lock_filled)
                            slist[key_num].clicked
                            break

                if closet.m_state == 1 and event.key == K_8:  # 자물쇠 확대후 숫자 입력
                    for key_num, value_num in lock_filled.items():
                        if value_num == 0:
                            pygame.mixer.music.load("doorlock_button.mp3")
                            pygame.mixer.music.play(1)
                            lock_filled[key_num] = 1
                            lock_number.insert(key_num, 8)
                            slist[key_num].change_img(n8.m_img, slist[key_num].m_firstlocation)
                            slist[key_num].set_alpha(255)
                            print(lock_number)
                            print(lock_filled)
                            slist[key_num].clicked
                            break

                if closet.m_state == 1 and event.key == K_9:  # 자물쇠 확대후 숫자 입력
                    for key_num, value_num in lock_filled.items():
                        if value_num == 0:
                            pygame.mixer.music.load("doorlock_button.mp3")
                            pygame.mixer.music.play(1)
                            lock_filled[key_num] = 1
                            lock_number.insert(key_num, 9)
                            slist[key_num].change_img(n9.m_img, slist[key_num].m_firstlocation)
                            slist[key_num].set_alpha(255)
                            print(lock_number)
                            print(lock_filled)
                            slist[key_num].clicked
                            break

                if closet.m_state == 1 and event.key == K_0:  # 자물쇠 확대후 숫자 입력
                    for key_num, value_num in lock_filled.items():
                        if value_num == 0:
                            pygame.mixer.music.load("doorlock_button.mp3")
                            pygame.mixer.music.play(1)
                            lock_filled[key_num] = 1
                            lock_number.insert(key_num, 0)
                            slist[key_num].change_img(n0.m_img, slist[key_num].m_firstlocation)
                            slist[key_num].set_alpha(255)
                            print(lock_number)
                            print(lock_filled)
                            slist[key_num].clicked
                            break

    # screen.blit(textbox.m_img, textbox.m_location)
    print()
    pygame.display.update()  # display update
pygame.quit()
