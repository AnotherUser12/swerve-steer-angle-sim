class steer_motor():
    def __init__(self, initial_angle, desired_angle=False, dtheta=1):
        self.current_angle=initial_angle
        self.dtheta=abs(dtheta)
        if(desired_angle==False):
            self.desired_angle=self.current_angle
        else:
            self.desired_angle=desired_angle

    def get_current_angle(self):
        return self.current_angle
    def set_current_angle(self, angle):
        self.current_angle=angle
    def set_desired_angle(self, angle):
        self.desired_angle=angle
    def periodic(self):
        direction=self.desired_angle-self.current_angle
        direction=direction/abs(direction) if direction!=0 else 0
        self.set_current_angle(self.current_angle+direction*self.dtheta)

def calc_desired_angle(current_angle,naive_desired_angle):
    delta=naive_desired_angle-current_angle
    initial_delta_mod_360=delta%360
    final_delta_mod_360=initial_delta_mod_360-360 if initial_delta_mod_360>180 else initial_delta_mod_360
    desired_angle=current_angle+final_delta_mod_360
    debug_output=(delta, initial_delta_mod_360, final_delta_mod_360)
    return desired_angle, debug_output


    
