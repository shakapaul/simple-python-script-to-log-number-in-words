#!/usr/bin/env python

def happy():
  numbers = {'0':'zero','1':'one','2':'two','3':'three','4':'four','5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine'}
  nums = str(raw_input("Enter Numbers To Be Converted To Number Words: "))
  output = []

  for num in nums:
    output.append(numbers[num]) 
 
  print ", ".join(output)
  
if __name__ == "__main__":
  happy()

