class StringUtility:
  def __init__(self,string):
    self.string = str(string)
  def __str__(self):
    return(self.string)

  def vowels(self):
    '''
    counts the number of vowels in the given string and retruns the number of vowels
  
    args: self(class) class name 
  
    return: count(str) returns the number of vowels in the given str
    '''

    list = self.string.upper()
    count = 0
    for i in list:
      if i == "A":
        count += 1
      elif i == "E":
        count += 1 
      elif i == "I":
        count += 1
      elif i == "O":
        count += 1
      elif i == "U":
        count += 1
      if count >= 5:
        count = "many"
        break
    return(str(count))
  def bothEnds(self): 
    '''
    takes given string and creates new string out of the first two and last two letters

    args: self(class) class name

    return: ends_string(str) first two and last two letters of the given string
    '''
    string = self.string
    if len(string) < 2:
      return("")
    else: string =(self.string[0] + self.string[1] + self.string[-2] + self.string[-1])
    return(string)

  def fixStart(self):
    '''
    takes given string and replaces all reocerences of the first letter with "*" but does not replace the first letter
    args: self(class) class name

    return: string(str) the given str with replaced letters
    '''
    if len(self.string) == 0:
      return(self.string)
    replacer = self.string[0]
    string = self.string
    for i in self.string:
      if i == replacer:
        string = string.replace(i,"*")
    string = string.replace("*",replacer,1)
    

    return(string)
  def asciiSum(self):
    '''
    takes the given string and adds each charechters ascii value together

    args: 

    return: the sum of all the values of the string
    '''
    string = self.string
    sum = 0
    for i in string:
      sum = sum + ord(i)
  
    return(sum)
  def cipher(self):
    '''
    given string is converted into ASCII then is added by the amount of charechters in the string, shifting the letters. It is then converted back to a str.
    args: None

    return: the given string shifted by the amount of charechters in it.
    '''
    LOWERCASE_A = 97
    UPPERCASE_A = 65
    LOWERCASE_Z = 122
    UPPERCASE_Z = 90
    MAXLOWER = 149
    MAXUPPER = 92
    string = self.string
    new_string = ""
    shift_value = len(string)
    print(shift_value)
    for i in string:
      ascii_value = ord(i)
      if (ascii_value >=UPPERCASE_A and ascii_value <= UPPERCASE_Z):
        if (ascii_value + shift_value) > UPPERCASE_Z:
           new_string += chr((UPPERCASE_A - 1) + ((ascii_value + shift_value)% UPPERCASE_Z))
        else:
          new_string = new_string + chr(ascii_value + shift_value)
          
      elif (ascii_value >= LOWERCASE_A and ascii_value <= LOWERCASE_Z):
        if (ascii_value + shift_value) > LOWERCASE_Z:
          if (ascii_value + shift_value) >= MAXLOWER:
            new_string +=  chr((2*(LOWERCASE_A - 1)) + ((ascii_value + shift_value)% 122) -122)
          else:
            new_string +=  chr((LOWERCASE_A - 1) + ((ascii_value + shift_value)% 122))
        
        else:
          new_string +=chr(ascii_value + shift_value)
      else: new_string += chr(ascii_value)
    return(new_string)
