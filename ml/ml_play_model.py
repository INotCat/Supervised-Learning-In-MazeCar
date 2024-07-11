import pygame, sys, os, pickle

index = sys.argv[16]
print("Map number: "+index)
class MLPlay:
    def __init__(self, ai_name,*args,**kwargs):
        with open('/Users/harris/MLGame/Maze_Car/model/'+'K'+index+'model.pickle', 'rb') as f:
           self.model = pickle.load(f)
        self.player_no = ai_name
        self.r_sensor_value = 0
        self.l_sensor_value = 0
        self.f_sensor_value = 0
        self.control_list = {"left_PWM": 0, "right_PWM": 0}
        self.game_status = None;
        self.run = 0;
        self.dataFinal = [];
        # print("Initial ml script")

    def update(self, scene_info: dict, keyboard: list = [], *args, **kwargs):
        """
        Generate the command according to the received scene information
        """
        if scene_info["status"] != "GAME_ALIVE":
            return "RESET"

        R_sensor_value = scene_info["R_sensor"]
        L_sensor_value = scene_info["L_sensor"]
        F_sensor_value = scene_info["F_sensor"]
        frame = scene_info["frame"]
       
        dataPerFrame = [[R_sensor_value,L_sensor_value,F_sensor_value,frame]]
        #print(dataPerFrame)
        decision = self.model.predict(dataPerFrame)
        #print(decision)
        #get the value of [[100 100]]
        self.control_list["right_PWM"] = decision[0][0]
        self.control_list["left_PWM"] = decision[0][1]
       
        return self.control_list

    def reset(self):
        """
        Reset the status
        """
        pass
