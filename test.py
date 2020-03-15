class Teams:
    def init(self, members):
        self.myTeam = members

    def __len(self):
        return len(self.myTeam)
    
    def __contains(self, members):
        return members in self.myTeam
    
    def __iter(self):
        return self
    
    def next(self):
        if self.member >= self.myTeam:
            raise StopIteration

def main():
  classmates = Teams(['John', 'Steve', 'Tim'])
  print (len(classmates))
  print (classmates.__contains('Steve' and 'Tim'))
  #iterator = iter(classmates)
  #for memmbers in classmates:
      #print(memmbers)
  

main()