meretin={
"и":
["*   **",
"*  * *",
"* *  *",
"**   *"],
"м":
["**    **",
"* *  * *",
"*  **  *",
"*      *",]}
m=input()
sm=m.split(' ')
for l in range(4):
    t=" "
    for i in sm:
        t+=meretin[i][l]
    print(t)
