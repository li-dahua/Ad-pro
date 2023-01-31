 
point_str =input("Enter the point of leading : "  )
points_left= int(point_str)

leading_calculation= float (points_left-3)
ball_holding=input("Enter the if the team haveing the ball : (yes or no)"  )

while ball_holding!=('yes') and ball_holding!=('no'):
    ball_holding=input("Enter the if the team haveing the ball : (yes or no)"  )

if ball_holding==  'yes':
    leading_calculation=leading_calculation+0.5
        
else:
    leading_calculation=leading_calculation-0.5

if leading_calculation < 0:
    leading_calculation=0

second_left= int(input("enter the number for second remaining: "))

if leading_calculation>second_left:
    print('lead is safe')
else:
    print('lead is not safe')