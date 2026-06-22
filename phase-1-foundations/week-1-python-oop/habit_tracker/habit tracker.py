import datetime
class Habit():
    def __init__(self,name):
        self.name=name
        self.date=datetime.date.today()
        self.completed_days=[]
        
    def mark_done(self):
        if datetime.date.today() not in self.completed_days:
            self.completed_days.append(datetime.date.today())
    

    def streak(self):
      streak=0
      today=datetime.date.today()
      if today in self.completed_days:
          current_day=today
      elif today-datetime.timedelta(days=1) in self.completed_days:
          current_day=today-datetime.timedelta(days=1)
      else:
          return streak
      while current_day in self.completed_days:
          streak+=1
          current_day=current_day-datetime.timedelta(days=1)
      return streak
    
    @classmethod
    def from_history(cls,name,date):
        habit=cls(name)
        habit.date=date
        return habit
    
    def to_dict(self):
        return {'name':self.name,'date':self.date.isoformat(),"completed_days":[day.isoformat() for day in self.completed_days]}
        

    @classmethod
    def from_dict(cls,data):
        habit=cls(data['name'])
        habit.created_date = datetime.date.fromisoformat(data["date"])
        habit.completed_days = [datetime.date.fromisoformat(d) for d in data["completed_days"]]
        return habit
import os
import json

class HabitTracker():
    def __init__(self,file_name):
        self.file_name=file_name
        self.habits=[]
        self.load_file()

    def load_file(self):
         if not os.path.exists(self.file_name):
             return 
         try:           
            with open(self.file_name,"r")as f:
                data=json.load(f)
            self.habits=[Habit.from_dict(d) for d in data]
         except json(json.JSONDecodeError, KeyError, ValueError) as e:
            print(f"Warning: couldn't load saved data ({e}). Starting fresh.")
            self.habits = []
                           
    
    def save_file(self):
        data=[habit.to_dict() for habit in self.habits]
        with open(self.file_name,"w") as f:
            json.dump(data,f)
        

    
    
    def add_habit(self,habit_name):
        if self.habits==[]:
            return self.habits.append(Habit(habit_name)) 
        for habit in self.habits:
            if habit_name.lower()==habit.name.lower():
                return print("This habit has already been added")  
       
            
        self.habits.append(Habit(habit_name))
        return self.save_file()
            
        
    def del_habit(self,habit_name):
        for habit in self.habits:
            if habit_name.lower()==habit.name.lower():
                self.habits.remove(habit)
                return self.save_file()
        
                
        print("Habit Not FOund")
                
    
    def mark_habit_done(self,habit_name):
        for habit in self.habits:
            if habit_name.lower()==habit.name.lower():
                habit.mark_done()
                return self.save_file()
        print('Habit Not found')
            
    def view_habits(self):
        if self.habits!=[]:
            for habit in self.habits:
               print(f'--->{habit.name},Streak:{habit.streak()}')
        else:
            print("No habits yet, add one to get started")
    
    def add_historical_habit(self,name,date):
        if date>datetime.date.today():
            raise ValueError("Date cannot be in the future")
        for habit in self.habits:
            if name.lower()==habit.name.lower():
                 return print("This habit has already been added")  
        self.habits.append(Habit.from_history(name,date))
        return self.save_file()
        
if __name__=='__main__':
    Ht1=HabitTracker('habit_tracker_data')
    while True:
        print("========================")
        print("     HABIT TARCKER     ")
        print("========================")
        print("1. Add a habit")
        print("2. Mark a habit as done")
        print("3. Delete a habit") 
        print("4. View all habits")
        print("5. Add historical habit")
        print("6. Quit")
        print("------------------------")
        choice=input("CHOOSE AN OPTION: ")
        choice=choice.strip()
        if choice=="1":
            habit_name=input("Please enter the habit name: ")
            Ht1.add_habit(habit_name.strip())
        elif choice=="2":
            habit_name=input("Please enter the habit that you completed today: ")
            Ht1.mark_habit_done(habit_name.strip())
        elif choice=="3":
            habit_name=input("Please enter the habit that you want to delete: ")
            Ht1.del_habit(habit_name.strip())
        elif choice=="4":
            Ht1.view_habits()
        elif choice=="5":
            while True:
                habit_name=input("Please enter the habit name: ")  

                date=input("Please enter the day you started this habbit in this format(yyyy-mm-dd):")
                try:
                    date=datetime.datetime.strptime(date, "%Y-%m-%d").date()
                    if date>datetime.date.today():
                        print("Date cannot be in the future")
                        continue
                    break
                except ValueError:
                    print("Invalid date format, try again")
            Ht1.add_historical_habit(habit_name.strip(),date)        
        elif choice=="6":
            break
        else:
            print("Invalid Choice.")




