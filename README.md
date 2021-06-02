# CPSC449-Project3 Server Side Sessions
Web Back-End Engineering

learn to make HTTP requests from a Python program and use this ability to store server-side session data in a separate storage service

## Group-Member
- Yi Wei Lee
- Ramiro Aispuro
- Tasnima Chowdhury

# How to run project

1. Navigate to cpsc499-master/bottle/counter
2. run the program in terminal, open two terminal
3.  type in one terminal:
    ` $ foreman start `
    -   you can check the localhost in here, we got 
       -   localhost:5000 is for app.py
       -   localhost:5100 is for kv.py
4. Run the dump.py in another terminal
-   input the value into the dump.py that connect to kv.py
-   run the dump.py
      -    in the terminal type :
          `$ python3 ./dump.py http://localhost:5100 `

5. Open two browsers link to localhost:5000
6. increase or reset
7. in the terminal type:
    `python3 ./dump.py http://localhost:5100` will get the session.

# Sources 
1. Professor code from flask
2. requests method `https://requests.readthedocs.io/en/master/user/quickstart/`

