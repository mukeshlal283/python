class RailwayForum:
    
    def form(self):
        print(f"my name is {self.name} ")
        print(f"my train is {self.train} ")

traininfo = RailwayForum()    #make new application
traininfo.name = "MUKESH"     #set info 
traininfo.train = "rajdhaani exp."   #set info
 
traininfo.form()      #call
