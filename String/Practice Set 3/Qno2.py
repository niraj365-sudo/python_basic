'''
    Program to fill in a letter template given below with name and date

        letter =  Dear <|Name|>,
                            You are selected!
                                    <|Date|>
'''
from dataclasses import replace
import datetime
from re import template
name = input("Enter your name:")
template=''' Dear <|Name|>,
                     You are selected!
                                    <|Date|> '''

print(template.replace('<|Name|>',name).replace('<|Date|>','2079'))

