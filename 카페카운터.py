from tkinter import *

window = Tk()
window.title("카운터 주문받기")

#안내
Label(window, text="메뉴 선택후 주문하기를 눌러주세요(테이크아웃만 가능, 단체X)", fg="red").grid(row=0, column = 0,columnspan=3)
Label(window, text="=======메뉴표=======\n\n 아메리카노(M)  1000 \n 아메리카노(L)   1500 \n 카페라떼          2500 \n 아이스             2000 \n 초코라떼          2500 \n 스무디             3500 \n 녹차                2000 \n 프라푸치노       3000 \n 물                  500 \n\n=====================").grid(row=1, column = 4)
#주문 내역
T=Text(window, height = 20, width= 45, fg="white",bg="#002C00")
T.grid(row=1, column = 0, columnspan=3)
T.insert(END,"-----------< 메뉴 >----------- | --< 가격 >--\n")

#주문수량+
count1=0
count2=0
count3=0
count4=0
count5=0
count6=0
count7=0
count8=0
count9=0

#주문 번호
ttorder=0

#메뉴 선택시 주문목록에 출력
def order1():
  global count1
  count1+=1
  T.insert(END, "         아메리카노(M)              1000\n")
def order2():
  global count2
  count2+=1
  T.insert(END, "         아메리카노(L)              1500\n")
def order3():
  global count3
  count3+=1
  T.insert(END, "           카페라떼                 2500\n")
def order4():
  global count4
  count4+=1
  T.insert(END, "           아이스티                 2000\n")
def order5():
  global count5
  count5+=1
  T.insert(END, "           초코라떼                 2500\n")
def order6():
  global count6
  count6+=1
  T.insert(END, "            스무디                  3500\n")
def order7():
  global count7
  count7+=1
  T.insert(END, "             녹차                   2000\n")
def order8():
  global count8
  count8+=1
  T.insert(END, "          프라푸치노                3000\n")
def order9():
  global count9
  count9+=1
  T.insert(END, "              물                     500\n")

#주문하기 클릭시 실행
def torder():
  global ttorder
  ttorder+=1
  T.insert(END,"\n----< 메뉴 >----- | --< 수량 >-- | -< 금액 >-\n")
  T.insert(END, "   아메리카노(M)          ")
  T.insert(END,count1)
  T.insert(END,"           ")
  T.insert(END,count1*1000)
  T.insert(END, "\n   아메리카노(L)          ")
  T.insert(END,count2)
  T.insert(END,"           ")
  T.insert(END,count2*1500)
  T.insert(END, "\n    카페라떼              ")
  T.insert(END,count3)
  T.insert(END,"           ")
  T.insert(END,count3*2500)
  T.insert(END, "\n    아이스티              ")
  T.insert(END,count4)
  T.insert(END,"           ")
  T.insert(END,count4*2000)
  T.insert(END, "\n    초코라떼              ")
  T.insert(END,count5)
  T.insert(END,"           ")
  T.insert(END,count5*2500)
  T.insert(END, "\n     스무디               ")
  T.insert(END,count6)
  T.insert(END,"           ")
  T.insert(END,count6*3500)
  T.insert(END, "\n      녹차                ")
  T.insert(END,count7)
  T.insert(END,"           ")
  T.insert(END,count7*2000)
  T.insert(END, "\n   프라푸치노             ")
  T.insert(END,count8)
  T.insert(END,"           ")
  T.insert(END,count8*3000)
  T.insert(END, "\n       물                 ")
  T.insert(END,count9)
  T.insert(END,"           ")
  T.insert(END,count9*500)
  T.insert(END,"\n---------------------------------------------\n")
  T.insert(END, " 총 금액: ")
  T.insert(END, count1*1000+ count2*1500+count3*2500+count4*2000+count5*2500+count6*3500+count7*2000+count8*3000+count9*500)

  
#영수증 파이썬 쉘에 출력
def receipt():
  print("============================================")
  print("\n")
  print("번호로 불러드리겠습니다.")
  print("\n")
  print("주문 번호: ",ttorder)
  print("\n")
  print("픽업시 주문 번호를 직원에게 제시해 주시기 바랍니다.")
  print("\n")
  print("=================절취선======================")
  print("\n")
  print("ONLYTAKEOUT_CAFE            TEL : 02-970-8282\n")
  print("서울특별시 노원구 화랑로 621 8282\n")
  print("대표자: 이은경     ")
  print("2020-03-10          NO: 000-",ttorder)
  print("\n----< 메뉴 >----- | --< 수량 >-- | -< 금액 >-\n")
  print( "   아메리카노(M)       ",count1,"              ",count1*1000)
  print("   아메리카노(L)       ",count2,"              ",count2*1500)
  print("     카페라떼          ",count3,"              ",count3*2500)
  print("     아이스티          ",count4,"              ",count4*2000)
  print("     초코라떼          ",count5,"              ",count5*2500)
  print("      스무디           ",count6,"              ",count6*3500)
  print( "       녹차            ",count7,"              ",count7*2000)
  print("   프라푸치노          ",count8,"              ",count8*3000)
  print("        물             ",count9,"              ",count9*500)
  print("---------------------------------------------")
  print(" 총 금액: ",count1*1000+ count2*1500+count3*2500+count4*2000+count5*2500+count6*3500+count7*2000+count8*3000+count9*500)
  print("\n이용해 주셔서 감사합니다.")
  print("\n")
  print("============================================")

