from SteerMotor import *
from Dash import *
from time import sleep
import random
def main():
    initial_angle=-897
    naive_desired_angle=720
    motor=steer_motor(initial_angle, naive_desired_angle,1.03)
    dash=dashboard(["Initial Angle", "Naive Desired Angle","Desired Angle","Current Angle",  "Displacement", 
                    "Naive Desired Angle Mod 360", "Current Angle Mod 360", 
                    "Delta", "Initial Delta % 360","Final Delta % 360", 
                    "Test Num", "Tolerance Condition", "Displacement Condition", "Satisfaction Counter"])
    for i in range(0, 100):
        test(motor, dash, random.randint(-1000, 1000), random.randint(-1000,1000), i)
    print("SUCCESS!")
        
    # while(True):
    #     dash.read(0.01)
    #     desired_angle, debug_output=calc_desired_angle(motor.get_current_angle(), naive_desired_angle)
    #     delta, initial_delta_mod_360, final_delta_mod_360=debug_output
    #     dash.update({"initial Angle": initial_angle, 
    #                 "Current Angle": motor.get_current_angle(),
    #                  "Naive Desired Angle": naive_desired_angle, 
    #                  "Delta": delta, 
    #                  "Initial Delta % 360":initial_delta_mod_360,
    #                  "Final Delta % 360":final_delta_mod_360, 
    #                  "Desired Angle":desired_angle, 
    #                  "Naive Desired Angle Mod 360":naive_desired_angle%360, 
    #                  "Current Angle Mod 360":motor.get_current_angle()%360,
    #                  "Displacement":motor.get_current_angle()-initial_angle})

    #     motor.set_desired_angle(desired_angle)
    #     motor.periodic()

def test(motor, dash, initial_angle, naive_desired_angle, test_num=0, satisfaction_number=20, tolerance=3):
    motor.set_current_angle(initial_angle)
    counter=0
    while(counter<satisfaction_number):
        dash.read(0.000001)
        desired_angle, debug_output=calc_desired_angle(motor.get_current_angle(), naive_desired_angle)
        delta, initial_delta_mod_360, final_delta_mod_360=debug_output
        
        
        tolerance_condition=abs(naive_desired_angle%360-motor.get_current_angle()%360)<tolerance
        displacement_condition=abs(motor.get_current_angle()-initial_angle)<=180
        if(tolerance_condition and displacement_condition):
            counter+=1
        else:
            counter=0

        
        dash.update({"initial Angle": initial_angle, 
                    "Current Angle": motor.get_current_angle(),
                     "Naive Desired Angle": naive_desired_angle, 
                     "Delta": delta, 
                     "Initial Delta % 360":initial_delta_mod_360,
                     "Final Delta % 360":final_delta_mod_360, 
                     "Desired Angle":desired_angle, 
                     "Naive Desired Angle Mod 360":naive_desired_angle%360, 
                     "Current Angle Mod 360":motor.get_current_angle()%360,
                     "Displacement":motor.get_current_angle()-initial_angle,
                     "test num": test_num,
                     "tolerance condition":tolerance_condition,
                     "displacement condition": displacement_condition,
                     "satisfaction counter": counter})
        motor.set_desired_angle(desired_angle)
        motor.periodic()
if(__name__=="__main__"):
    main()

    