import streamlit as st
import datetime as datetime
from datetime import date

st.set_page_config(page_title="NMOJI AGE CALCULATOR", page_icon=":star:", layout="centered")
st.write("""
         # Welcome to our NMOJI AGE CALCULATOR!!
         ## Hello there, We made this app from scratch to write your name in emojis & calculate your age in no time.
         """)

col1, col2 = st.columns(2)

with col1:
   option = st.selectbox(
       'What is your gender?',
       ('Male', 'Female'))
   st.write("Please, enter your name")
   username = st.text_input("").casefold()         
   maledict = {
    0:":prince:",
1:":adult:",
2:":man:",
3:":man_beard:",
4:":red_haired_man:",
5:":white_haired_man:",
6:":person_red_hair:",
7:":person_curly_hair:",
8:":person_white_hair:",
9:":person_bald:",
10:":blond_haired_man:",
11:":older_man:",
12:":frowing_person:",
13:":pouting_man:",
14:":no_good:",
15:":ok_man:",
16:":information_desk_person:",
17:":raising_hand_man:",
18:":bowing_man:",
19:":facepalm:",
20:":bearded_person:",
21:":older_adult:",
22:":office_worker:",
23:":technologist:",
24:":ninja:",
25:":boy:",
26:":frowing_man:",
}
   femaledict = {
    0:":girl:",
1:":red_haired_woman:",
2:":curly_haired_woman:",
3:":white_haired_woman:",
4:":older_woman:",
5:":blond_woman:",
6:":frowning_woman:",
7:":pouting_woman:",
8:":no_good_woman:",
9:":ok_woman:",
10:":tipping_hand_woman:",
11:":deaf_woman:",
12:":woman_facepalming:",
13:":raising_hand_woman:",
14:":bowing_woman:",
15:":woman_shrugging:",
16:":woman_office_worker:",
17:":princess:",
18:":woman_teacher:",
19:":woman_farmer:",
20:":woman_technologist:",
21:":policewoman:",
22:":woman_in_tuxedo:",
23:":pregnant_woman:",
24:":bride_with_veil:",
25:":woman_student:",
26:":woman_judge:",
}
   letdict = {
    "a":0,
"b":1,
"c":2,
"d":3,
"e":4,
"f":5,
"g":6,
"h":7,
"i":8,
"j":9,
"k":10,
"l":11,
"m":12,
"n":13,
"o":14,
"p":15,
"q":16,
"r":17,
"s":18,
"t":19,
"u":20,
"v":21,
"w":22,
"x":23,
"y":24,
"z":25,
" ":26
}
   nmoji = ""
   if option == 'Male':
      for i in username:
          letIndex = letdict[i]
          emoValue = maledict[letIndex]
          nmoji = nmoji + " " + emoValue
   else :
       for i in username:
           letIndex = letdict[i]
           emoValue = femaledict[letIndex]
           nmoji = nmoji + " " + emoValue
   st.write("""
            ### Your name in emojis 
             """, nmoji)
   d = st.date_input("When's your birthday?",datetime.date(2000, 1, 1))  
   def age(birthdate):
       today = date.today()
       age_value = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
       return age_value
   st.write("""
            ### Your age is
            """, age(d))

with col2:
    from PIL import Image
    image = Image.open('nmoji.png')
    st.image(image, use_column_width="always")
    st.caption('This app was created by: Amgad Salah')

