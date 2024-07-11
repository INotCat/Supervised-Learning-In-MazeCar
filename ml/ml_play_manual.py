import pygame, sys, os, pickle


class MLPlay:
    def __init__(self, ai_name,*args,**kwargs):
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
        if pygame.K_w in keyboard or pygame.K_UP in keyboard:
            self.control_list["left_PWM"] = 200
            self.control_list["right_PWM"] = 200
        elif pygame.K_a in keyboard or pygame.K_LEFT in keyboard:
            self.control_list["left_PWM"] = -150
            self.control_list["right_PWM"] = 150
        elif pygame.K_d in keyboard or pygame.K_RIGHT in keyboard:
            self.control_list["left_PWM"] = 150
            self.control_list["right_PWM"] = -150
        elif pygame.K_s in keyboard or pygame.K_DOWN in keyboard:
            self.control_list["left_PWM"] = -150
            self.control_list["right_PWM"] = -150
        else:

            self.control_list["left_PWM"] = 100
            self.control_list["right_PWM"] = 100




        R_sensor_value = scene_info["R_sensor"]
        L_sensor_value = scene_info["L_sensor"]
        F_sensor_value = scene_info["F_sensor"]
        Right_PWM_value = self.control_list["right_PWM"]
        Left_PWM_value = self.control_list["left_PWM"]
        frame = scene_info["frame"]
     



        #Save data
        dataPerFrame = [R_sensor_value,L_sensor_value,F_sensor_value,frame,Right_PWM_value,Left_PWM_value]
       
        # Append data per frame to a big list we save to file
        self.dataFinal.append(dataPerFrame)
     
        # Flush afterr save
        dataPerFrame = []
        #self.game_status = scene_info["status"]
        #print(self.game_status)
        #if(self.game_status == "GAME_PASS"):
        #    self.game_status = "GAME_PASS"
        #    self.run += 1;
        #    print("run:"+self.run)
            
        
        return self.control_list

    def reset(self):
        """
        Reset the status
        """
        index = sys.argv[16];
        print(index)
        
    
        filepath = "/Users/harris/MLGame/Maze_Car/log/data_" + index
        filename = index + ".pickle"
        print(filename+filepath)
        
        with open(os.path.join(filepath, filename), "wb") as f:
            pickle.dump(self.dataFinal, f)
        
        #if self.run == 1:
        #    sys.exit
        # print("reset ml script")
        pass
