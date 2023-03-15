# SXD-Technical-Exercise
**Part 1: Math**<br/>
if $x_1 + x_2 \leq 5$ , $2x_1 + x_2 \leq 8$ , and $x_1 , x_2 \geq 0$ <br/>
then you can subtract the first equation from the second one to get you: $x_1 \leq 3$<br/>
since $x_1 \leq 3$ then $x_2 \leq 2$ <br/>
since we're looking for the min: Min $-3 * x_1 = -9$ and Min $1 * x_2 = 0$ <br/>
So, Min Z $= -9 + 0 = -9$ <br/> <br/>
**Part 2: Programming** <br/>
See Part2.py <br/> <br/>
**Part 3: Systems** <br/>
See Part2.py, Part3.py, & db.sql <br/> <br/>
*What type of database would you choose? Why?* <br/>
I chose a relational database (mySQL) because it provides strong data integrity features and can handle sub-millisecond latency. <br/><br/>
*Assume your target user audience are all math students in the US. How would you size your database accordingly? What strategies would you consider to prevent overloading a single database instance with requests?* <br/>
Since there is a large amount of math students in the US, the database should be large enough to handle a significant amount of users. To prevent overloading a single database instance with requests you could replicate the databse multiple times. <br/> <br/>
*Did you set up your database locally or on cloud infrastructure?* <br/>
I set up my database locally however it is hosted through docker. 