#다음 주문 받기
def reset():
  T.delete(1.0,END)
  T.insert(END,"-----------< 메뉴 >----------- | --< 가격 >--\n")
  global count1
  count1=0
  global count2
  count2=0
  global count3
  count3=0
  global count4
  count4=0
  global count5
  count5=0
  global count6
  count6=0
  global count7
  count7=0
  global count8
  count8=0
  global count9
  count9=0

  #주문하기 클릭시 실행
def torder():
  global ttorder
  ttorder+=1
  T.insert(END,"\n----< 메뉴 >----- | --< 수량 >-- | -< 금액 >-\n")
  T.insert(END, "   아메리카노(M)          ")
  T.insert(END,count1)
  T.insert(END,"           ")
  T.insert(END,count1*1000)
  T.insert(END, "\n   아메리카노(L)          ")
  T.insert(END,count2)
  T.insert(END,"           ")
  T.insert(END,count2*1500)
  T.insert(END, "\n    카페라떼              ")
  T.insert(END,count3)
  T.insert(END,"           ")
  T.insert(END,count3*2500)
  T.insert(END, "\n    아이스티              ")
  T.insert(END,count4)
  T.insert(END,"           ")
  T.insert(END,count4*2000)
  T.insert(END, "\n    초코라떼              ")
  T.insert(END,count5)
  T.insert(END,"           ")
  T.insert(END,count5*2500)
  T.insert(END, "\n     스무디               ")
  T.insert(END,count6)
  T.insert(END,"           ")
  T.insert(END,count6*3500)
  T.insert(END, "\n      녹차                ")
  T.insert(END,count7)
  T.insert(END,"           ")
  T.insert(END,count7*2000)
  T.insert(END, "\n   프라푸치노             ")
  T.insert(END,count8)
  T.insert(END,"           ")
  T.insert(END,count8*3000)
  T.insert(END, "\n       물                 ")
  T.insert(END,count9)
  T.insert(END,"           ")
  T.insert(END,count9*500)
  T.insert(END,"\n---------------------------------------------\n")
  T.insert(END, " 총 금액: ")
  T.insert(END, count1*1000+ count2*1500+count3*2500+count4*2000+count5*2500+count6*3500+count7*2000+count8*3000+count9*500)
  
  
  

#메뉴 선택 버튼
b1 = Button(window, text="아메리카노(M)", width = 15, command=order1,fg="white",bg="#002266")
b1.grid(row=2,column=0)
b2 = Button(window, text="아메리카노(L)",width = 15, command=order2,fg="white",bg="#002266")
b2.grid(row=2,column=1)
b3 = Button(window, text="카페라떼",width = 15, command=order3,fg="white",bg="#002266")
b3.grid(row=2,column=2)
b4 = Button(window, text="아이스티",width = 15, command=order4,fg="white",bg="#002266")
b4.grid(row=3,column=0)
b5 = Button(window, text="초코라떼",width = 15, command=order5,fg="white",bg="#002266")
b5.grid(row=3,column=1)
b6 = Button(window, text = "스무디",width = 15, command=order6,fg="white",bg="#002266")
b6.grid(row=3,column=2)
b7 = Button(window, text = "녹차",width = 15, command=order7,fg="white",bg="#002266")
b7.grid(row=4,column=0)
b8 = Button(window, text = "프라푸치노",width = 15, command=order8,fg="white",bg="#002266")
b8.grid(row=4,column=1)
b9= Button(window, text = "물",width = 15, command=order9,fg="white",bg="#002266")
b9.grid(row=4,column=2)

#빈칸

Label(window, text=" ").grid(row=5, column = 0,columnspan=3)
Label(window, text="---계산하기---").grid(row=6, column = 0,columnspan=3)

#계산, 영수증, 프로그램 종료 버튼
b10= Button(window, text = "주문하기",width = 15, command=torder,fg="white",bg="black")
b10.grid(row=7,column=0)
b11= Button(window, text = "주문번호/영수증출력",width = 15, command=receipt,fg="white",bg="black")
b11.grid(row=7,column=1)
b12= Button(window, text = "새 주문 받기",width = 15, command = reset,fg="white",bg="black")
b12.grid(row=7,column=2)



window.mainloop()
