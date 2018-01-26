class Counter:
  def __init__(self):
    
    self.counter = 0
    
    #Counters for weapons#
    self.bullet_wait = 0
    self.bullet_delay = 10
    
    self.special_wait = 0
    self.special_delay = 20
    
    #Counters for enemy#
    self.enemy1_wait = 40
    self.enemy1_delay = 40
    self.enemy2_wait = 60 
    self.enemy2_delay = 60 
    self.boss_wait = 200
    self.boss_delay = 200
    
    
  def weapon_timer_update(self): 
    if self.bullet_wait > 0:
      self.bullet_wait -= 1
    if self.special_wait > 0:
      self.special_wait -= 1
      
  def enemy_timer_update(self):
    if self.enemy1_wait > 0:
      self.enemy1_wait -= 1
    if self.enemy2_wait > 0:
      self.enemy2_wait -= 1
    if self.boss_wait > 0:
      self.boss_wait -= 1
    
  def counter_update(self):
    self.counter += 1
    
    #Decreasing Delay#
    if self.counter > 1000:
      self.enemy1_delay = self.enemy1_delay/2
      self.enemy2_delay = self.enemy2_delay/2
      self.boss_delay = self.boss_delay/2
      
      self.counter = 0 
      

  def update(self):
    self.weapon_timer_update()
    self.enemy_timer_update()
    self.counter_update()
    
    