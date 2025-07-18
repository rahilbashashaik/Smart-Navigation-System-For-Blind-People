import unittest
 
  class TestUltrasonicSensor ( unittest . TestCase ) :
 def setUp( self ) :
 ””” Initialize the UltrasonicSensor and NavigationSystem before each test .”””
 s elf . ultrasonic sensor = UltrasonicSensor ()
 s elf . nav system = NavigationSystem ( self . ultrasonic sensor )
 def test obstacle detection
 normal range ( self ) :
 ”””Test obstacle detection at a normal range (e.g. , 2 meters) .”””
 
   s elf . ultrasonic sensor . set distance (2.0) # Obstacle at 2 meters
 distance = self . ultrasonic sensor . get distance ()
 s elf . assertEqual ( distance , 2.0)
 r esponse = self . nav system . handle obstacle ( distance )
 s elf . assertEqual ( response , ”Obstacle detected 3 meters ahead , prepare to adjust path”)
 def test no
 obstacle detection ( self ) :
 ”””Test that no obstacle is detected when the distance is infinite .”””
 s elf . ultrasonic sensor . set distance ( float ( ’ inf ’) ) # No obstacle detected
 distance = self . ultrasonic sensor . get distance ()
 s elf . assertEqual ( distance , float ( ’ inf ’) )
 r esponse = self . nav system . handle obstacle ( distance )
 s elf . assertEqual ( response , ”Path is clear”)
 def test obstacle detection
 c l ose range ( self ) :
 ”””Test obstacle detection at close range (e.g. , 0.2 meters) .”””
 s elf . ultrasonic sensor . set distance (0.2) # Obstacle at 0.2 meters
 distance = self . ultrasonic sensor . get distance ()
 s elf . assertEqual ( distance , 0.2)
 r esponse = self . nav system . handle obstacle ( distance )

 self .assertEqual(response , ”Emergency! Obstacle too close , stop immediately!”)
 
  def test obstacle detection long range(self):
  ”””Test obstacle detection at long range (e.g. , 5 meters) .”””
  self .ultrasonic sensor . set distance(5.0) # Obstacle at 5 meters
  distance = self .ultrasonic sensor .get distance()
  self .assertEqual(distance , 5.0)
  response = self .nav system.handle obstacle(distance)
  self .assertEqual(response , ”Obstacle detected , distance is safe for now”)
 
  def test path rerouting after obstacle(self):
  ”””Test the rerouting functionality when an obstacle is detected at close range.”””
  self .ultrasonic sensor . set distance(1.0) # Obstacle at 1 meter
  distance = self .ultrasonic sensor .get distance()
 self .assertEqual(distance , 1.0)
 reroute response = self .nav system. reroute path(distance)
  self .assertEqual(reroute response , ”Path adjustment required , please turn left”)
 
  def test invalid distance(self):
  ”””Test invalid distance input (below 0 or above 5 meters) .”””
  with self . assertRaises(ValueError):
 self .ultrasonic sensor . set distance(−1.0) # Invalid distance: less than 0
  with self . assertRaises(ValueError):
  self .ultrasonic sensor . set distance(6.0) # Invalid distance: greater than 5
 
  if name == ’ main ’:
  unittest .main()