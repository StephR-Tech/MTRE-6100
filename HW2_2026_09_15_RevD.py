#.............................................................................................#
# Stephanie Rawls 
# MTRE 6100 Advanced Programming 
# Homework Assignment 2

import numpy as np
# import matplotlib as plot 
#.............................................................................................#
 # Defining variables and initializing vars to be used across all functions 

bel_x_t_1 = [.25, .25, .25, .25]
bel_x_t = [0 , 0, 0, 0]
p_move_bwd = 0
p_move_fwd = .7
p_move_slip = .2
p_move_overshoot = .1
Probabilities = [p_move_bwd, p_move_fwd, p_move_slip, p_move_overshoot]
Position = ['P0' , 'P1', 'P2','P3']
indx = [] 
t = 0

pass

def prediction(bel_x_t, Position, Probabilities, bel_x_t_1):
    # This function focuses on executing Bayes Filter First Step which defines the 'raw'
    # probability of each proposed position in xt

    for j in range(len(Position)):
        # Here we are grabbing the Position we want to calc its Prob for xt = Position.indx
        indx = j #Position.index(j)

        

        # Lets begin probability calc. This is all based on we commaned a ut movement
        # and we moved to positionx from the xt-1 positiony

        # Initialize the variables
        belief_fwd = 0
        belief_fwd2 = 0

        # Slipped Scenario: Calculate The Probability xt = xt-1
        belief_s = Probabilities[2] * bel_x_t_1[indx]
        if indx >= 1:
            # Moved Forward Correctly: xt = x_t_1 + 1
            belief_fwd = Probabilities[1] * bel_x_t_1[indx - 1]
        if indx >= 2:
            # Moved Forward with Overshoot: xt = x_t_1 + 2
            belief_fwd2 = Probabilities[3] * bel_x_t_1[indx - 2]

        # Finding the Probabililities xt = positionx given xt-1 are all the other positions
        summation_xt = sum([belief_s, belief_fwd, belief_fwd2])

        # placing the probability for this specific position xt
        bel_x_t[indx] = summation_xt
   
    # Now we calculate this over again for the next value
    # once done we can move to the confirmation phase
   
   

    
pass 

def confirmation(bel_x_t, sensor_reading):
    

    # Provide the Probabilities based on the sensor 
    z_t_wall = .75
    z_t_notwall = .25 

    z_t_door = .7
    z_t_notdoor = .3

    # Apply the correction factor for sensor based on location
    for k in range(len(bel_x_t)):
        # we check for if its acually a wall or not
        # use this probability based on the given state
        if sensor_reading == 'wall':

            if k %2 == 0:
                bel_x_t[k] = bel_x_t[k] * z_t_wall 
            else:
                bel_x_t[k] = bel_x_t[k] * z_t_notwall 

        elif sensor_reading == 'door': 
            if k %2 == 1:
                bel_x_t[k] = bel_x_t[k] * z_t_door 
            else:
                bel_x_t[k] = bel_x_t[k] * z_t_notdoor 

    # Create a normalization constant based on our output from prediction()
    Norm_x = 1 / sum(bel_x_t)
    
    for r in range(len(bel_x_t)):
        bel_x_t[r] = bel_x_t[r] * Norm_x 
        bel_x_t[r] = round(bel_x_t[r], 4) # rounding to 4 decimal places for easier reading

        print(" The Value for bel x(t) = ", Position[r],'=', bel_x_t[r], 'at t = ', t )

    # Plotting the values for t = y 
        # plot.figure(t)
        # plot.bar([0,1,2,3] ,bel_x_t )
        # plot.ylabel("bel x(t)")
        # plot.xlabel('Grid Positions')
        # plot.title('Bayes Filter for Calculating Belief State')
 

def main():
    global bel_x_t
    global bel_x_t_1
    global sensor_reading
    global t
    userinput = input('Please enter the sensor reading (wall or door): ')
    userinput = userinput.lower()
    sensor_reading = userinput
    
    for i in range(2):
        bel_x_t = [0 , 0, 0, 0]
        t = t + 1
        prediction(bel_x_t, Position, Probabilities, bel_x_t_1,)
        confirmation(bel_x_t, sensor_reading)
        bel_x_t_1 = bel_x_t.copy() # update the belief state for the next iteration
    final_bel = np.column_stack((Position,bel_x_t)).astype(object)
    print('Final Belief State at t =', t, '\n', 'bel x(t) = ', '\n', final_bel)
    

if __name__ == "__main__":
        main()

