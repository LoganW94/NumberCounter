
def count_num(num):
  zero = 0
  one = 0
  two = 0
  three = 0
  four = 0
  five = 0
  six = 0
  seven = 0  
  eight = 0
  nine = 0
  
  while num > 0:
    new_num = num
    ten_thou = 0
    thou = 0
    hun = 0
    tens = 0
    ones = 0
    places = [ten_thou, thou, hun, tens, ones]
    
    while new_num >= 10000:
      places[0] +=1
      new_num -= 10000
    while new_num >= 1000:
      places[1] +=1
      new_num -= 1000
    while new_num >= 100:
      places[2] +=1
      new_num -= 100
    while new_num >= 10:
      places[3] +=1
      new_num -= 10
    while new_num >= 1:
      places[4] +=1
      new_num -= 1
        
    num -= 1
    
    for x in places:
  
      if x == 0:
        zero += 1  
      if x == 1:
        one +=1
      if x == 2:
        two +=1
      if x == 3:
        three += 1
      if x == 4:
        four +=1 
      if x == 5:
        five += 1
      if x == 6:
        six += 1
      if x == 7:
        seven += 1
      if x == 8:
        eight += 1
      if x == 9:
        nine +=1
      
  
  print(
    """
    zeros: %s
    ones: %s
    twos: %s
    threes: %s
    fours: %s
    fives: %s
    sixes %s
    sevens: %s 
    eights: %s 
    nines: %s
    """ 
    % (zero, one, two, three, four, five, six, seven, eight, nine ) )
  
count_num(10000)