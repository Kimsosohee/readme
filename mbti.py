print("<<<MBTI 테스트>>>") 
        
 print("Q1. 갑작스러운 여행으로 혼자 오게 된 낯선 장소, 이런 곳에서 나는  \n 1. 혼자 조용히 여행을 즐긴다. \n 2. 여행 중 만난 사람들과 쉽게 친해진다") 
 choice1 = int(input()) 
 
 
 print("Q2. 여행 중 다음 행선지를 위해 버스를 탔을 때, 버스에서 나는 어떤 생각을 할까? \n 1. '오늘 저녁은…' 남은 일정에 대해 생각한다. \n 2. '내가 여기 산다면…' 의식의 흐름에 따라 상상의 나래를 펼친다.") 
 choice2 = int(input()) 
 
 
 print("Q3. 버스 옆자리에 마음에 드는 이상형이 있다. 어쩌다 대화를 시작한 나는  \n 1.풍부한 공감과 리액션을 해준다. \n 2. 이것저것 궁금한 것을 질문한다.") 
 choice3 = int(input()) 
 
 
 print("Q4. 아직 여행 마지막 날의 일정을 짜지 못한 나는  \n 1. 미루다 전날 잠들기 직전에 짠다. \n 2. 틈틈히 루트를 구상해 놓는다.") 
 choice4 = int(input()) 
 
 
 if choice1==1 and choice2==1 and choice3==1 and choice4==1: 
     print("당신은 ISFP") 
      
 elif choice1==2 and choice2==1 and choice3==1 and choice4==1: 
     print("당신은 ESFP") 
      
 elif choice1==1 and choice2==2 and choice3==1 and choice4==1: 
      print("당신은 INFP") 
       
 elif choice1==1 and choice2==1 and choice3==1 and choice4==2: 
      print("당신은 ISFJ") 
       
 elif choice1==2 and choice2==2 and choice3==1 and choice4==1: 
     print("당신은 ENFP") 
      
 elif choice1==2 and choice2==2 and choice3==2 and choice4==1: 
     print("당신은 ENTP") 
      
 elif choice1==2 and choice2==2 and choice3==2 and choice4==2: 
     print("당신은 ENTJ") 
      
 elif choice1==1 and choice2==1 and choice3==2 and choice4==2: 
     print("당신은 ISTJ") 
      
 elif choice1==1 and choice2==2 and choice3==2 and choice4==1: 
     print("당신은 INTP") 
      
 elif choice1==2 and choice2==1 and choice3==1 and choice4==2: 
     print("당신은 ESFJ") 
      
 elif choice1==2 and choice2==1 and choice3==2 and choice4==2: 
     print("당신은 ESTJ") 
      
 elif choice1==2 and choice2==2 and choice3==1 and choice4==2: 
     print("당신은 ENFJ") 
      
 elif choice1==1 and choice2==2 and choice3==2 and choice4==2: 
     print("당신은 INTJ") 
      
 elif choice1==1 and choice2==1 and choice3==2 and choice4==1: 
     print("당신은 ISTP") 
 
 
 elif choice1==2 and choice2==1 and choice3==2 and choice4==1: 
     print("당신은 ESTP") 
 
 
 else: print("당신은 INFJ") 

 
